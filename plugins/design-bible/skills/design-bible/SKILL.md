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

*   **Clarity and Intent:** Every component and style is designed to be clear, unambiguous, and purposeful. We favor explicit rules over implicit assumptions.
*   **Thematic Flexibility:** The system is designed to support multiple, distinct visual themes from a single set of semantic rules.
*   **Accessibility First:** All components must meet modern accessibility standards, ensuring usability for everyone.
*   **Token-Driven:** All visual styles—from colors to spacing—are derived from a central set of design tokens. Components are built from tokens; they do not define their own styles.

## 1. GOLDEN RULES

Your behaviour:

* ALWAYS ask the user for which style they want from your UI style catalogue if they don't specify one themselves. NEVER proceed without having them choose a style.

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

* ALWAYS use the specific font from your UI style catalogue selected entry when creating input fields, for both default and placeholder typography usages.

* ALWAYS add an "Inline Alert" under the input field states input-error, input-alert and input-success. Vertical spacing between input and inline alert should ALWAYS be spacing-sm.

* ALWAYS add a coherent icon to the left of any inline alert. Spacing between icon and inline alert should ALWAYS be spacing-sm. Size of icon should ALWAYS be 16px x 16px, and stroke-width 1.5px.

* ALWAYS overwrite the base typography text-color when creating an "Inline Alert" component.

* ONLY use "Chart Colors" to compose color palettes to be used for data visualization on charts and graphs. ALWAYS follow good practices of color matching and contrast, like having semi-sat colors as the default usage go-to.

* ALWAYS overwrite the default table header cell's font-weight, so you can apply your own design styles instead.

* ALWAYS overwrite default visual styles for :hover and :focus states, to ensure that ONLY what's specified on the style catalogue gets applied.

* ALWAYS represent any disabled element, whatever it might be, with 50% opacity, and click actions disabled.

* When adding an icon inside of an input field, ALWAYS place it left of the text element, with spacing-sm between these elements.

* ALWAYS overwrite system default Toggle components, so you can apply your own design styles instead;

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

1.  On the [Heroicons website](https://heroicons.com/), find your icon and click "Copy SVG".
2.  Paste the `<svg>` code directly into your HTML.
3.  Set the `width`, `height`, and `stroke-width` attributes on the `<svg>` element to match the style guide rules.

### For Native Mobile & Desktop (iOS, Android)

For native applications, download the `.svg` file and import it as a project asset.

1.  On the [Heroicons website](https://heroicons.com/), find your icon and click "Download SVG".
2.  Import the downloaded file into your project's asset management system according to platform best practices:

*   **iOS:** Add the `.svg` file to your asset catalog (`.xcassets`).

*   **Android:** Import the `.svg` file into Android Studio, which will convert it into a `VectorDrawable` XML file.

## 3. UI STYLE CATALOGUE

Here are the multiple styles you've specialized yourself in:

### STYLE 01: HYPERETH

#### Visual tokens

- **Core Tokens:**
  
  - font-family-base: Work Sans;
  - color-base-white: #FFFFFF;
  - color-base-black: #020203;

- **Color Tokens:** 
  
  - color-background-page: color-base-black;
  - color-background-primary: color-base-white;
  - color-background-secondary: #FFFFFF06;
  - color-background-tertiary: #FFFFFF03;
  - color-background-quaternary: #FFFFFF09;
  - color-text-primary: color-base-white;
  - color-text-secondary: #FFFFFFBF;
  - color-text-body: #FFFFFFA8;
  - color-text-placeholder: #FFFFFF54;
  - color-text-inverse: color-base-black;
  - color-border-default: #FFFFFF13; 
  - color-border-strong: #FFFFFF20;
  - color-border-hover: #FFFFFF26;
  - color-border-focus: #FFFFFF80;

- **Semantic Color Tokens:**
  
  - color-semantic-success: #1EBA4D;
  - color-semantic-success-muted: #1EBA4DBF;
  - color-semantic-success-faded: #1EBA4D80;
  - color-semantic-warning: #BA9D1E;
  - color-semantic-warning-muted: #BA9D1EBF;
  - color-semantic-warning-faded: #BA9D1E80;
  - color-semantic-danger: #BA1E3D;
  - color-semantic-danger-muted: #BA1E3DBF;
  - color-semantic-danger-faded: #BA1E3D80;

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
  
  - border-default: 0.75px solid color-border-default;
  - border-hover: 0.75px solid color-border-hover;
  - border-focus: 0.75px solid color-border-focus;
  - border-danger: 0.75px solid color-semantic-danger-faded;
  - border-warning: 0.75px solid color-semantic-warning-faded;
  - border-success: 0.75px solid color-semantic-success-faded;
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

#### Component rules for this style:

- **Page:**
  
  - page-background: color-background-page;
  - typography-page-title: font-size-xl, font-weight-semibold, color-text-primary;
  - typography-page-subtitle: font-size-lg, font-weight-medium, color-text-primary;
  - typography-body: font-size-md, font-weight-light, color-text-body;
  - typography-small: font-size-sm, font-weight-light, color-text-body;
  - typography-smaller: font-size-xs, font-weight-regular, color-text-primary;
  - typography-placeholder: font-size-md, font-weight-light, color-text-placeholder;

- **Primary Button:** color-background-primary background, color-text-inverse text, font-weight-regular, radius-md, no border;

- **Secondary Button:** color-background-secondary background, color-text-primary text, font-weight-regular, radius-md, border-default;

- **Tertiary Button:** no background, color-text-primary text, font-weight-regular, radius-md, no border;

- **Navigation / Tabs:**
  
  - Tab Bar (container holding the tabs):

    - tab-bar-container: no background, no borders, no padding, spacing-md between Tab Items;

  - Tab Item (individual tab element):

    - tab-default-state: 36px height, color-background-secondary background, font-size-sm color-text-primary text, border-default, radius-md;
    - tab-default-hover: border-hover;
    
    - tab-active-state: 36px height, color-background-primary background, font-size-sm color-text-inverse text, no border, radius-md;
    - tab-active-hover: no changes;

- **Cards:** color-background-secondary background, radius-lg, border-default;

- **Tables:** 
  
  - table-container: radius-md, color-border-default;
  - cell-padding: spacing-md;
  - table-header: color-background-secondary background, color-text-body, font-weight-light;
  - table-body: color-background-tertiary background, color-text-secondary, font-weight-light;
  - table-body-hover: color-background-quaternary background, color-text-secondary, font-weight-light;

- **Input Fields:**
  
  - input-default: color-background-secondary background, radius-md, border-default;
  - input-hover: color-background-secondary background, radius-md, border-hover;
  - input-focus: color-background-secondary background, radius-md, border-focus;
  - input-danger: color-background-secondary background, radius-md, border-danger;
  - input-warning: color-background-secondary background, radius-md, border-warning;
  - input-success: color-background-secondary background, radius-md, border-success;

- **Dropdown Menus:**
  
  - Trigger Button:
    
    - dropdown-trigg-default: Follows all input-default rules. MUST have a chevron-down icon on the right side, with spacing-md from the edge;
    - dropdown-trigg-hover: Follows all input-hover rules;
    - dropdown-trigg-focus: Follows all input-focus rules;
    - dropdown-trigg-open: Follows all input-focus rules, and the icon MUST change to chevron-up;
  
  - Dropdown Panel:
    
    - dropdown-panel: color-base-black background, radius-md, border-default, vertical spacing from under "Trigger Button" spacing-sm;
  
  - Dropdown Option Item:
    
    - option-default: typography-small, color-text-body, font-weight-light;
    - option-hover: color-background-secondary background, typography-small, color-text-body, font-weight-light;
    - option-selected: color-background-quaternary background, typography-small, color-text-secondary, font-weight-regular;
    - All states above MUST feature spacing-sm padding on all sides;

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
  
  - icon-stroke-width: 1.5px; 
  - If used inside of full-size-button or medium-size-button, icon-size: 20px x 20px; 
  - If used on small-size-button, icon-size: 18px x 18px.
  - If used inside of an input field, icon-size: 16px x 16px;

- **Inline Alerts:**
  
  - alert-danger: typography-smaller, color-semantic-danger-muted;
  - alert-warning: typography-smaller, color-semantic-warning-muted;
  - alert-success: typography-smaller, color-semantic-success-muted;

### STYLE 02: 1RPC

#### Visual tokens

- **Core Tokens:**
  
  - font-family-base: Work Sans;
  - color-base-white: #FFFFFF;
  - color-base-orange: #E06612;
  - color-base-dark-blue: #070E17;

- **Color Tokens:**
  
  - color-background-page: color-base-dark-blue;
  - color-background-primary: color-base-orange;
  - color-background-secondary: #0A111A;
  - color-background-tertiary: #0E151E;
  - color-background-hover: #101720;
  - color-background-midway: #17171C;
  - color-text-primary: color-base-white;
  - color-text-secondary: #FFFFFFBF;
  - color-text-body: #FFFFFFA8;
  - color-text-placeholder: #FFFFFF54;
  - color-border-default: #FFFFFF13;
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

#### Component rules for this style:

- **Page:**
  
  - page-background: color-background-page;
  - typography-page-title: font-size-xl, font-weight-semibold, color-text-primary;
  - typography-page-subtitle: font-size-lg, font-weight-medium, color-text-primary;
  - typography-body: font-size-md, font-weight-light, color-text-body;
  - typography-small: font-size-sm, font-weight-light, color-text-body;
  - typography-smaller: font-size-xs, font-weight-medium, color-text-primary;
  - typography-placeholder: font-size-md, font-weight-light, color-text-placeholder;

- **Primary Button:** color-background-primary background, color-text-primary text, font-weight-regular, radius-md, no border;

- **Secondary Button:** color-background-secondary background, color-text-primary text, font-weight-regular, radius-md, border-default;

- **Tertiary Button:** no background, color-text-primary text, font-weight-regular, radius-md, no border;

- **Navigation / Tabs:**
  
  - Tab Bar (container holding the tabs):

    - tab-bar-container: no background, no borders, no padding, spacing-xlg between Tab Items;

  - Tab Item (individual tab element):

    - tab-default-state: no background, font-size-md color-text-body text, transparent bottom border-lumina, bottom padding spacing-sm;
    - tab-default-hover: color-text-secondary text;
    
    - tab-active-state: no background, font-size-md color-text-primary text, bottom border-lumina, bottom padding spacing-sm;
    - tab-active-hover: no changes;

- **Cards:** color-background-secondary background, radius-lg, border-default;

- **Tables:** 
  
  - table-container: radius-md, border-default;
  - cell-padding: spacing-md;
  - table-header: color-background-tertiary background, color-text-primary text, font-weight-regular;
  - table-body: color-background-secondary background, color-text-body, font-weight-light;
  - table-body-hover: color-background-hover background, color-text-secondary, font-weight-light;

- **Input Fields:**
  
  - input-default: color-background-secondary background, radius-md, border-default;
  - input-hover: color-background-secondary background, radius-md, border-hover;
  - input-focus: color-background-secondary background, radius-md, border-focus;
  - input-danger: color-background-secondary background, radius-md, border-danger;
  - input-warning: color-background-secondary background, radius-md, border-warning;
  - input-success: color-background-secondary background, radius-md, border-success;

- **Dropdown Menus:**
  
  - Trigger Button:
    
    - dropdown-trigg-default: Follows all input-default rules. MUST have a chevron-down icon on the right side, with spacing-md from the edge;
    - dropdown-trigg-hover: Follows all input-hover rules;
    - dropdown-trigg-focus: Follows all input-focus rules;
    - dropdown-trigg-open: Follows all input-focus rules, and the icon MUST change to chevron-up;
  
  - Dropdown Panel:
    
    - dropdown-panel: color-background-page background, radius-md, border-default, vertical spacing from under "Trigger Button" spacing-sm;
  
  - Dropdown Option Item:
    
    - option-default: typography-small, color-text-body, font-weight-light;
    - option-hover: color-background-secondary background, typography-small, color-text-body, font-weight-light;
    - option-selected: color-background-tertiary background, typography-small, color-text-secondary, font-weight-regular;
    - All states above MUST feature spacing-sm padding on all sides;

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
  
  - icon-stroke-width: 1.75px; 
  - If used inside of full-size-button or medium-size-button, icon-size: 20px x 20px; 
  - If used on small-size-button, icon-size: 18px x 18px.
  - If used inside of an input field, icon-size: 16px x 16px;

- **Inline Alerts:**
  
  - alert-danger: typography-smaller, color-semantic-danger-muted;
  - alert-warning: typography-smaller, color-semantic-warning-muted;
  - alert-success: typography-smaller, color-semantic-success-muted;
