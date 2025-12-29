# UI Screenshot Reviewer Plugin

**Expert UI/UX design review of screenshots** - Acts as a picky designer analyzing every pixel for typography, colors, spacing, layout, and accessibility issues.

## Overview

This plugin provides a specialized skill that reviews existing screenshots and provides critical, actionable design feedback. Perfect for:
- Pre-deployment design audits
- Design system consistency validation
- Accessibility (WCAG) compliance checks
- Visual quality assurance
- Pixel-perfect design reviews

## Features

### Comprehensive Analysis
- ✅ **Typography** - Font consistency, hierarchy, readability, line-height, letter-spacing
- ✅ **Colors** - WCAG contrast ratios, brand consistency, interactive states
- ✅ **Spacing** - Margins, padding, alignment, whitespace balance
- ✅ **Visual Details** - Shadows, borders, border-radius, transitions, hover states
- ✅ **Layout** - Alignment, hierarchy, balance, responsive behavior
- ✅ **Accessibility** - Touch targets, contrast, readability, focus indicators

### Prioritized Feedback
- 🔴 **Critical Issues** - Blocking problems (must fix before deployment)
- ⚠️ **High Priority** - Significant UX impacts (fix soon)
- 💡 **Medium Priority** - Nice-to-have improvements

### Specific & Actionable
Every issue includes:
- What's wrong (with measurements)
- Why it's wrong (impact on users)
- How to fix it (exact values/code)
- Where to fix it (component/file when possible)

## Installation

1. Navigate to the marketplace repository
2. Install the plugin:
   ```bash
   /plugin install ui-screenshot-reviewer@automata-claude-plugins
   ```

## Usage

### Basic Usage

Simply invoke the skill and provide your screenshot directory:

```
/ui-screenshot-review

"Review screenshots in /Users/lin/Documents/project/screenshots"
```

### With Context

Provide context about your app for more tailored feedback:

```
/ui-screenshot-review

"Analyze UI screenshots in ./test_results/screenshots - it's a SaaS dashboard for data analytics"
```

### Example Commands

- "Review screenshots in `/path/to/screenshots`"
- "Perform picky design review on screenshots in `./screenshots` for e-commerce checkout"
- "Analyze docs site screenshots in `/Users/lin/Documents/docs-automata/test_results/screenshots`"

## What You Get

### Design Review Report (`design_review.md`)

The skill generates a comprehensive markdown report:

```markdown
# Design Review Report

**Screenshots Analyzed:** 24
**Critical Issues:** 3 🔴
**High Priority:** 8 ⚠️
**Medium Priority:** 5 💡

## 🔴 Critical Issues

### 1. WCAG Contrast Violation - Primary CTA
**Screenshot:** home_hero.png
**Issue:** White text on light orange
**Measurement:** #fff on #ffb380 = 1.9:1 ❌
**Required:** 4.5:1 minimum (WCAG AA)
**Fix:** Darken bg to #ff6b35 (4.6:1) ✅

### 2. Touch Target Too Small - Mobile Nav
**Screenshot:** mobile_nav.png
**Current:** 32×32px ❌
**Required:** 44×44px minimum
**Fix:** Increase to 48×48px with padding: 12px

## ⚠️ High Priority Issues

### 1. Typography Scale Inconsistency
**Found:** h1=30px, h2=22px, h3=17px
**Expected:** h1=32px, h2=24px, h3=18px
**Fix:** Update to 8px-based scale

...
```

## Review Criteria

The skill checks **28+ specific criteria** across 6 categories:

### Typography (6 checks)
- Font family consistency
- Font size hierarchy
- Font weight usage
- Line-height readability
- Letter-spacing
- Text alignment

### Colors (5 checks)
- Text contrast (WCAG)
- Brand color consistency
- Interactive state colors
- Border/divider colors
- Shadow colors

### Spacing (4 checks)
- Spacing scale adherence
- Component padding consistency
- Alignment precision
- Whitespace balance

### Visual Details (5 checks)
- Box shadow consistency
- Border styles/widths
- Border-radius consistency
- Transition timing
- Hover/focus states

### Layout (4 checks)
- Alignment issues
- Visual hierarchy
- Balance and symmetry
- Responsive behavior

### Accessibility (4 checks)
- Touch target sizes (44×44px)
- Color contrast ratios
- Text readability
- Focus indicators

## Example Issues & Fixes

### Critical Examples

```
🔴 Contrast: #666 on #999 (2.8:1) → #444 on #999 (5.2:1)
🔴 Touch target: 32×32px → 48×48px
🔴 Overlap: Sidebar 280px on 375px viewport → Collapse on mobile
```

### High Priority Examples

```
⚠️ Card padding: 16px vs 24px → Standardize to 24px
⚠️ Font sizes: 15px, 17px, 22px → Use scale: 14px, 16px, 24px
⚠️ Border-radius: 4px vs 8px → Standardize to 8px
```

## Supported Image Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- WebP (.webp)

## Tips for Best Results

1. **Organize screenshots by state**
   - home_default.png
   - home_hover_button.png
   - home_modal_open.png

2. **Include all UI states**
   - Default, hover, active, focus, disabled
   - Empty states, error states, loading states
   - Light mode and dark mode (if applicable)

3. **Capture full pages**
   - Include headers, footers, sidebars
   - Show complete UI context
   - Avoid cropped screenshots

4. **Provide context**
   - Mention app type (SaaS, e-commerce, docs, etc.)
   - Note target audience (developers, consumers, etc.)
   - Specify if brand guidelines exist

## What Makes This "Picky"?

The skill doesn't miss ANY of these:
- Random font sizes (15px, 17px when scale is 14px, 16px, 18px)
- Off-brand colors (#ff7042 when brand is #ff6b35)
- Inconsistent spacing (12px, 20px when scale is 8px, 16px, 24px)
- Missing hover states
- Poor contrast (even if it passes, warns if borderline)
- Misaligned elements (even 1px off)
- Mixed border-radius values
- Inconsistent shadows
- Small touch targets
- Missing focus indicators

## Use Cases

### Pre-Deployment Audit
```
Review all screenshots before launch
Catch accessibility issues
Ensure design system compliance
```

### Design System Validation
```
Verify typography scale adherence
Check color palette consistency
Validate spacing system usage
```

### Handoff Quality Check
```
Designer → Developer handoff
Ensure implementation matches designs
Catch inconsistencies early
```

### Continuous Quality
```
Regular screenshot reviews
Track design debt
Maintain visual consistency
```

## Requirements

- Screenshot directory must exist
- Screenshots must be in supported formats (PNG, JPEG, WebP)
- Write permissions for output directory (to save design_review.md)

## Output Location

By default, the design review report is saved to:
- Same directory as screenshots: `design_review.md`
- Or custom path if specified

## Pro Tips

1. **Run regularly** - After each major feature
2. **Fix critical first** - 🔴 issues block deployment
3. **Track improvements** - Compare reports over time
4. **Share with team** - Use reports in design reviews
5. **Automate** - Include in CI/CD for continuous quality

## Support

For issues, questions, or feature requests:
- GitHub: [automata-claude-plugins](https://github.com/automata/claude-plugins)
- Email: support@automata.com

## License

MIT License - See LICENSE file for details

---

**Make every pixel perfect!** 🎨
