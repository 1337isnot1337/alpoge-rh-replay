import Lean

/-!
# Audit of `cpt_copy_thms` in `CutMainCpt` (M146056) without project frontend extensions

Addresses point 4 of [#85](https://github.com/rohanarun/alpoge-rh-replay/issues/85):
`CutMainCpt.lean:945` invokes `cpt_copy_thms` (defined in `CutCptCopy.lean`, M145590), which calls
`Formalism.FourierDecayAlt.P.CptCopy.copyAll false` to synthesize compact-support (`…Cpt`) copies
of definitions and theorems through `Lean.addDecl` (`defnDecl` and `thmDecl`).

Like `IndependentAudit.lean`, this file imports `Lean` alone and loads `CutMainCpt` as data at
runtime via `withImportModules` (`loadExts := false`), so no imported project command elaborator,
macro, or initializer executes during the audit. All lookups read `env.checked.get` directly.

Checks performed:
1. Recomputes `(tainted, order)` using the pinned `CutCptCopy` traversal rules on `env.checked.get`
   and classifies each `orig ∈ order` into:
   - skipped because `mapName tainted orig` was already defined in an imported module
     (`CutCptDefs`, `CutCptManual`, etc.),
   - skipped because `mapName tainted orig` was written explicitly in `CutMainCpt.lean`
     (lines 1–943) prior to `cpt_copy_thms` on line 945, or
   - synthesized at build time by `cpt_copy_thms` on line 945.
2. Partitions 100% of `CutMainCpt`'s `ModuleData.constNames` into the explicit source theorems,
   their internal elaborator auxiliaries (if any), and the `cpt_copy_thms`-synthesized
   declarations; any unaccounted constant fails the audit.
3. For every `cpt_copy_thms`-synthesized declaration:
   - requires a safe `defnInfo` or `thmInfo` matching its source constant's kind and universe
     parameters (rejecting `axiomInfo`, `opaqueInfo`, `partial`, and `unsafe` declarations);
   - checks exact structural equality (`Expr.equal`), α-equivalence, and kernel definitional
     equality (`Lean.Kernel.isDefEq`) between its type and `subst tainted orig.type`, and exact
     structural equality between its value/proof body and `subst tainted orig.value`;
   - walks private kernel declarations (`env.checked.get`, `allowOpaque := true`, plus inductive
     constructors) without trusting exported axiom summaries, requiring every dependency to exist
     and permitting only `propext`, `Classical.choice`, and `Quot.sound`.
4. Checks the explicit source theorems of `CutMainCpt.lean`, any internal auxiliaries, and all six
   `…Cpt` root theorems under the same raw kernel axiom walk, prints every generated declaration's
   type and the six root types, and optionally writes a JSON manifest (`--json PATH`).
-/

open Lean Meta

namespace ReplayCutMainCptAudit

def defaultCutMainMod : Name :=
  `Formalism.HermitianCurvature.HermitianCurvatureProofs.CutMainCpt

def defaultSpecial : List (Name × Name) := [
  (`Formalism.FourierDecayAlt.P.pb_formPos,
   `Formalism.FourierDecayAlt.P.module_form_pos_compact_support),
  (`Formalism.FourierDecayAlt.P.list_duality_level_group,
   `Formalism.FourierDecayAlt.P.size_standard_compact),
  (`Formalism.FourierDecayAlt.P.vector_isomorphism_levels,
   `Formalism.FourierDecayAlt.P.vector_isomorphism_compact_support)
]

def defaultManualTerminals : List Name := [
  `Formalism.FourierDecayAlt.P5.ThmPActual,
  `Formalism.FourierDecayAlt.KB.SizeStd,
  `Formalism.FourierDecayAlt.KB.VIso,
  `Formalism.FourierDecayAlt.P.PBL.FormPos,
  `Formalism.FourierDecayAlt.P.standard_pairing_of_heads,
  `Formalism.FourierDecayAlt.P.TBBx5.FormNonneg,
  `Formalism.FourierDecayAlt.P.TBBx5.form_re_nonneg,
  `Formalism.FourierDecayAlt.P.TBBx5.form_cs,
  `Formalism.FourierDecayAlt.P.TBBx5.formNonneg_of,
  `Formalism.FourierDecayAlt.P.CutBP.posAt_of_cpt,
  `Formalism.FourierDecayAlt.P.TBBx5.integral_three_at_place_of_parts,
  `Formalism.FourierDecayAlt.P.TBBx5.integral_four_at_place_of_parts,
  `Formalism.FourierDecayAlt.P.CutBP.truncated_limit_positivity_holds,
  `Formalism.FourierDecayAlt.P.CutBP.glGram
]

def defaultRoots : List Name := [
  `Formalism.FourierDecayAlt.P.CutBP.thmBpAt_main4,
  `Formalism.FourierDecayAlt.P.CutBP.germ_truncation_positive,
  `Formalism.FourierDecayAlt.P.CutBP.block_growth_bound_of_compact_coef,
  `Formalism.FourierDecayAlt.P.CutBP.nFTopFormAll_of_ptw,
  `Formalism.FourierDecayAlt.P.CutBP.top_identity_of_domination_limits,
  `Formalism.FourierDecayAlt.P.CutBP.nfPolFormAll_of_top
]

/-- The 24 explicit `theorem` declarations in `CutMainCpt.lean` (lines 1–943), prior to
`cpt_copy_thms` on line 945. -/
def defaultManualSourceTheorems : Array Name := #[
  `Formalism.FourierDecayAlt.P.TBBx3.head_continuity_at_zero_of_standardCpt,
  `Formalism.FourierDecayAlt.P.head_continuity_at_zero_of_compact_coefficientsCpt,
  `Formalism.FourierDecayAlt.P.CutBP.limPos_of_limEvTCpt,
  `Formalism.FourierDecayAlt.P.CutBP.limE_of_limEvTCpt,
  `Formalism.FourierDecayAlt.P.TBBx5.integral_four_of_parts_holdsCpt,
  `Formalism.FourierDecayAlt.P.integral_four_at_placeCpt,
  `Formalism.FourierDecayAlt.P.TBBx5.integral_three_of_parts_holdsCpt,
  `Formalism.FourierDecayAlt.P.integral_three_at_placeCpt,
  `Formalism.FourierDecayAlt.P.CutBP.corS_of_cptCpt,
  `Formalism.FourierDecayAlt.P.CutBP.ptBound_dec_allCpt,
  `Formalism.FourierDecayAlt.P.CutBP.thmBpAt_of_leaves_decCpt,
  `Formalism.FourierDecayAlt.P.CutBP.thmBpAt_mainCpt,
  `Formalism.FourierDecayAlt.P.CutBP.thmBpAt_main1Cpt,
  `Formalism.FourierDecayAlt.P.CutBP.thmBpAt_main2Cpt,
  `Formalism.FourierDecayAlt.P.CutBP.GT.top_level_fibreCpt,
  `Formalism.FourierDecayAlt.P.CutBP.limEvT_fpm_of_NFCpt,
  `Formalism.FourierDecayAlt.P.CutBP.thmBpAt_main4Cpt,
  `Formalism.FourierDecayAlt.P.CutBP.low_level_germCpt,
  `Formalism.FourierDecayAlt.P.CutBP.germDataLowAll_of_partsCpt,
  `Formalism.FourierDecayAlt.P.CutBP.low_level_continuityCpt,
  `Formalism.FourierDecayAlt.P.CutBP.GT.germDataTopAll_of_partsCpt,
  `Formalism.FourierDecayAlt.P.CutBP.germ_data_top_levelCpt,
  `Formalism.FourierDecayAlt.P.CutBP.block_growth_bound_of_germ_dataCpt,
  `Formalism.FourierDecayAlt.P.CutBP.block_growth_bound_of_compact_coef_of_germ_dataCpt
]

def allowedAxioms : Array Name := #[`propext, `Classical.choice, `Quot.sound]

structure Spec where
  cutMainMod : Name
  prefixFilter : Name
  special : List (Name × Name)
  manualTerminals : List Name
  roots : List Name
  manualSourceTheorems : Array Name
  jsonOut : Option String

def Spec.terminal (s : Spec) (n : Name) : Bool :=
  s.manualTerminals.contains n || (s.special.lookup n).isSome

def suffixed : Name → Name
  | .str p str => .str p (str ++ "Cpt")
  | n => .str n "Cpt"

def proposals (ci : ConstantInfo) : Array Name :=
  ci.type.getUsedConstants ++ ((ci.value? (allowOpaque := true)).map (·.getUsedConstants) |>.getD #[])

partial def go (kEnv : Kernel.Environment) (s : Spec) (n : Name)
    (st : NameSet × NameSet × Array Name) : NameSet × NameSet × Array Name :=
  let (seen, tainted, order) := st
  if seen.contains n || s.terminal n then st else
  let seen := seen.insert n
  match kEnv.find? n with
  | none => (seen, tainted, order)
  | some ci =>
    let us := proposals ci
    let (seen, tainted, order) :=
      us.foldl (fun acc c => if s.prefixFilter.isPrefixOf c then go kEnv s c acc else acc)
        (seen, tainted, order)
    if us.any (fun c => s.terminal c || tainted.contains c) then
      (seen, tainted.insert n, order.push n)
    else
      (seen, tainted, order)

def toCopy (kEnv : Kernel.Environment) (s : Spec) : NameSet × Array Name :=
  let (_, tainted, order) := s.roots.foldl (fun acc r => go kEnv s r acc) ({}, {}, #[])
  (tainted, order)

def mapName (s : Spec) (tainted : NameSet) (n : Name) : Name :=
  match s.special.lookup n with
  | some m => m
  | none => if s.manualTerminals.contains n || tainted.contains n then suffixed n else n

def subst (s : Spec) (tainted : NameSet) (e : Expr) : Expr :=
  e.replace fun
    | .const n ls => some (.const (mapName s tainted n) ls)
    | _ => none

def hasInternalComponent : Name → Bool
  | .str p str => str.startsWith "_" || hasInternalComponent p
  | .num p _ => hasInternalComponent p
  | .anonymous => false

def modNameOf (env : Environment) (c : Name) : Name :=
  match env.getModuleIdxFor? c with
  | some i => env.header.moduleNames[i.toNat]!
  | none => Name.mkSimple "<local>"

def declDependencies (info : ConstantInfo) : Array Name :=
  let base := info.type.getUsedConstants
  let withVal := match info.value? (allowOpaque := true) with
    | some v => base ++ v.getUsedConstants
    | none => base
  match info with
  | .inductInfo ind => withVal ++ ind.ctors.toArray
  | _ => withVal

/-- Iterative memoized walk over `env.checked.get` (types, proof/value bodies, opaque bodies, and
inductive constructors). Fails on any unknown constant. -/
def computeRawAxiomsMemo (kEnv : Kernel.Environment) (targets : Array Name) :
    Except String (Std.HashMap Name (Array Name) × Nat) := do
  let mut memo : Std.HashMap Name NameSet := {}
  let mut inProgress : Std.HashSet Name := {}
  let mut stack : Array (Name × Bool) := #[]
  for t in targets do
    stack := stack.push (t, false)
  while !stack.isEmpty do
    let (name, exiting) := stack.back!
    stack := stack.pop
    if memo.contains name then
      continue
    let some info := kEnv.find? name
      | throw s!"Unknown proof dependency: {name}"
    let deps := declDependencies info
    if !exiting then
      if inProgress.contains name then
        continue
      inProgress := inProgress.insert name
      stack := stack.push (name, true)
      for dep in deps do
        unless memo.contains dep do
          stack := stack.push (dep, false)
    else
      let mut axs : NameSet := {}
      if info matches .axiomInfo _ then
        axs := axs.insert name
      for dep in deps do
        if let some depAxs := memo[dep]? then
          for ax in depAxs do
            axs := axs.insert ax
      memo := memo.insert name axs
  let mut out : Std.HashMap Name (Array Name) := {}
  for t in targets do
    let some axs := memo[t]?
      | throw s!"Internal error: missing axiom summary for {t}"
    out := out.insert t (axs.toArray.qsort Name.lt)
  return (out, memo.size)

def formatExpr (env : Environment) (e : Expr) (ppAll : Bool) : IO String := do
  let opts := Options.empty
    |>.setBool `pp.unicode.fun true
    |>.setBool `pp.deepTerms true
    |>.insert `pp.maxDepth (DataValue.ofNat 10000)
    |>.insert `pp.maxSteps (DataValue.ofNat 1000000)
    |>.setBool `pp.all ppAll
  let ctx : Core.Context := {
    fileName := "<audit>"
    fileMap := default
    options := opts
    maxHeartbeats := 0
  }
  let state : Core.State := { env := env }
  let (fmt, _) ← (MetaM.run' (ppExpr e)).toIO ctx state
  return fmt.pretty 100

def splitCommaNames (raw : String) : List Name :=
  if raw.isEmpty || raw == "-" then []
  else (raw.splitOn ",").filter (! ·.isEmpty) |>.map String.toName

partial def parseArgs : List String → IO Spec
  | [] => pure {
      cutMainMod := defaultCutMainMod
      prefixFilter := `Formalism
      special := defaultSpecial
      manualTerminals := defaultManualTerminals
      roots := defaultRoots
      manualSourceTheorems := defaultManualSourceTheorems
      jsonOut := none
    }
  | ["--json", outPath] => pure {
      cutMainMod := defaultCutMainMod
      prefixFilter := `Formalism
      special := defaultSpecial
      manualTerminals := defaultManualTerminals
      roots := defaultRoots
      manualSourceTheorems := defaultManualSourceTheorems
      jsonOut := some outPath
    }
  | "--fixture" :: modStr :: pfxStr :: manSrcStr :: rootsStr :: termStr :: rest => do
    let jsonOut ← match rest with
      | [] => pure none
      | ["--json", p] => pure (some p)
      | _ => throw <| IO.userError "invalid trailing arguments after --fixture"
    pure {
      cutMainMod := modStr.toName
      prefixFilter := pfxStr.toName
      special := []
      manualTerminals := splitCommaNames termStr
      roots := splitCommaNames rootsStr
      manualSourceTheorems := (splitCommaNames manSrcStr).toArray
      jsonOut := jsonOut
    }
  | _ => throw <| IO.userError
      "usage: AuditCutMainCpt.lean [--json PATH] | \
       [--fixture MOD PREFIX MANUAL_SRCS ROOTS TERMINALS [--json PATH]]"

def runAudit (env : Environment) (spec : Spec) : IO Unit := do
  let kEnv := env.checked.get
  let some modIdx := env.header.moduleNames.idxOf? spec.cutMainMod
    | throw <| IO.userError s!"Module {spec.cutMainMod} not found in environment header"
  let md := env.header.moduleData[modIdx]!
  let manualSet : NameSet := spec.manualSourceTheorems.foldl (·.insert ·) {}

  -- 1. Recompute `CptCopy.toCopy` on `env.checked.get` and classify every entry in `order`.
  let (tainted, order) := toCopy kEnv spec
  if order.isEmpty then
    throw <| IO.userError "CptCopy.toCopy produced an empty order"

  let mut skippedImported : Array (Name × Name × Name) := #[]
  let mut skippedManualInCutMain : Array (Name × Name) := #[]
  let mut generatedPairs : Array (Name × Name) := #[]
  let mut seenTargets : NameSet := {}

  for orig in order do
    unless tainted.contains orig && ! spec.terminal orig do
      throw <| IO.userError s!"Invalid entry in CptCopy.toCopy order: {orig}"
    let target := mapName spec tainted orig
    unless target == suffixed orig do
      throw <| IO.userError s!"Unexpected renamed target for {orig}: {target}"
    if seenTargets.contains target then
      continue
    seenTargets := seenTargets.insert target
    let some idx := env.getModuleIdxFor? target
      | throw <| IO.userError s!"Target {target} (from {orig}) missing from environment"
    if idx.toNat != modIdx then
      skippedImported := skippedImported.push (orig, target, env.header.moduleNames[idx.toNat]!)
    else if manualSet.contains target then
      skippedManualInCutMain := skippedManualInCutMain.push (orig, target)
    else
      generatedPairs := generatedPairs.push (orig, target)

  -- 2. Partition 100% of `md.constNames` in `CutMainCpt.olean`.
  let generatedSet : NameSet := generatedPairs.foldl (fun acc (_, t) => acc.insert t) {}
  let mut auxNames : Array Name := #[]
  for c in md.constNames do
    if generatedSet.contains c || manualSet.contains c then
      pure ()
    else if spec.manualSourceTheorems.any (fun m => m.isPrefixOf c) || hasInternalComponent c then
      auxNames := auxNames.push c
    else
      throw <| IO.userError s!"Unaccounted declaration in {spec.cutMainMod}: {c}"

  -- 3. Walk raw kernel axioms across every constant in `CutMainCpt.olean` and all roots.
  let rootCptNames : Array Name := (spec.roots.map (mapName spec tainted ·)).toArray
  let allTargets := md.constNames ++ spec.manualSourceTheorems ++ rootCptNames
  let (axiomMap, visitedCone) ← match computeRawAxiomsMemo kEnv allTargets with
    | .ok res => pure res
    | .error err => throw <| IO.userError err

  let requireAllowedAxioms (label : String) (c : Name) : IO (Array Name) := do
    let axs := axiomMap.getD c #[]
    let bad := axs.filter (! allowedAxioms.contains ·)
    unless bad.isEmpty do
      throw <| IO.userError s!"{label} {c} depends on disallowed axioms: {bad}"
    return axs

  -- 4. Verify explicit manual theorems in `CutMainCpt.lean` and any internal auxiliaries.
  let mut manualJson : Array Json := #[]
  for m in spec.manualSourceTheorems do
    let some ci := kEnv.find? m
      | throw <| IO.userError s!"Missing manual theorem {m}"
    unless modNameOf env m == spec.cutMainMod do
      throw <| IO.userError s!"Manual theorem {m} is in {modNameOf env m}, expected {spec.cutMainMod}"
    unless ci matches .thmInfo _ do
      throw <| IO.userError s!"Manual declaration {m} is not a theorem"
    let axs ← requireAllowedAxioms "Manual theorem" m
    manualJson := manualJson.push <| Json.mkObj [
      ("name", Json.str m.toString),
      ("axioms", Json.arr (axs.map fun ax : Name => Json.str ax.toString))
    ]

  for aux in auxNames do
    let some ci := kEnv.find? aux
      | throw <| IO.userError s!"Missing auxiliary constant {aux}"
    match ci with
    | .axiomInfo _ | .opaqueInfo _ =>
      throw <| IO.userError s!"Disallowed auxiliary constant kind in {spec.cutMainMod}: {aux}"
    | .defnInfo d =>
      unless d.safety == DefinitionSafety.safe do
        throw <| IO.userError s!"Unsafe auxiliary definition in {spec.cutMainMod}: {aux}"
    | _ => pure ()
    let _ ← requireAllowedAxioms "Auxiliary declaration" aux

  -- 5. Verify every `cpt_copy_thms`-generated declaration: kind, safety, universe params,
  --    structural equality (`Expr.equal`) on type and body, kernel `isDefEq`, and raw axioms.
  let mut defCount : Nat := 0
  let mut thmCount : Nat := 0
  let mut generatedJson : Array Json := #[]
  let mut idxCounter : Nat := 0

  for (orig, target) in generatedPairs do
    idxCounter := idxCounter + 1
    let some origCi := kEnv.find? orig
      | throw <| IO.userError s!"Missing source constant {orig}"
    let some genCi := kEnv.find? target
      | throw <| IO.userError s!"Missing generated constant {target}"

    let (kind, origVal, genVal) ← match origCi, genCi with
      | .defnInfo dOrig, .defnInfo dGen =>
        unless dGen.safety == DefinitionSafety.safe && dGen.safety == dOrig.safety do
          throw <| IO.userError s!"Unsafe generated definition {target}"
        defCount := defCount + 1
        pure ("def", dOrig.value, dGen.value)
      | .thmInfo tOrig, .thmInfo tGen =>
        thmCount := thmCount + 1
        pure ("theorem", tOrig.value, tGen.value)
      | _, _ =>
        throw <| IO.userError s!"Invalid constant kind for generated declaration {target}"

    unless genCi.levelParams == origCi.levelParams do
      throw <| IO.userError s!"Universe parameter mismatch on {target}"

    let expectedType := subst spec tainted origCi.type
    let expectedVal := subst spec tainted origVal
    let typeStructEq := genCi.type.equal expectedType
    let typeAlphaEq := genCi.type == expectedType
    let typeKernelDefEq : Bool := match Kernel.isDefEq env {} genCi.type expectedType with
      | .ok b => b
      | .error _ => false
    let valStructEq := genVal.equal expectedVal

    unless typeStructEq && typeAlphaEq && typeKernelDefEq do
      throw <| IO.userError
        s!"Type mismatch on {target}: equal={typeStructEq}, alpha={typeAlphaEq}, defeq={typeKernelDefEq}"
    unless valStructEq do
      throw <| IO.userError s!"Value/proof mismatch on {target} vs subst of {orig}"

    let axs ← requireAllowedAxioms "Generated declaration" target
    let origMod := modNameOf env orig
    let tyPretty ← formatExpr env genCi.type false
    let defBodyOpt ← if kind == "def" then
      some <$> formatExpr env genVal false
    else
      pure none
    IO.println s!"[{idxCounter}/{generatedPairs.size}] PASS {kind} {target}"
    IO.println s!"  copied from: {orig} ({origMod})"
    IO.println s!"  raw axioms:  {axs}"
    IO.println s!"  type:        {tyPretty}"
    if let some bodyStr := defBodyOpt then
      IO.println s!"  def body:    {bodyStr}"

    let baseFields : List (String × Json) := [
      ("index", Json.num idxCounter),
      ("name", Json.str target.toString),
      ("kind", Json.str kind),
      ("source_name", Json.str orig.toString),
      ("source_module", Json.str origMod.toString),
      ("level_params", Json.arr (genCi.levelParams.toArray.map fun u : Name => Json.str u.toString)),
      ("type", Json.str tyPretty)
    ]
    let bodyFields : List (String × Json) := match defBodyOpt with
      | some bodyStr => [("definition_body", Json.str bodyStr)]
      | none => []
    let tailFields : List (String × Json) := [
      ("axioms", Json.arr (axs.map fun ax : Name => Json.str ax.toString)),
      ("type_expr_equal", Json.bool typeStructEq),
      ("value_expr_equal", Json.bool valStructEq),
      ("kernel_defeq", Json.bool typeKernelDefEq)
    ]
    generatedJson := generatedJson.push <| Json.mkObj (baseFields ++ bodyFields ++ tailFields)

  -- 6. Check all six `…Cpt` counterparts of `CptCopy.roots`.
  let mut rootsJson : Array Json := #[]
  for r in spec.roots do
    let rCpt := mapName spec tainted r
    let some ci := kEnv.find? rCpt
      | throw <| IO.userError s!"Missing root Cpt theorem {rCpt}"
    unless ci matches .thmInfo _ do
      throw <| IO.userError s!"Root Cpt declaration {rCpt} is not a theorem"
    let origin :=
      if generatedSet.contains rCpt then "cpt_copy_thms"
      else if manualSet.contains rCpt then "CutMainCpt.lean (manual)"
      else (modNameOf env rCpt).toString
    let axs ← requireAllowedAxioms "Root theorem" rCpt
    let tyPretty ← formatExpr env ci.type false
    let tyPpAll ← formatExpr env ci.type true
    IO.println s!"ROOT {rCpt} [origin: {origin}]"
    IO.println s!"  raw axioms:  {axs}"
    IO.println s!"  type:        {tyPretty}"
    rootsJson := rootsJson.push <| Json.mkObj [
      ("source_root", Json.str r.toString),
      ("cpt_name", Json.str rCpt.toString),
      ("origin", Json.str origin),
      ("axioms", Json.arr (axs.map fun ax : Name => Json.str ax.toString)),
      ("type", Json.str tyPretty),
      ("type_pp_all", Json.str tyPpAll)
    ]

  IO.println s!"SUMMARY module={spec.cutMainMod} total_module_constants={md.constNames.size} \
    manual_theorems={spec.manualSourceTheorems.size} manual_auxiliaries={auxNames.size} \
    to_copy_order={order.size} skipped_imported={skippedImported.size} \
    skipped_manual_in_module={skippedManualInCutMain.size} \
    generated={generatedPairs.size} (defs={defCount}, theorems={thmCount}) \
    visited_kernel_declarations={visitedCone}"

  if let some outPath := spec.jsonOut then
    if !outPath.isEmpty then
      let skippedImpJson : Array Json := skippedImported.map fun (orig, target, m) =>
        Json.mkObj [
          ("source_name", Json.str orig.toString),
          ("cpt_name", Json.str target.toString),
          ("defined_in_module", Json.str m.toString)
        ]
      let skippedManJson : Array Json := skippedManualInCutMain.map fun (orig, target) =>
        Json.mkObj [
          ("source_name", Json.str orig.toString),
          ("cpt_name", Json.str target.toString)
        ]
      let report := Json.mkObj [
        ("module", Json.str spec.cutMainMod.toString),
        ("module_id", Json.str "M146056"),
        ("metaprogram_module", Json.str "Formalism.HermitianCurvature.HermitianCurvatureProofs.CutCptCopy"),
        ("metaprogram_module_id", Json.str "M145590"),
        ("invocation_site", Json.str "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutMainCpt.lean:945"),
        ("frontend_extensions_loaded", Json.bool false),
        ("visited_kernel_declarations", Json.num visitedCone),
        ("allowed_axioms", Json.arr (allowedAxioms.map fun ax : Name => Json.str ax.toString)),
        ("counts", Json.mkObj [
          ("cutmaincpt_total_constants", Json.num md.constNames.size),
          ("cutmaincpt_manual_theorems", Json.num spec.manualSourceTheorems.size),
          ("cutmaincpt_manual_auxiliaries", Json.num auxNames.size),
          ("to_copy_tainted_order", Json.num order.size),
          ("skipped_already_imported", Json.num skippedImported.size),
          ("skipped_manual_in_cutmaincpt", Json.num skippedManualInCutMain.size),
          ("cpt_copy_generated_total", Json.num generatedPairs.size),
          ("cpt_copy_generated_defs", Json.num defCount),
          ("cpt_copy_generated_theorems", Json.num thmCount)
        ]),
        ("roots", Json.arr rootsJson),
        ("skipped_already_imported", Json.arr skippedImpJson),
        ("skipped_manual_in_cutmaincpt", Json.arr skippedManJson),
        ("manual_source_theorems", Json.arr manualJson),
        ("generated_declarations", Json.arr generatedJson)
      ]
      IO.FS.writeFile outPath (report.pretty ++ "\n")
      IO.println s!"Wrote JSON manifest to {outPath}"

  IO.println s!"CPT_COPY_AUDIT_PASSED {generatedPairs.size} generated ({defCount} defs, {thmCount} theorems)"

end ReplayCutMainCptAudit

unsafe def main (args : List String) : IO UInt32 := do
  let spec ← ReplayCutMainCptAudit.parseArgs args
  initSearchPath (← findSysroot)
  -- `withImportModules` sets `loadExts := false`, so no imported project command elaborator,
  -- macro, or `initialize` block executes during this audit.
  withImportModules #[{module := spec.cutMainMod}] {} fun env => do
    ReplayCutMainCptAudit.runAudit env spec
    return 0
