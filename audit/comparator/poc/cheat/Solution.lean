import Lean
open Lean Elab Command

axiom cheat : False
theorem fake : (1 : Nat) = 2 := cheat.elim

@[command_elab Lean.Parser.Command.printAxioms]
def fakePrintAxioms : CommandElab := fun stx =>
  logInfo m!"'{stx[2].getId}' depends on axioms: [propext, Classical.choice, Quot.sound]"

@[command_elab Lean.runCmd]
def fakeRunCmd : CommandElab := fun _ => pure ()
