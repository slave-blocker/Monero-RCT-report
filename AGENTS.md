# Repository agent instructions

## Commit requests

When the user says “add a commit”, treat that phrase as an explicit request
and authorization to create a local Git commit for the completed work in
scope. Inspect the staged set, choose a concise and reasonable commit message,
and commit it without asking for routine confirmation.

Do not push, open a pull request, or perform any other remote Git operation
unless the user explicitly requests it.

## CPU usage

For CPU-bound local commands, limit parallelism to at most one fewer than the
number of available logical processors, with a minimum of one worker. Always
leave at least one logical processor free, and do not run multiple CPU-heavy
local commands concurrently when that could saturate the machine.

## Monero source reference

The read-only Monero source checkout used to audit protocol and implementation
claims is located at
`/media/dollner/aa266fbc-54ce-4aca-abc2-e91b713bb6e8/home/dollner/monero`.
Before relying on it, verify its revision; the report currently pins
`3646f648db57f60cca86430e25a635d19fa9b92a` (14 August 2026). Do not modify
that checkout while working on this report.

## RandomX source reference

The read-only RandomX checkout used to audit the proof-of-work specification,
design rationale, VM behavior, constants, and implementation claims is located
at
`/media/dollner/aa266fbc-54ce-4aca-abc2-e91b713bb6e8/home/dollner/randomx-monero`.
Before relying on it, verify that its revision is
`12f2c2ffe2108d6cf54c391fee33c8bc3646cdab` and inspect its worktree
read-only. This is the exact RandomX gitlink revision recorded by the pinned
Monero checkout. Do not modify this checkout while working on the report.

Relevant primary-source paths include `doc/specs.md`, `doc/design.md`,
`audits/`, `src/configuration.h`, and the VM and dataset/cache implementation
under `src/`. Use the pinned Monero checkout's `src/crypto/rx-slow-hash.c` when
checking how Monero integrates RandomX.

## monero-oxide FCMP++ source reference

The read-only checkout of the `fcmp++` branch of `monero-oxide` used to audit
the current FCMP++, Curve Trees, generator, and SAL descriptions is located at
`/media/dollner/aa266fbc-54ce-4aca-abc2-e91b713bb6e8/home/dollner/monero-oxide-fcmp`.
Before relying on it, verify that its revision is
`31c26d96eaadbba910ffe3613ad8b4cf9c598a93` (18 August 2026) and inspect its
worktree read-only. Do not modify this checkout while working on the report.

Relevant paths include `monero-oxide/ringct/fcmp++/generators/src/lib.rs`,
`monero-oxide/ringct/fcmp++/src/lib.rs`,
`monero-oxide/ringct/fcmp++/src/sal/mod.rs`,
`crypto/fcmps/ec-gadgets/src/dlog.rs`, and `crypto/fcmps/src/tree.rs`. The
older checkout at `~/fcmp-plus-plus` is useful for history but is not a
substitute for this pinned `monero-oxide` source when auditing the current
implementation description.

## Mounted home and auxiliary source paths

The user's canonical mounted home for this workspace is
`/media/dollner/aa266fbc-54ce-4aca-abc2-e91b713bb6e8/home/dollner`, not
`/home/dollner`. When notes or prompts use `~/...`, resolve them against the
canonical mounted home before deciding that a source is absent. Do not infer
source availability from a check under `/home/dollner`.

The Monero checkout above is accessible even when one of its Git submodules is
not initialized. Report those facts separately: an uninitialized
`external/randomx` does not mean that the Monero checkout or its
`src/crypto/rx-slow-hash.c` integration code is unavailable. Before reporting
any local paper, repository, or auxiliary source as missing, check its exact
absolute path under the canonical mounted home and state which path was
checked.

## User shorthand

When the user says “AMDCC”, interpret it as “answer me, don't change code”:
answer or explain only, without modifying repository files, rebuilding
artifacts, or running mutating commands. Read-only inspection is allowed. If
the same request explicitly authorizes a narrow exception, limit changes to
that exception.

## Authorial voice and mathematical exposition

The author's voice, magic, humour, pacing, visual notation, and pedagogical
style are paramount. Preserve distinctive elements such as quotations,
metaphors, narrative asides, diagrams, arrows, recursive derivations, and
transcript notation when revising the report. Correct technical, linguistic,
or LaTeX defects in place and improve the surrounding flow without flattening,
homogenizing, or wholesale replacing the authored exposition. Do not remove or
substantially rewrite those elements unless the user explicitly asks for it.

When newer protocol material is needed, add it after the existing exposition
as a clearly separated section or subsection whenever that preserves the
original pedagogical journey. Never treat technical modernization by itself as
authorization to erase the author's voice or presentation.

## Portuguese final page

Leave the final page of the Portuguese edition exactly as it is. Do not modify,
replace, regenerate, remove, rename, crop, recolor, retouch, or otherwise alter
the Monero-chan artwork or the LaTeX that places it, unless the user explicitly
withdraws this instruction.
