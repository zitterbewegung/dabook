# daBook — mathematical research archive

A versioned catalogue of theorems, lemmas, conjectures, counterexamples, failed
approaches, and proof gaps from the **daBook** mathematical research project.

This collection adopts the *organizational idea*, not the authorship or
verification claims, of [openai/math](https://github.com/openai/math): a central
manuscript map, families of related results, per-manuscript source and build
notes, a formalization catalogue, and a permanent correction history.

**Research data, not a certified corpus.** A `PROVED` label here means there is a
complete, inspectable elementary proof *in this repository*, subject to human
review; it is not a claim of novelty, journal refereeing, or Lean verification.
Other results from earlier chats are marked `REPORTED_UNVERIFIED` when their full
proof is not accessible. No claim about solving a famous open problem follows
from the inclusion of a research note here.

## Start here

- [CONTENTS.md](CONTENTS.md) — family-by-family manuscript and claim index.
- [STATUS.md](STATUS.md) — verification and correction dashboard.
- [overview.md](overview.md) — narrative map of the research programs.
- [preprints/](preprints/) — full, checkable standalone proof drafts and their source notes.
- [families/](families/) — every known research-family ledger, including unresolved work.
- [metadata/claims.json](metadata/claims.json) — machine-readable claim status and provenance.
- [lean/](lean/) — formalization inventory; *no completed Lean formalizations are asserted*.
- [sources/](sources/) — source map, a verbatim research note, and the August 14, 2026 central findings report (partial text).
- [reports/PRIOR_ART.md](reports/PRIOR_ART.md) — literature check and novelty cautions.
- [reasoning_traces/](reasoning_traces/) — public-facing summaries of proof ideas, not raw private reasoning.
- [history.md](history.md) — dated changes and corrections.

## Validation

With Python 3.10 or later, from the root:

```bash
python -m unittest discover -s tests -v
python scripts/check_catalog.py
```

These tests check finite-field identities exhaustively over small prime fields
and audit metadata links. They are **not** replacements for a proof.

## Publishing to the existing GitHub repository

The archive is a **local Git repository** with commit history. Publication in
this environment was blocked by a GitHub integration permission error (HTTP
403), so no remote push is claimed. With an authenticated local Git CLI, use:

```bash
bash scripts/publish_to_github.sh
```

This clones `zitterbewegung/dabook`, overlays these files on a *new review
branch*, retains unrelated files and the existing license, pushes that branch,
and offers a draft pull request when `gh` is installed. It does not update
`main` or force-push. The script requires `git`, `rsync`, and Python 3.

## Scope and coverage limitation

The accessible materials for this edition are the uploaded file
`Nondegenerate Collinear Triples.txt`, the August 14, 2026
`daBook — Central Findings Report` (verbatim, ending mid-sentence in §19.8),
the available project-conversation summaries and excerpts, and the publicly
accessible prior art listed in
`reports/PRIOR_ART.md`. Full transcripts and many prior papers/certificates were
not directly accessible. This is therefore a **source-limited initial catalogue**,
not a representation that every theorem ever discussed has been recovered.
Missing statements are recorded explicitly, never reconstructed from memory.
See [sources/SOURCE_MAP.md](sources/SOURCE_MAP.md). The central report is an
authoritative snapshot of what the project *reported*, not a verification
certificate. Report-level labels such as `PROVED` refer to earlier chat
assertions unless this archive has an independent proof.

## Independent verification and citations

For each result, cite the individual claim ID and linked document, not this
README. Submit missing source transcripts, counterexamples, precise theorem
statements, and formal proof files by pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

This repository is not affiliated with or endorsed by OpenAI's math repository.
