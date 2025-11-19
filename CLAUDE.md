# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository is a **Claude Code plugin marketplace** - a centralized catalog for discovering, installing, and managing Claude Code extensions across a team or organization. The marketplace is defined by a single JSON file that lists available plugins and describes where to find them.

## Core Architecture

### Marketplace Configuration
- **Location**: `.claude-plugin/marketplace.json`
- **Schema**: Follows the official Claude Code marketplace specification
- **Structure**:
  - `name`: Marketplace identifier (must be kebab-case)
  - `owner`: Maintainer information (name and email)
  - `metadata`: Optional description and version
  - `plugins`: Array of plugin entries

### Plugin Sources
Plugins can be hosted in three ways:
1. **Local (relative paths)**: Plugin source code in `plugins/` directory within this repo
2. **GitHub repositories**: External GitHub repos specified with `{"source": "github", "repo": "owner/name"}`
3. **Git URLs**: Any git repository specified with `{"source": "url", "url": "https://..."}`

### Plugin Entry Schema
Each plugin entry in the marketplace can include:
- **Required**: `name` (identifier), `source` (location)
- **Recommended**: `description`, `version`, `author`
- **Advanced**: `commands`, `agents`, `hooks`, `mcpServers` (custom component paths)
- **Control**: `strict` (default: `true`) - when `false`, plugin.json is optional

## Common Development Tasks

### Validate Marketplace JSON
```bash
# Using Claude Code validation
claude plugin validate .

# Manual JSON syntax check (requires jq)
cat .claude-plugin/marketplace.json | jq .
```

### Test Marketplace Locally
```bash
# In Claude Code, add this marketplace locally
/plugin marketplace add /workspaces/claude-plugins

# Install a plugin from the marketplace
/plugin install plugin-name@automata-claude-plugins

# List all marketplaces
/plugin marketplace list

# Update marketplace metadata
/plugin marketplace update automata-claude-plugins
```

### Adding a New Plugin

**For locally hosted plugins:**
1. Create plugin directory: `plugins/plugin-name/`
2. Add plugin files (commands, agents, hooks, etc.)
3. Add entry to `.claude-plugin/marketplace.json`:
```json
{
  "name": "plugin-name",
  "source": "./plugins/plugin-name",
  "description": "What the plugin does",
  "version": "1.0.0",
  "author": {"name": "Author Name"}
}
```

**For externally hosted plugins:**
Add entry pointing to external source:
```json
{
  "name": "plugin-name",
  "source": {"source": "github", "repo": "owner/repo"},
  "description": "What the plugin does"
}
```

### Updating the Marketplace
1. Edit `.claude-plugin/marketplace.json` to add/modify plugin entries
2. Validate JSON syntax
3. Test locally before committing
4. Update README.md's "Available Plugins" section if needed

## Repository Structure

```
.claude-plugin/
  marketplace.json       # Main marketplace configuration file
plugins/                 # Optional: locally hosted plugin source code
  plugin-name/          # Individual plugin directory
    .claude-plugin/
      plugin.json       # Plugin manifest (required)
    commands/           # Slash commands (at root level)
    agents/             # Agent definitions (at root level)
    hooks/              # Lifecycle hooks (at root level)
    skills/             # Skills (at root level)
README.md              # Marketplace usage documentation
CONTRIBUTING.md        # Plugin contribution guidelines
CLAUDE.md             # This file
```

### Official Plugin Directory Structure

Each plugin must follow this exact structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Required: Plugin metadata and configuration
├── commands/                # Optional: Slash commands (e.g., /my-command)
│   └── command-name.md
├── agents/                  # Optional: Specialized agents
│   └── agent-name.md
├── hooks/                   # Optional: Lifecycle hooks
│   └── hook-name.md
├── skills/                  # Optional: Skills
│   └── skill-name.md
└── README.md               # Optional: Plugin documentation
```

**Important Rules:**
1. ✓ `plugin.json` **MUST** be in `.claude-plugin/plugin.json` (not at root)
2. ✓ All component directories (`commands/`, `agents/`, `hooks/`, `skills/`) **MUST** be at the plugin root
3. ✗ **DO NOT** nest components inside `.claude/` or `.claude-plugin/` directories
4. ✗ **DO NOT** put `plugin.json` at the root level

This structure is required by the official Claude Code plugin specification and ensures compatibility with the plugin system.

## Important Considerations

### Marketplace Name
- Must be kebab-case (lowercase with hyphens)
- Used as identifier when installing: `/plugin marketplace add owner/repo`
- Cannot contain spaces or special characters

### Plugin Naming
- Use kebab-case for plugin names
- Must be unique within the marketplace
- Descriptive and clear (e.g., "deployment-tools", "code-formatter")

### Version Management
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Update version numbers when plugin functionality changes
- Document version changes in commit messages

### JSON Validation
- Marketplace JSON must be valid before committing
- Use `claude plugin validate .` or `jq` to verify syntax
- Common errors: trailing commas, unescaped quotes, missing brackets

### Testing Workflow
Always test plugins locally before adding to marketplace:
1. Add marketplace locally with absolute path
2. Install the plugin
3. Verify all plugin components work (commands, agents, hooks)
4. Check for any errors or missing dependencies

### Strict vs Non-Strict Plugins
- `strict: true` (default): Plugin must have `plugin.json` file; marketplace fields supplement it
- `strict: false`: plugin.json is optional; marketplace entry can serve as complete manifest
- Use non-strict mode for simple plugins without separate manifest files

## Git Workflow

### Branch Naming
- Feature branches: `add-plugin-<plugin-name>`
- Updates: `update-plugin-<plugin-name>`
- Fixes: `fix-<issue-description>`

### Commit Messages
```bash
# Adding new plugin
git commit -m "Add <plugin-name> plugin"

# Updating plugin
git commit -m "Update <plugin-name> to v<version>"

# Fixing marketplace
git commit -m "Fix marketplace JSON syntax error"
```

## References

- [Claude Code Plugin Documentation](https://docs.claude.com/en/plugins)
- [Plugin Marketplace Guide](https://docs.claude.com/en/plugin-marketplaces)
- [Plugin Development Guide](https://docs.claude.com/en/plugins#develop-more-complex-plugins)
- [Plugins Reference](https://docs.claude.com/en/plugins-reference)
