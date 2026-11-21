#!/usr/bin/env python3
"""Exercise the exact driver with the pinned native Lean 4.33.1 toolchain.

Run: python3 tests/exact-replay-native.py /path/to/lean-4.33.1/bin
Use an externally memory-limited builder. Each subprocess has a 120s timeout.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('lean_bin', type=Path)
    args = parser.parse_args()
    lean_bin = args.lean_bin.resolve()
    source = Path(__file__).resolve().parents[1] / 'kernel/ExactReplay.lean'
    with tempfile.TemporaryDirectory(prefix='exact-replay-native-') as tmp:
        root = Path(tmp)
        driver = root / 'ExactReplay.lean'
        shutil.copyfile(source, driver)
        env = dict(os.environ, LEAN_PATH=str(root), LEAN_NUM_THREADS='8',
                   LEAN_STACK_SIZE_KB='65536', PATH=f'{lean_bin}:{os.environ["PATH"]}')

        def run(name, command, success=True):
            result = subprocess.run(list(map(str, command)), cwd=root, env=env,
                                    text=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, timeout=120)
            if (result.returncode == 0) != success:
                raise RuntimeError(f'{name}: exit {result.returncode}\n{result.stdout}')
            print(f'PASS {name}', flush=True)
            return result.stdout

        version = run('pinned compiler version', [lean_bin / 'lean', '--version'])
        assert 'version 4.33.1' in version, version
        names = [f'Fixture{i}' for i in range(10)]
        for name in [*names, 'Fixture0.Child']:
            path = root / (name.replace('.', '/') + '.lean')
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f'theorem {name.replace(".", "_")}_checked : 1 + 1 = 2 := rfl\n')
            run('compile ' + name, [lean_bin / 'lean', '-o', path.with_suffix('.olean'), path])

        def exact(name, arguments, success=True):
            driver.write_text(source.read_text() + '\n#eval replayExactModules '
                              + json.dumps(list(map(str, arguments))) + '\n')
            return run(name, [lean_bin / 'lean', driver], success=success)

        def completed(output):
            return [line.removeprefix('replaying ') for line in output.splitlines()
                    if line.startswith('replaying ')]

        for workers in (1, 8):
            output = exact(f'exact coverage with {workers} workers', [workers, *names])
            assert sorted(completed(output)) == sorted(names), output
            assert output.count('exact replay completed 10 modules') == 1, output

        native = run('native leaf-module reference', [lean_bin / 'leanchecker', '--verbose', *names[1:]])
        assert sorted(completed(native)) == sorted(names[1:]), native
        # Native selection expands prefixes; the exact driver intentionally does not.
        native = run('native prefix reference', [lean_bin / 'leanchecker', '--verbose', 'Fixture0'])
        assert sorted(completed(native)) == ['Fixture0', 'Fixture0.Child'], native

        for label, arguments in [
                ('late missing module', [2, *names, 'IntentionallyMissing']),
                ('duplicate target', [2, names[0], names[0]]),
                ('zero workers', [0, names[0]]),
                ('too many workers', [2, names[0]]),
                ('invalid workers', ['invalid', names[0]]),
                ('empty target list', [1]),
                ('empty module name', [1, ''])]:
            output = exact(label, arguments, success=False)
            assert 'exact replay completed ' not in output, output
            assert 'exact replay failed:' in output, output
            assert 'IntentionallyMissing' not in completed(output), output


if __name__ == '__main__':
    main()
