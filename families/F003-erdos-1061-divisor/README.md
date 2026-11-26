# F003 — Erdős Problem #1061: divisor-sum equation

**Target (external problem statement).** With `σ` the sum-of-divisors
function, estimate the number `S(X)` of positive integer pairs `(a,b)` with
`a+b≤X` and `σ(a)+σ(b)=σ(a+b)`; the problem asks whether `S(X)~cX`
for a positive constant `c`. Counting ordered vs unordered solutions must
be specified before comparison.

## Project-reported statements (proofs not recovered)

- `DV-001` **REPORTED_UNVERIFIED:** For a project-defined `Δ₂(c)`, the
  logarithmic moment `S_k(H)=Σ_{|Δ₂(c)|≤H}(1+log c)^k/c`
  reportedly satisfies `S_k(H) ≪_k (1+log H)^{k+2}`.
  The definition of `Δ₂(c)` and range of `c` are not available here.
- `DV-002` **REPORTED_UNVERIFIED:** When `k=2^s` and `2^s+1` is prime,
  a fixed-ratio local-core classification reportedly has unique
  `d_0=2^{s-1}`. The local-core predicate was not recovered.
- `DV-003` **REPORTED_UNVERIFIED:** When `k=2^q−1` is a Mersenne prime,
  reported unique local core `d_0=2^{q-1}`; exact predicate missing.
- `DV-004` **REPORTED_UNVERIFIED:** Ratio `1:8` reportedly has unique local
  core `d_0=12`.
- `DV-005` **COMPUTATIONAL_EVIDENCE (reported, data not recovered):**
  Seed examples `(k,d_0)=(9,2),(15,3600),(39,60)` were listed in a chat.
  The original scripts and semantic definitions are unavailable.

## Explicit remaining analytic tasks

`DV-006` **OPEN_GAP:** Opposite-sign linear-linear coefficient energy

\[
E(X)=\sum \frac{\mathrm{singular\_factor}\,\gcd(A,D)}{cD+dA},
\quad A=\Delta_2(c)>0,\ -D=\Delta_2(d)<0,
\quad \gcd(A,D)\mid 3(2-c-d),
\]

under the project's additional affine prime-system restrictions. The
relevant summation domain, singular factor, and complete `Δ_2` definition
must be recovered before this becomes a formal theorem.

`DV-007` **OPEN_GAP:** Original `S(X)~cX` asymptotic. No proof is claimed.

**Dependency:** F001 collects associated projected-Segre and shifted
hyperbola formulas, but these do not settle the arithmetic prime systems.

**Primary reference:** https://www.erdosproblems.com/1061.
**Chats:** `Erdos problem 1061 proof`, `1061: Average Divisor Problems`,
`Promising Problem: Divisor Equation`, `1061 Erdos_support_paper Mathematical
Paper and Journals`.
