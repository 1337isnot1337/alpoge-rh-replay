"""Verify the CutMainCpt (`cpt_copy_thms`) audit manifest and runner script against the module index."""

import gzip
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


def find_working_bash():
    candidates = [r"C:\Program Files\Git\bin\bash.exe"] if os.name == "nt" else []
    which_bash = shutil.which("bash")
    if which_bash:
        candidates.append(which_bash)
    for cand in candidates:
        if Path(cand).exists():
            probe = subprocess.run([cand, "-c", "command -v sha256sum || command -v shasum"], capture_output=True)
            if probe.returncode == 0:
                return cand
    return None


WORKING_BASH = find_working_bash()


ROOT = Path(__file__).resolve().parents[1]
AUDIT_DIR = ROOT / "audit"
SCRIPT = AUDIT_DIR / "cpt-copy-check.sh"
AUDITOR = AUDIT_DIR / "AuditCutMainCpt.lean"
MANIFEST = AUDIT_DIR / "cpt-copy-declarations.json"
MODULES_GZ = ROOT / "tracker" / "modules.jsonl.gz"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


class CptCopyAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.by_id = {}
        cls.by_mod = {}
        with gzip.open(MODULES_GZ, "rt", encoding="utf-8") as stream:
            for line in stream:
                if line.strip():
                    row = json.loads(line)
                    cls.by_id[row["id"]] = row
                    cls.by_mod[row["module"]] = row

        closure = set()
        stack = ["M146056"]
        while stack:
            cur = stack.pop()
            if cur in closure:
                continue
            closure.add(cur)
            stack.extend(cls.by_id[cur]["imports"])
        cls.cutmain_closure = closure
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_files_use_lf_line_endings(self):
        for path in (SCRIPT, AUDITOR, MANIFEST, ROOT / "tests" / "cpt-copy-audit-native.py"):
            raw = path.read_bytes()
            self.assertNotIn(b"\r\n", raw, f"CRLF found in {path}")

    def test_script_source_pins_match_tracker_index(self):
        text = SCRIPT.read_text(encoding="utf-8")
        pins = re.findall(
            r"check_source\s+(M\d{6})\s+([0-9a-f]{64})\s+\\\s*\n\s*(\S+)",
            text,
        )
        self.assertEqual([mid for mid, _, _ in pins], ["M145590", "M145591", "M145592", "M146056"])
        for mid, digest, rel_path in pins:
            row = self.by_id[mid]
            expected_rel = "src/" + row["module"].replace(".", "/") + ".lean"
            self.assertEqual(rel_path, expected_rel)
            self.assertEqual(digest, row["source_sha256"])

    def test_manifest_counts_and_closure_consistency(self):
        m = self.manifest
        self.assertEqual(m["module_id"], "M146056")
        self.assertEqual(m["module"], self.by_id["M146056"]["module"])
        self.assertEqual(m["metaprogram_module_id"], "M145590")
        self.assertEqual(m["metaprogram_module"], self.by_id["M145590"]["module"])
        self.assertIs(m["frontend_extensions_loaded"], False)
        self.assertEqual(len(self.cutmain_closure), 1661)

        counts = m["counts"]
        self.assertEqual(counts["to_copy_tainted_order"], 56)
        self.assertEqual(counts["skipped_already_imported"], 11)
        self.assertEqual(counts["skipped_manual_in_cutmaincpt"], 24)
        self.assertEqual(counts["cpt_copy_generated_total"], 21)
        self.assertEqual(counts["cpt_copy_generated_defs"], 3)
        self.assertEqual(counts["cpt_copy_generated_theorems"], 18)
        self.assertEqual(
            counts["to_copy_tainted_order"],
            counts["skipped_already_imported"]
            + counts["skipped_manual_in_cutmaincpt"]
            + counts["cpt_copy_generated_total"],
        )
        self.assertEqual(
            counts["cpt_copy_generated_total"],
            counts["cpt_copy_generated_defs"] + counts["cpt_copy_generated_theorems"],
        )
        self.assertEqual(
            counts["cutmaincpt_total_constants"],
            counts["cutmaincpt_manual_theorems"]
            + counts["cutmaincpt_manual_auxiliaries"]
            + counts["cpt_copy_generated_total"],
        )

    def test_generated_declarations_types_and_axioms(self):
        decls = self.manifest["generated_declarations"]
        self.assertEqual(len(decls), 21)
        defs = [d for d in decls if d["kind"] == "def"]
        thms = [d for d in decls if d["kind"] == "theorem"]
        self.assertEqual(len(defs), 3)
        self.assertEqual(len(thms), 18)

        for idx, d in enumerate(decls, start=1):
            self.assertEqual(d["index"], idx)
            self.assertTrue(d["name"].endswith("Cpt"), d["name"])
            self.assertIn(d["source_module"], self.by_mod)
            src_id = self.by_mod[d["source_module"]]["id"]
            self.assertIn(src_id, self.cutmain_closure)
            self.assertIs(d["type_expr_equal"], True)
            self.assertIs(d["value_expr_equal"], True)
            self.assertIs(d["kernel_defeq"], True)
            self.assertNotIn("⋯", d["type"])
            self.assertTrue(set(d["axioms"]).issubset(ALLOWED_AXIOMS), d["axioms"])
            if d["kind"] == "def":
                self.assertEqual(d["type"], "Prop")
                self.assertTrue(d.get("definition_body"))
                self.assertNotIn("⋯", d["definition_body"])

        for imp in self.manifest["skipped_already_imported"]:
            self.assertIn(imp["defined_in_module"], self.by_mod)
            imp_id = self.by_mod[imp["defined_in_module"]]["id"]
            self.assertIn(imp_id, self.cutmain_closure)

        roots = self.manifest["roots"]
        self.assertEqual(len(roots), 6)
        for r in roots:
            self.assertIn(r["origin"], ("cpt_copy_thms", "CutMainCpt.lean (manual)"))
            self.assertTrue(set(r["axioms"]).issubset(ALLOWED_AXIOMS))
            self.assertNotIn("⋯", r["type"])
            self.assertNotIn("⋯", r["type_pp_all"])

        for man in self.manifest["manual_source_theorems"]:
            self.assertTrue(set(man["axioms"]).issubset(ALLOWED_AXIOMS))

    @unittest.skipUnless(WORKING_BASH, "working POSIX bash is required for shell script smoke test")
    def test_shell_runner_rejects_missing_env_and_tampered_source(self):
        bash = WORKING_BASH
        base_path = str(Path(bash).parent) + os.pathsep + "/usr/bin:/bin"
        clean_env = {"PATH": base_path, "MSYS_NO_PATHCONV": "1"}
        res_no_env = subprocess.run(
            [bash, str(SCRIPT)],
            env=clean_env,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(res_no_env.returncode, 0)
        self.assertIn("LEAN_PATH", res_no_env.stderr)

        with tempfile.TemporaryDirectory() as tmp:
            lean_dir = Path(tmp)
            rel_dir = lean_dir / "src/Formalism/HermitianCurvature/HermitianCurvatureProofs"
            rel_dir.mkdir(parents=True)
            for name in ("CutCptCopy.lean", "CutCptDefs.lean", "CutCptManual.lean", "CutMainCpt.lean"):
                (rel_dir / name).write_text("-- tampered\n", encoding="utf-8")
            res_bad_hash = subprocess.run(
                [bash, str(SCRIPT)],
                cwd=lean_dir,
                env={"PATH": base_path, "LEAN_PATH": str(lean_dir), "MSYS_NO_PATHCONV": "1"},
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(res_bad_hash.returncode, 0)
            self.assertIn("source SHA-256 mismatch", res_bad_hash.stderr)


if __name__ == "__main__":
    unittest.main()
