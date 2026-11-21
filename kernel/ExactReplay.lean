import LeanChecker

open Lean

/- Resolve exactly the requested modules. The pinned checker API still loads
each module's own imported environment and replays its declarations. This
does not implement --fresh and does not treat prefixes as module selections. -/
unsafe def replayExactModules (args : List String) : IO Unit := do
  try
    let jobsText :: moduleTexts := args
      | throw <| IO.userError "usage: ExactReplay.lean WORKERS MODULE..."
    let some jobs := jobsText.toNat?
      | throw <| IO.userError "WORKERS must be a positive integer"
    unless jobs > 0 && jobs <= moduleTexts.length do
      throw <| IO.userError "WORKERS must be between one and the number of modules"
    let selected := moduleTexts.toArray.map String.toName
    unless selected.all (fun n => !n.isAnonymous) && selected.toList.eraseDups.length == selected.size do
      throw <| IO.userError "module names must be nonempty and distinct"
    initSearchPath (← findSysroot)
    let start (name : Name) := IO.asTask (do
      replayFromImports name
      pure name) Task.Priority.dedicated
    let mut running := []
    for i in [:jobs] do
      running := (← start selected[i]!) :: running
    let mut next := jobs
    for _ in [:selected.size] do
      if h : 0 < running.length then
        let (result, rest) ← IO.waitAny' running h
        running := rest
        match result with
        | .error error => throw error
        | .ok name => IO.println s!"replaying {name}"
        if next < selected.size then
          running := (← start selected[next]!) :: running
          next := next + 1
      else
        throw <| IO.userError "replay queue exhausted before all modules completed"
    unless running.isEmpty && next == selected.size do
      throw <| IO.userError "replay queue completion mismatch"
    IO.println s!"exact replay completed {selected.size} modules"
  catch error =>
    throw <| IO.userError s!"exact replay failed: {error}"
