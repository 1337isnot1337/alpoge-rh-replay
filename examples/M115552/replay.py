"""Rebuild M115552, compare every public declaration, and measure synchronous elaboration."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

from make_diff import HERE, MODULE, SOURCE, check_hash, inputs, regenerate

NAMESPACE = b"UpperTheory.Reformulated.B.Qi13"
DECL = re.compile(r"^(?:@\[reducible\] )?(private )?(?:noncomputable )?(?:theorem|def) ([\w.]+)", re.M)


def measure(text, src, env, lean, label):
    code = text.decode()
    declarations = list(DECL.finditer(code))
    path = src / "Measure.lean"
    path.write_bytes(DECL.sub(lambda m: "#count_heartbeats in\n" + m.group(), code).encode())
    proc = subprocess.run([*lean, path.name], cwd=src, env=env, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, encoding="utf-8")
    if proc.returncode:
        raise RuntimeError(proc.stdout)
    counts = [int(x) for x in re.findall(r"\bUsed (\d+) heartbeats", proc.stdout)]
    if len(counts) != len(declarations) or len(counts) != 12:
        raise ValueError(f"{label}: incomplete heartbeat report\n{proc.stdout}")
    public = 0
    for match, beats in zip(declarations, counts):
        name = match.group(2).split(".")[-1]
        if not match.group(1):
            public += beats
        print(f"  {label} {name}: {beats}", flush=True)
    print(f"{label}: {public} public; {sum(counts)} including private proofs", flush=True)
    return {"public": public, "total": sum(counts)}


def run(project, src, receipt, original, revised, audit, reference):
    pin = receipt["mathlib"]
    manifest = json.loads((project / "lake-manifest.json").read_text())
    if [d["rev"] for d in manifest["packages"] if d["name"] == "mathlib"] != [pin]:
        raise ValueError("Unexpected Mathlib pin in lake-manifest.json")
    if (project / "lean-toolchain").read_text().strip() != receipt["toolchain"]:
        raise ValueError("Unexpected project toolchain")
    mathlib = project / ".lake/packages/mathlib"
    real_pin = subprocess.check_output(["git", "-C", str(mathlib), "rev-parse", "HEAD"], text=True).strip()
    if real_pin != pin:
        raise ValueError(f"Mathlib checkout is {real_pin}; expected {pin}")
    version = subprocess.check_output(["lean", "--version"], text=True).strip()
    if "version 4.33.1," not in version or receipt["lean_commit"] not in version:
        raise ValueError(f"Unexpected Lean version: {version}")
    print(f"{version}\nMathlib {pin}", flush=True)
    search = os.environ["LEAN_PATH"].split(os.pathsep)
    env = {**os.environ, "LEAN_PATH": os.pathsep.join([str(src), *[str(Path(p).resolve()) for p in search if p]])}
    lean = ["lean", "--root=.", *receipt["lean_flags"]]
    target = src / SOURCE.relative_to("src")
    target.parent.mkdir(parents=True, exist_ok=True)
    (src / "PublishedMemOfClosed.lean").write_bytes(reference)
    target.write_bytes(revised)
    (src / "AuditAll.lean").write_bytes(audit)
    for mod in ("PublishedMemOfClosed", MODULE, "AuditAll"):
        path = Path(*mod.split("."))
        print(f"Compiling {mod}", flush=True)
        subprocess.run([*lean, "-o", str(path.with_suffix(".olean")), str(path.with_suffix(".lean"))],
                       cwd=src, env=env, check=True)
    subprocess.run(["leanchecker", "-v", "PublishedMemOfClosed", MODULE, "AuditAll"], cwd=src, env=env, check=True)
    for label, code in [("published", original), ("revised", revised)]:
        measured = measure(code, src, env, lean, label)
        expected = receipt["heartbeats"].get(label)
        if expected is not None and measured != expected:
            print(f"Reference heartbeat counts on the recorded machine: {expected}", flush=True)
    print("REPLAY_M115552_KERNEL_PASSED", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--sources-only", action="store_true")
    args = parser.parse_args()
    project = args.project.resolve()
    receipt = json.loads((HERE / "receipt.json").read_text())
    regenerate(project, receipt)
    original, revised = inputs(project, receipt)
    reference = check_hash(original.replace(NAMESPACE, b"PublishedMemOfClosed"), receipt["sha256"]["reference"],
                           "renamed reference")
    audit = check_hash((HERE / "AuditAll.lean").read_bytes().replace(b"\r\n", b"\n"), receipt["sha256"]["audit"], "audit")
    print("Verified original, revised, renamed reference, audit and regenerated diff SHA-256.", flush=True)
    if not args.sources_only:
        with tempfile.TemporaryDirectory(prefix="m115552-") as tmp:
            run(project, Path(tmp).resolve(), receipt, original, revised, audit, reference)


if __name__ == "__main__":
    main()
