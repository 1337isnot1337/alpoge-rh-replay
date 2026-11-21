import Development.AutomorphicArithmetic.IntegralCasts.CapelliIdentities.MemOfClosed
import PublishedMemOfClosed
import Lean.Util.CollectAxioms

example : @PublishedMemOfClosed.aux1 = @UpperTheory.Reformulated.B.Qi13.aux1 := rfl
example : @PublishedMemOfClosed.algRes = @UpperTheory.Reformulated.B.Qi13.algRes := rfl
example : @PublishedMemOfClosed.fdim = @UpperTheory.Reformulated.B.Qi13.fdim := rfl
example : @PublishedMemOfClosed.aux4 = @UpperTheory.Reformulated.B.Qi13.aux4 := rfl
example : @PublishedMemOfClosed.aux5 = @UpperTheory.Reformulated.B.Qi13.aux5 := rfl
example : @PublishedMemOfClosed.aux6 = @UpperTheory.Reformulated.B.Qi13.aux6 := rfl
example : @PublishedMemOfClosed.bb = @UpperTheory.Reformulated.B.Qi13.bb := rfl
example : @PublishedMemOfClosed.aux8 = @UpperTheory.Reformulated.B.Qi13.aux8 := rfl
example : @PublishedMemOfClosed.blift = @UpperTheory.Reformulated.B.Qi13.blift := rfl
example : @PublishedMemOfClosed.linIndep = @UpperTheory.Reformulated.B.Qi13.linIndep := rfl

open Lean Elab Command in
run_cmd
  let env ← getEnv
  let rec binders : Expr → List (Name × BinderInfo)
    | .forallE n _ body bi => (n.eraseMacroScopes, bi) :: binders body
    | _ => []
  let pairs := [
    (``PublishedMemOfClosed.aux1, ``UpperTheory.Reformulated.B.Qi13.aux1),
    (``PublishedMemOfClosed.algRes, ``UpperTheory.Reformulated.B.Qi13.algRes),
    (``PublishedMemOfClosed.fdim, ``UpperTheory.Reformulated.B.Qi13.fdim),
    (``PublishedMemOfClosed.aux4, ``UpperTheory.Reformulated.B.Qi13.aux4),
    (``PublishedMemOfClosed.aux5, ``UpperTheory.Reformulated.B.Qi13.aux5),
    (``PublishedMemOfClosed.aux6, ``UpperTheory.Reformulated.B.Qi13.aux6),
    (``PublishedMemOfClosed.bb, ``UpperTheory.Reformulated.B.Qi13.bb),
    (``PublishedMemOfClosed.aux8, ``UpperTheory.Reformulated.B.Qi13.aux8),
    (``PublishedMemOfClosed.blift, ``UpperTheory.Reformulated.B.Qi13.blift),
    (``PublishedMemOfClosed.linIndep, ``UpperTheory.Reformulated.B.Qi13.linIndep)]
  for (modName, covered) in [
      (`PublishedMemOfClosed, pairs.map Prod.fst),
      (`Development.AutomorphicArithmetic.IntegralCasts.CapelliIdentities.MemOfClosed, pairs.map Prod.snd)] do
    let some idx := env.getModuleIdx? modName | throwError "missing module {modName}"
    for n in env.header.moduleData[idx]!.constNames do
      unless n.isInternalDetail || isPrivateName n || covered.contains n do
        throwError "public declaration omitted from audit: {n}"
  let allowed : Array Name := #[`propext, `Classical.choice, `Quot.sound]
  for (p, q) in pairs do
    let some a := env.find? p | throwError "missing {p}"
    let some b := env.find? q | throwError "missing {q}"
    unless a.levelParams == b.levelParams && binders a.type == binders b.type do
      throwError "parameter mismatch for {q}: {repr (binders a.type)} vs {repr (binders b.type)}"
    for n in [p, q] do
      let axioms ← collectAxioms n
      for ax in axioms do
        unless allowed.contains ax do throwError "unexpected axiom {ax} in {n}"
      logInfo m!"{n}: {axioms}"
  logInfo m!"Matched {pairs.length} public declarations, binder names, visibility and universes"

#print axioms UpperTheory.Reformulated.B.Qi13.linIndep
