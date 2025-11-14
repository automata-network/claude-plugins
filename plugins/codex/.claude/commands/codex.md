# Codex Command

Delegates to a Task agent to run OpenAI Codex CLI for complex tasks when there are issues that need additional analysis or fixes.

## Usage
- `/codex [prompt]` - Run Codex to analyze or fix issues (Codex decides based on prompt)

## Instructions

When the user invokes this command, you (Claude) should:

1. Launch a Task agent to handle the entire codex execution:
   - Use the Task tool with an appropriate agent type (e.g., general-purpose)
   - Pass the full user prompt/arguments to the agent
   - The agent should:
     - Parse the command arguments to determine if it's a resume or new execution
     - Construct the appropriate bash command:
       - For resume commands: `echo "[prompt]" | codex exec resume --last` or `codex exec resume --last`
       - For new execution: `codex --yolo [-C <DIR>] exec "[prompt]"`
         - Analyze the prompt to determine appropriate working directory scope with `-C <DIR>` if needed
         - If prompt mentions specific directories/paths, use `-C <DIR>` to limit scope
         - If prompt is broad/general, omit `-C` to use entire codebase
     - Execute the bash command
     - Capture the session ID from the output (shown at beginning)
     - Return the complete results
   - Wait for the Task agent to complete before proceeding

2. Report results to the user:
   - After the Task agent completes, report the results
   - Show the output and any changes made by Codex
   - Include a helpful note with the session ID so the user can manually resume if needed:
     - Format: "To resume this session manually, run: `codex resume <SESSION_ID>`"
     - This allows the user to continue the conversation interactively in their terminal

## Example invocations
- `/codex investigate the authentication bug in the login flow`
- `/codex fix the type errors in src/utils/helper.ts`
- `/codex where are we in the project?`
