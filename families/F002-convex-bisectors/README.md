# F002 — perpendicular bisectors and convex-gap incidence

**Area:** Euclidean convex geometry, combinatorial incidence.
**Historical motivation:** Erdős Problem #97 and the project's
four-separator/marked-witness program.

| Claim | Status | Content |
|---|---|---|
| CV-001 | PROVED | Each open boundary arc from `x` to `y` meets their bisector exactly once |
| CV-002 | PROVED | One center per target in an arc gap; `k|A|≤|B|` |
| CV-003 | PROVED | Multiplicity product around a finite closed cross-gap cycle ≤1 |
| CV-004 | REPORTED_UNVERIFIED | Two-gap closed marked-correspondence theorem, full constraints not recovered |
| CV-005 | REPORTED_UNVERIFIED | Four-vertex curvature separator and normalized mass >1/4 |
| CV-006 | REPORTED_UNVERIFIED | Claimed unbounded two-circle local marked family |
| CV-007 | EXTERNAL_RESULT | 2026 newer reported proofs disproving Erdős #97 / fixed-k form, not replayed here |

**Complete manuscript for CV-001 to CV-003:**
[article.md](../../preprints/F002-Convex-Bisector-Counting/article.md).

**Crucial condition:** each gap is a connected boundary arc that avoids both
points defining the bisector. A full global Erdős #97 result does not follow
from local multiplicity counting.

**External status:** The original `erdosproblems.com/97` page inspected still
labels it open; newer 2026 formal-claim corpora assert disproof from
Kruer--Kohlmeyer constructions. See prior-art audit.
