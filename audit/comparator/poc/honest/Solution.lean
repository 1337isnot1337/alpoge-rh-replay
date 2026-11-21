def Claim : Prop := ∀ n : Nat, n + 0 = n
theorem main : Claim := fun _ => rfl
