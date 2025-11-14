# Contributing to the Claude Plugins Marketplace

Thank you for contributing to our Claude Code plugin marketplace! This guide will help you add new plugins or update existing ones.

## Adding a New Plugin

### Option 1: Plugin Hosted in This Repository

If you want to host the plugin source code in this repository:

1. **Create plugin directory**:
   ```bash
   mkdir -p plugins/your-plugin-name
   ```

2. **Add plugin files** to `plugins/your-plugin-name/`:
   - `plugin.json` - Plugin manifest (optional if using `strict: false`)
   - Command files in `.claude/commands/` (if applicable)
   - Agent files (if applicable)
   - Hook scripts (if applicable)
   - MCP server configurations (if applicable)

3. **Update marketplace.json**:
   ```json
   {
     "name": "your-plugin-name",
     "source": "./plugins/your-plugin-name",
     "description": "Brief description of what your plugin does",
     "version": "1.0.0",
     "author": {
       "name": "Your Name",
       "email": "your.email@example.com"
     }
   }
   ```

### Option 2: Plugin Hosted Externally

If your plugin is hosted in a separate repository:

**For GitHub repositories**:
```json
{
  "name": "your-plugin-name",
  "source": {
    "source": "github",
    "repo": "owner/repository"
  },
  "description": "Brief description of what your plugin does"
}
```

**For other Git repositories**:
```json
{
  "name": "your-plugin-name",
  "source": {
    "source": "url",
    "url": "https://gitlab.com/team/plugin.git"
  },
  "description": "Brief description of what your plugin does"
}
```

## Plugin Entry Schema

### Required Fields

- `name` - Plugin identifier (kebab-case, no spaces)
- `source` - Where to fetch the plugin from (relative path, GitHub repo, or Git URL)

### Recommended Fields

- `description` - Brief explanation of plugin functionality
- `version` - Semantic version number (e.g., "1.0.0")
- `author` - Object with `name` and optionally `email`
- `homepage` - URL to plugin documentation
- `keywords` - Array of searchable tags

### Optional Advanced Fields

- `commands` - Custom paths to command files or directories
- `agents` - Custom paths to agent files
- `hooks` - Custom hooks configuration
- `mcpServers` - MCP server configurations
- `strict` - Set to `false` if plugin doesn't have a `plugin.json` file
- `category` - Plugin category for organization
- `tags` - Additional tags for searchability

### Example: Full Plugin Entry

```json
{
  "name": "deployment-tools",
  "source": "./plugins/deployment-tools",
  "description": "Automated deployment workflow tools",
  "version": "2.1.0",
  "author": {
    "name": "DevOps Team",
    "email": "devops@example.com"
  },
  "homepage": "https://docs.example.com/plugins/deployment-tools",
  "repository": "https://github.com/example/deployment-tools",
  "license": "MIT",
  "keywords": ["deployment", "ci-cd", "automation"],
  "category": "devops",
  "commands": [
    "./commands/deploy/",
    "./commands/rollback.md"
  ],
  "agents": [
    "./agents/deployment-planner.md"
  ]
}
```

## Validation and Testing

### Validate Your Changes

Before submitting:

```bash
# Validate marketplace JSON syntax
claude plugin validate .

# Or manually check JSON syntax
cat .claude-plugin/marketplace.json | jq .
```

### Test Locally

1. **Add marketplace locally**:
   ```bash
   /plugin marketplace add /workspaces/claude-plugins
   ```

2. **Try installing your plugin**:
   ```bash
   /plugin install your-plugin-name@claude-plugins
   ```

3. **Verify plugin works**:
   - Test all commands
   - Verify agents load correctly
   - Check hooks trigger as expected

## Submission Process

1. **Create a feature branch**:
   ```bash
   git checkout -b add-plugin-your-plugin-name
   ```

2. **Make your changes**:
   - Add plugin files (if hosting locally)
   - Update `.claude-plugin/marketplace.json`
   - Update the "Available Plugins" section in `README.md`

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add your-plugin-name plugin"
   ```

4. **Push and create pull request**:
   ```bash
   git push origin add-plugin-your-plugin-name
   ```

5. **Submit pull request** with:
   - Clear description of what the plugin does
   - Any special installation or usage instructions
   - Testing results

## Plugin Quality Guidelines

- **Clear naming**: Use descriptive, kebab-case names
- **Good documentation**: Provide clear descriptions and usage instructions
- **Version control**: Use semantic versioning
- **Testing**: Verify plugin works before submitting
- **Dependencies**: Document any external dependencies or requirements
- **Licensing**: Ensure your plugin has appropriate licensing

## Updating Existing Plugins

1. **Update plugin source** (if hosted in this repo)
2. **Update version number** in marketplace.json
3. **Update description** if functionality changed
4. **Document changes** in commit message
5. **Test thoroughly** before submitting

## Getting Help

- Review [Claude Code Plugin Documentation](https://docs.claude.com/en/plugins)
- Check [Plugin Marketplace Guide](https://docs.claude.com/en/plugin-marketplaces)
- Open an issue in this repository for questions

## Code of Conduct

- Be respectful and collaborative
- Provide constructive feedback
- Help others learn and grow
- Follow team guidelines and standards
