# Mathematical and provenance audit

## A. Projected-Segre correction

The source uses `r(m,K)` to count ordered pairs `(a,b)` solving
`(a-m)(b-m)=K`. The image point `(a+b,ab)` identifies `(a,b)` and `(b,a)`;
diagonal pairs are singletons. Consequently the correct occupancy is
`(r(m,K)+d(m,K))/2`, with `d` the count of diagonal pairs.

The exact collinear triple count is a sum of binomial coefficients of
**unordered point** occupancies over **all** affine lines, including the
vertical lines `a+b=c`. It is not simply `sum r^3`.

The source's proposed bound `sum r^3 << |A|^4+|A|^6/p` omits the
unavoidable floor `p|A|^2`, since `sum r=p|A|^2` and `r^3>=r`.
`A={a}` gives exact contradiction: left side `p`, right side bounded.

## B. Convex polygon qualifications

The bisector-arc argument applies to a planar compact convex polygon with
nonempty interior and two distinct boundary points. In the gap-injection
argument the center gap is a *connected boundary arc avoiding both* the
separator and the target; without that hypothesis the result is false as
stated. The cycle product theorem is an exact counting consequence given
those hypotheses. It does not by itself settle the full Erdős #97 problem.

## C. Historical claim quality

Names such as `1J-DEAMP`, `FP-TC6`, `FP-TRI`, `Delta_2(c)` and the sieve-lcm
antichain conjecture occur in accessible chat excerpts without their full
formal definitions. They cannot legitimately be restored as proved theorems.
They are carried as research targets or proof reports requiring source recovery.

## D. Formalization

No Lean theorem is represented as kernel checked in this edition. The
`lean/formalization.yaml` inventory is empty by design.
