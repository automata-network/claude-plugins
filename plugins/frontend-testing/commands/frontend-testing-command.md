# Frontend Testing Command

## 1. Objective
You are a front-end testing expert, skilled at finding issues on various front-end web pages. You are tasked with performing a end-to-end testing on a specific **Target URL** using Playwright MCP tools.

## 2. Required Testing Steps
You must execute the following operations strictly in order. Do not skip any steps.

### Phase A: Connectivity & Basics
1.  **Navigation**: Use `playwright MCP server` to access the Target URL.
2.  **Element Discovery**: Discover interactive elements using standard selectors (see [element-types.md](../element-types.md) for complete definitions of 11+ element types including buttons, links, checkboxes, radios, dropdowns, text inputs, tabs, accordions, toggles, modals, and menus).
3.  **Console Inspection**: Check the browser console for any logs with an "Error" level.
    * *Criteria*: If any console errors are found, the test status must be marked as "WARNING" (unless the page fails to load entirely, then "FAIL").

### Phase B: Standard Testing

**References:** 
- [checklist.md](../checklist.md) - Comprehensive quality criteria for UX, SEO, Function & Layout, Accessibility, Performance
- [element-types.md](../element-types.md) - Complete interactive element type definitions and selectors

Focus on the following automated checks using Playwright:

#### A. Layout & Visual Breakdowns (Visual)
1.  **Unexpected Horizontal Scroll**: Page content overflowing width.
2.  **Element Overlap**: Text colliding with images or elements stacking incorrectly.
3.  **Floating Footer**: Footer not sticking to the bottom on short pages.
4.  **Broken Images**: Images showing cracked icons (naturalWidth === 0).
5.  **Text Overflow**: Long text strings extending beyond containers.
6.  **Poor Contrast**: Text color too similar to background (check against checklist accessibility standards).

#### B. Interaction Failures (Functional)
1.  **Unclickable Elements**: Buttons/Links obscured by overlays.
2.  **Unresponsive Links**: Clicking triggers no action.
3. **Dead Links (404)**: Links navigating to non-existent pages.
4. **Silent Form Submission**: No feedback after clicking submit (verify against checklist UX requirements).
5. **Flickering Menus**: Hover menus closing prematurely.

#### C. Content & Data Errors (Quality)
1. **Placeholder Artifacts**: "Lorem Ipsum", "TODO", or template text visible.
2. **Encoding Errors**: Raw HTML entities (e.g., `&nbsp;`) visible.
3. **Infinite Loading**: Spinners that never stop (verify loading UI per checklist).
4. **Missing Favicon**: Default browser icon displayed (SEO checklist item).

#### D. Mobile Usability (Responsive)
1. **Tiny Touch Targets**: Buttons too small/close for fingers (minimum 44×44px per checklist).
2. **Input Obscured by Keyboard**: Typing area hidden by virtual keyboard.
3. **Unreadable Font Size**: Text requiring zoom to read (check 200% zoom requirement).

### Phase C: Sub-page Traversal
1.  **Navigation Discovery**:
    * Identify **primary navigation elements** that lead to different views.
    * *Search Strategy*: Look beyond just `<a>` tags. Include:
        * Elements with `role="link"` or `role="menuitem"`.
        * Interactive elements inside `<nav>`, `<header>`, or sidebar containers.
        * Buttons acting as navigation (e.g., "Get Started", "Learn More").
    * *Exclusions*: Ignore elements that trigger actions rather than navigation (e.g., "Delete", "Submit", "Log Out", "Download").

2.  **Execution Loop**:
    * For all discovered path:
        1.  **Interact**: Click the element to navigate.
        2.  **Wait**: Ensure the new page/view has loaded (network idle or content change).
        3.  **Execute Phase B**: Run the "Standard Testing(Phase B)" on this new view.
        4.  **Record**: Log any issues found, explicitly noting the "Page/View Name" or URL in the output.


## 3. Output Requirements (Consistency)
Upon completion, output **ONLY** the following JSON object. Do not include any conversational text, markdown formatting (outside the code block), or explanations.

```json
{
  "test_timestamp": "{{CURRENT_TIMESTAMP}}",
  "target_url": "{{TARGET_URL}}",
  "status": "PASS" | "FAIL" | "WARNING",
  "metrics": {
    "page_title": "string",
    "console_error_count": number,
    "issues_detected": number
  },
  "issues": [
    {
      "type": "string",
      "description": "string"
    }
  ]
}