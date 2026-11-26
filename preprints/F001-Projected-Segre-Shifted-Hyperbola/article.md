# Exact shifted-hyperbola moments and projected-Segre line fibers

**Manuscript status:** elementary self-contained proofs; no claim of novelty or
formal verification. **Source:** daBook F001 and uploaded
`Nondegenerate Collinear Triples.txt`. **Version:** 2026-11-25.

## Setup and conventions

Let `p` be prime, `F=F_p`, and let `A ⊂ F` be a finite set with `n=|A|`.
Put

\[
S_A=\{(a+b,ab):a,b\in A\},\qquad
r_m(K)=\#\{(a,b)\in A^2:(a-m)(b-m)=K\}.
\]

The count `r_m(K)` includes ordered parameter pairs, whereas `S_A` is a
set of distinct geometric points. All lines are *affine* lines in `F^2`.

## Theorem PS-001: unordered-pair injectivity

The map `\{a,b\}\mapsto(a+b,ab)` on two-element multisets drawn from `A`
is injective. Consequently `|S_A|=n(n+1)/2`.

**Proof.** Given `(u,v)=(a+b,ab)`, the monic polynomial
`T^2-uT+v=(T-a)(T-b)` determines the root multiset `{a,b}` uniquely.
There are `n` doubleton multisets `{a,a}` and `n(n-1)/2` with distinct
entries. \(\square\)

## Theorem PS-002: exact line fibers

For the nonvertical line `L_{m,b}: v=mu+b`, set `K=m^2+b` and

\[
d_m(K)=\#\{a\in A:(a-m)^2=K\}.
\]

Then

\[
|L_{m,b}\cap S_A|=\frac{r_m(K)+d_m(K)}2.
\]

For the vertical line `V_c:u=c`, set

\[
s(c)=\#\{(a,b)\in A^2:a+b=c\},\quad
h(c)=\#\{a\in A:2a=c\}.
\]

Then `|V_c ∩ S_A|=(s(c)+h(c))/2`.

**Proof.** The first line equation is
`ab=m(a+b)+b`, equivalently to

\[
(a-m)(b-m)=m^2+b.
\]

Swapping `a` and `b` leaves the point `(a+b,ab)` unchanged. Every
nondiagonal pair orbit has size two and every diagonal orbit has size
one; the diagonal count is exactly `d_m(K)`. The vertical case uses
`a+b=c` and the same orbit count. \(\square\)

## Theorem PS-003: exact second moment

Define additive energy

\[
E_+(A)=\#\{(a,b,c,d)\in A^4:a+b=c+d\}.
\]

Then the identity

\[
\boxed{\sum_{m,K\in F}r_m(K)^2
=n^4-E_+(A)+p(2n^2-n)}
\]

holds for every finite subset `A` of the prime field, including the
empty set.

**Proof.** Expand the square and sum first over `K`. For each
`(a,b,c,d)∈A^4`, the number of `m∈F` satisfying

\[
(a-m)(b-m)=(c-m)(d-m)
\]

is the number of solutions to

\[
ab-cd=m(a+b-c-d).
\]

If `a+b≠c+d`, there is exactly one `m`. There are
`n^4-E_+(A)` such quadruples. If `a+b=c+d`, the equality holds for all
`p` values of `m` exactly when `ab=cd`, and never otherwise. Equality
of sums and products means the two unordered root pairs coincide.
There are `n` diagonal ordered pairs, each with one matching ordered
pair, and `n^2-n` off-diagonal ordered pairs, each with two matches.
Hence the number of pairs with identical sum and product is `2n^2-n`.
Adding the contributions yields the identity. \(\square\)

## Theorem PS-004: exact unoriented geometric collinear-triple count

Let

\[
q_m(K)=\frac{r_m(K)+d_m(K)}2,\qquad
q^V(c)=\frac{s(c)+h(c)}2.
\]

The number `T_3(S_A)` of **unordered triples of distinct collinear points**
of `S_A` is exactly

\[
\boxed{
T_3(S_A)=\sum_{m,K\in F}\binom{q_m(K)}3
+\sum_{c\in F}\binom{q^V(c)}3.}
\]

**Proof.** Nonvertical affine lines have unique equations `v=mu+b`,
and `b↔K=m^2+b` is a bijection for each `m`. The other affine lines
are precisely `u=c`. PS-002 supplies their exact distinct-point
occupancies. Three distinct collinear points define a unique affine
line. Summing `binom(occupancy,3)` over the `p^2+p` lines counts each
unordered triple exactly once. \(\square\)

**Warning.** Replacing this identity by `sum_{m,K}r_m(K)^3` is
mathematically incorrect: it misses vertical lines, double-counts
swapped pair presentations, ignores diagonal contributions, and
replaces a binomial coefficient by a cube.

## Theorem PS-005: first moment and counterexample to a proposed bound

For all `A`,

\[
\sum_{m,K\in F}r_m(K)=pn^2,
\qquad
\sum_{m,K\in F}r_m(K)^3\ge pn^2.
\]

In particular there is no absolute constant `C` such that

\[
\sum_{m,K\in F}r_m(K)^3\le C(n^4+n^6/p)
\]

holds for all primes `p` and all nonempty `A⊂F_p`.

**Proof.** For each `m` and each ordered pair `(a,b)∈A^2`, exactly one
`K=(a-m)(b-m)` occurs, proving the first identity. Every
nonnegative integer `r` obeys `r^3≥r`, proving the inequality. For
`A={a}`, precisely one `K=(a-m)^2` has `r_m(K)=1` for each `m`,
so the cubic moment is exactly `p`. The proposed right-hand side is
`C(1+1/p)`, a contradiction for sufficiently large primes. \(\square\)

A possible refined moment bound must at least account for this
`pn^2` contribution. **No replacement uniform estimate is asserted.**

## Theorem PS-010: elementary plane-section classification

Consider the affine surface `Σ={(x,y,z)∈F^3:z=xy}` and the projection
`π(x,y,z)=(x+y,z)`. The preimage in `Σ` of a nonvertical target line
`z=m(x+y)+b` is the affine curve

\[
(x-m)(y-m)=K,\quad K=m^2+b.
\]

For `K=0` it is the union of the two affine lines `x=m` and `y=m`.
For `K≠0` the polynomial `(x-m)(y-m)-K` is irreducible in
`F[x,y]` and defines an affine hyperbola. The preimage of a vertical
target line `x+y=c` is an affine line.

**Proof.** The nonvertical assertion is PS-002. For `K≠0`, after
translation let `X=x-m`, `Y=y-m`. The polynomial `XY-K` is degree one
in `X` over the domain `F[Y]`; a nontrivial factor independent of `X`
would divide both `Y` and `K`, hence be a unit. Thus `XY-K` is
irreducible. A vertical line preimage satisfies `x+y=c` with
`z=xy` determined, an affine line. \(\square\)

## Dependencies and research frontier

The moment calculation is an exact identity, not a proof of any
`|A|^{4-δ}` bound for the number of lines carrying at least three
points. A strong higher moment or incidence theorem would need
density hypotheses and a correct baseline term. The relation to the
original divisor-sum problem Erdős #1061 remains conjectural.

## Prior art

For general finite-field second moments see Murphy--Petridis,
https://arxiv.org/abs/1601.03981. This article makes no novelty or
precedence claim about the elementary specializations above.
