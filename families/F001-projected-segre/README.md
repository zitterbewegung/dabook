# F001 — projected symmetric product and shifted-hyperbola energy

**Area:** finite fields, incidence combinatorics, algebraic geometry.
**Origin:** Erdős #1061 companion finite-field thread and the uploaded
`Nondegenerate Collinear Triples.txt` note.

Let `F=F_p`, `A` be a finite subset, `n=|A|`, and
`S_A={(a+b,ab):a,b in A} subset F^2`.
Let `r_m(K)=#{(a,b) in A^2:(a-m)(b-m)=K}`.

| Claim | Exact status | Content |
|---|---|---|
| PS-001 | PROVED | `(a+b,ab)` is injective on unordered pairs |
| PS-002 | PROVED | Every affine line has an explicit factor/fiber description |
| PS-003 | PROVED | `sum r_m(K)^2=n^4-E_+(A)+p(2n^2-n)` |
| PS-004 | PROVED | Correct exact formula for three-point lines, with diagonal and vertical correction |
| PS-005 | FAILED_DISPROVED | Unqualified conjecture `sum r^3 << n^4+n^6/p` fails for singleton `A` |
| PS-006 | OPEN_GAP | Find a sharp, correctly normalized third-moment estimate |
| PS-007 | REPORTED_UNVERIFIED | Conjugation formula for structured Möbius family; `T` and `lambda` not specified in source |
| PS-008 | OPEN_GAP | Uniform sum of projective-linearized slices |
| PS-009 | OPEN_GAP | Nontrivial bound for 3-point lines of `S_A` in a specified size regime |
| PS-010 | PROVED | Plane preimages are shifted hyperbolas, splitting precisely when `K=0` |

**Full manuscript:** [article.md](../../preprints/F001-Projected-Segre-Shifted-Hyperbola/article.md).
**Tests:** [test_projected_segre.py](../../tests/test_projected_segre.py).
**Precedence:** Murphy--Petridis and Möbius incidence results; see prior-art audit.

A proof of PS-003 does not alone imply the high-order incidence estimate sought
in Erdős #1061. Original source claims of novelty are not independently established.
