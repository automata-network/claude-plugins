# Codex Plugin

⚠️ **EXPERIMENTAL - Version 0.0.1-alpha**

This plugin is in early development and not ready for production use.

## Overview

Integration with OpenAI Codex CLI for complex code generation, modification, and debugging tasks. This plugin provides a convenient interface to leverage Codex's capabilities directly from Claude Code.

## Features

- **`/codex` Command**: Execute Codex CLI tasks for code generation, debugging, and analysis
- **Codex Runner Agent**: Specialized agent for orchestrating iterative Codex executions
- **Session Management**: Resume previous Codex sessions for continued development

## Installation

Install from the automata-claude-plugins marketplace:

```bash
/plugin install codex@automata-claude-plugins
```

## Usage

### Basic Command

```bash
/codex [prompt]
```

### Examples

```bash
# Investigate issues
/codex investigate the authentication bug in the login flow

# Fix specific errors
/codex fix the type errors in src/utils/helper.ts

# General queries
/codex where are we in the project?
```

### Resuming Sessions

After a Codex execution, you'll receive a session ID. To resume manually:

```bash
codex resume <SESSION_ID>
```

Or use the command to resume the last session:

```bash
/codex resume
```

## How It Works

1. The `/codex` command launches a Task agent
2. The agent constructs and executes the appropriate Codex CLI command
3. Results are analyzed and returned to you
4. Session IDs are provided for manual resumption if needed

## Requirements

- OpenAI Codex CLI must be installed and configured
- Codex must be accessible via the `codex` command in your PATH

## Current Status

**Version**: 0.0.1-alpha
**Status**: Early development
**Stability**: Experimental

This plugin is under active development. Expect breaking changes and incomplete features.

## Support

For issues or questions, please contact the Automata Network DevOps team at devops@ata.network.
