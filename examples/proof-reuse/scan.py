"""Find repeated theorem scripts or candidate statement shapes in the pinned source tree."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
# This recognizes column-zero declarations and indented continuations in the archive.
# Keep explicit universe parameters and everything after the name in the fingerprint.
DECL = re.compile(
    rb"^(?:private )?(?:theorem|lemma) ([A-Za-z_][A-Za-z_0-9']*(?:\.[A-Za-z_][A-Za-z_0-9']*)*)"
    rb"(?=[ \t:({\[]|\.\{)([^\n]*(?:\n(?:[ \t][^\n]*)?)*)", re.M
)


def indexed_sources(project, tasks=None):
    with gzip.open(ROOT / 'tracker/modules.jsonl.gz', 'rt', encoding='utf-8') as stream:
        for row in map(json.loads, stream):
            if tasks is not None and row['id'] not in tasks:
                continue
            path = project / 'src' / (row['module'].replace('.', '/') + '.lean')
            data = path.read_bytes()
            if hashlib.sha256(data).hexdigest() != row['source_sha256']:
                raise ValueError(f"Source hash mismatch for {row['id']} at {path}")
            yield row, data


IDENT = r"[^\W\d][\w']*"
WORD = re.compile(IDENT)
LABEL = re.compile(r'\s*:=')
BINDERS = re.compile(rf"\s*({IDENT}(?:\s+{IDENT})*)\s*:(?!=)")
DELIMS = {'(': ')', '{': '}', '[': ']'}
# Binding notation inside a type can shadow an earlier parameter. Fall back
# to the literal header rather than guessing its scope with substitutions.
INNER_BINDING = re.compile(r'λ|∑|∏|∫|⨆|⨅|↦|\||\b(?:fun|let|match|forall|exists)\b')
QUANTIFIER = re.compile(r'[∀∃]([^,]*)(?:,|$)')


def alpha_header(header):
    """Rename named parameters in successive outer binder groups."""
    if INNER_BINDING.search(header) or '$' in header:
        return header
    names = {}

    def rename(text):
        def replace(match):
            if ((match.start() and text[match.start() - 1] == '.') or
                    LABEL.match(text, match.end())):
                return match[0]
            return names.get(match[0], match[0])
        return WORD.sub(replace, text)

    pieces = []
    pos = 0
    while pos < len(header):
        if header[pos] == ':':
            # Bound variables may occur in binder types too. If a quantifier's
            # binder text mentions a renamed parameter, prefer a missed match.
            for quantifier in QUANTIFIER.finditer(header):
                if any(word in names for word in WORD.findall(quantifier[1])):
                    return header
            return ''.join(pieces) + rename(header[pos:])
        if header[pos].isspace():
            pieces.append(header[pos])
            pos += 1
            continue
        if header[pos] not in DELIMS:
            return header
        stack = [DELIMS[header[pos]]]
        end = pos + 1
        while stack and end < len(header):
            char = header[end]
            if char in DELIMS:
                stack.append(DELIMS[char])
            elif char in ')}]':
                if char != stack.pop():
                    return header
            end += 1
        if stack:
            return header
        group = header[pos + 1:end - 1]
        bound = BINDERS.match(group)
        if bound:
            variables = bound[1].split()
            if any(v == '_' or v in names for v in variables) or len(set(variables)) != len(variables):
                return header
            # The names in this group are in scope *after* its type.
            type_text = rename(group[bound.end():])
            canonical = [f'${len(names) + i}' for i in range(len(variables))]
            names.update(zip(variables, canonical))
            group = ' '.join(canonical) + ' :' + type_text
        else:
            group = rename(group)
        pieces.append(header[pos] + group + header[end - 1])
        pos = end
    return header


def statement_prefix(block):
    """Ignore proof-valued default arguments when locating the declaration's proof."""
    for delimiter in re.finditer(rb':= by', block):
        prefix = block[:delimiter.start()]
        if all(prefix.count(a) == prefix.count(b) for a, b in
               ((b'(', b')'), (b'[', b']'), (b'{', b'}'))):
            if re.search(rb'\blet\b', prefix):
                return None
            return prefix
    return None


def statement_header(block):
    prefix = statement_prefix(block)
    return ' '.join(prefix.decode('utf-8').split()) if prefix is not None else None


def declarations(data, mode='exact'):
    # Skip files that might put apparent commands inside multiline comments, strings or quotations.
    if any(marker in data for marker in (b'/-', b'"', b'`')):
        return
    for match in DECL.finditer(data):
        block = match[2].strip()
        if b':= by' in block and b'--' not in block:
            fingerprint = block
            if mode != 'exact':
                header = statement_header(block)
                if header is None:
                    continue
                if mode == 'alpha':
                    header = alpha_header(header)
                fingerprint = header.encode('utf-8')
            yield hashlib.sha256(fingerprint).digest(), match, block


def scan(project, limit, wanted, mode='exact'):
    counts = Counter()
    examples = {}
    matches = []
    modules = 0
    for row, data in indexed_sources(project):
        modules += 1
        for key, match, _ in declarations(data, mode):
            counts[key] += 1
            if counts[key] == 2 or key in wanted:
                location = dict(task=row['id'], name=match[1].decode(),
                                line=data.count(b'\n', 0, match.start()) + 1)
                if counts[key] == 2:
                    examples[key] = location
                if key in wanted:
                    matches.append(dict(sha256=key.hex(), **location))
    repeated = sorted(examples, key=lambda k: (-counts[k], k))
    result = dict(modules=modules, candidates=sum(counts.values()), repeated_groups=len(repeated),
                occurrences_after_first=sum(counts[k] - 1 for k in repeated),
                top=[dict(sha256=k.hex(), occurrences=counts[k], example=examples[k])
                     for k in repeated[:limit]], matches=matches)
    if mode != 'exact':
        result['mode'] = mode
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path, help='prepared lean/ directory')
    parser.add_argument('--mode', choices=['exact', 'header', 'alpha'], default='exact',
                        help='hash the original script (default), normalized header, or renamed outer binders')
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--match', action='append', default=[], metavar='SHA256',
                        help='include every task, declaration name and line for this fingerprint')
    args = parser.parse_args()
    if args.limit < 0 or any(not re.fullmatch('[0-9a-fA-F]{64}', k) for k in args.match):
        parser.error('use a nonnegative limit and full SHA-256 fingerprints')
    print(json.dumps(scan(args.project, args.limit, {bytes.fromhex(k) for k in args.match}, args.mode), indent=2))


if __name__ == '__main__':
    main()
