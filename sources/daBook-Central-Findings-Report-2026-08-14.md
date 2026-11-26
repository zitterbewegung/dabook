# daBook — Central Findings Report

**Canonical project synthesis**  
**Status date:** August 14, 2026

## Scope and evidentiary standard

This report consolidates the substantive mathematical findings visible in the daBook project history supplied to this conversation, together with the attached project note on projected-Segre / shifted-hyperbola structure. It deduplicates repeated continuations and separates established results from conjectural or incomplete research directions.

Every substantive assertion is marked as one of:

- **PROVED** — explicitly recorded in project context as proved or completed.
- **CONDITIONAL** — proved subject to stated hypotheses or dependent on another unproved assertion.
- **COMPUTATIONAL EVIDENCE** — established only through numerical, brute-force, symbolic, or finite verification.
- **CONJECTURE** — proposed as a target statement without proof.
- **FAILED/DISPROVED** — an attempted theorem, route, formulation, constant, or argument recorded as false or insufficient.
- **OPEN GAP** — unresolved frontier or a claim whose proof is not available in the accessible project context.

Because several project chats are represented here by continuation summaries rather than their entire transcripts, theorem statements that occur only in those summaries are reported faithfully but not reconstructed beyond the information actually available. Where a constant, hypothesis, or proof detail is missing, it is marked uncertain rather than supplied from inference.

---

# 1. Executive synthesis

The daBook project has developed into several partially connected mathematical research programs rather than one isolated Erdős-problem effort.

The most mature strands are:

1. **Erdős Problem 1061 and its descendants:** divisor-sum equations led to a substantial body of structural mathematics involving trace-zero Möbius involutions, projected symmetric products, shifted hyperbolas, finite-field incidence geometry, multiplicative energy, coefficient-energy estimates, and an attempted cryptographic application to ECDLP.

2. **Erdős Problem 97:** the original convex-geometric problem was reduced through curvature separators and marked witness correspondences. Important local obstructions were classified, a proposed local boundedness principle was disproved by an explicit two-circle construction, and a stronger global closure principle was developed. The project records the **two-gap closed marked-correspondence theorem as proved**, but a larger global closure theorem remained the critical frontier.

3. **Erdős Problem 886:** a number-theoretic divisibility/LCM/antichain program produced useful reductions and standalone lemmas, but the final “sieve-LCM antichain theorem for \(z^2-1\)” and related routes remained unresolved in the accessible summaries.

4. **Erdős Problem 1:** the project appears not to have reached a proof of the original problem, but it produced negative results, auxiliary lemmas, and candidate standalone material judged potentially worth publishing independently. Exact theorem statements are not present in the current cross-chat synopsis and therefore cannot safely be reconstructed.

5. **Finite-field rational exponential sums / incidence geometry:** what began as supporting machinery for Erdős 1061 became a broader program involving split-quadric reductions, projected Segre geometry, Möbius energy, shifted reciprocal interval energy, exact or corrected square-moment identities, and conjectural classification results for rational phases.

6. **ECDLP / Coppersmith program:** the 1061 machinery inspired an index-calculus/Coppersmith line of attack. Significant intermediate algebraic and energy statements were apparently proved or corrected, but the central finite-cover/box-based Coppersmith decomposition oracle and its cryptographic consequence were not established. The project itself explicitly distinguished a structurally sound architecture from a complete proof and rejected at least one unjustified constant.

A recurring theme across the strongest work is that difficult-looking nonlinear relations often simplify under a projective, Möbius, Segre, or translated-product coordinate change. The clearest instance is

\[
(x,y)\longmapsto (x+y,xy),
\]

for which a nonvertical line

\[
v=mu+b
\]

pulls back to

\[
xy=m(x+y)+b
\]

and therefore to the translated hyperbola

\[
(x-m)(y-m)=m^2+b.
\]

This identity converts a geometric collinearity problem into multiplicative combinatorics and is now one of the central reusable structures of the project. The attached note explicitly identifies this shifted-hyperbola viewpoint as more promising than the earlier generic Möbius-family incidence approach. Nondegenerate Collinear Triples

The project’s most important methodological correction is therefore:

> **Do not search first for a generic incidence theorem when the geometry can be collapsed to a highly structured multiplicative fiber.**

That principle appears repeatedly in the 1061, rational-exponential-sum, and ECDLP branches.

---

# 2. Status dashboard

| Program | Current status | Strongest established point | Main unresolved frontier |
|---|---|---|---|
| Erdős 1061 | Major structural progress; original full problem status uncertain from available summaries | Fixed-ratio classifications; logarithmic-moment coefficient estimate; projected-Segre / shifted-hyperbola reduction; several finite-field energy identities/reductions | Sharp shifted-hyperbola third moment / incidence bound and remaining analytic coefficient-energy problem |
| Projected Segre / shifted hyperbola | Active, high-value standalone program | Line pullback identity \((x-m)(y-m)=K\); moment reformulation | Prove sharp cubic moment \(\sum_{m,K}r(m,K)^3\) or classify rich fibers |
| Rational exponential sums / split quadrics | Substantial theory, partly open | General bilinearization mechanisms and several exact identities recorded as proved | Split-quadric universality/classification, branch-contact classification, mixed-Tate explanation |
| ECDLP / Coppersmith | Incomplete | Pipeline reductions, corrected TRI/energy work, several finite-frequency statements targeted/proved in continuations | Finite-cover / ordinary-box Coppersmith theorem and decomposition oracle |
| Erdős 97 | Strong geometric reduction | Four-separator reduction; closed two-gap marked correspondence theorem; multiplicity-product argument | Full global witness closure / remaining hard-pattern cycles |
| Erdős 886 | Partial | Several reductions and candidate standalone lemmas | Sieve-LCM antichain theorem for \(z^2-1\); resolution of competing routes |
| Erdős 1 | Incomplete | Negative results and auxiliary lemmas reported | Original problem and exact publication-quality formulation of standalone results |
| Ulam prime sequence problem | Literature/research reconnaissance only in visible project context | Problem identified and relevant-paper search requested | Infinite starting sequence remains unresolved here |
| Research-paper synthesis / formalization | Organizational rather than mathematical | Paper-suite plans, companion guide, Lean handoff prompts | Formal proof certificates and canonical final manuscripts |

---

# 3. Erdős Problem 1061: divisor-sum structure and fixed-ratio arithmetic

## 3.1 Origin of the program

The 1061 work began as a divisor-sum equation problem and expanded into several distinct subprograms:

- fixed-ratio classifications;
- coefficient polynomials such as \(\Delta_2(c)\);
- affine prime systems;
- opposite-sign coefficient energy;
- projected symmetric-product geometry;
- finite-field incidence and energy;
- Möbius involutions and product fibers;
- later, an ECDLP/Coppersmith application.

The exact original Erdős 1061 statement is not reproduced in the accessible project synopsis, so it is not restated here.

---

## 3.2 Fixed-ratio local-core classifications

### Fermat-prime ratios

**PROVED.** For

\[
k=2^s
\]

with

\[
2^s+1
\]

prime, the project records a **complete fixed-ratio classification**: the unique local core is

\[
d_0=2^{s-1}.
\]

The phrase “local core” is inherited from the project; the precise defining divisor equation is not present in the current context.

### Mersenne-prime ratios

**PROVED.** For

\[
k=2^p-1
\]

prime, the unique local core is

\[
d_0=2^{p-1}.
\]

Again, this is reported as a complete classification within the fixed-ratio framework.

### Ratio \(1:8\)

**PROVED.** The ratio \(1:8\) has the unique local core

\[
d_0=12.
\]

### Additional seed families

**COMPUTATIONAL EVIDENCE / VERIFIED SEEDS.** The following families were explicitly recorded as verified:

\[
k=9,\qquad d_0=2,
\]

\[
k=15,\qquad d_0=3600,
\]

\[
k=39,\qquad d_0=60.
\]

The visible project context does not specify whether these were proved symbolically for an infinite associated family or only checked as seed solutions. They should therefore not be promoted to full classification theorems without returning to the original chat.

---

## 3.3 Small-coefficient logarithmic-moment theorem

A later analytic continuation records the estimate

\[
S_k(H)
=
\sum_{|\Delta_2(c)|\le H}
\frac{(1+\log c)^k}{c}
\ll_k
(1+\log H)^{k+2}.
\]

### Status

**PROVED.** This estimate was explicitly supplied as the theorem from which the next analysis should continue.

### Interpretation

It bounds the reciprocal/logarithmic mass of parameter values \(c\) for which the coefficient polynomial \(\Delta_2(c)\) is small.

### Consequence

This estimate gives a mechanism for separating the parameter space according to coefficient size and controlling “small coefficient” portions through logarithmic moments rather than crude counting.

### Caveat

The exact definition of \(\Delta_2(c)\) is not present in the accessible cross-chat context, so no explicit polynomial formula is inserted here.

---

## 3.4 Opposite-sign linear-linear coefficient energy

The project isolated an energy of the form

\[
E(X)
=
\sum
\left[
\text{singular\_factor}
\frac{\gcd(A,D)}{cD+dA}
\right],
\]

over parameter pairs satisfying

\[
A=\Delta_2(c)>0,
\]

\[
-D=\Delta_2(d)<0,
\]

and

\[
\gcd(A,D)\mid 3(2-c-d),
\]

with the additional requirement that the associated affine prime system can produce a prime \(p\le X\).

The requested decomposition was:

\[
|A|,D\le (\log X)^L,
\]

one coefficient small and one large, and

both coefficients large.

The proposed strategy was to expand

\[
\gcd(A,D)
\]

by divisor sums and exploit

\[
\gcd(A,D)\mid 3(2-c-d)
\]

for congruence savings.

### Status

**OPEN GAP.** The accessible project history records this as an analytic frontier, not a completed estimate.

### Important deduction

**PROVED INPUT.** The logarithmic-moment theorem above supplies nontrivial control of the small-coefficient ranges.

### Unresolved point

A globally strong enough estimate for \(E(X)\), especially in the large-large regime and after singular-factor accounting, is not recorded as proved in the available summaries.

---

# 4. Projected symmetric products and shifted-hyperbola geometry

This is one of the clearest and most reusable mathematical outputs of the project.

Define

\[
S_A
=
\{(a+b,ab):a,b\in A\}.
\]

More generally write

\[
(u,v)=(x+y,xy).
\]

Consider a nonvertical affine line

\[
v=mu+b.
\]

Then a preimage point satisfies

\[
xy=m(x+y)+b,
\]

hence

\[
xy-mx-my=b,
\]

so

\[
(x-m)(y-m)=m^2+b.
\]

Thus every nonvertical line in the projected \((x+y,xy)\)-plane pulls back to a translated multiplicative fiber

\[
(x-m)(y-m)=K,
\qquad
K=m^2+b.
\]

## 4.1 Projected symmetric-product line classification

**PROVED.**

\[
xy=m(x+y)+b
\iff
(x-m)(y-m)=m^2+b.
\]

This elementary identity is structurally central.

### Consequences

**PROVED.**

- Nonvertical lines correspond to shifted hyperbolas.
- Rich lines in \(S_A\) are equivalent to values of \(m,K\) for which many pairs \((x,y)\in A^2\) satisfy
  \[
  (x-m)(y-m)=K.
  \]
- Collinearity problems in the image can therefore be translated into multiplicative coincidence problems.

The attached note explicitly elevates this identity as the most promising direction arising from the earlier report. Nondegenerate Collinear Triples

---

## 4.2 Shifted-hyperbola representation function

Define

\[
r(m,K)
=
\#\{(x,y)\in A^2:(x-m)(y-m)=K\}.
\]

Then line incidence counts become moments of \(r\).

### Cubic moment formulation

A key recorded reformulation is

\[
T
=
\sum_\ell \binom{r_\ell}{3},
\]

with the essential obstruction represented by the cubic shifted-hyperbola moment

\[
\sum_{m,K} r(m,K)^3.
\]

The attached report phrases the remaining incidence question as the possibility that this cubic moment is significantly larger than its random-scale behavior. Nondegenerate Collinear Triples

### Status

**PROVED REDUCTION.** The conversion of line richness to shifted-hyperbola multiplicities is proved.

**OPEN GAP.** A sharp global cubic-moment bound remains unresolved in the supplied material.

---

## 4.3 Strong shifted-hyperbola moment conjecture

The project proposed

\[
\boxed{
\sum_{m,K}
r(m,K)^3
\ll
|A|^4+\frac{|A|^6}{p}
}
\]

for \(A\subseteq\mathbb F_p\).

### Status

**CONJECTURE.**

### Significance

If true at the appropriate level of uniformity, the project expected it to essentially settle the remaining projected-Segre incidence obstruction arising in the 1061 program.

### Caveat

No proof is recorded in the accessible project history.

---

## 4.4 Three-point line target

Another proposed target is

\[
\#\{\text{3-point lines in }S_A\}
\ll |A|^{4-\delta}
\]

for some explicit

\[
\delta>0.
\]

### Status

**CONJECTURE / OPEN GAP.**

The attached note states that no existing theorem had been identified in the project report that directly yielded such a bound. Nondegenerate Collinear Triples

---

# 5. Möbius linearization and trace-zero involution structure

A major structural identity discovered in the project is a Möbius conjugacy of the form

\[
T_{a,b,d}(x)
=
-\phi_{a,d}^{-1}
\!\left(
\lambda\,\phi_{a,d}(x)
\right),
\]

where

\[
\phi_{a,d}(x)
=
\frac{x-a}{x+d}.
\]

For fixed \((a,d)\), the family becomes multiplicative scaling in projective coordinates and hence behaves like a line pencil after conjugation.

### Status

**PROVED STRUCTURAL IDENTITY**, as reported in the attached research note.

### Interpretation

The nonlinear \(PGL_2\)-family is conjugate, slice by slice, to a one-parameter dilation family.

### Limitation

**OPEN GAP.** The project did not have a theorem summing this slice-wise linearization uniformly over all \((a,d)\).

The attached note identifies exactly this missing uniformity as a potential source of a standalone theorem. Nondegenerate Collinear Triples

### Methodological outcome

**FAILED/INSUFFICIENT ROUTE.** Generic Möbius-family incidence theory was judged less promising than exploiting the more rigid shifted-hyperbola representation available after passing to the projected symmetric product.

This is not a disproof of the Möbius program; it is a ranking result: the project concluded that the shifted-product geometry is sharper for the immediate 1061 obstruction.

---

# 6. Exact Möbius energy and shifted-hyperbola square moments

One of the research-paper synthesis chats explicitly listed an:

> “Exact Möbius-energy identity” equating a diagonal square moment of shifted-hyperbola fibers with the multiplicative energy of a Möbius image after exceptional fibers are separated.

### Status

**PROVED**, according to the project synopsis.

### Exact formula

**UNCERTAIN / NOT RECOVERABLE FROM CURRENT CONTEXT.**

The source summary does not contain the complete algebraic formula, so this report does not attempt to recreate it.

### Associated result

The same synthesis described:

- translated reciprocal interval energy;
- corrected diagonal shifted-hyperbola square moments;
- trace-zero Möbius involutions;
- product-fiber hyperbolas.

These were intended to become central contributions of a standalone paper rather than mere supporting lemmas for Erdős 1061.

### Status

The project presentation suggests at least some corresponding identities were **PROVED**, but the exact statements and hypotheses are absent from the visible project history. They should therefore be treated as **PROVED-IN-PROJECT, FORMULA UNCERTAIN** until audited against the source chat or manuscript.

---

# 7. Projected Segre and split-quadric research program

The finite-field work expanded into a general program around nonlinear identities that become bilinear after suitable transformations.

## 7.1 Projected Segre viewpoint

The map

\[
(x,y)\mapsto (x+y,xy)
\]

was interpreted as a projection of a Segre-type surface such as

\[
\Sigma=\{(x,y,xy)\}.
\]

Collinear configurations downstairs correspond to plane-section phenomena upstairs.

### Status

**PROVED GEOMETRIC REINTERPRETATION** at the elementary incidence level.

### Proposed theorem

A project note suggested proving that every relevant plane section is either irreducible or belongs to finitely many exceptional families.

### Status

**CONJECTURE / OPEN GAP.**

No complete plane-section classification is recorded.

---

## 7.2 General split-quadric reduction

The rational-exponential-sum research program targeted a coefficient-uniform theorem showing that a broad class of paired multiplicative and linear identities transforms, after translation, into a split bilinear quadric.

### Status

**PARTIALLY PROVED / OPEN GENERALIZATION.**

The project repeatedly refers to a “general split-quadric reduction theorem” as a central desired contribution. It is not possible from the accessible context to determine whether the fully coefficient-uniform theorem was eventually proved.

The following narrower mechanism is securely present:

**PROVED.** A translated product relation can arise from linear constraints after a suitable coordinate shift, exemplified by

\[
xy=m(x+y)+b
\iff
(x-m)(y-m)=m^2+b.
\]

---

## 7.3 Split-quadric classification conjecture

The project later formulated a much stronger classification principle:

> Every split-quadric reduction of a linear-over-quadratic phase is generated by dual-isotropic completion, Segre coordinate changes, and projective automorphisms of the underlying quadric.

### Status

**CONJECTURE.**

No proof or counterexample is recorded in the accessible synopsis.

---

## 7.4 Branch-contact classification conjecture

The project proposed:

> The stable birational type of a projected degree-\(d\) section is determined by degree, reducibility data, and the contact partition with the discriminant conic, together with residue-field information at nonrational contact points.

### Status

**CONJECTURE.**

### Remaining work

A complete classification of branch contacts, especially at nonrational points, was identified as an open algebraic-geometric task.

---

## 7.5 Mixed-Tate complete-fiber conjecture

The project proposed that complete phase fibers admit a stratification by tori and affine spaces explaining certain polynomial point counts without requiring cancellation from higher-weight cohomology.

### Status

**CONJECTURE / PLAUSIBLE.**

The precise point-count formulas labeled “(25)–(26)” are not available in the current synopsis and therefore are not reproduced.

---

# 8. Rational exponential sums: open energy calculations

The advanced-conjectures thread listed several concrete next experiments.

One was

\[
R_2(K)
=
\sum_m r_A(m,K)^2,
\]

to be computed separately for:

- \(K\) square,
- \(K\) nonsquare,
- \(K=0\),

with the aim of identifying formulas in terms of resultant-level energies and Paley correlations.

### Status

**OPEN GAP / COMPUTATIONAL PROGRAM.**

No final closed formula is visible in the accessible project summary.

Another target was the complete \(U\)-Fourier spectrum of a function related to

\[
t\longmapsto E_\times(I^{-1}+t,\ldots),
\]

but the expression is truncated in the project synopsis.

### Status

**OPEN GAP.**

The incomplete source prevents a reliable full statement.

---

# 9. Erdős Problem 97: convex geometry and witness closure

This is one of the most developed non-1061 branches.

The project reached an audited “four-separator reduction” and then a closed marked-correspondence theorem.

## 9.1 Curvature intervals

**PROVED.** Every witness pair yields two forced curvature intervals of normalized mass

\[
> \frac14.
\]

The exact definition of the normalized curvature measure is not present in the current synopsis.

---

## 9.2 Four-vertex separator

**PROVED.** Every counterexample has a four-vertex curvature separator.

This reduced arbitrarily complicated counterexamples to a configuration controlled by at most four separator gaps.

---

## 9.3 Same-gap witness bound

**PROVED.** Each gap vertex has at most two same-gap witnesses.

---

## 9.4 Bounded pair/triple target families

**PROVED.** Bounded pair/triple target families are bounded.

The exact numerical bounds are not present in the accessible project summary.

---

## 9.5 Clean monotone hard-pattern cycle

**PROVED REDUCTION.** Arbitrarily large counterexamples force a clean monotone hard-pattern cycle among at most four unbounded gaps.

This moved the problem from local configurations to a global cyclic witness structure.

---

## 9.6 Inversion formula

Let \(s\) be a marked separator witness and \(p\) the center of a selected witness circle.

**PROVED.** Inversion at \(s\) sends the selected witness circle centered at \(p\) to the perpendicular bisector of

\[
0
\quad\text{and}\quad
J(p),
\]

where \(J\) denotes the inversion map used in the project.

This is a major geometric simplification: circle incidence becomes a perpendicular-bisector condition.

---

## 9.7 Disproof of a local boundedness theorem

A proposed local theorem for an adjacent-marked \(sGH^2\) family was tested.

**FAILED/DISPROVED.**

A single adjacent-marked \(sGH^2\) family is **not bounded**.

The project records an **exact two-circle construction** giving arbitrarily long strict-convex marked families in which both gap curvatures are

\[
<\frac14.
\]

### Consequence

Local pattern theorems are insufficient.

This counterexample was important because it forced the project to replace local boundedness with **global witness closure**.

---

# 10. Erdős 97: closed marked-correspondence theorem

A later continuation records the following chain.

## 10.1 Perpendicular-bisector crossing lemma

**PROVED.** If \(x,y\) are boundary points of a convex polygon, their perpendicular bisector meets each open boundary arc from \(x\) to \(y\) exactly once.

---

## 10.2 Uniqueness across disjoint gaps

Let \(G,H\) be disjoint gaps, let

\[
s\notin G\cup H,
\]

and fix

\[
q\in H.
\]

**PROVED.** At most one

\[
p\in G
\]

satisfies

\[
|p-q|=|p-s|.
\]

This is the key injectivity statement used in correspondence counting.

---

## 10.3 Cross-multiplicity inequality

If every

\[
p\in A\subset G
\]

has \(k\) marked-circle witnesses in

\[
B\subset H,
\]

then

\[
k|A|\le |B|.
\]

### Status

**PROVED.**

The proof is by the preceding uniqueness/injectivity property.

---

## 10.4 Multiplicity-product bound on a closed cycle

**PROVED.** Around any closed marked component cycle, the product of cross multiplicities is at most

\[
1.
\]

Since the multiplicities are positive integers, every multiplicity on such a closed cycle must equal

\[
1.
\]

### Consequence

High-multiplicity correspondence cycles cannot close.

This is a genuinely global obstruction and is stronger than the disproved local boundedness principle.

---

## 10.5 Two-gap closed marked-correspondence theorem

**PROVED.** Two cross witnesses in each direction between two gaps are impossible.

This is explicitly recorded in the project as the **two-gap closed marked-correspondence theorem**.

### Significance

This theorem appears to close the principal two-gap cyclic obstruction.

---

## 10.6 Endpoint-marked same-gap closure

The project further records:

> If the marked separator is an endpoint of the center gap and every center has an internal same-gap witness, finite closure is ...

The source summary truncates the conclusion.

### Status

**UNCERTAIN.**

A theorem was apparently being formulated or proved, but the exact statement cannot be recovered safely from the supplied project history.

---

## 10.7 Remaining Erdős 97 frontier

**OPEN GAP.** The main unresolved issue after the two-gap theorem was full **global witness closure** across all allowable hard-pattern cycles, potentially involving up to four unbounded gaps.

The project explicitly recognized that proving boundedness of isolated local patterns could not resolve this.

### Recommended direction

Reduce every surviving hard-pattern cycle to a finite directed correspondence system and seek either:

1. a global injectivity/product inequality forcing all cycle multiplicities to \(1\), followed by a contradiction from strict convex order; or
2. an explicit construction demonstrating that a surviving cycle really can close.

A computational structured search was requested in the project, but no final counterexample or global proof is recorded in the visible summaries.

---

# 11. Erdős Problem 886

The 886 program appears to involve divisor structure, LCM growth, and antichain arguments related to

\[
z^2-1.
\]

The project repeatedly targeted a:

> **sieve-LCM antichain theorem for \(z^2-1\).**

## 11.1 Overall status

**OPEN GAP.** The original problem is not recorded as solved in the accessible project synopsis.

## 11.2 Sieve-LCM antichain route

**OPEN GAP.** A prompt was developed specifically to search for a proof of the sieve-LCM antichain theorem.

The project also asked to:

- inspect proposed online solutions;
- test all possible routes;
- attempt to prove or disprove both major remaining routes;
- solve the resulting system.

The available conversation summary does not preserve the theorem statement or the outcome of those final attempts.

### Required caution

No purported proof of Erdős 886 should be inferred from the existence of those prompts.

---

## 11.3 Standalone-paper potential

The 886 work appears to have generated lemmas and possible standalone results, because the project later discussed exporting comments and formal paper drafts.

### Status

**UNCERTAIN.**

Exact theorem statements are unavailable in the present project synopsis, so they cannot be catalogued rigorously here.

---

# 12. Erdős Problem 1

This thread involved repeated attempts to push successive “next meaningful theorems” toward a proof of Erdős Problem 1.

## 12.1 Final problem status

**OPEN GAP.** There is no reliable indication in the supplied project history that Erdős Problem 1 was solved.

## 12.2 Negative-result note

The project explicitly discussed posting a **negative result note** on the Erdős problem page.

### Status

**FAILED/DISPROVED ROUTE.**

At least one substantial attempted route was strong enough to merit recording as a negative result.

The exact hypothesis that was disproved is not in the visible summary and should not be reconstructed.

## 12.3 Standalone lemmas

The project asked whether the resulting lemmas were publishable independently and concluded that at least some appeared sufficiently interesting to outline as a short paper.

### Status

**PROVED-IN-PROJECT, STATEMENTS UNCERTAIN.**

No exact lemma text is available in the current project context.

## 12.4 Publication planning

The project requested:

- a negative-result note;
- a short paper outline of standalone lemmas/theorems;
- journal selection;
- appropriate style/template;
- verification of the resulting draft.

These are artifacts or editorial conclusions, not additional mathematical proofs.

---

# 13. ECDLP program derived from Erdős 1061

The ECDLP branch attempted to convert the arithmetic/finite-field structure developed around 1061 into an index-calculus or decomposition method for elliptic curves.

The project’s own summaries are careful that the attack was incomplete.

## 13.1 Pipeline status

A quoted audit states:

> “architecture correct, no fatal error, but not proved — and the constant 108 is not justified.”

### Status

**FAILED/DISPROVED:** any claim that the pipeline was already a complete proof.

**FAILED/DISPROVED:** the specific constant

\[
108
\]

as previously asserted, because it lacked justification.

**PARTIALLY VALIDATED:** the broad architecture had no identified fatal structural error at that audit point.

---

## 13.2 Coppersmith decomposition bottleneck

The cryptographic program identified one main missing ingredient:

> a lattice/decomposition oracle capable of handling a family with many variables without the usual multivariate Coppersmith degradation.

The project investigated literature directions in which lattice bounds improve rather than worsen with variable count.

### Status

**OPEN GAP.**

No theorem sufficient for the ECDLP decomposition oracle is recorded as proved.

---

## 13.3 Ordinary box-based Coppersmith theorem

The project explicitly requested proofs of:

- the “new ordinary box-based Coppersmith” theorem;
- a “finite-cover Coppersmith theorem.”

### Status

**OPEN GAP / PARTIALLY ADVANCED.**

The available project synopsis does not say that either theorem was fully established.

---

## 13.4 TRI and energy corrections

Several continuations requested correction of:

- the TRI theorem;
- a “sharp energy theorem”;
- “Middle-density FP-TC6”;
- “Every-frequency FP-TRI.”

The project notes that the corrected TRI **may already have been solved**, but this was itself stated uncertainly.

### Status

- Corrected TRI: **UNCERTAIN / POSSIBLY PROVED.**
- Sharp energy theorem: **UNCERTAIN.**
- Middle-density FP-TC6: **OPEN OR UNCERTAIN.**
- Every-frequency FP-TRI: **OPEN OR UNCERTAIN.**

The full statements are absent, so no stronger status can responsibly be assigned.

---

## 13.5 1J-DEAMP and interval-specific statements

Another continuation targeted:

- theorem “1J-DEAMP”;
- an “elliptic interval specific statement.”

### Status

**UNCERTAIN.**

The project history records attempts to prove them but does not preserve final theorem statements or a verified completion in the synopsis.

---

## 13.6 Cryptographic consequence

**OPEN GAP.** Nothing in the accessible project record justifies a claim that the elliptic-curve discrete logarithm problem was solved or that a provably faster general ECDLP algorithm resulted.

The correct status is that ECDLP served as a motivating application for a chain of exact arithmetic and lattice questions.

---

# 14. Collinear triples and the attached “Nondegenerate Collinear Triples” note

The attached project note reinforces and sharpens the projected-Segre branch.

Its central observation is that the nonlinear Möbius formulation can be linearized slice-wise, but the more direct projected symmetric-product formulation is structurally superior for the immediate problem.

It records four suggested routes:

1. classify rich lines in
   \[
   S=\{(x+y,xy)\};
   \]

2. use projected Segre geometry;

3. derive an “orchard energy” or second/third moment identity;

4. attack the remaining Erdős-1061 theorem directly through shifted-hyperbola multiplicities.

The note identifies the strongest conjectural bound as

\[
\sum_{m,K}r(m,K)^3
\ll
|A|^4+\frac{|A|^6}{p}.
\]

It also ranks the hyperbola formulation as the most promising immediate route and a general split-torus \(PGL_2\) incidence theorem as the most ambitious. Nondegenerate Collinear Triples

### Status of this note

The structural identities are **PROVED**.

The moment estimates and three-point-line power saving are **CONJECTURE / OPEN GAP**.

---

# 15. General bilinearization research program

One of the project’s explicit long-term themes was:

> Investigate nonlinear arithmetic identities that become bilinear after suitable coordinate changes.

This umbrella program includes:

- Möbius conjugation;
- translation to product fibers;
- projective coordinate changes;
- Segre embeddings/projections;
- split quadrics;
- dual-isotropic completion.

## Established examples

### Shifted product

**PROVED.**

\[
xy=m(x+y)+b
\iff
(x-m)(y-m)=m^2+b.
\]

### Möbius dilation conjugacy

**PROVED.**

\[
T_{a,b,d}(x)
=
-\phi_{a,d}^{-1}
\!\left(\lambda\phi_{a,d}(x)\right).
\]

## General universality

**OPEN GAP.**

No theorem in the visible project context establishes that every relevant linear-over-quadratic or paired multiplicative-linear identity is generated by the same finite set of geometric transformations.

---

# 16. Ulam prime-sequence problem

The project also contains a literature-search thread concerning the following problem.

Start from a finite increasing sequence of primes

\[
q_1<\cdots<q_m
\]

and continue recursively so that \(q_{n+1}\) is the smallest prime of the form

\[
q_n+q_i-1
\]

with an admissible earlier index \(i\), as described in the user’s formulation.

For example, starting from

\[
3,5
\]

the sequence begins

\[
3,5,7,11,13,17,\ldots
\]

The question is whether there exists an initial finite sequence producing an infinite sequence.

### Status

**OPEN GAP in daBook.**

The visible project record shows a request for relevant literature but no proof, counterexample, or new theorem arising from this branch.

---

# 17. Cross-program dependencies

## 17.1 Erdős 1061 → finite-field incidence

The divisor problem generated affine prime systems and coefficient constraints that ultimately led to incidence questions.

The projected symmetric-product transformation

\[
(x,y)\mapsto(x+y,xy)
\]

then revealed the translated-product fiber

\[
(x-m)(y-m)=K.
\]

Thus the strongest finite-field program is not independent of 1061 historically, even though the resulting lemmas may be publishable independently.

---

## 17.2 Finite-field incidence → Möbius energy

Shifted hyperbola fibers can be rewritten through reciprocal or Möbius transformations.

This produced exact energy identities connecting:

- diagonal square moments;
- multiplicative energy;
- Möbius images;
- exceptional fibers.

The project explicitly planned to foreground these structures in a companion or standalone paper rather than present them solely as 1061 machinery.

---

## 17.3 Finite-field structure → ECDLP

The ECDLP program imported:

- arithmetic coefficient decompositions;
- energy estimates;
- interval structure;
- multivariable algebraic relations;
- Coppersmith-style small-root ideas.

However, this dependency is one-way at present: the finite-field/divisor results do not rely on the ECDLP application.

---

## 17.4 Erdős 97: inversion → correspondence counting

For Erdős 97,

\[
\text{circle geometry}
\longrightarrow
\text{inversion}
\longrightarrow
\text{perpendicular-bisector incidence}
\longrightarrow
\text{injective correspondences}
\longrightarrow
\text{multiplicity-product bounds}.
\]

This is conceptually parallel to the 1061 program: a nonlinear geometric relation is transformed until a rigid counting statement becomes visible.

---

# 18. Contradictions, corrections, and failed approaches

A central-purpose report must preserve the failures because several substantially changed the direction of the research.

## 18.1 Erdős 97 local boundedness failure

**FAILED/DISPROVED.**

The proposed boundedness of a single adjacent-marked \(sGH^2\) family is false.

An exact two-circle construction yields arbitrarily long strict-convex marked families with both relevant gap curvatures below

\[
\frac14.
\]

### Correction

Replace local boundedness with a global witness-closure theorem.

---

## 18.2 Generic Möbius incidence as primary route

**FAILED AS PRIORITIZATION / INSUFFICIENT.**

The project originally searched for a generic \(PGL_2\)-family second-moment or incidence theorem.

The later shifted-hyperbola reduction revealed more structure than such a generic theorem would exploit.

### Correction

Work with

\[
(x-m)(y-m)=K
\]

and its moments first.

---

## 18.3 ECDLP constant \(108\)

**FAILED/DISPROVED AS JUSTIFIED CLAIM.**

A previous ECDLP argument used or claimed the constant

\[
108.
\]

An audit concluded the constant was not justified.

### Correction

Any theorem or complexity estimate depending quantitatively on \(108\) must be rederived from a valid bound.

---

## 18.4 ECDLP completion claim

**FAILED/DISPROVED.**

The architecture was described as plausible/correct in broad form, but not proved.

No completed ECDLP attack should be inferred from intermediate lemmas.

---

## 18.5 TRI formulation

**FAILED/REQUIRES CORRECTION.**

The project explicitly refers to a “corrected TRI,” implying an earlier formulation or proof was defective.

The exact defect is not present in the current synopsis.

---

## 18.6 Erdős 1 attempted route

**FAILED/DISPROVED ROUTE.**

The project considered posting a negative-result note, demonstrating that at least one plausible attack had been ruled out.

Exact details must be recovered from the source chat before publication.

---

# 19. Strongest currently identifiable open questions

## 19.1 Shifted-hyperbola cubic moment

Prove, disprove, or sharpen

\[
\sum_{m,K}
r(m,K)^3
\ll
|A|^4+\frac{|A|^6}{p},
\]

where

\[
r(m,K)
=
\#\{(x,y)\in A^2:(x-m)(y-m)=K\}.
\]

This is arguably the cleanest standalone finite-field frontier in the project.

### Recommended attacks

- expand the third moment into six-tuples and eliminate \(m,K\);
- classify diagonal and near-diagonal degeneracies;
- apply multiplicative energy after the shift \(A-m\);
- Fourier analyze in \(K\);
- stratify by zero/nonzero fibers;
- seek exact second-moment identities first and interpolate with maximal-richness estimates;
- determine whether Paley-character correlations control square/nonsquare \(K\) strata.

---

## 19.2 Rich-line theorem for \(S_A\)

Seek

\[
\#\{\ell:|S_A\cap\ell|\ge 3\}
\]

or

\[
\sum_\ell \binom{|S_A\cap\ell|}{3}
\]

with a power saving over trivial bounds.

A natural target is

\[
\#\{\text{3-point lines}\}
\ll |A|^{4-\delta}.
\]

### Why this matters

It is a geometric restatement of the same shifted-product moment problem and may admit incidence-geometric tools unavailable in the raw arithmetic formulation.

---

## 19.3 Exact second moment \(R_2(K)\)

Compute

\[
R_2(K)=\sum_m r_A(m,K)^2
\]

for:

\[
K=0,
\]

nonzero square \(K\), and

non-square \(K\).

The project expected possible connections with resultant energies and Paley correlations.

---

## 19.4 Uniform Möbius-slice summation

Given the slice-wise conjugacy

\[
T_{a,b,d}
=
-\phi_{a,d}^{-1}
\circ(\lambda\cdot)
\circ\phi_{a,d},
\]

prove an incidence or moment estimate that remains uniform after summing over \((a,d)\).

This would be broader than the shifted-hyperbola theorem and could constitute a separate \(PGL_2\) incidence result.

---

## 19.5 Opposite-sign coefficient energy

Complete the estimate for

\[
E(X)
=
\sum
\text{singular\_factor}
\frac{\gcd(A,D)}{cD+dA}
\]

subject to

\[
A=\Delta_2(c)>0,
\qquad
-D=\Delta_2(d)<0,
\]

\[
\gcd(A,D)\mid3(2-c-d).
\]

The small-small range should use

\[
S_k(H)
\ll_k(1+\log H)^{k+2},
\]

while the mixed and large-large regimes require genuine congruence or denominator savings.

---

## 19.6 Full Erdős 97 global witness closure

Generalize the proved two-gap marked-correspondence theorem to all residual four-gap hard-pattern cycles.

The key challenge is to convert multiplicity-one around closed cycles into an outright geometric impossibility.

---

## 19.7 Sieve-LCM antichain theorem for \(z^2-1\)

Recover the precise statement from the Erdős 886 chat and either prove it or exhibit a counterexample.

This should precede further attempts at the original problem because it was repeatedly identified as the critical bottleneck.

---

## 19.8 Finite-cover / box-based Coppersmith theorem

For the ECDLP program, isolate the exact algebraic theorem independent of cryptographic motivation:

> Under what degree, height, box, congr