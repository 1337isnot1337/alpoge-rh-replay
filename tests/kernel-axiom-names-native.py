#!/usr/bin/env python3
"""Native negative control for the pinned nanoda axiom-name flattening behavior."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "kernel"))
import packet_check


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("toolchain_bin", type=Path)
    parser.add_argument("lean4export", type=Path)
    parser.add_argument("nanoda", type=Path)
    args = parser.parse_args()
    lean = args.toolchain_bin.resolve() / "lean"
    exporter = args.lean4export.resolve()
    nanoda = args.nanoda.resolve()
    version = subprocess.check_output([str(lean), "--version"], text=True)
    assert packet_check.LEAN_VERSION in version and packet_check.LEAN_COMMIT in version
    with tempfile.TemporaryDirectory(prefix="kernel-axiom-names-") as directory:
        root = Path(directory)
        env = os.environ.copy()
        env["PATH"] = str(lean.parent) + os.pathsep + env.get("PATH", "")
        env["LEAN_PATH"] = str(root)
        sources = {
            "AliasDependency": 'axiom «Classical.choice» : False\n',
            "AliasRoot": 'import AliasDependency\ntheorem aliasFalse : False := «Classical.choice»\n',
            "Canonical": 'noncomputable def chooseNat (h : Nonempty Nat) : Nat := Classical.choice h\n',
        }
        for module, source in sources.items():
            (root / f"{module}.lean").write_text(source, encoding="utf-8")
            subprocess.run([str(lean), f"{module}.lean", "-o", f"{module}.olean"],
                           cwd=root, env=env, check=True)
        for module, declaration in [("Canonical", "chooseNat"), ("AliasRoot", "aliasFalse")]:
            exported = root / f"{module}.ndjson"
            with exported.open("wb") as stdout:
                subprocess.run([str(exporter), module, "--", declaration], cwd=root, env=env,
                               stdout=stdout, check=True)
            cfg = packet_check.make_nanoda_config(exported, 2)
            cfg["print_axioms"] = False
            config = root / f"{module}.json"
            config.write_text(json.dumps(cfg), encoding="utf-8")
            result = subprocess.run([str(nanoda), str(config)], text=True, capture_output=True)
            assert result.returncode == 0, result.stderr
            assert "with no errors" in result.stdout and "skipping" not in result.stdout
            # The unmodified pinned Rust checker accepts both exports. Only the
            # canonical two-component name may pass our entry-point validation.
            if module == "Canonical":
                info = packet_check.count_export_records(exported)
                assert info["axioms"] == ["Classical.choice"]
            else:
                try:
                    packet_check.count_export_records(exported)
                except packet_check.CheckFailure as exc:
                    assert "unpermitted axiom name components" in str(exc)
                else:
                    raise AssertionError("Single-component axiom alias passed the structural allowlist")
        print("PASS: canonical axiom accepted; flattened-name alias rejected despite pinned nanoda acceptance")


if __name__ == "__main__":
    main()
