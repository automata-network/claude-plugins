# Git Workflow Plugin

Streamlined Git workflow commands for managing branches, commits, and pull requests with best practices built-in.

## Commands

### `/start-work`

Start a new work session with proper branch setup.

**What it does:**
- Checks current git state and handles uncommitted changes
- Determines the main branch (main or master)
- Fetches latest from the main branch
- Creates a new feature branch from origin main
- Suggests descriptive branch names based on your task

**Safety features:**
- Prompts if you're already on a feature branch
- Ensures you're starting from the latest main branch

### `/push-work`

Commit your changes and push to GitHub with best practices.

**What it does:**
- Shows what files changed
- Creates descriptive commit messages using conventional commit format
- Stages and commits changes selectively
- Syncs with main branch using rebase
- Pushes to remote with `--force-with-lease` for safety

**Commit format:**
- Uses conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `style:`, `chore:`
- No emojis (professional format)
- Descriptive and accurate messages

**Safety features:**
- Prevents commits on main/master branches
- Handles rebase conflicts gracefully
- Uses `--force-with-lease` to prevent overwriting others' work

### `/draft-pr`

Create or update a draft pull request for review.

**What it does:**
- Checks for uncommitted changes
- Ensures branch is pushed and synced with main
- Checks if PR already exists
- Analyzes all commits to generate comprehensive PR description
- Creates new draft PR or updates existing one

**PR description includes:**
- Summary of changes
- List of what was modified
- Testing considerations (if applicable)

**Safety features:**
- Prevents PRs from main/master branches
- Won't update merged or closed PRs (creates new one instead)
- Provides clear next steps after PR creation

## Typical Workflow

1. **Start new work:**
   ```
   /start-work
   ```
   Tell Claude what you want to work on, and it will set up a proper feature branch.

2. **Make your changes** using Claude Code as normal

3. **Save and push your work:**
   ```
   /push-work
   ```
   Claude will create a meaningful commit message and push to GitHub.

4. **Create pull request:**
   ```
   /draft-pr
   ```
   Claude will analyze your changes and create a draft PR with a comprehensive description.

## Requirements

- Git must be installed and configured
- GitHub CLI (`gh`) must be installed and authenticated (for `/draft-pr`)
- Repository must have a remote configured

## Best Practices

- Always use `/start-work` before beginning new features
- Commit frequently with `/push-work` to avoid losing work
- Use `/draft-pr` early to get feedback, even if work isn't complete
- Keep commits focused and atomic

## Safety Features

This plugin enforces several best practices:

- **No direct commits to main/master** - Prevents accidental commits to protected branches
- **Branch-based workflow** - All work happens on feature branches
- **Conventional commits** - Standardized commit message format
- **Safe force pushes** - Uses `--force-with-lease` to prevent overwriting others' work
- **Rebase workflow** - Keeps commit history clean and linear
- **Draft PRs** - Encourages early feedback without marking work as ready

## License

MIT
