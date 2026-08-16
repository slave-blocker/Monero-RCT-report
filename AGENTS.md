# Repository agent instructions

## Commit requests

When the user says “add a commit”, treat that phrase as an explicit request
and authorization to create a local Git commit for the completed work in
scope. Inspect the staged set, choose a concise and reasonable commit message,
and commit it without asking for routine confirmation.

Do not push, open a pull request, or perform any other remote Git operation
unless the user explicitly requests it.
