---
allowed-tools: Bash(git *)
description: Start a new work session with branch setup
---

Help the user start working on a new task.

Ask what they want to work on, then:

1. Check current git state and handle any uncommitted changes appropriately
2. Determine the main branch: Check if `main` or `master` exists and use that as the base branch
3. Fetch latest from the main branch: `git fetch origin <main-branch>`
4. Suggest a branch name like `feature/descriptive-name` based on their task
5. Create branch from origin main: `git checkout -b <branch> origin/<main-branch>`
6. Show a friendly summary with branch name and next steps

If they're already on a feature branch, ask if they want to continue or start new work.