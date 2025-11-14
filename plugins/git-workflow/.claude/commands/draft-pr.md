---
allowed-tools: Bash(git *), Bash(gh *)
description: Create or update a draft pull request for review
---

Create or update a draft pull request for the user's work.

**Don't allow PRs from main/master branches.**

1. Check for uncommitted changes - if any, suggest using /push-work first
2. Determine the main branch (main or master) to use as the base
3. Make sure branch is pushed and synced with the main branch
4. Check if PR already exists: `gh pr list --head <branch> --state all`
   - Parse the output to determine PR state (open/merged/closed)
5. Analyze all commits from the main branch to generate a good PR description
6. Create or update PR based on step 4:
   - **If no PR exists:** Create new draft PR with `gh pr create --base <main-branch> --draft --title "..." --body "..."`
   - **If PR exists and is open:** Update existing PR with `gh pr edit <number> --title "..." --body "..."`
   - **If PR exists and is merged/closed:** Create new draft PR (don't update merged/closed PRs)
7. Show PR URL and next steps

Use heredoc for PR body to handle markdown properly.

PR description should include:
- Summary of changes
- List of what was modified
- Testing considerations (if applicable)