# IMS v1 Annotation Examples

Comprehensive examples demonstrating how to apply Interaction Metadata Schema (IMS v1) annotations to common UI patterns.

## Example 1: Modal Dialog

```html
<!-- Trigger button -->
<button
  data-ui-action="show-delete-confirm"
  data-ui-trigger="click"
  data-ui-effect="delete-dialog.visible"
>
  Delete Item
</button>

<!-- Modal in hidden state -->
<div
  data-ui-scope="delete-dialog"
  data-ui-state="hidden"
  class="modal"
>
  <p>Are you sure?</p>

  <!-- Confirm button -->
  <button
    data-ui-action="confirm-delete"
    data-ui-trigger="click"
    data-ui-effect="delete-dialog.hidden item.deleted"
    data-ui-requires="delete-dialog.visible"
  >
    Confirm
  </button>

  <!-- Cancel button -->
  <button
    data-ui-action="cancel-delete"
    data-ui-trigger="click"
    data-ui-effect="delete-dialog.hidden"
  >
    Cancel
  </button>
</div>

<!-- Modal in visible/ready state (after showing) -->
<div
  data-ui-scope="delete-dialog"
  data-ui-state="ready"
  data-ui-ready="true"
  data-ui-snapshot="delete-confirmation-shown"
  class="modal visible"
>
  <!-- Same content -->
</div>
```

**Key Points:**
- Modal has two states: `hidden` and `ready` (when visible)
- Confirm button has `data-ui-requires` to indicate precondition
- Multiple effects can be listed: `"delete-dialog.hidden item.deleted"`
- Ready state requires `data-ui-snapshot` attribute

---

## Example 2: Loading State

```html
<!-- Search button -->
<button
  data-ui-action="search-products"
  data-ui-trigger="click"
  data-ui-effect="search-results.loading"
>
  Search
</button>

<!-- Results container - loading -->
<div
  data-ui-scope="search-results"
  data-ui-state="loading"
>
  <span class="spinner">Loading...</span>
</div>

<!-- Results container - ready -->
<div
  data-ui-scope="search-results"
  data-ui-state="ready"
  data-ui-ready="true"
  data-ui-snapshot="search-results-displayed"
>
  <div class="result">Product 1</div>
  <div class="result">Product 2</div>
</div>
```

**Key Points:**
- Loading state uses `status="loading"` (implied by `data-ui-state="loading"`)
- Transition from `loading` → `ready` state
- Only `ready` state has `data-ui-ready="true"` and snapshot
- Loading state does NOT require snapshot (not ready yet)

---

## Example 3: Dropdown Menu

```html
<!-- Dropdown trigger -->
<button
  data-ui-action="toggle-menu"
  data-ui-trigger="click"
  data-ui-effect="nav-menu.visible"
>
  Menu ▼
</button>

<!-- Dropdown menu -->
<ul
  data-ui-scope="nav-menu"
  data-ui-state="ready"
  data-ui-ready="true"
  data-ui-snapshot="nav-menu-expanded"
  class="dropdown"
>
  <li>
    <a
      data-ui-action="navigate-home"
      data-ui-trigger="click"
      data-ui-effect="page.home nav-menu.hidden"
    >
      Home
    </a>
  </li>
  <li>
    <a
      data-ui-action="navigate-about"
      data-ui-trigger="click"
      data-ui-effect="page.about nav-menu.hidden"
    >
      About
    </a>
  </li>
</ul>
```

**Key Points:**
- Navigation items trigger multiple effects (page change + menu close)
- Menu visible state is immediately ready (no loading)
- Each navigation link has unique action ID
- Snapshot captures expanded menu state

---

## Common Patterns

### Pattern: Toggle Visibility

```
Action: toggle-X
Trigger: click
Effects: X.visible OR X.hidden
States: X with status hidden/ready
```

**Example:**
```html
<button
  data-ui-action="toggle-sidebar"
  data-ui-trigger="click"
  data-ui-effect="sidebar.visible"
>
  Toggle Sidebar
</button>

<aside
  data-ui-scope="sidebar"
  data-ui-state="ready"
  data-ui-ready="true"
  data-ui-snapshot="sidebar-expanded"
>
  Sidebar content
</aside>
```

---

### Pattern: Form Submission

```
Action: submit-form
Trigger: click
Effects: form.loading → form.success OR form.error
States: form with status loading/ready/error
```

**Example:**
```html
<form>
  <input type="email" name="email" />

  <button
    data-ui-action="submit-newsletter"
    data-ui-trigger="click"
    data-ui-effect="newsletter-form.loading"
  >
    Subscribe
  </button>
</form>

<!-- Loading state -->
<div
  data-ui-scope="newsletter-form"
  data-ui-state="loading"
>
  <span class="spinner">Submitting...</span>
</div>

<!-- Success state -->
<div
  data-ui-scope="newsletter-form"
  data-ui-state="success"
  data-ui-ready="true"
  data-ui-snapshot="newsletter-success"
>
  <p>Thanks for subscribing!</p>
</div>

<!-- Error state -->
<div
  data-ui-scope="newsletter-form"
  data-ui-state="error"
  data-ui-ready="true"
  data-ui-snapshot="newsletter-error"
>
  <p>Something went wrong. Please try again.</p>
</div>
```

---

### Pattern: Navigation

```
Action: navigate-to-X
Trigger: click
Effects: page.X current-page.hidden
States: page with status ready, snapshot required
```

**Example:**
```html
<nav>
  <a
    href="/dashboard"
    data-ui-action="navigate-dashboard"
    data-ui-trigger="click"
    data-ui-effect="page.dashboard current-page.hidden"
  >
    Dashboard
  </a>

  <a
    href="/settings"
    data-ui-action="navigate-settings"
    data-ui-trigger="click"
    data-ui-effect="page.settings current-page.hidden"
  >
    Settings
  </a>
</nav>

<!-- Dashboard page -->
<main
  data-ui-scope="page"
  data-ui-state="dashboard"
  data-ui-ready="true"
  data-ui-snapshot="dashboard-page-loaded"
>
  Dashboard content
</main>
```

---

### Pattern: Hover Preview

```
Action: preview-X
Trigger: hover
Effects: tooltip.visible
States: tooltip with status ready
```

**Example:**
```html
<button
  data-ui-action="show-help-tooltip"
  data-ui-trigger="hover"
  data-ui-effect="help-tooltip.visible"
>
  Help
</button>

<div
  data-ui-scope="help-tooltip"
  data-ui-state="ready"
  data-ui-ready="true"
  data-ui-snapshot="help-tooltip-shown"
  class="tooltip"
>
  Click here for assistance
</div>
```

---

## JSON Schema Validation

The full JSON Schema for validation:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Interaction Metadata Schema v1",
  "type": "object",
  "required": ["version", "interactions"],
  "properties": {
    "version": {
      "type": "string",
      "enum": ["1.0"]
    },
    "interactions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "trigger", "effects"],
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[a-z][a-z0-9\\-]*$"
          },
          "scope": {
            "type": "string"
          },
          "trigger": {
            "type": "string",
            "enum": ["click", "hover", "scroll", "focus", "wait", "auto", "keyboard"]
          },
          "effects": {
            "type": "array",
            "minItems": 1,
            "items": {
              "type": "string",
              "pattern": "^[a-z][a-z0-9\\-]*\\.[a-z][a-z0-9\\-]*$"
            }
          },
          "requires": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      }
    },
    "states": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["scope", "name", "status"],
        "properties": {
          "scope": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "enum": ["hidden", "loading", "animating", "ready", "error", "disabled"]
          },
          "ready": {
            "type": "boolean"
          },
          "snapshot": {
            "type": "string"
          }
        },
        "allOf": [
          {
            "if": { "properties": { "ready": { "const": true } } },
            "then": { "required": ["snapshot"] }
          }
        ]
      }
    }
  }
}
```

---

## Complete JSON Manifest Example

```json
{
  "version": "1.0",
  "interactions": [
    {
      "id": "show-delete-confirm",
      "scope": "delete-dialog",
      "trigger": "click",
      "effects": ["delete-dialog.visible"]
    },
    {
      "id": "confirm-delete",
      "scope": "delete-dialog",
      "trigger": "click",
      "effects": ["delete-dialog.hidden", "item.deleted"],
      "requires": ["delete-dialog.visible"]
    },
    {
      "id": "cancel-delete",
      "scope": "delete-dialog",
      "trigger": "click",
      "effects": ["delete-dialog.hidden"]
    },
    {
      "id": "search-products",
      "scope": "search-results",
      "trigger": "click",
      "effects": ["search-results.loading"]
    },
    {
      "id": "toggle-menu",
      "scope": "nav-menu",
      "trigger": "click",
      "effects": ["nav-menu.visible"]
    },
    {
      "id": "navigate-home",
      "trigger": "click",
      "effects": ["page.home", "nav-menu.hidden"]
    },
    {
      "id": "navigate-about",
      "trigger": "click",
      "effects": ["page.about", "nav-menu.hidden"]
    }
  ],
  "states": [
    {
      "scope": "delete-dialog",
      "name": "hidden",
      "status": "hidden"
    },
    {
      "scope": "delete-dialog",
      "name": "visible",
      "status": "ready",
      "ready": true,
      "snapshot": "delete-confirmation-shown"
    },
    {
      "scope": "item",
      "name": "deleted",
      "status": "ready",
      "ready": true,
      "snapshot": "item-removed"
    },
    {
      "scope": "search-results",
      "name": "loading",
      "status": "loading"
    },
    {
      "scope": "search-results",
      "name": "ready",
      "status": "ready",
      "ready": true,
      "snapshot": "search-results-displayed"
    },
    {
      "scope": "nav-menu",
      "name": "visible",
      "status": "ready",
      "ready": true,
      "snapshot": "nav-menu-expanded"
    },
    {
      "scope": "nav-menu",
      "name": "hidden",
      "status": "hidden"
    },
    {
      "scope": "page",
      "name": "home",
      "status": "ready",
      "ready": true,
      "snapshot": "home-page-loaded"
    },
    {
      "scope": "page",
      "name": "about",
      "status": "ready",
      "ready": true,
      "snapshot": "about-page-loaded"
    }
  ]
}
```

---

## Advanced Example: Multi-Step Form

```html
<!-- Step 1: Personal Info -->
<form
  data-ui-scope="signup-form"
  data-ui-state="step-1"
  data-ui-ready="true"
  data-ui-snapshot="signup-step-1"
>
  <input
    type="text"
    name="name"
    data-ui-action="fill-name"
    data-ui-trigger="keyboard"
    data-ui-effect="signup-form.name-filled"
  />

  <button
    data-ui-action="goto-step-2"
    data-ui-trigger="click"
    data-ui-effect="signup-form.step-2"
    data-ui-requires="signup-form.name-filled"
  >
    Next
  </button>
</form>

<!-- Step 2: Email -->
<form
  data-ui-scope="signup-form"
  data-ui-state="step-2"
  data-ui-ready="true"
  data-ui-snapshot="signup-step-2"
>
  <input
    type="email"
    name="email"
    data-ui-action="fill-email"
    data-ui-trigger="keyboard"
    data-ui-effect="signup-form.email-filled"
  />

  <button
    data-ui-action="submit-signup"
    data-ui-trigger="click"
    data-ui-effect="signup-form.submitting"
    data-ui-requires="signup-form.email-filled"
  >
    Submit
  </button>
</form>

<!-- Submitting state -->
<div
  data-ui-scope="signup-form"
  data-ui-state="submitting"
>
  <span class="spinner">Creating account...</span>
</div>

<!-- Success state -->
<div
  data-ui-scope="signup-form"
  data-ui-state="success"
  data-ui-ready="true"
  data-ui-snapshot="signup-complete"
>
  <p>Account created successfully!</p>
</div>
```

**Key Points:**
- Multi-step flow with state transitions: `step-1` → `step-2` → `submitting` → `success`
- Each step is `ready` and has a snapshot
- `data-ui-requires` ensures preconditions are met
- Form inputs use `keyboard` trigger
- Submitting state uses `loading` status (no snapshot)

---

## Best Practices

### 1. Semantic Naming
✅ **Good:**
```html
<button data-ui-action="add-to-cart">Add to Cart</button>
```

❌ **Bad:**
```html
<button data-ui-action="btn-click-1">Add to Cart</button>
```

### 2. Effect-State Correspondence
✅ **Good:**
```html
<!-- Action declares effect -->
<button data-ui-effect="cart.item-added">Add</button>

<!-- State exists for the effect -->
<div data-ui-scope="cart" data-ui-state="item-added"></div>
```

❌ **Bad:**
```html
<!-- Effect declared but no corresponding state -->
<button data-ui-effect="cart.item-added">Add</button>
<!-- No element with cart scope and item-added state! -->
```

### 3. Ready State Requirements
✅ **Good:**
```html
<div
  data-ui-state="ready"
  data-ui-ready="true"
  data-ui-snapshot="modal-shown"
>
```

❌ **Bad:**
```html
<!-- Missing snapshot! -->
<div
  data-ui-state="ready"
  data-ui-ready="true"
>
```

### 4. Trigger Vocabulary
✅ **Good:**
```html
<button data-ui-trigger="click">Submit</button>
<input data-ui-trigger="keyboard">
<div data-ui-trigger="hover">Info</div>
```

❌ **Bad:**
```html
<!-- Invalid triggers! -->
<button data-ui-trigger="press">Submit</button>
<input data-ui-trigger="type">
<div data-ui-trigger="mouseover">Info</div>
```

---

## Validation Checklist

Use this checklist when reviewing IMS v1 annotations:

- [ ] All `data-ui-action` IDs are unique and kebab-case
- [ ] All `data-ui-trigger` values are from the closed set (click, hover, scroll, focus, wait, auto, keyboard)
- [ ] All `data-ui-effect` values follow `scope.state` format
- [ ] Every effect has a corresponding state definition
- [ ] All `data-ui-status` values are from the closed set (hidden, loading, animating, ready, error, disabled)
- [ ] All elements with `data-ui-ready="true"` have `data-ui-snapshot` attribute
- [ ] All `data-ui-requires` values reference existing states
- [ ] Semantic naming used for action IDs (intent-based, not implementation-based)
- [ ] Scopes are reused appropriately for related states
- [ ] No orphaned effects (effects without corresponding states)

---

For more information, see [SKILL.md](SKILL.md).
