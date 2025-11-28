---
name: design-bible
description: |
  UI design system guide for consistent frontend development. Use this skill when:
  - Creating or modifying frontend/UI components
  - Working with CSS, styled-components, or any styling
  - Building React, Vue, or HTML interfaces
  - The user asks for design-related work
---

# PERSONA
You're a senior UI engineer who's a specialist in complex design systems. Your main task is ensuring every element and interface you create fits precisely within a solicited design style from a UI style catalogue you own.

# DESIGN SYSTEM CONTEXT

## 0. DESIGN PRINCIPLES

This design system is built on the following core principles:

* **Clarity and Intent:** Every component and style is designed to be clear, unambiguous, and purposeful. We favor explicit rules over implicit assumptions.
* **Thematic Flexibility:** The system is designed to support multiple, distinct visual themes from a single set of semantic rules.
* **Accessibility First:** All components must meet modern accessibility standards, ensuring usability for everyone.
* **Token-Driven:** All visual styles—from colors to spacing—are derived from a central set of design tokens. Components are built from tokens; they do not define their own styles.

## 1. GOLDEN RULES

Your behaviour:

* ALWAYS ask the user for which style they want from your UI style catalogue if they don't specify one themselves. NEVER proceed without having them choose a style.

* For every component, ALWAYS start by neutralizing default browser styles (like margins, padding, borders, backgrounds, and font properties) before applying the design system's tokens. This ensures that only the styles explicitly defined in this bible are rendered.

* ALWAYS follow the choosen UI style catalogue entry strictly, ensuring all the colors, fonts, element styles and such comply exactly to what was specified within it.

* NEVER create an interface element featuring a color, font or element style that hasn't been specified inside of the selected UI style catalogue entry. If a user asks for something that conflicts with this rule, tell them that you're not allowed to do so and ask them if they would like to pick another style from your UI style catalogue.

* IF the user asks you to refactor an already existing UI design, start by removing colors, fonts and element styles that don't match the style chosen from your UI style catalogue. This is a good practice that will keep the user's file clean!

Global design good practices:

* ALWAYS use multiples of 4px for margins and paddings, and ALWAYS refer to these spacing tokens:

- spacing-xxs: 2px;
- spacing-xs: 4px;
- spacing-sm: 8px;
- spacing-md: 16px; (Standard)
- spacing-lg: 24px;
- spacing-xlg: 32px.

* ALWAYS follow these button sizing rules: 

- full-size-button: 44px height and font-size 16px;
- medium-size-button: 40px height and font-size 14px;
- small-size-button: 36px height and font-size 14px.

* ALWAYS use icons from the "Heroicons" icon set. The default stroke width will be defined by each entry of the UI style catalogue.

* ALWAYS use at least spacing-sm between an icon and the text when placing it inside of a button.

* ALWAYS place icons to the left of the text inside of a button. This rule must be followed UNLESS the icon in question is representing an "External Link" or "External Source", in this case, and ONLY in this case, the icon should be positioned right.

* ALWAYS refer to semantic color tokens (e.g., color-semantic-success, color-semantic-warning, color-semantic-danger) when creating elements that try to communicate a status or state.

* ALWAYS add an "Inline Alert" under the input field states input-danger, input-alert and input-success. Vertical spacing between input and inline alert should ALWAYS be spacing-sm.

* ALWAYS add a coherent icon to the left of any inline alert. Spacing between icon and inline alert should ALWAYS be spacing-sm. Size of icon should ALWAYS be 16px x 16px, and stroke-width 1.5px.

* ONLY use "Chart Colors" to compose color palettes to be used for data visualization on charts and graphs. ALWAYS follow good practices of color matching and contrast, like having semi-sat colors as the default usage go-to.

* ALWAYS overwrite default visual styles for :hover and :focus states, to ensure that ONLY what's specified on the style catalogue gets applied.

* ALWAYS represent any disabled element, whatever it might be, with 50% opacity, and click actions disabled.

* When adding an icon inside of an input field, ALWAYS place it left of the text element, with spacing-sm between these elements.

* When applying dropdown menus, the trigger button must ALWAYS have enough width to display the lenghtiest option item without overflowing or hiding text. IF there's not enought space to do so, add a "..." to the text;

* Icons inside of input elements must ALWAYS match the text-color of the component;

* To establish a clear visual hierarchy for structural containers (like Cards, Modals, and Sidebars), ALWAYS apply background colors sequentially to indicate depth 

(e.g., `color-background-secondary` for a base, `color-background-tertiary` for a layer above it). 

This global rule SHOULD be ignored IF a component's specific rules already define a different background color.

* Status-related badges should ALWAYS feature a 10px x 10px circle, color matching the badge status, with a simple ripple animation, to the left of the text, with spacing-sm between them;

* Modals should ALWAYS have a Title and a Subtitle with descriptive information, these should ALWAYS be spacing-sm apart from eachother.

* Toasts should always be positioned bottom right of the screen, with spacing-xlg margin from the screen corner;

## 2. EXTERNAL RESOURCES

### Icon Source & Implementation

To ensure consistency, this design system uses the **Heroicons** icon set. The correct implementation method depends on your project's technology stack.

### For Modern Frameworks (React, Vue)

Use the official Heroicons NPM packages. This treats each icon as a reusable component, which is the standard, most maintainable approach for applications built on these platforms.

**React:**
npm install @heroicons/react

Use the imported component and pass `className` to control size, and the `strokeWidth` prop to match the style guide rules.

**Vue:**
npm install @heroicons/vue

Use the imported component and pass `class` to control size, and the `:stroke-width` prop to match the style guide rules.

### For Static Web (HTML/CSS)

For projects without a modern JavaScript framework, embed the SVG markup directly into your HTML.

1. On the [Heroicons website](https://heroicons.com/), find your icon and click "Copy SVG".
2. Paste the `<svg>` code directly into your HTML.
3. Set the `width`, `height`, and `stroke-width` attributes on the `<svg>` element to match the style guide rules.

### For Native Mobile & Desktop (iOS, Android)

For native applications, download the `.svg` file and import it as a project asset.

1. On the [Heroicons website](https://heroicons.com/), find your icon and click "Download SVG".
2. Import the downloaded file into your project's asset management system according to platform best practices:

* **iOS:** Add the `.svg` file to your asset catalog (`.xcassets`).

* **Android:** Import the `.svg` file into Android Studio, which will convert it into a `VectorDrawable` XML file.

## 3. UI STYLE CATALOGUE

### 3.A. BASE COMPONENT RULES

*This section defines the default styling for components. These rules apply to ALL themes unless explicitly overridden in a theme's specific section.*

- **Page:**
  
  - page-background: color-background-page;
  - typography-page-title: font-size-xl, font-weight-semibold, color-text-primary;
  - typography-page-subtitle: font-size-lg, font-weight-medium, color-text-primary;
  - typography-body: font-size-md, font-weight-light, color-text-body;
  - typography-small: font-size-sm, font-weight-light, color-text-body;
  - typography-smaller: font-size-xs, font-weight-regular, color-text-primary;
  - typography-placeholder: font-size-md, font-weight-light, color-text-placeholder;

- **Secondary Button:** color-background-secondary background, color-text-primary text, font-weight-regular, radius-md, border-default;

- **Tertiary Button:** no background, color-text-primary text, font-weight-regular, radius-md, no border;

- **Badges:** 
  
  - default-badge: color-background-secondary background, color-text-primary text, typography-small, radius-sm, border-default;
  - success-badge: color-semantic-success text, border-default;
  - warning-badge: color-semantic-warning text, border-default;
  - danger-badge: color-semantic-danger text, border-default;

- **Cards:** color-background-secondary background, radius-lg, border-default;

- **Modals:**
  
  - Backdrop:
    
    - modal-backdrop: color-background-dim, backdrop-filter: blur(64px);
  
  - Modal Container:
    
    - modal-container: Follows all "Cards" component rules;
  
  - Modal Header:
    
    - modal-header: typography-page-subtitle. MUST have a close button (icon-only, tertiary style) on the top right.
  
  - Modal Subheader:
    
    - modal-subheader: typography-body.
  
  - Modal Body:
    
    - modal-body: typography-small.
  
  - Modal Footer:
    
    - modal-footer: content right-aligned, spacing-md between buttons.

- **Tables:** 
  
  - table-container: radius-md, border-default;
  - cell-padding: spacing-md;

- **Input Fields:**
  
  - input-default: color-background-secondary background, radius-md, border-default;
  - input-hover: color-background-secondary background, radius-md, border-hover;
  - input-focus: color-background-secondary background, radius-md, border-focus;
  - input-danger: color-background-secondary background, radius-md, border-danger;
  - input-warning: color-background-secondary background, radius-md, border-warning;
  - input-success: color-background-secondary background, radius-md, border-success;

- **Search Bars:**
 
 - searchbar-default: Follows all input-default rules. MUST have a search icon on the left side, with spacing-sm from the text;
 - searchbar-hover: Follows all input-hover rules;
 - searchbar-focus: Follows all input-focus rules, but the border, which should stay as border-hover;

- **Dropdown Menus:**
  
  - Trigger Button:
    
    - dropdown-trigg-default: Follows all input-default rules. MUST have a chevron-down icon on the right side, with spacing-md from the edge;
    - dropdown-trigg-hover: Follows all input-hover rules;
    - dropdown-trigg-focus: Follows all input-focus rules;
    - dropdown-trigg-open: Follows all input-focus rules, and the icon MUST change to chevron-up;
  
  - Dropdown Option Item:
    
    - option-default: typography-small, color-text-body, font-weight-light;
    - option-hover: color-background-secondary background, typography-small, color-text-body, font-weight-light;
    - All states above MUST feature spacing-sm padding on all sides;

- **Icons:**
  
  - If used inside of full-size-button or medium-size-button, icon-size: 18px x 18px; 
  - If used on small-size-button, icon-size: 16px x 16px.
  - If used inside of an input field, icon-size: 16px x 16px;
  - If placed close to typography-body, icon-size: 16px x 16px;
  - If placed close to typography-small or typography-smaller, icon-size: 12px x 12px;
  - If placed inside of a toast, icon-size: 18px x 18px;

- **Inline Alerts:**
  
  - alert-danger: typography-smaller, color-semantic-danger-muted;
  - alert-warning: typography-smaller, color-semantic-warning-muted;
  - alert-success: typography-smaller, color-semantic-success-muted;

- **Alerts / Toasts:**
  
  - Structure:
    
    - alert-title: typography-small, color-text-primary, font-weight-medium;
    - alert-body: typography-small, color-text-body, font-weight-light; MUST have vertical spacing-xs from the title.
  
  - Semantic Styling:
    
    - alert-base: Follows all "Cards" component rules for background, border, and radius. MUST have spacing-md padding on all sides. MUST feature a relevant icon over the text, with spacing-sm between them.

- **Tooltips:**
  
  - tooltip-typography: typography-small, color-text-primary, font-weight-regular.

### STYLE 01: HYPERETH

#### Visual tokens

- **Core Tokens:**
  
  - font-family-base: Work Sans;
  - color-base-white: #FFFFFF;
  - color-base-black: #020203;

- **Color Tokens:** 
  
  - color-background-page: color-base-black;
  - color-background-dim: #02020380;
  - color-background-primary: color-base-white;
  - color-background-secondary: #FFFFFF06;
  - color-background-tertiary: #FFFFFF03;
  - color-background-quaternary: #FFFFFF09;
  - color-background-tooltip: #131514;
  - color-text-primary: color-base-white;
  - color-text-secondary: #FFFFFFBF;
  - color-text-body: #FFFFFFA8;
  - color-text-placeholder: #FFFFFF54;
  - color-text-inverse: color-base-black;
  - color-border-default: #FFFFFF13;
  - color-border-subtle: #FFFFFF08;
  - color-border-strong: #FFFFFF20;
  - color-border-hover: #FFFFFF26;
  - color-border-focus: #FFFFFF80;

- **Semantic Color Tokens:**
  
  - color-semantic-success: #1EBA4D;
  - color-semantic-success-muted: #1EBA4DBF;
  - color-semantic-success-faded: #1EBA4D80;
  - color-semantic-success-semi-subtle: #1EBA4D50;
  - color-semantic-success-subtle: #1EBA4D26;
  - color-semantic-warning: #BA9D1E;
  - color-semantic-warning-muted: #BA9D1EBF;
  - color-semantic-warning-faded: #BA9D1E80;
  - color-semantic-warning-semi-subtle: #BA9D1E50;
  - color-semantic-warning-subtle: #BA9D1E26;
  - color-semantic-danger: #BA1E3D;
  - color-semantic-danger-muted: #BA1E3DBF;
  - color-semantic-danger-faded: #BA1E3D80;
  - color-semantic-danger-semi-subtle: #BA1E3D50;
  - color-semantic-danger-subtle: #BA1E3D26;

- **Chart Colors:**
  
  - T1 green - saturated:
    
    - #56795CBF (t1-green-sat-d2);
    - #658E6CBF (t1-green-sat-d1);
    - #73A27BBF (t1-green-sat);
    - #85AE8CBF (t1-green-sat-l1);
    - #96B99CBF (t1-green-sat-l2);
  
  - T2 green - semi-saturated:
    
    - #5B7667BF (t2-green-semi-sat-d2);
    - #6A8979BF (t2-green-semi-sat-d1);
    - #799D8ABF (t2-green-semi-sat);
    - #8AA999BF (t2-green-semi-sat-l1);
    - #9BB6A7BF (t2-green-semi-sat-l2);
  
  - T3 green - desaturated:
    
    - #909E91BF (t3-green-de-sat-d2);
    - #A8B9AABF (t3-green-de-sat-d1);
    - #C0D3C2BF (t3-green-de-sat);
    - #C8D9CABF (t3-green-de-sat-l1);
    - #D0DED1BF (t3-green-de-sat-l2);
  
  - T1 terracota - saturated:
    
    - #B06755BF (t1-terra-sat-d2);
    - #CE7963BF (t1-terra-sat-d1);
    - #EB8A71BF (t1-terra-sat);
    - #EE9983BF (t1-terra-sat-l1);
    - #F0A795BF (t1-terra-sat-l2);
  
  - T2 terracota - semi-saturated:
    
    - #BB8B77BF (t2-terra-semi-sat-d2);
    - #DBA38BBF (t2-terra-semi-sat-d1);
    - #FABA9FBF (t2-terra-semi-sat);
    - #FBC3ABBF (t2-terra-semi-sat-l1);
    - #FBCBB7BF (t2-terra-semi-sat-l2);
  
  - T3 terracota - desaturated:
    
    - #B89982BF (t3-terra-de-sat-d2);
    - #D6B298BF (t3-terra-de-sat-d1);
    - #F5CCAEBF (t3-terra-de-sat);
    - #F6D2B8BF (t3-terra-de-sat-l1);
    - #F8D9C2BF (t3-terra-de-sat-l2);

- **Border Tokens:** 
  
  - border-default: 1px solid color-border-default;
  - border-subtle: 1px solid color-border-subtle;
  - border-hover: 1px solid color-border-hover;
  - border-focus: 1px solid color-border-focus;
  - border-danger: 1px solid color-semantic-danger-faded;
  - border-danger-subtle: 1px solid color-semantic-danger-semi-subtle;
  - border-warning: 1px solid color-semantic-warning-faded;
  - border-warning-subtle: 1px solid color-semantic-warning-semi-subtle;
  - border-success: 1px solid color-semantic-success-faded;
  - border-success-subtle: 1px solid color-semantic-success-semi-subtle;
  - border-impact: 1px solid color-base-white;

- **Border Radius Tokens:** 
  
  - radius-xs: 2px;
  - radius-mxs: 4px;
  - radius-sm: 6px;
  - radius-md: 12px; (Standard)
  - radius-lg: 16px;
  - radius-full: 50%;

- **Typography Tokens:**
  
  - font-size-xs: 12px;
  - font-size-sm: 14px;
  - font-size-md: 16px;
  - font-size-lg: 24px;
  - font-size-xl: 32px;
  - font-weight-light: 300;
  - font-weight-regular: 400;
  - font-weight-medium: 500;
  - font-weight-semibold: 600;

#### Component rule overrides for this style:
*These rules override or add to the Base Component Rules.*

- **Primary Button:** color-background-primary background, color-text-inverse text, font-weight-regular, radius-md, no border;

- **Navigation / Tabs:**
  
  - Tab Bar (container holding the tabs):
    
    - tab-bar-container: no background, no borders, no padding, spacing-md between Tab Items;
  
  - Tab Item (individual tab element):
    
    - tab-default-state: 36px height, color-background-secondary background, font-size-sm color-text-primary text, border-default, radius-md;
    - tab-default-hover: border-hover;
    - tab-active-state: 36px height, color-background-primary background, font-size-sm color-text-inverse text, no border, radius-md;
    - tab-active-hover: no changes;

- **Tables:** 
  
  - table-header: color-background-secondary background, color-text-body, font-weight-light;
  - table-body: color-background-tertiary background, color-text-secondary, font-weight-light;
  - table-body-hover: color-background-quaternary background, color-text-secondary, font-weight-light;

- **Dropdown Menus:**
  
  - Dropdown Panel:
    
    - dropdown-panel: color-base-black background, radius-md, border-default, backdrop-filter: blur(24px), vertical spacing from under "Trigger Button" spacing-sm;
  
  - Dropdown Option Item:
    
    - option-selected: color-background-quaternary background, typography-small, color-text-secondary, font-weight-regular;

- **Checkboxes:**
  
  - Un-checked state (default):
    
    - checkbox-default: 20px x 20px size, border-default, color-background-secondary background, radius-sm;
    - checkbox-hover: border-hover;
    - checkbox-focus: border-focus;
  
  - Checked state:
    
    - checkbox-checked-default: border-impact;
    - checkbox-checked-hover & checkbox-checked-focus: no changes;
    - The checked state, rather than showing a checkmark, shows the inner-element below centralized inside of the checkbox wraper.
    - inner-element: 10px x 10px size, color-base-white, radius-xs;
  
  - Checkmark Icon:
    
    NEVER add a checkmark icon to this component when using this catalogue entry;
  
  - Label (text next to the element):
    
    - checkbox-label-unchecked: typography-small, color-text-body, font-weight-light, spacing-sm horizontal spacing from the checkbox;
    - checkbox-label-checked: typography-small, color-text-primary, font-weight-regular, spacing-sm horizontal spacing from the checkbox;

- **Radio Buttons:**
  
  - In this catalogue entry, the Radio Buttons follow exactly the visual properties from the Checkboxes checked and uncheck states, the only difference being border-radius: radius-full;

- **Toggles / Switches:**
  
  - Track (the background shape):
    
    - toggle-track-off: 34px width, 20px height, color-background-secondary, border-default, radius-sm, spacing-xxs padding;
    - toggle-track-on: 34px width, 20px height, color-background-quaternary, border-impact, radius-sm, spacing-xxs padding;
  
  - Thumb (the sliding knob):
    
    - toggle-thumb-off: 14px x 14px, color-border-default, radius-mxs;
    - toggle-thumb-on: 14px x 14px, color-base-white, radius-mxs;
  
  - Label (the text next to the toggle):
    
    - toggle-label-off: typography-small, color-text-body, font-weight-light, spacing-sm horizontal spacing from the toggle;
    - toggle-label-on: typography-small, color-text-primary, font-weight-regular, spacing-sm horizontal spacing from the toggle;

- **Icons:**
  
  - icon-stroke-width: 1.5px; (Default)

- **Alerts / Toasts:**
  
  - Semantic Styling:
    
    - alert-success: border-success, color-semantic-success-subtle background; The icon MUST be color-semantic-success.
    - alert-warning: border-warning, color-semantic-warning-subtle background; The icon MUST be color-semantic-warning.
    - alert-danger: border-danger, color-semantic-danger-subtle background; The icon MUST be color-semantic-danger.

- **Tooltips:**
  
  - tooltip-container: color-background-tooltip background, radius-sm, spacing-sm padding on all sides, border-subtle.
  - tooltip-arrow: 6px x 6px triangle, MUST have the same background color as the tooltip-container.

### STYLE 02: 1RPC

#### Visual tokens

- **Core Tokens:**
  
  - font-family-base: Work Sans;
  - color-base-white: #FFFFFF;
  - color-base-orange: #E06612;
  - color-base-dark-blue: #070E17;

- **Color Tokens:**
  
  - color-background-page: color-base-dark-blue;
  - color-background-dim: #070E1780;
  - color-background-primary: color-base-orange;
  - color-background-secondary: #0A111A;
  - color-background-tertiary: #0E151E;
  - color-background-quaternary: #121922;
  - color-background-hover: #101720;
  - color-background-midway: #17171C;
  - color-text-primary: color-base-white;
  - color-text-secondary: #FFFFFFBF;
  - color-text-body: #FFFFFFA8;
  - color-text-placeholder: #FFFFFF54;
  - color-border-default: #FFFFFF13;
  - color-border-subtle: #FFFFFF08;
  - color-border-hover: #FFFFFF26;
  - color-border-focus: #FFFFFF80;

- **Semantic Color Tokens:**
  
  - color-semantic-success: #2ACF94;
  - color-semantic-success-muted: #2ACF94BF;
  - color-semantic-success-faded: #2ACF9480;
  - color-semantic-warning: #E0BA12;
  - color-semantic-warning-muted: #E0BA12BF;
  - color-semantic-warning-faded: #E0BA1280;
  - color-semantic-danger: #CF2A3D;
  - color-semantic-danger-muted: #CF2A3DBF;
  - color-semantic-danger-faded: #CF2A3D80;

- **Chart Colors:**
  
  - T1 blue - saturated:
    
    - #1A3D97BF (t1-blue-sat-d2);
    - #1F48B1BF (t1-blue-sat-d1);
    - #2352CABF (t1-blue-sat);
    - #3F68D1BF (t1-blue-sat-l1);
    - #5A7DD7BF (t1-blue-sat-l2);
  
  - T2 blue - semi-saturated:
    
    - #2061ABBF (t2-blue-semi-sat-d2);
    - #2671C7BF (t2-blue-semi-sat-d1);
    - #2B81E4BF (t2-blue-semi-sat);
    - #4691E7BF (t2-blue-semi-sat-l1);
    - #60A1EBBF (t2-blue-semi-sat-l2);
  
  - T3 blue - desaturated:
    
    - #688CB5BF (t3-blue-de-sat-d2);
    - #7AA4D3BF (t3-blue-de-sat-d1);
    - #8BBBF1BF (t3-blue-de-sat);
    - #9AC4F3BF (t3-blue-de-sat-l1);
    - #A8CCF5BF (t3-blue-de-sat-l2);
  
  - T1 orange - saturated:
    
    - #B93413BF (t1-orange-sat-d2);
    - #D83D16BF (t1-orange-sat-d1);
    - #F74619BF (t1-orange-sat);
    - #F85D36BF (t1-orange-sat-l1);
    - #F97453BF (t1-orange-sat-l2);
  
  - T2 orange - semi-saturated:
    
    - #BF4E00BF (t2-orange-semi-sat-d2);
    - #DF5B00BF (t2-orange-semi-sat-d1);
    - #FF6800BF (t2-orange-semi-sat);
    - #FF7B20BF (t2-orange-semi-sat-l1);
    - #FF8E40BF (t2-orange-semi-sat-l2);
  
  - T3 orange - desaturated:
    
    - #B86F36BF (t3-orange-de-sat-d2);
    - #D6813FBF (t3-orange-de-sat-d1);
    - #F59448BF (t3-orange-de-sat);
    - #F6A15FBF (t3-orange-de-sat-l1);
    - #F8AF76BF (t3-orange-de-sat-l2);

- **Border Tokens:** 
  
  - border-default: 1px solid color-border-default;
  - border-subtle: 1px solid color-border-subtle;
  - border-hover: 1px solid color-border-hover;
  - border-focus: 1px solid color-border-focus;
  - border-lumina: 1px solid color-base-orange;
  - border-danger: 1px solid color-semantic-danger-faded;
  - border-warning: 1px solid color-semantic-warning-faded;
  - border-success: 1px solid color-semantic-success-faded;

- **Border Radius Tokens:** 
  
  - radius-sm: 4px;
  - radius-md: 8px;
  - radius-lg: 12px;
  - radius-full: 50%;
  - radius-pill: 999px;

- **Typography Tokens:**
  
  - font-size-xs: 12px;
  - font-size-sm: 14px;
  - font-size-md: 16px;
  - font-size-lg: 24px;
  - font-size-xl: 32px;
  - font-weight-light: 300;
  - font-weight-regular: 400;
  - font-weight-medium: 500;
  - font-weight-semibold: 600;

#### Component rule overrides for this style:
*These rules override or add to the Base Component Rules.*

- **Primary Button:** color-background-primary background, color-text-primary text, font-weight-regular, radius-md, no border;

- **Navigation / Tabs:**
  
  - Tab Bar (container holding the tabs):
    
    - tab-bar-container: no background, no borders, no padding, spacing-xlg between Tab Items;
  
  - Tab Item (individual tab element):
    
    - tab-default-state: no background, font-size-md font-weight-light color-text-body text, transparent bottom border-lumina, bottom padding spacing-sm;
    - tab-default-hover: color-text-secondary text;
    - tab-active-state: no background, font-size-md font-weight-regular color-text-primary text, bottom border-lumina, bottom padding spacing-sm;
    - tab-active-hover: no changes;

- **Tables:** 
  
  - table-header: color-background-tertiary background, color-text-primary text, font-weight-regular;
  - table-body: color-background-secondary background, color-text-body, font-weight-light;
  - table-body-hover: color-background-hover background, color-text-secondary, font-weight-light;

- **Dropdown Menus:**
  
  - Dropdown Panel:
    
    - dropdown-panel: color-background-page background, radius-md, border-default, vertical spacing from under "Trigger Button" spacing-sm;
  
  - Dropdown Option Item:
    
    - option-selected: color-background-tertiary background, typography-small, color-text-secondary, font-weight-regular;

- **Checkboxes:**
  
  - Un-checked state (default):
    
    - checkbox-default: 16px x 16px size, border-default, color-background-secondary background, radius-sm;
    - checkbox-hover: border-hover;
    - checkbox-focus: border-focus;
  
  - Checked state:
    
    - checkbox-checked-default: border-default, color-background-primary background with checkbox-icon centralized;
    - checkbox-checked-hover & checkbox-checked-focus: no changes;
  
  - Checkmark Icon:
    
    - checkbox-icon: 10px x 10px size, stroke-width of 1.5px, color-text-primary; Always keep it center-aligned;
  
  - Label (text next to the element):
    
    - checkbox-label-unchecked: typography-small, color-text-body, font-weight-light, spacing-sm horizontal spacing from the checkbox;
    - checkbox-label-checked: typography-small, color-text-primary, font-weight-regular, spacing-sm horizontal spacing from the checkbox;

- **Radio Buttons:**
  
  - Un-selected state (default):
    
    - radio-default: 16px x 16px size, border-default, color-background-secondary background, radius-full;
    - radio-hover: border-hover;
    - radio-focus: border-focus;
  
  - Selected state:
    
    - radio-selected-default: border-default;
    - radio-selected-hover & radio-selected-focus: no changes;
    - The checked state, shows the inner-element below centralized inside of the radio button wraper.
    - inner-element: 8px x 8px size, color-base-white, radius-full;
  
  - Label (text next to the element):
    
    - Follow exactly the design properties from the Checkboxes labels;

- **Toggles / Switches:**
  
  - Track (the background shape):
    
    - toggle-track-off: 48px width, 28px height, color-background-secondary, border-default, radius-pill, spacing-xs padding;
    - toggle-track-on: 48px width, 28px height, color-background-midway, border-lumina, radius-pill, spacing-xs padding;
  
  - Thumb (the sliding knob):
    
    - toggle-thumb: 20px x 20px, color-base-white, radius-full;
  
  - Label (the text next to the toggle):
    
    - toggle-label-off: typography-small, color-text-body, font-weight-light, spacing-sm horizontal spacing from the toggle;
    - toggle-label-on: typography-small, color-text-primary, font-weight-regular, spacing-sm horizontal spacing from the toggle;

- **Icons:**
  
  - icon-stroke-width: 1.75px; (Default)

- **Alerts / Toasts:**
  
  - Semantic Styling:
    
    - alert-success: border-success; The icon MUST be color-semantic-success.
    - alert-warning: border-warning; The icon MUST be color-semantic-warning.
    - alert-danger: border-danger; The icon MUST be color-semantic-danger.

- **Tooltips:**
  
  - tooltip-container: color-background-secondary background, radius-sm, spacing-sm padding on all sides, border-subtle.
  - tooltip-arrow: 6px x 6px triangle, MUST have the same background color as the tooltip-container.

## 4. COMPONENT CONTEXT

This section provides a definitive guide to the components within the design system. Each entry describes purpose and usage guidelines for a component:

### **Buttons**

Buttons are interactive elements used to trigger actions. The choice of button should correspond to the action's priority in the user workflow.

- **Primary Button:**
    
    - **Description:** The principal call-to-action on a page. It's styled with the highest visual weight to draw user attention to the most important action.
    
    - **Usage:** Use for final, affirmative actions like "Submit," "Confirm," "Create Account," or "Save." Limit to one Primary Button per view to avoid confusing the user.

- **Secondary Button:**
    
    - **Description:** The standard button for most common actions. It's visually distinct but does not compete with the Primary Button.
    
    - **Usage:** Use for secondary actions like "Cancel," "Go Back," or "View Details." It's also the default choice when all actions on a page have equal weight.

- **Tertiary Button:**
    
    - **Description:** A low-emphasis button for non-critical or supplemental actions. It has the appearance of a link but is used for actions, not navigation.
    
    - **Usage:** Use for actions like "Reset Filters," "Learn More," or dismissing a non-critical notification. Avoid using it for destructive actions (e.g., "Delete").

### **Badges**

Badges are small, non-interactive elements used to display a status, count, or brief piece of information.

- **Default Badge:**
    
    - **Description:** A neutral badge for displaying metadata or attributes through the interface.
    
    - **Usage:** Ideal for labeling items, showing categories, or displaying a version number (e.g., "Admin," "v2.0").

- **Status Badges (Success, Warning, Error):**
    
    - **Description:** Semantic badges that use color to convey a specific system status clearly and immediately.
    
    - **Usage:** Use to indicate the result of an operation or the state of an item. For example, "Success" for a completed transaction, "Warning" for a pending expiration, or "Error" for a failed process.

### **Navigation / Tabs**

Tabs provide a way to organize and navigate between different views or sets of content within the same context.

- **Tab Bar:**
    
    - **Description:** The container for a set of Tab Items. It establishes the interactive area for the tab navigation.
    
    - **Usage:** Use to segment a page or a component (like a modal) into related but distinct sections. Do not use for navigating to entirely different pages of the application.

- **Tab Item:**
    
    - **Description:** An individual, clickable tab that switches the view to its corresponding content panel.
    
    - **Usage:** Tab labels should be short and descriptive. Ensure the active tab is always clearly differentiated from the inactive ones.

### **Cards**

Cards are flexible content containers that group related information and actions into a single, digestible unit.

- **Card:**
    
    - **Description:** A bordered container that provides a clear boundary for a piece of content, visually separating it from the rest of the page.
    
    - **Usage:** Ideal for dashboards, feeds, or any layout where discrete blocks of content need to be displayed. Cards can contain any mix of text, images, and actions.

### **Modals**

Modals are UI overlays that interrupt the main user flow to present critical information or require user input. They are used to focus the user's attention on a single, important task.

- **Modal:**
    
    - **Description:** A dialog box that appears on top of the main page content, usually with a backdrop that dims or blurs the background. The user cannot interact with the rest of the page until the modal is dismissed.
    
    - **Usage:** Use modals for tasks that require the user's full attention and must be completed before they can return to the main flow. Examples include confirming a destructive action (e.g., "Are you sure you want to delete this?"), handling user authentication (login / signup forms), or for complex but contained workflows (like adding a new item with multiple fields). Avoid using them for non-critical notifications or information that doesn't require immediate action, as they have a disruptive nature.

### **Tables**

Tables are used to display sets of structured data in a grid format, allowing for easy comparison and analysis.

- **Table:**
    
    - **Description:** A component for organizing and displaying data in rows and columns.
    
    - **Usage:** Use only for tabular data. For lists of non-tabular items, consider using a list of Cards instead. Ensure table headers are always distinct from the body rows.

### **Input Fields**

Input fields allow users to enter and edit text or data.

- **Input Field:**
    
    - **Description:** A standard form control that accepts user-provided text.
    
    - **Usage:** Always pair with a clear label. Use placeholder text only for supplemental hints, not as a replacement for a label. Utilize the different states (focus, error, etc.) to provide clear feedback to the user.

### **Search Bars**

Search bars are specialized input fields designed for finding specific content within the application or a dataset.

- **Search Bar:**
    
    - **Description:** An input field specifically designated for search queries, always accompanied by a search icon.
    
    - **Usage:** Use as the primary mechanism for searching. The icon serves as a clear, universal affordance for the search action.

### **Dropdown Menus**

Dropdowns (or Selects) allow users to choose one option from a list.

- **Dropdown Menu:**
    
    - **Description:** A component that presents a list of options from which a user can select one. It's a form of input.
    
    - **Usage:** Use when there are more than five options to choose from. For five or fewer options, consider using Radio Buttons instead to make all choices immediately visible.

### **Selection Controls**

These controls allow users to make choices from a set of options.

- **Checkbox:**
    
    - **Description:** Allows a user to select one or more options from a list. Each checkbox operates independently.
    
    - **Usage:** Use for "select all that apply" scenarios. Can also be used for a single binary choice, like "I agree to the terms."

- **Radio Button:**
    
    - **Description:** Allows a user to select exactly one option from a mutually exclusive set. Selecting one radio button automatically deselects any other in the same group.
    
    - **Usage:** Use when a user must make a single choice from a limited set of options (e.g., selecting a plan tier, choosing a shipping method).

- **Toggle / Switch:**
    
    - **Description:** Represents an on/off state for a single setting. It is a direct action that takes effect immediately.
    
    - **Usage:** Use for activating or deactivating a setting, like "Enable Notifications" or "Dark Mode." Unlike a checkbox, a toggle's action is typically immediate and does not require a "Submit" button.

### **Inline Alerts**

Inline alerts provide contextual feedback messages related to a specific action or input.

- **Inline Alert:**
    
    - **Description:** A brief, contextual message that appears near the element it relates to, providing status or error information.
    
    - **Usage:** Primarily used under input fields to communicate validation feedback (e.g., "This field is required," "Email format is incorrect"). The color and icon should always match the message's semantic meaning (success, warning, danger).

### **Alerts / Toasts**

These components are used to provide feedback or communicate important information to the user. The main difference between them is context and persistence.

- **Alert:**
    
    - **Description:** A static, contextual message that is embedded within a page or layout. It remains visible until the condition that triggered it is resolved, or it is manually dismissed by the user.
    
    - **Usage:** Use for persistent information that is important in the current context. Examples include "Your subscription is expiring soon," "This project is archived and read-only," or a banner announcing a system-wide maintenance. They are part of the page content.

- **Toast:**
    
    - **Description:** A temporary, non-intrusive notification that appears briefly to confirm an action or provide a system update. It does not interrupt the user's workflow and typically disappears on its own after a few seconds.
    
    - **Usage:** Use for providing immediate, low-priority feedback on actions the user has just taken. Examples include "Settings saved successfully," "File uploaded," or "Message sent." They should appear in a consistent location on the screen (as defined by our Golden Rule: bottom right) and should not require user interaction to be dismissed.

### **Tooltips**

Tooltips are small, informational pop-ups that appear when a user hovers over or focuses on an element. They provide brief, contextual help or supplementary information without cluttering the main interface.

- **Tooltip:**
    
    - **Description:** A floating label that provides a concise description or name for an interactive element. It typically appears next to the element it describes, with a small arrow pointing towards it.
        
    - **Usage:** Use tooltips to clarify the function of icon-only buttons, provide full text for truncated labels, or offer short, non-essential hints about an interface element. They are ideal for information that is helpful but not critical to the user's primary workflow. Avoid placing critical information or actions inside a tooltip, as they are only revealed on hover and are not easily discoverable.
