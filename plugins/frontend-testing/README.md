# Overview
Claude plugin to detect pre-defined issues of a frontend site.

# Installation
Follow the readme under root folder of the repo to install marketplace, then install the plugin using the following command:
```bash
/plugin install frontend-testing@automata-claude-plugins
```

# Usage

## Automated Testing
Use the slash command below to test the website with Playwright:
```bash
/frontend-testing:frontend-testing-command <domain>
```

## Pre-Deployment Checklist
The `frontend-deployment-checklist` skill is automatically available when working on frontend code. It provides guidance for verifying:
- Analytics & tracking setup
- Code quality standards
- UX (loading states, error handling)
- SEO (meta tags, Open Graph, favicon)
- Function & layout (forms, dark mode, responsive design)

Invoke it by asking Claude to "check deployment readiness" or "run pre-deployment verification".

# Permissions
You can add the following section to your ".claude/settings.json" file to provide permission to playwright, so that you don't need to approve all actions everytime when claude code want to execute a new type of operation using playwright.
```bash
  "permissions": {
    "allow": [
      "mcp__playwright__browser_navigate",
      "mcp__playwright__browser_evaluate",
      "mcp__playwright__browser_click",
      "mcp__playwright__browser_navigate_back",
      "mcp__playwright__browser_take_screenshot",
      "mcp__playwright__browser_close",
      "mcp__playwright__browser_console_messages",
      "mcp__playwright__browser_resize",
      "mcp__playwright__browser_hover",
      "mcp__playwright__browser_snapshot"
    ]
  }
```

# Contributing
Follow the format of `Phase B` of the command markdown file to add new issues into the checklist, and test it in your local.
Update the `permissions` above if this issue require other permissions.