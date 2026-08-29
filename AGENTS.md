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
