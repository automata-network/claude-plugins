---
allowed-tools: Bash(git *)
description: Commit your changes and push to GitHub
---

Save the user's work and push to remote.

**Don't allow commits on main/master branches** - tell them to use /start-work first.

1. Show what files changed
2. Review the changes and create a descriptive commit message based on what actually changed
   - Use conventional commit format: `feat:`, `fix:`, `refactor:`, `docs:`, `style:`, `chore:`
   - Be specific and accurate
   - No emojis in commit messages
3. Stage and commit meaningfully (not just `git add -A` - be selective if needed)
4. Determine the main branch (main or master) and sync with it: `git fetch origin <main-branch> && git rebase origin/<main-branch>`
5. Push: `git push origin <branch> --force-with-lease`

If rebase fails with conflicts:
- Abort the rebase: `git rebase --abort`
- Warn that there are conflicts that need to be resolved
- Push without rebase: `git push origin <branch>`

Use heredoc format for commit messages to handle multi-line properly.