#!/usr/bin/env python3
"""Build unported packets on the port target without creating success records.

This fork-only diagnostic uses the repository's source materializer and Lake
configuration. Optional diagnostic patches are diffs against pristine sources;
they are never treated as landed port records. Results are checkpointed after
all setup stages and after every module, including failed compiler attempts.
Repeat --module to probe selected packet members; successful subsets are marked
partial_success and cannot count as a complete packet build.
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
import traceback

ROOT = Path(__file__).resolve().parent.parent
EXPECTED_LEAN = "leanprover/lean4:v4.36.0"
EXPECTED_MATHLIB = "fc4f59e577feb1a4956671bc04ac18aaaf8cd842"
EXPECTED_LEAN_COMMIT = "611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9"
spec = importlib.util.spec_from_file_location("port_ci", ROOT / "scripts/port-ci-build.py")
ci = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(ci)
sys.path.insert(0, str(ROOT / "tracker"))
from validate_ports import validate_patch_content  # noqa: E402


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def command_output(cmd: list[str], cwd: Path | None = None) -> str:
    return subprocess.check_output(cmd, cwd=cwd, text=True).strip()


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, text):
        for stream in self.streams:
            stream.write(text)
        return len(text)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def save_result(output: Path, result: dict) -> None:
    temporary = output / "result.json.tmp"
    temporary.write_text(json.dumps(result, indent=2) + "\n")
    temporary.replace(output / "result.json")


def select_targets(packet: str, requested: list[str] | None,
                   ledger: dict) -> tuple[list[str], list[str]]:
    packet_ids = sorted(mid for mid, row in ledger.items() if row["packet"] == packet)
    if not packet_ids:
        raise RuntimeError("Unknown packet: " + packet)
    if requested is None:
        return packet_ids, packet_ids
    if len(requested) != len(set(requested)):
        raise RuntimeError("Duplicate requested module IDs")
    outside = sorted(set(requested) - set(packet_ids))
    if outside:
        raise RuntimeError("Requested modules do not belong to " + packet + ": " + ", ".join(outside))
    if not requested:
        raise RuntimeError("A module probe must request at least one module")
    return sorted(requested), packet_ids


def package_pins(workspace: Path) -> list[dict]:
    manifest = json.loads((workspace / "lake-manifest.json").read_text())
    pins = []
    for entry in manifest["packages"]:
        if entry.get("type") != "git":
            raise RuntimeError(f"Unexpected non-git dependency: {entry['name']}")
        folder = workspace / manifest.get("packagesDir", ".lake/packages") / entry["name"]
        head = command_output(["git", "rev-parse", "HEAD"], folder)
        if head != entry["rev"]:
            raise RuntimeError(f"Dependency revision mismatch: {entry['name']}")
        if command_output(["git", "status", "--porcelain", "--untracked-files=no"], folder):
            raise RuntimeError(f"Modified dependency sources: {entry['name']}")
        pins.append({"name": entry["name"], "commit": head})
    if {p["name"]: p["commit"] for p in pins}.get("mathlib") != EXPECTED_MATHLIB:
        raise RuntimeError("Mathlib checkout does not match port target")
    return pins


def apply_patch(workspace: Path, patch: Path, row: dict) -> None:
    errors = list(validate_patch_content(patch, "src/" + ci.module_relpath(row["module"])))
    if errors:
        raise RuntimeError("\n".join(errors))
    subprocess.run(["git", "apply", "--check", "--whitespace=nowarn", str(patch)],
                   cwd=workspace, check=True)
    subprocess.run(["git", "apply", "--whitespace=nowarn", str(patch)],
                   cwd=workspace, check=True)


def build_one(lake: str, workspace: Path, output: Path, mid: str, row: dict,
              source_record: dict, timeout: int) -> dict:
    command = [lake, "--no-cache", "build", f"+{row['module']}:olean"]
    log_path = output / "modules" / f"{mid}.log"
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    clock = time.monotonic()
    timed_out = False
    capture_errors = []
    print(f"\nBEGIN_MODULE {mid} {row['module']}", flush=True)
    with log_path.open("w") as log:
        header = (f"Module: {mid} {row['module']}\nStarted: {started}\n"
                  + "Command: " + json.dumps(command) + "\n"
                  + "Pinned source SHA-256: " + row["source_sha256"] + "\n"
                  + "Compiled source SHA-256: " + source_record["compiled_source_sha256"] + "\n\n")
        log.write(header)
        log.flush()
        print(header, end="", flush=True)
        proc = subprocess.Popen(command, cwd=workspace, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, start_new_session=True,
                                text=True, encoding="utf-8", bufsize=1)

        def capture():
            try:
                assert proc.stdout is not None
                for line in proc.stdout:
                    log.write(line)
                    log.flush()
                    print(line, end="", flush=True)
            except Exception as exc:
                capture_errors.append(repr(exc))

        def signal_group(sig):
            try:
                os.killpg(proc.pid, sig)
            except ProcessLookupError:
                pass

        reader = threading.Thread(target=capture, daemon=True)
        reader.start()
        try:
            try:
                proc.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                timed_out = True
                signal_group(signal.SIGTERM)
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    signal_group(signal.SIGKILL)
                    proc.wait(timeout=5)
                signal_group(signal.SIGKILL)
            reader.join(timeout=10)
            if reader.is_alive():
                capture_errors.append("Compiler descendants kept the output pipe open after exit")
                signal_group(signal.SIGKILL)
                reader.join(timeout=5)
                if reader.is_alive():
                    raise RuntimeError("Compiler transcript reader did not terminate after cleanup")
        except BaseException:
            signal_group(signal.SIGKILL)
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass
            reader.join(timeout=5)
            raise
        finally:
            if not reader.is_alive() and proc.stdout is not None:
                proc.stdout.close()
        elapsed = round(time.monotonic() - clock, 3)
        trailer = (f"\nExit status: {proc.returncode}\nElapsed seconds: {elapsed}\n"
                   + f"Timed out: {timed_out}\n")
        if capture_errors:
            trailer += "Transcript capture errors: " + json.dumps(capture_errors) + "\n"
        log.write(trailer)
        print(trailer, end="", flush=True)
    transcript = log_path.read_text()
    source = workspace / "src" / ci.module_relpath(row["module"])
    unchanged_during_build = digest(source) == source_record["compiled_source_sha256"]
    has_sorry = bool(ci.SORRY_DIAG_RE.search(transcript))
    obj = workspace / ".lake/build/lib/lean" / (row["module"].replace(".", "/") + ".olean")
    success = proc.returncode == 0 and not timed_out and not capture_errors and not has_sorry and unchanged_during_build and obj.is_file()
    result = {"module": row["module"], "started_utc": started, "elapsed_seconds": elapsed,
              "command": command, "exit_code": proc.returncode, "timed_out": timed_out,
              "transcript_capture_errors": capture_errors,
              "sorry_diagnostic": has_sorry, "source_unchanged_during_build": unchanged_during_build,
              "success": success, "log": f"modules/{mid}.log", "log_sha256": digest(log_path),
              "object_sha256": digest(obj) if success else None,
              **source_record}
    print("END_MODULE " + mid + " " + json.dumps(result, sort_keys=True), flush=True)
    return result


def run(args, result: dict) -> int:
    workspace, output = args.workspace.resolve(), args.output.resolve()
    target = ci.load_target()
    if target["lean"] != EXPECTED_LEAN or target["mathlib"] != EXPECTED_MATHLIB:
        raise RuntimeError("Repository port target differs from requested Lean/Mathlib 4.36.0")
    if workspace.exists() and any(workspace.iterdir()):
        raise RuntimeError("Diagnostic workspace must be fresh and empty")
    workspace.mkdir(parents=True, exist_ok=True)
    ledger = ci.load_ledger()
    ids, packet_ids = select_targets(args.packet, args.module, ledger)
    closure = ci.transitive_closure(ids, ledger)
    external = set(closure) - set(ids)
    result.update({"target": target, "target_ids": ids, "packet_ids": packet_ids,
                   "packet_complete": False, "closure_ids": closure,
                   "tracker_commit": command_output(["git", "rev-parse", "HEAD"], ROOT),
                   "ledger_sha256": digest(ci.MODULES_LEDGER), "status": "preparing"})
    save_result(output, result)
    ci.materialize_sources(workspace, closure, ledger, None, ci.DEFAULT_SOURCE_BASE_URL)
    source_records = {}
    for mid in closure:
        row = ledger[mid]
        record = ci.load_record(mid)
        if mid in external and record is None:
            raise RuntimeError("Missing landed prerequisite port: " + mid)
        if record is not None:
            for key in ("module", "source_sha256", "lean", "mathlib"):
                expected = row[key] if key in ("module", "source_sha256") else target[key]
                if record.get(key) != expected:
                    raise RuntimeError(f"Invalid landed record {mid}: {key}")
        overlay = args.diagnostic_patches.resolve() / f"{mid}.patch"
        patch = None
        kind = "unchanged"
        if overlay.is_file():
            if mid not in ids:
                raise RuntimeError("Diagnostic patch may only modify a requested packet member: " + mid)
            patch, kind = overlay, "diagnostic"
        elif record is not None and record.get("notes") != "unchanged":
            patch, kind = ci.PATCHES / f"{mid}.patch", "landed"
            if not patch.is_file():
                raise RuntimeError("Missing landed patch: " + mid)
        elif (ci.PATCHES / f"{mid}.patch").exists():
            raise RuntimeError("Unexpected patch without a patched landed record: " + mid)
        if patch is not None:
            apply_patch(workspace, patch, row)
            shutil.copyfile(patch, output / "patches" / f"{mid}.patch")
        source = workspace / "src" / ci.module_relpath(row["module"])
        source_records[mid] = {"source_sha256": row["source_sha256"],
                               "compiled_source_sha256": digest(source), "patch_kind": kind,
                               "patch_sha256": digest(patch) if patch else None}
    result["sources"] = source_records
    (output / "source-manifest.json").write_text(json.dumps(source_records, indent=2) + "\n")
    ci.write_project_files(workspace, [ledger[mid]["module"] for mid in closure], target)
    ci.setup_lake_env(args.lake, workspace, clean_cache_archive=True)
    version = command_output([args.lake, "env", "lean", "--version"], workspace)
    lean_commit = command_output([args.lake, "env", "lean", "--githash"], workspace)
    if "version 4.36.0," not in version or lean_commit != EXPECTED_LEAN_COMMIT:
        raise RuntimeError("Unexpected compiler identity: " + version + " " + lean_commit)
    result["lean_version"] = version
    result["lean_commit"] = lean_commit
    result["dependencies"] = package_pins(workspace)
    result["lake_manifest_sha256"] = digest(workspace / "lake-manifest.json")
    shutil.copyfile(workspace / "lake-manifest.json", output / "lake-manifest.json")
    shutil.copyfile(workspace / "lakefile.toml", output / "lakefile.toml")
    result["status"] = "building"
    save_result(output, result)
    for mid in ids:
        result["modules"][mid] = build_one(args.lake, workspace, output, mid, ledger[mid],
                                            source_records[mid], args.module_timeout)
        save_result(output, result)
    if package_pins(workspace) != result["dependencies"]:
        raise RuntimeError("Dependencies changed during compilation")
    for mid in closure:
        source = workspace / "src" / ci.module_relpath(ledger[mid]["module"])
        if digest(source) != source_records[mid]["compiled_source_sha256"]:
            raise RuntimeError("Source changed during compilation: " + mid)
    if digest(workspace / "lake-manifest.json") != result["lake_manifest_sha256"]:
        raise RuntimeError("Lake manifest changed during compilation")
    passed = sum(row["success"] for row in result["modules"].values())
    result["packet_complete"] = ids == packet_ids and passed == len(ids)
    if passed != len(ids):
        result["status"] = "failed"
    else:
        result["status"] = "success" if result["packet_complete"] else "partial_success"
    result["passed"] = passed
    result["failed"] = len(ids) - passed
    return 0 if passed == len(ids) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", required=True)
    parser.add_argument("--module", action="append", metavar="MODULE_ID",
                        help="Build only this packet member; repeat for a diagnostic subset. "
                             "A passing subset is partial_success, never packet success.")
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--lake", default="lake")
    parser.add_argument("--diagnostic-patches", type=Path, default=ROOT / "port/diagnostic-patches")
    parser.add_argument("--module-timeout", type=int, default=900)
    args = parser.parse_args()
    if not re.fullmatch(r"P\d{4}", args.packet) or args.module_timeout <= 0:
        parser.error("Expected a packet ID and a positive per-module timeout")
    if args.module is not None and any(not re.fullmatch(r"M\d{6}", mid) for mid in args.module):
        parser.error("Expected module IDs of the form M000001")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    for name in ("modules", "patches"):
        (output / name).mkdir(exist_ok=True)
    result = {"packet": args.packet, "status": "initializing", "modules": {},
              "requested_module_ids": args.module, "packet_complete": False,
              "started_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "diagnostic_only": True, "creates_port_records": False,
              "cpu_count": os.cpu_count(), "lean_num_threads": os.environ.get("LEAN_NUM_THREADS")}
    save_result(output, result)
    exit_code = 1
    with (output / "run.log").open("w") as run_log:
        with contextlib.redirect_stdout(Tee(sys.stdout, run_log)), contextlib.redirect_stderr(Tee(sys.stderr, run_log)):
            try:
                exit_code = run(args, result)
            except Exception as exc:
                result["status"] = "error"
                result["error"] = str(exc)
                traceback.print_exc()
            finally:
                result["ended_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
                save_result(output, result)
                print("\nDIAGNOSTIC_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    checksums = {str(path.relative_to(output)): digest(path)
                 for path in sorted(output.rglob("*")) if path.is_file() and path.name != "sha256.json"}
    (output / "sha256.json").write_text(json.dumps(checksums, indent=2) + "\n")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
