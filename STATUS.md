# Status dashboard — 2026-11-26

**Definitions.** `PROVED` means a self-contained written proof appears in this
edition and was checked algebraically and/or by small-field tests.
`REPORTED_UNVERIFIED` means a prior project conversation calls it proved or
constructive but the precise argument is missing. `EXTERNAL_RESULT` reports
external literature or formalized claims with explicit independent-verification
limits. `FAILED_DISPROVED` means an exact counterexample is provided.
`OPEN_GAP` and `CONJECTURE` are not proved.

| Research theme | Proved here | Failed/disproved here | Critical gaps |
|---|---|---|---|
| Projected-Segre / shifted hyperbolas | Exact line fibers, second moment, triple-line count, section classification | Unqualified third moment bound | Uniform nontrivial collinear triple bound; sharp third moment |
| Convex polygon gaps | Bisector arc theorem, injection/counting, closed-cycle obstruction | — | Full global witness closure (historical project target); compare 2026 external disproof claims |
| Erdős #1061 divisor equation | — | — | Prove or disprove asymptotic `S(x) ~ cx`; recover fixed-ratio proofs |
| Erdős #886 | — | — | Exponent range `0 < epsilon < 1/4` |
| Erdős #1 | — | — | Recover exact lemmas, negative result, and full target statement |
| ECDLP / Coppersmith | — | — | Finite-cover, ordinary box, FP-TC6, FP-TRI, 1J-DEAMP |
| Rational phase / split-quadric | — | — | Uniform coefficient theorem, branch-contact and mixed-Tate descriptions |
| Ulam prime sequences | — | — | Infinite-sequence construction or counterexample |

**Important corrections.** The attached source equates `r(m,K)` (ordered
parameter pairs) with the number of distinct points of `S_A` on a line and
then writes the collinear triple count as a third moment. Both require
correction: see `PS-004`. Its bound
`sum r(m,K)^3 << |A|^4+|A|^6/p` is false uniformly in `p`: `PS-005`
uses `A` a singleton. These are mathematical corrections, not proof disputes.

**External update.** Newer 2026 work of Kruer--Kohlmeyer and
Kruer--Kohlmeyer--Price is reported to disprove Erdős #96 and #97, including
fixed-degree variants; status depends on the cited corpus and its Lean audit,
not on independent verification performed by this repository. The older
`erdosproblems.com` page still displayed an open label in the inspected material.
See `reports/PRIOR_ART.md` and F002.

**Source update (November 26).** The August 14 central findings report is
now preserved verbatim in `sources/`, with its final section visibly
truncated. Its `PROVED` labels do not supersede this repository’s
independent-proof requirements. See `sources/SOURCE_MAP.md`.
