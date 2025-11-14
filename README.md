# Claude Plugins Marketplace

A team plugin marketplace for Claude Code extensions. This repository provides a centralized catalog of plugins for discovering, installing, and managing Claude Code extensions across your organization.

## Using This Marketplace

### Add this marketplace to Claude Code

If this repository is hosted on GitHub:

```bash
/plugin marketplace add owner/claude-plugins
```

For other git hosting services:

```bash
/plugin marketplace add https://your-git-host.com/path/to/claude-plugins.git
```

For local development:

```bash
/plugin marketplace add /path/to/claude-plugins
```

### Install plugins from this marketplace

Once the marketplace is added, you can install plugins:

```bash
# Install a specific plugin
/plugin install plugin-name@claude-plugins

# Browse available plugins interactively
/plugin
```

### Verify marketplace installation

```bash
# List all configured marketplaces
/plugin marketplace list

# Update marketplace metadata
/plugin marketplace update claude-plugins
```

## Automatic Installation for Teams

Team members can automatically install this marketplace by adding it to their project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "claude-plugins": {
      "source": {
        "source": "github",
        "repo": "your-org/claude-plugins"
      }
    }
  }
}
```

When team members trust the repository folder, Claude Code will automatically install this marketplace and any plugins specified in the `enabledPlugins` field.

## Available Plugins

Currently, this marketplace contains no plugins. See [CONTRIBUTING.md](CONTRIBUTING.md) for information on adding plugins to this marketplace.

## Marketplace Structure

```
.claude-plugin/
  marketplace.json    # Main marketplace configuration
plugins/              # Optional: Host plugin source code here
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to add plugins to this marketplace.

## License

This marketplace is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Resources

- [Claude Code Plugin Documentation](https://docs.claude.com/en/plugins)
- [Plugin Marketplace Guide](https://docs.claude.com/en/plugin-marketplaces)
- [Plugin Development Guide](https://docs.claude.com/en/plugins#develop-more-complex-plugins)
