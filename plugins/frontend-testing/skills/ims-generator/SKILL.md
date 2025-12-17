---
name: ims-generator
description: Generates Interaction Metadata Schema (IMS v1) annotations for interactive web applications, ensuring every UI interaction has proper metadata for testing and agent execution
allowed-tools: Read, Write, Glob, Grep, Edit
---

# Interaction Metadata Schema (IMS v1) Generator

Generate standardized interaction metadata for web applications following the IMS v1 specification. This skill treats UIs as Directed Interaction Graphs where every action, effect, state, and readiness condition is explicitly annotated.

## Purpose

This skill enables you to generate standardized interaction metadata for web applications following the IMS v1 specification. The schema treats UIs as Directed Interaction Graphs where every action, effect, state, and readiness condition is explicitly annotated.

## Core Concept

An interactive UI follows this flow:

```
Action ──(trigger)──▶ Effect ──▶ State ──▶ Ready ──▶ Screenshot
```

Every interactive element must have:
- An **action** with a unique ID
- A **trigger** (from closed set)
- At least one **effect** (state transition)
- A **state** with status
- A **readiness condition** for screenshots

## Closed Vocabulary

### Triggers (ONLY these are allowed)

1. `click` - User clicks/taps
2. `hover` - Mouse hover
3. `scroll` - Scroll event
4. `focus` - Element receives focus
5. `wait` - Time-based trigger
6. `auto` - Automatic trigger
7. `keyboard` - Keyboard input

### Status Values (ONLY these are allowed)

1. `hidden` - Not visible
2. `loading` - Data/content loading
3. `animating` - In transition
4. `ready` - Stable and complete
5. `error` - Error state
6. `disabled` - Interaction disabled

## Generation Rules

### Critical Rules (MUST FOLLOW)

❌ **Never invent triggers** - only use the 7 allowed triggers
❌ **Never add ready=true without snapshot** - ready state requires screenshot ID
❌ **Never add effects without observable state** - every effect must have a corresponding state
❌ **Never use timing if state exists** - prefer state-based over wait-based
✅ **Prefer existing scopes** - reuse scope names for related interactions
✅ **Use semantic intent-based naming** - IDs should describe what, not how

### Required Fields

| Field | Requirement | Format |
|-------|-------------|--------|
| `action.id` | Required | kebab-case, starts with letter |
| `action.trigger` | Required | From closed set only |
| `action.effects` | Required | Minimum 1 item, format `scope.state` |
| `state.scope` | Required | Group related states |
| `state.name` | Required | State identifier |
| `state.status` | Required | From closed set only |

### Conditional Requirements

| Condition | Requirement |
|-----------|-------------|
| If `ready === true` | Then `snapshot` is REQUIRED |
| If user can interact with element | Then `action` metadata is REQUIRED |
| If effect is declared | Corresponding `state` MUST exist |

## Output Formats

### Format 1: DOM Annotations

```html
<button
  data-ui-action="open-settings"
  data-ui-trigger="click"
  data-ui-effect="settings.visible"
>
  Settings
</button>

<div
  data-ui-scope="settings"
  data-ui-state="ready"
  data-ui-ready="true"
  data-ui-snapshot="settings-modal-open"
  class="modal"
>
  <!-- Modal content -->
</div>
```

### Format 2: JSON Manifest

```json
{
  "version": "1.0",
  "interactions": [
    {
      "id": "open-settings",
      "scope": "settings",
      "trigger": "click",
      "effects": ["settings.visible"]
    }
  ],
  "states": [
    {
      "scope": "settings",
      "name": "visible",
      "status": "ready",
      "ready": true,
      "snapshot": "settings-modal-open"
    }
  ]
}
```

## Annotation Algorithm

When annotating a UI component, follow these steps:

### 1. Identify Interactive Elements
- Buttons, links, form inputs, toggles, etc.
- Each needs action metadata

### 2. For Each Interactive Element:
a. Assign unique `action.id` (kebab-case)
b. Determine `trigger` type (from closed set)
c. Identify what changes (effects)
d. Define effect as `scope.state` format

### 3. For Each Effect:
a. Create corresponding state definition
b. Assign `scope` (group related states)
c. Determine `status` (from closed set)
d. If visually stable, mark `ready=true` + `snapshot`

### 4. Validate:
- ✅ All actions have effects
- ✅ All effects have states
- ✅ All ready states have snapshots
- ✅ All triggers are from closed set
- ✅ All status values are from closed set

## Common Patterns

> **📖 For detailed examples and complete patterns, see [EXAMPLES.md](EXAMPLES.md)**

### Modal Dialog Pattern

```html
<!-- Trigger -->
<button
  data-ui-action="open-modal"
  data-ui-trigger="click"
  data-ui-effect="modal.visible"
>
  Open Dialog
</button>

<!-- Modal -->
<div
  data-ui-scope="modal"
  data-ui-state="visible"
  data-ui-status="ready"
  data-ui-ready="true"
  data-ui-snapshot="modal-open"
  class="modal"
>
  <button
    data-ui-action="close-modal"
    data-ui-trigger="click"
    data-ui-effect="modal.hidden"
  >
    Close
  </button>
</div>
```

### Form Submission Pattern

```html
<form>
  <input
    type="text"
    data-ui-action="fill-username"
    data-ui-trigger="keyboard"
    data-ui-effect="form.username-filled"
  />

  <button
    data-ui-action="submit-form"
    data-ui-trigger="click"
    data-ui-effect="form.submitting,form.submitted"
  >
    Submit
  </button>
</form>

<!-- Loading state -->
<div
  data-ui-scope="form"
  data-ui-state="submitting"
  data-ui-status="loading"
>
  Submitting...
</div>

<!-- Success state -->
<div
  data-ui-scope="form"
  data-ui-state="submitted"
  data-ui-status="ready"
  data-ui-ready="true"
  data-ui-snapshot="form-success"
>
  Success!
</div>
```

### Accordion/Dropdown Pattern

```html
<div class="accordion">
  <button
    data-ui-action="toggle-section-1"
    data-ui-trigger="click"
    data-ui-effect="section-1.expanded"
  >
    Section 1
  </button>

  <div
    data-ui-scope="section-1"
    data-ui-state="expanded"
    data-ui-status="ready"
    data-ui-ready="true"
    data-ui-snapshot="section-1-open"
    class="accordion-content"
  >
    Content here
  </div>
</div>
```

### Navigation Pattern

```html
<nav>
  <a
    href="/dashboard"
    data-ui-action="navigate-dashboard"
    data-ui-trigger="click"
    data-ui-effect="page.dashboard-loaded"
  >
    Dashboard
  </a>
</nav>

<div
  data-ui-scope="page"
  data-ui-state="dashboard-loaded"
  data-ui-status="ready"
  data-ui-ready="true"
  data-ui-snapshot="dashboard-page"
>
  <!-- Dashboard content -->
</div>
```

### Hover Effects Pattern

```html
<div
  data-ui-action="show-tooltip"
  data-ui-trigger="hover"
  data-ui-effect="tooltip.visible"
>
  Hover me
</div>

<div
  data-ui-scope="tooltip"
  data-ui-state="visible"
  data-ui-status="ready"
  data-ui-ready="true"
  data-ui-snapshot="tooltip-shown"
  class="tooltip"
>
  Tooltip content
</div>
```

## Usage Examples

> **📖 For comprehensive examples with validation schemas and multi-step forms, see [EXAMPLES.md](EXAMPLES.md)**

### Quick Start

Tell me to annotate your UI with IMS v1 metadata:

- "Add IMS annotations to my React components"
- "Generate interaction metadata for my web app"
- "Annotate all buttons and modals with IMS v1 schema"
- "Create a JSON manifest of all UI interactions"

### Advanced Usage

**Annotate Entire Component Directory:**
```
Scan ./src/components and add IMS v1 annotations to all interactive elements
```

**Generate JSON Manifest:**
```
Analyze my UI and create an IMS v1 JSON manifest of all interactions
```

**Validate Existing Annotations:**
```
Check my IMS annotations for compliance with v1 specification
```

**Convert Between Formats:**
```
Convert my DOM annotations to JSON manifest format
```

## Instructions

When you ask me to generate IMS annotations, I will:

1. **Analyze UI Components**
   - Scan specified directories for interactive elements
   - Identify buttons, links, forms, modals, and other interactive components
   - Map out the interaction flow

2. **Generate Metadata**
   - Create unique action IDs using semantic naming
   - Assign appropriate triggers from the closed set
   - Define effects in `scope.state` format
   - Create corresponding state definitions
   - Add readiness conditions and snapshot IDs

3. **Apply Annotations**
   - Add `data-ui-*` attributes to DOM elements (if HTML/JSX/TSX)
   - Generate JSON manifest (if requested)
   - Validate against IMS v1 specification

4. **Validation Report**
   - Check all required fields are present
   - Verify triggers and status values are from closed sets
   - Ensure effects have corresponding states
   - Confirm ready states have snapshot IDs
   - Report any violations

## Validation Checklist

| Check | Description |
|-------|-------------|
| ✅ All interactive elements have `action.id` | Every clickable/interactive element annotated |
| ✅ All triggers are from closed set | Only the 7 allowed triggers used |
| ✅ All effects follow `scope.state` format | Proper dot notation |
| ✅ All effects have corresponding states | No orphaned effects |
| ✅ All status values are from closed set | Only the 6 allowed statuses used |
| ✅ All `ready=true` states have snapshots | Screenshot IDs present |
| ✅ Semantic naming used | IDs describe intent, not implementation |
| ✅ Scopes are reused appropriately | Related states grouped together |

## Benefits

### For Testing
- Automated test generation from metadata
- Complete UI coverage validation
- State-based screenshot capture
- Interaction flow documentation

### For Agents
- Explicit action discovery
- State transition understanding
- Screenshot timing optimization
- Error state identification

### For Developers
- Self-documenting UI interactions
- Standardized annotation format
- Easy debugging of interaction flows
- Clear separation of actions, effects, and states

## Specification Compliance

This skill generates annotations strictly compliant with **IMS v1 specification**:

- ✅ Closed vocabulary enforcement (triggers, status)
- ✅ Required field validation
- ✅ Conditional requirement checks
- ✅ Effect-state correspondence
- ✅ Ready-snapshot pairing
- ✅ Semantic naming conventions

## What I'll Generate

### Annotated Components
- HTML/JSX/TSX files with `data-ui-*` attributes
- Vue/Svelte components with metadata
- Clean, spec-compliant annotations

### JSON Manifests
- Complete interaction catalog
- State definitions
- Screenshot markers
- Validation-ready format

### Validation Reports
- Specification compliance check
- Missing annotations report
- Invalid trigger/status detection
- Orphaned effects identification

## Requirements

No special dependencies required. This skill works with:
- HTML files
- React/JSX/TSX components
- Vue single-file components
- Svelte components
- Any web UI framework

## Quick Reference

### Annotation Syntax

```html
<!-- Action annotation -->
<element
  data-ui-action="unique-id"
  data-ui-trigger="click|hover|scroll|focus|wait|auto|keyboard"
  data-ui-effect="scope.state,scope.state2"
>

<!-- State annotation -->
<element
  data-ui-scope="scope-name"
  data-ui-state="state-name"
  data-ui-status="hidden|loading|animating|ready|error|disabled"
  data-ui-ready="true"
  data-ui-snapshot="screenshot-id"
>
```

### JSON Schema

```json
{
  "version": "1.0",
  "interactions": [
    {
      "id": "action-id",
      "scope": "scope-name",
      "trigger": "click",
      "effects": ["scope.state"]
    }
  ],
  "states": [
    {
      "scope": "scope-name",
      "name": "state-name",
      "status": "ready",
      "ready": true,
      "snapshot": "screenshot-id"
    }
  ]
}
```

---

## Additional Resources

- **[EXAMPLES.md](EXAMPLES.md)** - Comprehensive examples including:
  - Modal dialogs with multiple buttons
  - Loading states and async operations
  - Dropdown menus with navigation
  - Common patterns (toggle, form submission, navigation, hover)
  - JSON Schema validation
  - Complete JSON manifest examples
  - Multi-step form workflows
  - Best practices and validation checklists

---

## Validation Checklist

Before finalizing annotations:

- ☑ All interactive elements have `data-ui-action`
- ☑ All actions use only allowed triggers
- ☑ All actions have at least one effect
- ☑ All effects follow `scope.state` pattern
- ☑ All effects have corresponding state definitions
- ☑ All states have valid status values
- ☑ All `ready=true` states have snapshots
- ☑ Action IDs are unique and kebab-case
- ☑ Scope names are consistent and semantic
- ☑ No invented triggers or status values

---

## Benefits

This metadata enables:

**Automated Testing**: Generate Playwright/Cypress tests from annotations

**Visual Regression**: Screenshot capture at stable states

**Agent Execution**: AI can understand and interact with UI programmatically

**Documentation**: Self-documenting interaction flows

**Debugging**: Clear state transitions for troubleshooting

---

## When to Use This Skill

Use this skill when:

- Creating new interactive web applications
- Adding test automation metadata to existing UIs
- Building AI-navigable interfaces
- Documenting complex interaction flows
- Setting up visual regression testing
- Enabling agent-based UI testing

---

## Notes

- This is a constrained language - AI cannot invent new values
- Focus on observable states, not implementation details
- Prefer semantic naming over technical jargon
- Keep scopes consistent across related interactions
- Always validate against the JSON schema before finalizing

---

**Ready to annotate your UI with IMS v1 metadata!** Just tell me which components to process or provide a directory path to scan.
