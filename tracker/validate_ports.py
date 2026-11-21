"""Check port records against the pinned source ledger and port target."""
import json
import sys

from port import PATCHES, ROOT
from tasks import module_rows


def validate(folder, by_id, target):
    for patch in sorted(folder.glob('*.patch')):
        if not patch.with_suffix('.json').is_file():
            yield f'{patch.name}: missing module record'

    for path in sorted(folder.glob('*.json')):
        row = by_id.get(path.stem)
        if row is None:
            yield f'{path.name}: unknown module ID'
            continue
        try:
            record = json.loads(path.read_text())
        except (ValueError, OSError) as exc:
            yield f'{path.name}: {exc}'
            continue
        if not isinstance(record, dict):
            yield f'{path.name}: expected a JSON object'
            continue

        for key in ('module', 'source_sha256', 'lean', 'mathlib'):
            expected = row[key] if key in ('module', 'source_sha256') else target[key]
            if record.get(key) != expected:
                yield f'{path.name}: {key} must match {expected!r}'

        notes = record.get('notes')
        patch = path.with_suffix('.patch')
        if not isinstance(notes, str) or not notes.strip():
            yield f'{path.name}: missing notes'
        elif notes == 'unchanged' and patch.exists():
            yield f'{path.name}: unchanged record has a patch'
        elif notes != 'unchanged' and (not patch.is_file() or not patch.stat().st_size):
            yield f'{path.name}: missing or empty patch'


def main():
    target = json.loads((ROOT / 'port' / 'target.json').read_text())
    by_id = {row['id']: row for row in module_rows()}
    errors = list(validate(PATCHES, by_id, target))
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Validated {len(list(PATCHES.glob("*.json")))} port records.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
