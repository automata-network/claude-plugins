---
name: codex-tmux
description: Run Codex interactively in a managed tmux session with automatic question handling. Use when user wants to run Codex interactively, work with Codex in background, or when Codex needs to ask clarifying questions.
allowed-tools: Bash, AskUserQuestion
---

# Codex Tmux Skill

Run Codex in interactive mode within a managed tmux session. This skill transparently handles session management and monitors for questions from Codex, enabling interactive workflows.

## When to Use This Skill

Use this skill when:
- User wants to run Codex interactively
- User mentions tmux or background sessions
- User wants to continue a previous Codex session
- Codex needs to ask clarifying questions during execution
- User wants non-blocking Codex execution

## Instructions

Follow these steps to run Codex in a managed tmux session:

### 1. Parse Command Arguments

Extract the full user prompt for Codex. The prompt should describe the task Codex needs to perform.

### 2. Determine Working Directory Scope

Analyze the prompt to determine the appropriate scope:
- If the prompt mentions specific directories or paths (e.g., "in src/auth", "the api/ folder"), use `-C <DIR>` flag to limit scope
- If the prompt is broad or general (e.g., "fix all bugs", "analyze the codebase"), omit `-C` to use the entire codebase
- Examples:
  - "fix auth bugs in src/auth" → use `-C src/auth`
  - "analyze performance issues" → no `-C` flag (entire codebase)

### 3. Manage Tmux Session

Session management:
- **Session name**: Always use `codex-session`
- **Check if session exists**: Run `tmux has-session -t codex-session 2>/dev/null`
  - Exit code 0 = session exists
  - Exit code 1 = session doesn't exist
- **If session doesn't exist**: Create it with `tmux new-session -d -s codex-session`
- **If session exists**: Check if Codex is already running
  - Capture current pane: `tmux capture-pane -t codex-session -p -S -10`
  - Look for active Codex process indicators (prompts, running commands)
  - If Codex is busy, inform the user and suggest waiting or checking status with `tmux attach -t codex-session`

### 4. Send Prompt to Codex

Execute the Codex command in the tmux session:

```bash
tmux send-keys -t codex-session "codex --yolo [-C <DIR>] exec '[prompt]'" C-m
```

Important notes:
- Always use `--yolo` flag for non-interactive execution
- Use `exec` subcommand to start a new execution
- Properly escape the prompt with single quotes
- Include `-C <DIR>` if specific scope was determined in step 2

Inform the user that Codex is running in the background.

### 5. Monitor the Session

Wait and monitor for Codex output and questions:

1. **Initial wait**: Sleep for 3-5 seconds to allow Codex to start
2. **Capture output**: `tmux capture-pane -t codex-session -p -S -50`
3. **Look for question patterns**:
   - Lines ending with "?"
   - Prompts like "(y/n)", "(yes/no)", "choose:", "select:"
   - Multiple choice options (numbered lists followed by a prompt)
   - Any text indicating user input is needed
4. **Check for completion indicators**:
   - "✓" or "Done" or "Completed" messages
   - Shell prompt reappearing
   - No activity for several seconds

### 6. Handle Questions from Codex

When a question is detected:

1. **Extract the question text** from the captured output
2. **Use AskUserQuestion tool** to prompt the user:
   - Parse the question to create appropriate options
   - For yes/no questions, provide "Yes" and "No" options
   - For multiple choice, extract the options from Codex output
   - Set `multiSelect: false` for single-choice questions
3. **Send user's answer** back to tmux session:
   ```bash
   tmux send-keys -t codex-session "[answer]" C-m
   ```
4. **Continue monitoring**: Return to step 5 to wait for next question or completion

### 7. Report Results

When the task appears complete:

1. **Capture final output**: `tmux capture-pane -t codex-session -p -S -100`
2. **Show output to user**: Include relevant portions of what Codex did
3. **Extract session ID**: Look for session ID in the output (usually shown at the beginning)
4. **Provide next steps**:
   - Inform user the session is still active
   - Provide session ID for manual resumption
   - Suggest commands:
     - `tmux attach -t codex-session` to view/interact with session
     - `codex resume <SESSION_ID>` to resume via Codex CLI
     - Future invocations will reuse the same tmux session

### 8. Session Cleanup

- **Keep session alive**: Do NOT kill the session after completion
- The session should persist for future Codex commands
- Only kill the session if:
  - User explicitly requests it
  - Unrecoverable errors occur
  - Session becomes corrupted

To kill session if needed: `tmux kill-session -t codex-session`

## Examples

### Example 1: Simple Task
```
User: Run codex to fix the authentication bugs in src/auth
→ Creates/reuses tmux session
→ Runs: codex --yolo -C src/auth exec "fix the authentication bugs"
→ Monitors for questions
→ Reports results when complete
```

### Example 2: Interactive Task with Questions
```
User: Use codex to analyze the performance issues
→ Creates/reuses tmux session
→ Runs: codex --yolo exec "analyze the performance issues"
→ Codex asks: "Which module should I focus on? (1) API (2) Database (3) Frontend"
→ Use AskUserQuestion to prompt user
→ Send answer back to tmux session
→ Continue monitoring until complete
```

### Example 3: Broad Codebase Task
```
User: Run codex to refactor the error handling
→ Creates/reuses tmux session
→ Runs: codex --yolo exec "refactor the error handling" (no -C flag)
→ Monitors and handles any questions
→ Reports results
```

## Error Handling

- If tmux is not installed, inform user and suggest installation
- If Codex CLI is not available, inform user to install it
- If session creation fails, report error and suggest manual debugging
- If Codex execution fails, capture error output and report to user
- If question detection is unclear, show the output to user and ask for guidance

## Notes

- The skill uses `--yolo` flag to bypass Codex's built-in confirmations where possible
- Session persistence enables continuity across multiple invocations
- The tmux session can be manually accessed at any time with `tmux attach -t codex-session`
- Question detection is pattern-based and may need adjustment based on Codex output format
