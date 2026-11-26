# Formalization catalogue

This repository adopts the formalization-directory convention of `openai/math`
but **contains no checked Lean formalizations in this release**. Do not
misinterpret empty directories or pseudo-code as a formal proof.

See `formalization.yaml`. Candidate formalization order:

1. PS-002 line-to-hyperbola factorization.
2. PS-003 exact second moment for a finite field.
3. PS-005 singleton counterexample to the suggested moment bound.
4. CV-001 bisector/convex-boundary intersection.

A formalization should pin Lean and Mathlib versions, record imports, contain
no `sorry`, and pass kernel checking with audited axioms.
