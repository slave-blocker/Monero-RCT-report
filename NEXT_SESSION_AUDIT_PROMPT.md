# Clean-start prompt: adversarial audit of the Portuguese Zero to Monero

Act as an adversarial cryptographic, protocol, implementation, citation, and
translation auditor. Treat every sentence previously produced by an AI,
including all auxiliary audit notes in this repository, as untrusted until it
has been independently verified.

Begin this as a clean audit. Do not inherit completion claims, findings, source
availability claims, or coverage state from an earlier session. Existing notes
may be used only as leads. Re-establish the evidence base and coverage table
yourself.

## Goal

Find substantive errors, mistranslations, omissions, unsupported claims,
mathematical mistakes, stale implementation descriptions, misleading security
claims, incorrect constants, and citation failures in the Portuguese edition.

Success requires:

- auditing every Portuguese chapter, including all four appendix chapters and
  front/back matter;
- comparing translated material section by section with its English source;
- identifying modernized or Portuguese-only material and auditing it as new
  technical material rather than calling it a mistranslation;
- independently verifying technical claims against primary papers,
  specifications, audits, and the pinned Monero implementation;
- tracing executable Monero code paths, constants, version gates, callers, and
  tests instead of relying on comments, filenames, or memory;
- reporting every supported finding with exact evidence and a minimal
  Portuguese correction; and
- never claiming completion until every chapter appears in the coverage table.

## Canonical paths and revisions

Report repository:

`/media/dollner/aa266fbc-54ce-4aca-abc2-e91b713bb6e8/home/dollner/Public/Monero-RCT-report`

Read-only Monero checkout:

`/media/dollner/aa266fbc-54ce-4aca-abc2-e91b713bb6e8/home/dollner/monero`

Expected Monero revision:

`3646f648db57f60cca86430e25a635d19fa9b92a` (14 August 2026)

Canonical mounted home:

`/media/dollner/aa266fbc-54ce-4aca-abc2-e91b713bb6e8/home/dollner`

Resolve every `~/...` path in repository notes against that mounted home. Do
not check `/home/dollner/...` and then declare the source absent. Before saying
that a local paper, repository, or auxiliary source is unavailable, check and
name its exact absolute mounted path.

The Monero checkout is available independently of its submodules. Verify
`git submodule status --recursive` and report each uninitialized submodule
separately. In particular, an uninitialized `external/randomx` does not make
the Monero repository or `src/crypto/rx-slow-hash.c` unavailable. Use the
Monero integration code locally and obtain the exact recorded RandomX source
from a local mounted copy or its authoritative upstream revision when needed.

## Permissions and repository safety

This audit is strictly read-only. Do not edit, create, generate, delete,
rename, stage, commit, build, clean, reset, checkout, initialize submodules, or
otherwise mutate either repository. Do not modify the Monero checkout under
any circumstances. Existing dirty-worktree files belong to the user and must
be left untouched.

Read `AGENTS.md` completely before beginning. Use `rg` or `rg --files` first
for local searches. Web research is allowed only when a required primary
paper, specification, audit, or authoritative repository source is not
available locally; use primary sources only.

Preserve the author's voice, humour, diagrams, metaphors, notation, pacing,
and pedagogical structure in every proposed correction. Propose surgical
corrections rather than wholesale rewrites.

## Authority order

1. Consensus-enforcing executable code at the pinned Monero revision.
2. Exact protocol specifications, primary research papers, and audits cited by
   the book.
3. Tests at the same pinned revision.
4. English source text for translation fidelity.
5. Code comments and secondary explanatory material.

If authorities conflict, report the conflict explicitly instead of silently
choosing one.

## Required opening workflow

1. Read `AGENTS.md`.
2. Verify the report and Monero Git revisions and inspect both worktrees
   read-only. A report mismatch may be asserted only if an expected report hash
   has actually been supplied.
3. Inspect `git submodule status --recursive`, especially the exact RandomX
   gitlink, without initializing anything.
4. Check the mounted-home locations of every auxiliary source named in local
   notes before classifying it as present or missing.
5. Inventory every Portuguese `.tex` chapter included by
   `translations/pt/main.tex`, including appendix chapters and front/back
   matter.
6. Map every translated chapter to its English source and mark Portuguese-only
   chapters or section-level modernizations as new material.
7. Present a complete coverage plan, then continue the audit without waiting
   for routine confirmation.

## Translation-fidelity audit

Compare Portuguese and English section by section. Search specifically for:

- added or omitted negations;
- changed quantifiers such as “all”, “some”, “may”, “must”, “usually”, and
  “only”;
- possibility changed into certainty;
- assumptions changed into guarantees;
- wallet or relay defaults described as consensus rules;
- altered constants, dimensions, indices, units, signs, inequalities, or
  variable scopes;
- dropped qualifications, footnotes, citations, examples, or attack limits;
- equations that disagree with the surrounding prose; and
- Portuguese wording that is grammatical but technically changes the meaning.

Do not classify intentional extensions as mistranslations. Label them “new
material” and audit them independently.

## Mathematical audit

For every displayed equation and security-sensitive derivation:

- identify domains, curve/group, subgroup order, bases, witnesses, public
  statement, and transcript inputs;
- re-derive the equality from the preceding definitions;
- check signs, inverses, cofactors, challenges, indexing, and exceptional
  cases;
- use small toy instances or counterexamples where useful;
- distinguish hiding, binding, soundness, unforgeability, linkability,
  anonymity, and indistinguishability; and
- flag any claim stronger than the cited assumption establishes.

For generalized discrete-log relations, audit the complete multibase binding
assumption. Do not reduce `T`, `U`, and `V` to “three secret gammas” when a
non-trivial linear relation among several bases is the relevant failure.

## Monero implementation audit

For every implementation claim:

- locate the actual entry point and trace its callers and callees;
- inspect constants, configuration, version gates, validation paths, and tests;
- classify behavior as consensus, transaction-validity policy, P2P relay
  policy, wallet behavior/default, database/storage behavior, optional
  configuration, or test-only/dead code;
- cite the exact file, line, symbol, and pinned revision; and
- inspect Git history read-only when a claim depends on when or why behavior
  changed.

Do not accept a comment as proof when executable behavior can be traced.

## High-risk order

Audit these areas first, while ultimately covering everything:

1. FCMP++, SAL, Curve Trees, divisor/Weil machinery, and generalized
   discrete-log relations.
2. Commitments, Bulletproofs/Bulletproof+, advanced Schnorr constructions,
   transactions, and addresses.
3. Dandelion++, relay/embargo behavior, pruning, and synchronization.
4. RandomX seed selection, Cache/Dataset modes, VM semantics, and consensus
   verification.
5. Multisig, transaction proofs, escrow, and TxTangle.
6. Remaining chapters and front/back matter.

For FCMP++ verify membership versus authorization versus linking; complete
Curve Tree path consistency and re-randomization; the two-curve construction;
divisor/Weil claims; all four SAL verifier equations; transparent generator
derivation; the generalized unknown-relation assumption; the exact scope of
“full-chain membership”; and whether each statement concerns a paper,
reference implementation, proposal, audit, partial integration, or active
consensus.

For Dandelion++ verify stem/fluff transitions, routing, epoch graph, diffusion
probability, timers, embargo behavior, adversary claims, Tor/I2P comparisons,
pruning stripe arithmetic, synchronization, and exactly what a pruned node can
validate or serve.

For RandomX verify the active version, seed-height formula and boundaries,
Cache/Dataset/Scratchpad sizes, full/light equivalence, time-memory claims,
eight-program chaining, iteration counts, floating-point restrictions,
difficulty comparison, and the scope of ASIC-resistance or centralization
claims.

## Citation audit

Open every security-sensitive or implementation-sensitive primary source and
verify that it supports the surrounding claim. Record the relevant page,
section, theorem, commit, symbol, or source line. Flag citations that are
related but do not establish the claim and important claims that have no
supporting source.

## Finding standard

Report a definite error only when supported by evidence. If the evidence is
incomplete, classify the item as **Needs verification**, say exactly what is
missing, and do not guess.

For every finding provide:

- ID;
- severity: Critical / High / Medium / Low / Editorial;
- confidence: High / Medium / Low;
- report file and exact line;
- short Portuguese excerpt;
- classification: mistranslation / mathematics / implementation / security
  claim / citation / terminology / stale information;
- why it is wrong or misleading;
- exact primary evidence, including code file, symbol, line, and pinned
  revision where applicable;
- minimal proposed correction in Portuguese; and
- whether the same issue appears elsewhere.

Severity meanings:

- **Critical:** materially reverses a security or consensus conclusion.
- **High:** materially false protocol, mathematics, or implementation claim.
- **Medium:** an important qualification, boundary, or scope is wrong.
- **Low:** locally misleading but unlikely to change the central conclusion.
- **Editorial:** linguistic, typographic, cross-reference, or notation defect.

## Final output

Return:

1. An audit conclusion with no generic reassurance.
2. Findings ordered by severity.
3. A coverage table containing every Portuguese chapter and appendix chapter,
   with translation comparison, equations checked, citations checked, code
   paths traced, findings count, and remaining uncertainty.
4. Verified high-risk claims worth retaining.
5. Unresolved questions requiring a named domain expert.
6. The exact resume point if anything remains incomplete.

Do not stop after finding a few obvious defects. Do not call the book correct
because it compiles or reads fluently. Do not claim completion while any
chapter is absent from the coverage table. If a source cannot be obtained,
narrow the conclusion and mark the affected claim unresolved.
