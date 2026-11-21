#!/usr/bin/env python3
"""Audit the exact live modules already built by port-packet-diagnostic.py."""

import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import traceback

UPSTREAM_COMMIT = '749aefb802680024c33d06c58ad4b2ed75a1d3a1'
AUDIT_SHA256 = 'aa5d944f11e687880959ea125061ef562594ba8352076da4b83e2f496cb9e39b'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def stop_process_group(process):
    """Stop Lake and its owned Lean child before sealing the transcript."""
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        pass
    # Lake may have exited while a child still owns the log file descriptor.
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    process.wait(timeout=5)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--evidence', type=Path, required=True)
    parser.add_argument('--timeout', type=int, default=1200)
    args = parser.parse_args()
    repo, workspace, evidence = (p.resolve() for p in (args.repo, args.workspace, args.evidence))
    assert evidence.is_dir(), 'The original build evidence directory must exist'
    assert args.timeout > 0
    log_path = evidence / 'islattice-audit.log'
    receipt_path = evidence / 'islattice-audit.json'
    script_copy = evidence / 'islattice-audit.lean'
    runner_copy = evidence / 'islattice-audit-runner.py'
    for path in (log_path, receipt_path, script_copy, runner_copy):
        assert not path.exists(), f'Refusing to overwrite an existing audit: {path}'
    start = time.monotonic()
    receipt = {'schema_version': 1, 'status': 'failed', 'started_utc': utc_now(),
               'audit_upstream_commit': UPSTREAM_COMMIT, 'audit_script_sha256': AUDIT_SHA256,
               'script': script_copy.name, 'runner': runner_copy.name,
               'log': log_path.name, 'workspace': str(workspace), 'exit_code': None,
               'timed_out': False, 'errors': [], 'source_unchanged_during_audit': False,
               'objects_unchanged_during_audit': False}
    try:
        audit = repo / 'port/islattice_audit.lean'
        assert digest(audit) == AUDIT_SHA256, 'Unexpected upstream audit script bytes'
        shutil.copyfile(audit, script_copy)
        shutil.copyfile(Path(__file__).resolve(), runner_copy)
        receipt['audit_runner_sha256'] = digest(runner_copy)
        result_path = evidence / 'result.json'
        result = json.loads(result_path.read_text())
        receipt['build_result_sha256'] = digest(result_path)
        ci_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip()
        assert result['tracker_commit'] == ci_commit
        assert result['status'] in {'success', 'partial_success'} and result['failed'] == 0
        module_ids = result['target_ids']
        assert module_ids == sorted(set(module_ids)) and module_ids
        assert set(result['modules']) == set(module_ids)
        assert result['passed'] == len(module_ids)
        selection = json.loads((evidence / 'requested-selection.json').read_text())
        assert selection['packet'] == result['packet']
        assert selection['target_ids'] == module_ids
        assert json.loads((evidence / 'requested-modules.json').read_text()) == module_ids
        rows = {row['id']: row for row in map(json.loads, gzip.open(repo / 'tracker/modules.jsonl.gz', 'rt'))}
        module_names = [rows[mid]['module'] for mid in module_ids]
        assert len(module_names) == len(set(module_names))
        assert set(result['sources']) == set(result['closure_ids']) == set(selection['closure_ids'])
        source_paths = {mid: workspace / 'src' / (rows[mid]['module'].replace('.', '/') + '.lean')
                        for mid in result['closure_ids']}
        source_hashes = {mid: result['sources'][mid]['compiled_source_sha256'] for mid in source_paths}
        for mid, path in source_paths.items():
            assert digest(path) == source_hashes[mid], f'Source changed after build: {mid}'
        object_paths = {mid: workspace / '.lake/build/lib/lean' /
                       (rows[mid]['module'].replace('.', '/') + '.olean') for mid in module_ids}
        object_hashes = {}
        for mid in module_ids:
            build = result['modules'][mid]
            assert build['module'] == rows[mid]['module']
            assert build['success'] and build['exit_code'] == 0 and not build['timed_out']
            assert build['transcript_capture_errors'] == [] and not build['sorry_diagnostic']
            assert build['source_unchanged_during_build']
            assert build['compiled_source_sha256'] == source_hashes[mid]
            assert digest(object_paths[mid]) == build['object_sha256'], f'Object changed after build: {mid}'
            object_hashes[mid] = build['object_sha256']
        command = ['lake', 'env', 'lean', '--run', str(script_copy), *module_names]
        receipt.update({'packet': result['packet'], 'ci_commit': ci_commit,
                        'target': result['target'], 'lean_commit': result['lean_commit'],
                        'module_ids': module_ids, 'module_names': module_names,
                        'compiled_source_sha256': source_hashes, 'object_sha256': object_hashes,
                        'command': command})
        with log_path.open('wb') as stream:
            process = subprocess.Popen(command, cwd=workspace, stdout=stream,
                                       stderr=subprocess.STDOUT, start_new_session=True)
            try:
                receipt['exit_code'] = process.wait(timeout=args.timeout)
            except subprocess.TimeoutExpired:
                stop_process_group(process)
                receipt['exit_code'] = process.returncode
                receipt['timed_out'] = True
                receipt['errors'].append(f'Audit exceeded {args.timeout} seconds')
            except BaseException:
                stop_process_group(process)
                receipt['exit_code'] = process.returncode
                raise
        receipt['source_unchanged_during_audit'] = all(digest(path) == source_hashes[mid]
                                                     for mid, path in source_paths.items())
        receipt['objects_unchanged_during_audit'] = all(digest(path) == object_hashes[mid]
                                                      for mid, path in object_paths.items())
        assert receipt['source_unchanged_during_audit'], 'Source changed during audit'
        assert receipt['objects_unchanged_during_audit'], 'Object changed during audit'
        assert digest(script_copy) == AUDIT_SHA256, 'Audit script changed during execution'
        assert digest(runner_copy) == receipt['audit_runner_sha256'], 'Audit runner changed during execution'
        assert digest(result_path) == receipt['build_result_sha256'], 'Build result changed during audit'
        expected_summary = f'islattice-audit: {len(module_ids)} module(s), 0 hit(s)'
        receipt['expected_summary'] = expected_summary
        lines = log_path.read_text().splitlines()
        summary_lines = [line for line in lines if line.startswith('islattice-audit:')]
        assert summary_lines == [expected_summary], 'Audit did not report exactly zero hits for all live modules'
        assert not any(' uses Submodule.IsLattice in its ' in line for line in lines)
        assert receipt['exit_code'] == 0 and not receipt['timed_out']
        assert not receipt['errors']
        receipt['status'] = 'success'
    except BaseException as error:
        receipt['errors'].append(f'{type(error).__name__}: {error}')
        with log_path.open('ab') as stream:
            stream.write(('\nAudit runner failure:\n' + traceback.format_exc()).encode())
    finally:
        receipt['ended_utc'] = utc_now()
        receipt['elapsed_seconds'] = round(time.monotonic() - start, 3)
        receipt['log_sha256'] = digest(log_path)
        receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')
        checksums = {}
        for path in sorted(evidence.rglob('*')):
            assert not path.is_symlink(), f'Symlink in evidence: {path}'
            if path.is_file() and path != evidence / 'sha256.json':
                checksums[path.relative_to(evidence).as_posix()] = digest(path)
        (evidence / 'sha256.json').write_text(json.dumps(checksums, indent=2) + '\n')
        print(log_path.read_text(), end='')
        print('ISLATTICE_AUDIT_RESULT ' + json.dumps(receipt, separators=(',', ':')))
    return 0 if receipt['status'] == 'success' else 1


if __name__ == '__main__':
    raise SystemExit(main())
