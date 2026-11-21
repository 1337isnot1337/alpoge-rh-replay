import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = ROOT / "scripts" / "port-ci-build.py"

spec = importlib.util.spec_from_file_location("port_ci_build", SCRIPT_PATH)
assert spec is not None and spec.loader is not None
port_ci_build = importlib.util.module_from_spec(spec)
sys.modules["port_ci_build"] = port_ci_build
spec.loader.exec_module(port_ci_build)


class PortCiBuildTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.tmp = Path(temp.name)
        self.src = self.tmp / "archive_src"
        self.patches = self.tmp / "patches"
        self.workspace = self.tmp / "workspace"
        self.patches.mkdir()
        self.workspace.mkdir()

        self.base_src = b"theorem base : True := by trivial\n"
        self.leaf_src = b"import BuildAid.D1\ntheorem leaf : True := by\n  trivial\n"

        (self.src / "BuildAid").mkdir(parents=True)
        (self.src / "BuildAid" / "D1.lean").write_bytes(self.base_src)
        (self.src / "GroundTheory" / "LocalFields").mkdir(parents=True)
        (self.src / "GroundTheory" / "LocalFields" / "Foo.lean").write_bytes(self.leaf_src)

        self.by_id = {
            "M000001": {
                "id": "M000001",
                "module": "BuildAid.D1",
                "source_sha256": hashlib.sha256(self.base_src).hexdigest(),
                "imports": [],
                "packet": "P0001",
            },
            "M000002": {
                "id": "M000002",
                "module": "GroundTheory.LocalFields.Foo",
                "source_sha256": hashlib.sha256(self.leaf_src).hexdigest(),
                "imports": ["M000001"],
                "packet": "P0002",
            },
        }
        self.target = {
            "lean": "leanprover/lean4:v4.36.0",
            "mathlib": "fc4f59e577feb1a4956671bc04ac18aaaf8cd842",
        }

        (self.patches / "M000001.json").write_text(json.dumps({
            **self.target,
            "module": "BuildAid.D1",
            "source_sha256": self.by_id["M000001"]["source_sha256"],
            "notes": "unchanged",
        }))
        (self.patches / "M000002.json").write_text(json.dumps({
            **self.target,
            "module": "GroundTheory.LocalFields.Foo",
            "source_sha256": self.by_id["M000002"]["source_sha256"],
            "notes": "Use exact trivial.",
        }))
        (self.patches / "M000002.patch").write_text(
            "--- a/src/GroundTheory/LocalFields/Foo.lean\n"
            "+++ b/src/GroundTheory/LocalFields/Foo.lean\n"
            "@@ -1,3 +1,3 @@\n"
            " import BuildAid.D1\n"
            " theorem leaf : True := by\n"
            "-  trivial\n"
            "+  exact trivial\n"
        )

    def test_transitive_closure_and_packet_expansion(self):
        self.assertEqual(
            port_ci_build.expand_targets(["P0002"], self.by_id, self.patches),
            ["M000002"],
        )
        self.assertEqual(
            port_ci_build.transitive_closure(["M000002"], self.by_id),
            ["M000001", "M000002"],
        )

    def test_materialize_verify_patch_and_lakefile(self):
        closure = port_ci_build.transitive_closure(["M000002"], self.by_id)
        port_ci_build.materialize_sources(
            workspace=self.workspace,
            closure_ids=closure,
            by_id=self.by_id,
            local_src=self.src,
            source_base_url="unused",
        )
        self.assertEqual(port_ci_build.apply_patches(self.workspace, closure, self.patches), [])

        patched = (self.workspace / "src" / "GroundTheory" / "LocalFields" / "Foo.lean").read_text()
        self.assertIn("exact trivial", patched)

        module_names = [self.by_id[mid]["module"] for mid in closure]
        port_ci_build.write_project_files(self.workspace, module_names, self.target)

        self.assertEqual(
            (self.workspace / "lean-toolchain").read_text(),
            "leanprover/lean4:v4.36.0\n",
        )
        lakefile = (self.workspace / "lakefile.toml").read_text()
        self.assertIn('rev = "fc4f59e577feb1a4956671bc04ac18aaaf8cd842"', lakefile)
        self.assertIn('name = "BuildAid"', lakefile)
        self.assertIn('name = "GroundTheoryFields"', lakefile)
        self.assertIn("synthInstance.maxHeartbeats = 400000", lakefile)

    def test_sha256_mismatch_is_rejected(self):
        (self.src / "BuildAid" / "D1.lean").write_bytes(b"tampered\n")
        with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            port_ci_build.materialize_sources(
                workspace=self.workspace,
                closure_ids=["M000001"],
                by_id=self.by_id,
                local_src=self.src,
                source_base_url="unused",
            )

    def test_build_modules_rejects_sorry_diagnostic(self):
        fake_lake = self.tmp / "fake-lake.sh"
        fake_lake.write_text(
            "#!/bin/sh\n"
            "echo \"warning: src/BuildAid/D1.lean:1:8: declaration uses 'sorry'\"\n"
            "exit 0\n"
        )
        fake_lake.chmod(0o755)
        failed = port_ci_build.build_modules(
            lake=str(fake_lake),
            workspace=self.workspace,
            target_ids=["M000001"],
            by_id=self.by_id,
            patches_dir=self.patches,
        )
        self.assertEqual(failed, ["M000001"])

    def test_build_modules_passes_clean_build(self):
        fake_lake = self.tmp / "fake-lake-ok.sh"
        fake_lake.write_text("#!/bin/sh\necho 'Build completed successfully.'\nexit 0\n")
        fake_lake.chmod(0o755)
        failed = port_ci_build.build_modules(
            lake=str(fake_lake),
            workspace=self.workspace,
            target_ids=["M000001", "M000002"],
            by_id=self.by_id,
            patches_dir=self.patches,
        )
        self.assertEqual(failed, [])


if __name__ == "__main__":
    unittest.main()
