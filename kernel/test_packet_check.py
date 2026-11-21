#!/usr/bin/env python3
"""Unit tests for kernel/packet_check.py."""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

import packet_check


class PacketCheckTests(unittest.TestCase):
    def count_records(self, records):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "export.ndjson"
            path.write_text("\n".join(json.dumps(row) for row in records) + "\n", encoding="utf-8")
            return packet_check.count_export_records(path)

    @staticmethod
    def axiom_records(components):
        records = [{"meta": {"format": {"version": "3.1.0"}}}]
        prefix = 0
        for idx, component in enumerate(components, 1):
            records.append({"in": idx, "str": {"pre": prefix, "str": component}})
            prefix = idx
        records.append({"axiom": {"name": prefix, "levelParams": [], "type": 0, "isUnsafe": False}})
        return records

    def test_allowlist_accepts_each_canonical_name(self):
        for name in packet_check.PERMITTED_AXIOMS:
            with self.subTest(name=name):
                result = self.count_records(self.axiom_records(name.split(".")))
                self.assertEqual(result["axioms"], [name])
                self.assertTrue(result["axiom_names_checked_structurally"])

    def test_allowlist_rejects_names_that_flatten_to_allowed_strings(self):
        for parts in [["Classical.choice"], ["Quot.sound"], ["Lean.trustCompiler"], ["", "propext"]]:
            with self.subTest(parts=parts), self.assertRaisesRegex(packet_check.CheckFailure, "unpermitted axiom name components"):
                self.count_records(self.axiom_records(parts))

    def test_allowlist_rejects_unknown_axioms(self):
        with self.assertRaisesRegex(packet_check.CheckFailure, "unpermitted axiom name components"):
            self.count_records(self.axiom_records(["sorryAx"]))

    def test_name_table_rejects_missing_prefix_and_duplicate_index(self):
        for prefix in [99, False, "0"]:
            records = self.axiom_records(["propext"])
            records[1]["str"]["pre"] = prefix
            with self.subTest(prefix=prefix), self.assertRaisesRegex(packet_check.CheckFailure, "unknown name prefix"):
                self.count_records(records)
        records = self.axiom_records(["propext"])
        records.insert(2, {"in": 1, "str": {"pre": 0, "str": "other"}})
        with self.assertRaisesRegex(packet_check.CheckFailure, "duplicate name index"):
            self.count_records(records)

    def test_axiom_name_must_reference_an_existing_name(self):
        for index in [99, True, None, "1"]:
            records = self.axiom_records(["propext"])
            records[-1]["axiom"]["name"] = index
            with self.subTest(index=index), self.assertRaisesRegex(packet_check.CheckFailure, "unknown axiom name"):
                self.count_records(records)

    def test_name_component_kinds_are_preserved(self):
        records = self.axiom_records(["propext"])
        records[1] = {"in": 1, "num": {"pre": 0, "i": 0}}
        with self.assertRaisesRegex(packet_check.CheckFailure, "unpermitted axiom name components"):
            self.count_records(records)
        for component in [{"pre": 0, "i": -1}, {"pre": 0, "i": True}, {"pre": 0, "i": "0"}]:
            records[1]["num"] = component
            with self.subTest(component=component), self.assertRaisesRegex(packet_check.CheckFailure, "invalid name segment"):
                self.count_records(records)

    @unittest.skipUnless(os.name != "nt" and shutil.which("bash") and shutil.which("nice"), "POSIX shell pilot")
    def test_statement_pilot_checks_axiom_names_before_invoking_nanoda(self):
        script = Path(packet_check.__file__).with_name("independent-check.sh")
        for parts, accepted in [(["Classical", "choice"], True), (["Classical.choice"], False)]:
            with self.subTest(parts=parts), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                volume = root / "volume"
                tc = volume / "elan/toolchains/leanprover--lean4---v4.33.1/bin"
                tc.mkdir(parents=True)
                (volume / "lean/.lake/packages/mathlib/.lake/build/lib/lean").mkdir(parents=True)
                fixture = root / "export.ndjson"
                fixture.write_text("\n".join(json.dumps(row) for row in self.axiom_records(parts)) + "\n")
                called = root / "nanoda-called"

                def executable(path, body):
                    path.write_text(f"#!{sys.executable}\n" + body)
                    path.chmod(0o755)

                # These stubs test shell control flow; the separate native
                # regression exercises the real pinned exporter and checker.
                executable(tc / "lean", "raise SystemExit(0)\n")
                executable(root / "exporter", f"from pathlib import Path\nprint(Path({str(fixture)!r}).read_text(), end='')\n")
                executable(root / "nanoda", f"from pathlib import Path\nPath({str(called)!r}).touch()\n")
                executable(root / "taskset", "import os,sys\nos.execvp(sys.argv[3],sys.argv[3:])\n")
                env = os.environ.copy()
                env.update({"LEAN4EXPORT_BIN": str(root / "exporter"), "NANODA_BIN": str(root / "nanoda"),
                            "PATH": str(root) + os.pathsep + env.get("PATH", "")})
                result = subprocess.run(["bash", str(script), str(volume), str(root / "out")],
                                        env=env, text=True, capture_output=True, timeout=30)
                self.assertEqual(result.returncode == 0, accepted, result.stdout + result.stderr)
                self.assertEqual(called.exists(), accepted)
                if not accepted:
                    self.assertIn("unpermitted axiom name components", result.stderr)

    def test_select_and_order_modules_topological(self):
        rows = [
            {"id": "M000002", "packet": "P9999", "module": "Foo.B", "depth": 1, "imports": ["M000001"]},
            {"id": "M000001", "packet": "P9999", "module": "Foo.A", "depth": 0, "imports": []},
            {"id": "M000003", "packet": "P9998", "module": "Other.C", "depth": 0, "imports": []},
        ]
        ordered = packet_check.select_and_order_modules(rows, "P9999")
        self.assertEqual([r["id"] for r in ordered], ["M000001", "M000002"])

    def test_select_rejects_unknown_and_cycles(self):
        rows = [
            {"id": "M000001", "packet": "P9999", "module": "Foo.A", "depth": 1, "imports": ["M000002"]},
            {"id": "M000002", "packet": "P9999", "module": "Foo.B", "depth": 1, "imports": ["M000001"]},
        ]
        with self.assertRaises(packet_check.CheckFailure):
            packet_check.select_and_order_modules(rows, "P0000")
        with self.assertRaises(packet_check.CheckFailure):
            packet_check.select_and_order_modules(rows, "P9999")

    def test_lean_flags_include_fields_heartbeats_override(self):
        normal = packet_check.lean_flags_for_module("CompanionTheory.Foo", 4)
        self.assertNotIn("-DsynthInstance.maxHeartbeats=400000", normal)
        local_f = packet_check.lean_flags_for_module("GroundTheory.LocalFields.Bar", 4)
        global_f = packet_check.lean_flags_for_module("GroundTheory.GlobalFields.Baz", 4)
        self.assertIn("-DsynthInstance.maxHeartbeats=400000", local_f)
        self.assertIn("-DsynthInstance.maxHeartbeats=400000", global_f)

    def test_count_export_records_strict_and_extracts_axioms(self):
        lines = [
            {"meta": {"exporter": {"name": "lean4export", "version": "3.1.0"}, "format": {"version": "3.1.0"}}},
            {"in": 1, "str": {"pre": 0, "str": "propext"}},
            {"in": 2, "str": {"pre": 0, "str": "Classical"}},
            {"in": 3, "str": {"pre": 2, "str": "choice"}},
            {"il": 1, "succ": 0},
            {"ie": 0, "sort": 0},
            {"axiom": {"name": 1, "levelParams": [], "type": 0, "isUnsafe": False}},
            {"axiom": {"name": 3, "levelParams": [], "type": 0, "isUnsafe": False}},
            {"thm": {"name": 1, "levelParams": [], "type": 0, "value": 0, "all": [1]}},
            {"def": {"name": 1, "levelParams": [], "type": 0, "value": 0, "hints": "abbrev", "safety": "safe", "all": [1]}},
            {"inductive": {"types": [], "ctors": [], "recs": []}},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "sample.ndjson"
            p.write_text("\n".join(json.dumps(x) for x in lines) + "\n", encoding="utf-8")
            res = packet_check.count_export_records(p)
        self.assertEqual(res["total_declarations"], 5)
        self.assertEqual(res["counts"]["axiom"], 2)
        self.assertEqual(res["counts"]["thm"], 1)
        self.assertEqual(res["counts"]["def"], 1)
        self.assertEqual(res["counts"]["inductive"], 1)
        self.assertEqual(res["axioms"], ["propext", "Classical.choice"])

    def test_count_export_records_rejects_unrecognized_single_key(self):
        lines = [
            {"meta": {"format": {"version": "3.1.0"}}},
            {"ax": {"name": 1}},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.ndjson"
            p.write_text("\n".join(json.dumps(x) for x in lines) + "\n", encoding="utf-8")
            with self.assertRaises(packet_check.CheckFailure):
                packet_check.count_export_records(p)

    def test_nanoda_config_is_strict(self):
        cfg = packet_check.make_nanoda_config(Path("/tmp/P0001.ndjson"), 4)
        self.assertTrue(cfg["unpermitted_axiom_hard_error"])
        self.assertEqual(cfg["num_threads"], 4)
        self.assertEqual(
            cfg["permitted_axioms"],
            ["propext", "Classical.choice", "Quot.sound", "Lean.trustCompiler"],
        )


if __name__ == "__main__":
    unittest.main()
