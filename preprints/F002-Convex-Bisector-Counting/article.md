# Bisector intersection and finite marked-cycle obstructions

**Manuscript status:** self-contained proofs of the statements below.
**Version:** 2026-11-25.

## Definitions

Let `P` be a compact convex polygon in the Euclidean plane with nonempty
interior. Its boundary is a simple closed curve. Distinct `x,y∈∂P` divide
its boundary into two *open arcs* (endpoints removed). Their perpendicular
bisector is

\[
L_{x,y}=\{z\in\mathbb R^2:|z-x|=|z-y|\}.
\]

A *gap* below means a connected subset of an open boundary arc.

## Theorem CV-001: one bisector point on each arc

For any two distinct `x,y∈∂P`, `L_{x,y}` meets each of the two open
boundary arcs from `x` to `y` in **exactly one point**.

**Proof.** The affine linear function

\[
f(z)=|z-x|^2-|z-y|^2
    =2z\cdot(y-x)+|x|^2-|y|^2
\]

has `f(x)=-|x-y|^2<0` and `f(y)=|x-y|^2>0`. It vanishes on the
perpendicular bisector. Continuity and the intermediate value theorem
on each boundary arc give at least one zero on each arc. Since `x`
and `y` lie in opposite strict half-planes of `L_{x,y}`, the line
passes through the interior of `P`. The intersection of a line through
the interior with the boundary of a compact convex polygon consists
of exactly two points, the endpoints of its intersection segment with
`P`. Hence there are exactly two zeros total, one per arc.
`\square`

## Theorem CV-002: per-target injection and counting

Fix `s∈∂P`, a connected boundary gap `G⊂∂P`, and another connected
boundary gap `H⊂∂P`, where `G` is disjoint from `{s}∪H`. For any fixed
`q∈H` with `q≠s`, at most one `p∈G` satisfies

\[
|p-q|=|p-s|.
\]

If `A⊂G` and `B⊂H` are finite and each `p∈A` has at least `k`
distinct witnesses `q∈B` satisfying this equality, then

\[
k|A|\le |B|.
\]

**Proof.** By CV-001 the perpendicular bisector `L_{q,s}` has one
intersection on each boundary arc between `q` and `s`. Because the
connected gap `G` avoids `q,s`, it lies in one of the two arcs, so
there is at most one matching `p∈G`. Define the incidence set
`I={(p,q)∈A×B:|p-q|=|p-s|}`. By the hypothesis, `|I|≥k|A|`;
by the per-target result, `|I|≤|B|`. \(\square\)

The separation condition is essential: a disconnected `G` can include
one bisector intersection on each boundary arc.

## Theorem CV-003: closed finite marked-gap cycle

Let `A_1,...,A_t` be nonempty finite subsets of connected boundary
gaps `G_1,...,G_t`. Interpret subscripts modulo `t`. For each `i`
fix a point `s_i∈∂P` such that `G_i` avoids `{s_i}∪G_{i+1}`;
assume every `q∈A_{i+1}` differs from `s_i`. Suppose every
`p∈A_i` has at least `k_i≥1` distinct `q∈A_{i+1}` obeying

\[
|p-q|=|p-s_i|.
\]

Then `∏_{i=1}^t k_i≤1`. In particular all `k_i=1`.

**Proof.** Apply CV-002 at every directed edge of the cycle:
`k_i |A_i|≤|A_{i+1}|`. Multiply the inequalities. All sets are
nonempty, so `∏ k_i ≤ ∏|A_{i+1}|/∏|A_i|=1`. Because `k_i`
are positive integers, every factor equals one. \(\square\)

## Scope of the deductions

A *local* bounded-multiplicity theorem does not by itself guarantee that
a chosen witness graph has a finite closed cycle with the required
separation hypotheses. The older daBook project described broader
four-separator and two-gap closure results, but their precise
hypotheses and proofs were not recovered; those statements remain
`REPORTED_UNVERIFIED` in this edition.

Separately, newer 2026 external Lean manuscripts reportedly disprove
Erdős #97 and a fixed-k extension. This paper does not duplicate or
independently verify those results. See the literature audit.
