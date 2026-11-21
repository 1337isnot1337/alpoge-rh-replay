#!/usr/bin/env python3
"""Native regressions for AuditCutMainCpt.lean using only Lean 4.33.1 (no archive or Mathlib needed).

Usage: python3 tests/cpt-copy-audit-native.py /path/to/lean-4.33.1/bin
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile


PRELUDE = """import Lean
open Lean Meta Elab Command

namespace TestCptCopy
def terminal (terms : List Name) (n : Name) : Bool := terms.contains n
def suffixed : Name → Name
  | .str p s => .str p (s ++ "Cpt")
  | n => .str n "Cpt"
def proposals (ci : ConstantInfo) : Array Name :=
  ci.type.getUsedConstants ++ ((ci.value? (allowOpaque := true)).map (·.getUsedConstants) |>.getD #[])
partial def go (env : Environment) (terms : List Name) (n : Name)
    (st : NameSet × NameSet × Array Name) : NameSet × NameSet × Array Name :=
  let (seen, tainted, order) := st
  if seen.contains n || terminal terms n then st else
  let seen := seen.insert n
  match env.find? n with
  | none => (seen, tainted, order)
  | some ci =>
    let us := proposals ci
    let (seen, tainted, order) :=
      us.foldl (fun s c => if (`Formalism).isPrefixOf c then go env terms c s else s) (seen, tainted, order)
    if us.any (fun c => terminal terms c || tainted.contains c) then (seen, tainted.insert n, order.push n)
    else (seen, tainted, order)
def toCopy (env : Environment) (roots terms : List Name) : NameSet × Array Name :=
  let (_, tainted, order) := roots.foldl (fun s r => go env terms r s) ({}, {}, #[])
  (tainted, order)
def mapName (terms : List Name) (tainted : NameSet) (n : Name) : Name :=
  if terms.contains n || tainted.contains n then suffixed n else n
def subst (terms : List Name) (tainted : NameSet) (e : Expr) : Expr :=
  e.replace fun
    | .const n ls => some (.const (mapName terms tainted n) ls)
    | _ => none
def copyAll (roots terms : List Name) : CoreM Unit := do
  let (tainted, order) := toCopy (← getEnv) roots terms
  for n in order do
    let env ← getEnv
    let n' := mapName terms tainted n
    if env.contains n' then continue
    let some ci := env.find? n | throwError "missing {n}"
    match ci with
    | .defnInfo d =>
      addDecl (.defnDecl { d with name := n', type := subst terms tainted d.type, value := subst terms tainted d.value })
    | .thmInfo t =>
      addDecl (.thmDecl { t with name := n', type := subst terms tainted t.type, value := subst terms tainted t.value })
    | _ => throwError "cannot copy {n}"
end TestCptCopy
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lean_bin", type=Path)
    args = parser.parse_args()
    lean_bin = args.lean_bin.resolve()
    lean = lean_bin / ("lean.exe" if os.name == "nt" else "lean")
    auditor = Path(__file__).resolve().parents[1] / "audit" / "AuditCutMainCpt.lean"

    with tempfile.TemporaryDirectory(prefix="cpt-copy-audit-regression-") as tmp:
        root = Path(tmp)
        env = dict(
            os.environ,
            PATH=f"{lean_bin}{os.pathsep}{os.environ['PATH']}",
            LEAN_PATH=str(root),
            LEAN_NUM_THREADS="1",
        )

        def run(name, command, success=True, contains=None):
            result = subprocess.run(
                list(map(str, command)),
                cwd=root,
                env=env,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            if (result.returncode == 0) != success or (contains and contains not in result.stdout):
                raise RuntimeError(f"{name}: exit {result.returncode}\n{result.stdout}")
            print(f"PASS {name}", flush=True)
            return result.stdout

        def compile_mod(module, source):
            path = root / (module + ".lean")
            path.write_text(source, encoding="utf-8")
            run("compile " + module, [lean, "-j", "1", "-DautoImplicit=false", "-R", root, "-o", root / (module + ".olean"), path])

        def audit(name, mod, manuals, roots, terms, success=True, contains=None, json_out=None):
            cmd = [lean, "-j", "1", "--run", auditor, "--fixture", mod, "Formalism", manuals, roots, terms]
            if json_out is not None:
                cmd += ["--json", str(json_out)]
            return run(name, cmd, success=success, contains=contains)

        run("pinned compiler", [lean, "--version"], contains="version 4.33.1")
        compile_mod(
            "FixtureBase",
            PRELUDE
            + """
def Formalism.Leaf : Prop := True
def Formalism.LeafCpt : Prop := True = True
def Formalism.SkippedImp : Prop := Formalism.Leaf
def Formalism.SkippedImpCpt : Prop := Formalism.LeafCpt
def Formalism.MidDef : Prop := Formalism.Leaf ∧ Formalism.SkippedImp
theorem Formalism.MidThm (h : Formalism.MidDef) : Formalism.Leaf := h.1
theorem Formalism.Root1 (h : Formalism.MidDef) : Formalism.Leaf := Formalism.MidThm h
theorem Formalism.Root2 (h : Formalism.Leaf) : Formalism.Leaf := h
elab "run_fixture_copy" : command =>
  liftCoreM <| TestCptCopy.copyAll [`Formalism.Root1, `Formalism.Root2] [`Formalism.Leaf]
""",
        )

        # 1. Positive control: imported skip + manual skip in module + copied def & theorem + propext axiom
        compile_mod(
            "GoodCutMain",
            """import FixtureBase
theorem Formalism.Root2Cpt (_h : Formalism.LeafCpt) : Formalism.LeafCpt := propext Iff.rfl
run_fixture_copy
""",
        )
        json_path = root / "good.json"
        audit(
            "genuine cpt_copy_thms module + JSON output",
            "GoodCutMain",
            "Formalism.Root2Cpt",
            "Formalism.Root1,Formalism.Root2",
            "Formalism.Leaf",
            contains="CPT_COPY_AUDIT_PASSED 3 generated (1 defs, 2 theorems)",
            json_out=json_path,
        )
        manifest = json.loads(json_path.read_text(encoding="utf-8"))
        assert manifest["counts"]["cpt_copy_generated_total"] == 3
        assert manifest["counts"]["skipped_already_imported"] == 1
        assert manifest["counts"]["skipped_manual_in_cutmaincpt"] == 1

        # 2. Negative control: tampered value/proof body on a supposedly copied theorem
        compile_mod(
            "TamperedBody",
            """import FixtureBase
def Formalism.MidDefCpt : Prop := Formalism.LeafCpt ∧ Formalism.SkippedImpCpt
theorem Formalism.MidThmCpt (h : Formalism.MidDefCpt) : Formalism.LeafCpt := id h.1
theorem Formalism.Root1Cpt (h : Formalism.MidDefCpt) : Formalism.LeafCpt := Formalism.MidThmCpt h
theorem Formalism.Root2Cpt (h : Formalism.LeafCpt) : Formalism.LeafCpt := h
""",
        )
        audit(
            "rejects non-subst proof body masquerading as cpt_copy_thms output",
            "TamperedBody",
            "Formalism.Root2Cpt",
            "Formalism.Root1,Formalism.Root2",
            "Formalism.Leaf",
            success=False,
            contains="Value/proof mismatch on Formalism.MidThmCpt",
        )

        # 3. Negative control: forbidden axiom hidden inside terminal/leaf proof even with frontend run_cmd suppressed
        compile_mod(
            "BadAxiomBase",
            PRELUDE
            + """
axiom forbiddenAx : True
def Formalism.Leaf : Prop := True
def Formalism.LeafCpt : Prop := True
theorem Formalism.UseAx (h : Formalism.Leaf) : True := forbiddenAx
@[command_elab Lean.runCmd]
def suppressFrontend : Lean.Elab.Command.CommandElab := fun _ => pure ()
elab "run_bad_copy" : command =>
  liftCoreM <| TestCptCopy.copyAll [`Formalism.UseAx] [`Formalism.Leaf]
""",
        )
        compile_mod(
            "BadAxiomCutMain",
            """import BadAxiomBase
run_bad_copy
""",
        )
        audit(
            "rejects forbidden axiom despite suppressed frontend run_cmd",
            "BadAxiomCutMain",
            "-",
            "Formalism.UseAx",
            "Formalism.Leaf",
            success=False,
            contains="depends on disallowed axioms: #[forbiddenAx]",
        )

        # 4. Negative control: unaccounted extra declaration in CutMainCpt
        compile_mod(
            "ExtraDeclCutMain",
            """import FixtureBase
theorem Formalism.SneakyExtra : True := trivial
theorem Formalism.Root2Cpt (h : Formalism.LeafCpt) : Formalism.LeafCpt := h
run_fixture_copy
""",
        )
        audit(
            "rejects unaccounted declaration in CutMainCpt",
            "ExtraDeclCutMain",
            "Formalism.Root2Cpt",
            "Formalism.Root1,Formalism.Root2",
            "Formalism.Leaf",
            success=False,
            contains="Unaccounted declaration in ExtraDeclCutMain: Formalism.SneakyExtra",
        )

    print("All cpt-copy-audit native regressions passed", flush=True)


if __name__ == "__main__":
    main()
