# Preliminary prior-art and external-status audit

**Search date: 2026-11-25.** This is a targeted search, not an exhaustive
precedence investigation. A correct elementary identity may be long known.

## Finite-field incidence and shifted hyperbolas

Brendan Murphy and Giorgis Petridis, *A point-line incidence identity in
finite fields, and applications* (2016),
https://arxiv.org/abs/1601.03981, develops a second-moment identity for
point-line incidences. The F001 exact energy formula is a particular elementary
calculation and should **not** be advertised as a previously unknown analogue
until an actual precedence audit is complete. Relevant related work includes
Audie Warren and James Wheeler, *Incidences of Möbius transformations in
F_p* (2021),
https://www.ricam.oeaw.ac.at/files/reports/21/rep21-30.pdf.

The user-supplied note calls a general structured PGL_2 theorem missing, but
that literature-negative claim is not certified by this audit. Neither the
Möbius linearization nor elementary factorization implies new optimal
incidence bounds on their own.

## Erdős #97 and #96 (major status change)

The original page https://www.erdosproblems.com/97 is marked OPEN in the
inspected crawl. A **different, newer** corpus records 2026 proof claims by
Kruer--Kohlmeyer and Kruer--Kohlmeyer--Price, with Lean 4 proofs and a claim of
external checking, implying counterexamples to Erdős #97 and the fixed-k
variant. See
https://erdosproblems.ai/wiki/problems/distance_problems/E0097 and
https://erdosproblems.ai/wiki/problems/distance_problems/E0096/claims/2026_09_13_kruer_kohlmeyer_price.

The archive did not replay the Lean files and does not assert independent
acceptance by the original Erdős Problems curator or a journal. The project
work on convex-gap separators **must not** be presented as solving the problem
without addressing this newer prior art.

## Erdős #886 and related divisor-window literature

https://www.erdosproblems.com/886 states the short divisor-window problem.
Erdős and Rosenfeld, *The factor-difference set of integers*, Acta Arith.
79 (1997), 353–359, established a bound of the form `1+C^2` near `sqrt(n)`
for width `C n^(1/4)`. Thus the critical unsolved range is conventionally
`0<epsilon<1/4`. See
https://erdosproblems.ai/wiki/problems/divisors/E0886.

Pierre Letendre, *Divisors of an Integer in a Short Interval* (2025),
https://arxiv.org/abs/2503.12146, is the preprint discussed in the daBook
chat. Its relationship to the project-specific sieve-lcm antichain proposal
requires checking the actual candidate theorem; no independent new bound is
claimed here.

## Erdős #1061 and its exact target

https://www.erdosproblems.com/1061 asks for asymptotics of the number of
positive integer pairs with `a+b<=X` and
`sigma(a)+sigma(b)=sigma(a+b)`, potentially `~cX` for `c>0`. The project
fixed-ratio observations are not a proof of this density asymptotic.
The formal conjecture is listed at
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1061.lean.

## Other programs

No original ECDLP decomposition oracle, ordinary-box theorem, full FP-TRI
statement, or verified Lean proof was available. Consequently this edition
makes **no** cryptographic algorithm, complexity improvement, or theorem-of-
novelty claim in that program. For the Ulam sequence and finite-field phase
program, current source support is likewise insufficient to establish novelty.
