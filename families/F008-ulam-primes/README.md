# F008 — Ulam's recursively generated prime sequence

From the project conversation `Ulam prime sequence papers`:
start with a finite increasing sequence of primes
`q_1<⋯<q_m`, then recursively take `q_{n+1}` to be the smallest
eligible prime of the form `q_n+q_i−1` for an earlier index `i`
(the exact eligibility convention must be fixed from the original
problem). The example seed `(3,5)` was said to begin
`3,5,7,11,13,17,...`.

- `UL-001` **OPEN_GAP:** Determine whether some finite starting sequence
  produces an infinite sequence. No construction or proof exists in
  this archive.

The original conversation primarily requested prior research; exact
bibliographic sources were not included in the accessible excerpt.
