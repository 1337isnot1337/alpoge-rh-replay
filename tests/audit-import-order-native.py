#!/usr/bin/env python3
"""Check Audit.lean's imports against a project that redefines an expected name.

Uses only the pinned Lean compiler and temporary toy modules named Mathlib and
Main. This tests the verifier; it makes no claim about the RH archive.

Usage: python3 tests/audit-import-order-native.py /path/to/lean-4.33.1/bin
"""
import argparse
import os
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('lean_bin', type=Path)
    args = parser.parse_args()
    lean_bin = args.lean_bin.absolute()
    lean = lean_bin / 'lean'
    audit = Path(__file__).resolve().parents[1] / 'Audit.lean'
    imports = []
    for line in audit.read_text().splitlines():
        if line.startswith('import '):
            imports.append(line)
        elif line.strip():
            break
    header = '\n'.join(imports) + '\n'
    with tempfile.TemporaryDirectory(prefix='audit-import-order-') as temporary:
        root = Path(temporary)

        def run(directory, name, command, success=True, contains=None):
            env = dict(os.environ, LEAN_PATH=str(directory), PATH=f'{lean_bin}:{os.environ["PATH"]}')
            result = subprocess.run(list(map(str, command)), cwd=directory, env=env,
                                    text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if (result.returncode == 0) != success or (contains and contains not in result.stdout):
                raise RuntimeError(f'{name}: exit {result.returncode}\n{result.stdout}')
            print(f'PASS {name}', flush=True)

        def compile_module(directory, module, source):
            path = directory / (module + '.lean')
            path.write_text(source)
            run(directory, f'compile {directory.name}/{module}',
                [lean, '-R', directory, '-o', directory / (module + '.olean'), path])

        run(root, 'pinned compiler version', [lean, '--version'], contains='version 4.33.1')
        good = root / 'good'
        good.mkdir()
        compile_module(good, 'Mathlib', 'def IntendedStatement : Prop := True\n')
        compile_module(good, 'Main', 'import Mathlib\ntheorem claimed : IntendedStatement := True.intro\n')
        good_audit = good / 'Audit.lean'
        good_audit.write_text(header + 'example : IntendedStatement := claimed\n')
        run(good, 'shipped audit imports accept a genuine canonical theorem', [lean, good_audit])

        bad = root / 'redefined'
        bad.mkdir()
        compile_module(bad, 'Mathlib', 'def IntendedStatement : Prop := False\n')
        compile_module(bad, 'Main', 'def IntendedStatement : Prop := True\n'
                       'theorem claimed : IntendedStatement := True.intro\n')
        control = bad / 'Control.lean'
        control.write_text('import Main\nexample : IntendedStatement := claimed\n')
        run(bad, 'Main-only import accepts the project-defined proposition', [lean, control])
        bad_audit = bad / 'Audit.lean'
        bad_audit.write_text(header + 'example : IntendedStatement := claimed\n')
        run(bad, 'shipped audit imports reject a project replacement of the expected name',
            [lean, bad_audit], success=False,
            contains="environment already contains 'IntendedStatement' from Mathlib")


if __name__ == '__main__':
    main()
