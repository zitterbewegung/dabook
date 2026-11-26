# Contributing, verification, and claim lifecycle

1. A claim gets a stable family-prefixed ID (`PS-*`, `CV-*`, ...), exact
   quantifiers and hypotheses, and a source link/filename and date if known.
2. Assign `PROVED` only after a full proof is placed in `preprints/` or the
   appropriate family ledger. Computational checks alone use
   `COMPUTATIONAL_EVIDENCE`. Never infer an independent proof from a chat label.
3. Supply a counterexample and exact scope when marking `FAILED_DISPROVED`.
4. Record novelty and precedence separately from correctness. Cite the
   literature, including later concurrent results.
5. Add Lean only after checking toolchain, dependencies, unsolved goals,
   nonstandard axioms, and kernel replay. Empty formalization inventories
   should stay empty rather than claiming verification.
6. Add changes to `history.md`; preserve superseded or withdrawn claims with
   an explicit notice. Prefer new claims over silently strengthening old ones.
7. Preserve original inputs under `sources/` without editing. If a source is
   not available, give its title and explicitly say full text was not inspected.

This project has no automatically asserted priority, publication, peer-review,
or endorsement status.
