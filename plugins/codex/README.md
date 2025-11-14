# Codex Plugin

⚠️ **EXPERIMENTAL - Version 0.0.1-alpha**

This plugin is in early development and not ready for production use.

## Overview

Integration with OpenAI Codex CLI for complex code generation, modification, and debugging tasks. This plugin provides a convenient interface to leverage Codex's capabilities directly from Claude Code.

## Features

- **`/codex` Command**: Execute Codex CLI tasks for code generation, debugging, and analysis
- **Codex Runner Agent**: Specialized agent for orchestrating iterative Codex executions
- **Codex Tmux Skill**: Run Codex interactively in a managed tmux session with automatic question handling
- **Session Management**: Resume previous Codex sessions for continued development

## Installation

Install from the claude-plugins marketplace:

```bash
/plugin install codex@claude-plugins
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

### `/codex` Command
1. The command launches a Task agent
2. The agent constructs and executes the appropriate Codex CLI command
3. Results are analyzed and returned to you
4. Session IDs are provided for manual resumption if needed

### Codex Tmux Skill
1. Claude automatically invokes this skill when you request interactive Codex execution
2. Creates or reuses a persistent tmux session named `codex-session`
3. Executes Codex in the background and monitors for questions
4. Uses the AskUserQuestion tool to handle interactive prompts from Codex
5. Keeps the session alive for continued use across multiple invocations

The skill is model-invoked, meaning Claude decides when to use it based on your request. You don't need to explicitly call it - just mention interactive Codex execution or working with Codex in a tmux session.

## Requirements

- OpenAI Codex CLI must be installed and configured
- Codex must be accessible via the `codex` command in your PATH
- tmux (required for the Codex Tmux Skill)

## Current Status

**Version**: 0.0.1-alpha
**Status**: Early development
**Stability**: Experimental

This plugin is under active development. Expect breaking changes and incomplete features.

## Support

For issues or questions, please contact the Automata Network DevOps team at devops@ata.network.
