# Overview of result families

The project began with several Erdős problems and evolved into overlapping
programs in finite fields, geometry, analytic number theory, and elliptic-curve
algorithms. This edition splits algebraically provable facts from older proof
reports whose evidence is incomplete.

## The strongest complete results preserved here

**F001:** For `A` a finite subset of the prime field `F_p`, define
`r_m(K) = #{(a,b) in A^2 : (a-m)(b-m)=K}` and
`E_+(A) = #{(a,b,c,d) in A^4 : a+b=c+d}`. Then

```
sum_{m,K in F_p} r_m(K)^2
  = |A|^4 - E_+(A) + p(2|A|^2-|A|).
```

A proof appears in the F001 article. The exact unordered line occupancy has
an additional diagonal term; as a consequence the previously suggested
unqualified third-moment conjecture has an explicit singleton counterexample.

**F002:** The perpendicular bisector of any two distinct points on a convex
polygon boundary crosses each open boundary arc once. When a connected gap
contains neither endpoint, each fixed target on the opposite boundary has
at most one matching center in that gap. This yields the cycle product
obstruction to multiple marked cross-witnesses.

## Program boundaries

F003 studies `sigma(a)+sigma(b)=sigma(a+b)` and fixed-ratio parameterizations;
F001 arose as a supporting finite-field structure, but it does **not** prove
Erdős #1061. F004 studies divisors near `sqrt(n)`. F005 preserves an unresolved
Erdős #1 investigation. F006 records proposed algorithmic consequences for
elliptic-curve discrete logarithms; no faster ECDLP algorithm is established.
F007 collects prospective rational-phase and algebraic-geometric generalizations.
F008 records Ulam's prime-sequence question, with no proof claim.

## Source limitations

No original full chat export, independently reproducible notebooks from prior
conversations, or Lean certificates were supplied for this pass. A family may
therefore have many exact *topics* but fewer reconstructible theorems. The
catalogue explicitly acknowledges that limitation; see source map and audits.
