# F004 — Erdős Problem #886: divisors close above sqrt(n)

**Target:** For each `epsilon>0`, is the number of divisors of `n` in
`(sqrt(n),sqrt(n)+n^(1/2-epsilon))` bounded by a constant depending on
`epsilon`, for all sufficiently large `n`?

- `WM-001` **OPEN_GAP:** The exponent range `0<epsilon<1/4`, where
  known `n^(1/4)`-scale results do not settle the problem.
- `WM-002` **EXTERNAL_RESULT:** Erdős--Rosenfeld established a
  `1+C^2`-type upper bound for divisors in a `Cn^(1/4)` window; in
  particular this covers `epsilon≥1/4`. This is not a daBook proof.
- `WM-003` **OPEN_GAP:** The proposed *sieve-lcm antichain theorem for
  `z^2-1`*. Earlier daBook chats asked repeatedly for a proof or
  counterexample, but no exact statement/certificate is available.

A comparison to P. Letendre's 2025 arXiv preprint `2503.12146` was
requested in the project; this archive has only the context of that
request, not a novel proof relative to the paper.

**Sources:** `Erdos Problem 886 Proof` project conversation;
https://www.erdosproblems.com/886;
https://arxiv.org/abs/2503.12146.
