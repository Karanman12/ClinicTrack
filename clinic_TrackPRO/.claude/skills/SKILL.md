---
name: ClinicTrack Frontend Design Skill
description: Frontend design guidelines for ClinicTrack medical clinic management web app
trigger: /design or when discussing UI/UX, component patterns, or visual design
---

# ClinicTrack Frontend Design Skill

## Overview
This skill provides design guidance for ClinicTrack — a medical clinic management web app. Apply these rules when designing, modifying, or reviewing UI components.

## Color Tokens

| Token | Hex | Usage |
|-------|-----|-------|
| primary | `#0A1628` | Headers, primary buttons, sidebar |
| accent | `#00B4D8` | CTAs, links, active states, highlights |
| success | `#10B981` | Confirmations, positive states, online status |
| warning | `#F59E0B` | Alerts, pending states, attention needed |
| white | `#FFFFFF` | Card backgrounds, input backgrounds |
| light-gray | `#F8FAFC` | Page backgrounds, subtle dividers |

## Typography

- **Font**: Inter (Google Fonts)
- **Scale**: 12px → 14px → 16px → 20px → 24px → 32px → 40px → 56px
- **Hierarchy**:
  - H1: 32px/40px, font-weight 700
  - H2: 24px/32px, font-weight 600
  - H3: 20px/28px, font-weight 600
  - Body: 16px/24px, font-weight 400
  - Small: 14px/20px, font-weight 400
  - Caption: 12px/16px, font-weight 500

## Spacing System

- **Base unit**: 8px
- **Scale**: 4px → 8px → 12px → 16px → 24px → 32px → 48px → 64px → 96px
- Use multiples of 8 for padding, margins, and gaps
- Card padding: 24px
- Section gaps: 32px or 48px

## Component Patterns

### Buttons
- **Primary**: Navy background (#0A1628), white text, 12px 24px padding, 8px radius
- **Secondary**: White background, navy border, navy text
- **Ghost**: Transparent, navy text, no border
- **Hover**: Subtle brightness shift, 150ms transition
- **Height**: 40px (default), 36px (small), 48px (large)

### Cards
- White background, subtle shadow: `0 1px 3px rgba(10, 22, 40, 0.08)`
- Border radius: 12px
- Padding: 24px
- Hover state: slightly elevated shadow for interactive cards

### Form Inputs
- Height: 44px
- Border: 1px solid #E2E8F0
- Border radius: 8px
- Focus: 2px accent (#00B4D8) outline, no border color change
- Label: 14px, font-weight 500, above input

### Badges
- Padding: 4px 12px
- Border radius: 16px (pill shape)
- Font: 12px, font-weight 500
- Colors: Use semantic colors (success green, warning amber, accent)

## Animation Rules

- **Scroll reveals**: GSAP ScrollTrigger — fade-up, 0.6s duration, ease: "power2.out"
- **Staggered fade-ins**: Use GSAP stagger: 0.1 for lists and grid items
- **Hover transitions**: 150ms ease, subtle scale (1.02) or brightness shift
- **Page transitions**: Fade, 0.3s
- **Avoid**: Bouncy springs, excessive motion, parallax

## Medical UI Rules

- **Clean**: Maximum 5 colors, ample white space, no visual clutter
- **Trustworthy**: Stable layouts, consistent spacing, professional typography
- **Professional**: No playful animations, no decorative elements
- **No dark patterns**: No hidden costs, no deceptive button placement
- **Accessibility**: WCAG AA contrast ratios, focusable elements, semantic HTML

## Anti-Patterns to Avoid

- ❌ Gradient soup (gradients on backgrounds or buttons)
- ❌ Neon accents or glow effects
- ❌ Oversized emojis or decorative icons
- ❌ Excessive shadows or glassmorphism
- ❌ Compact, dense layouts — prioritize readability
- ❌ Decorative animations that don't serve a purpose

## Responsive Behavior

- **Mobile-first**: Design for 320px first, then scale up
- **Breakpoints**:
  - Mobile: < 640px
  - Tablet: 640px - 1024px
  - Desktop: > 1024px
- **Touch targets**: Minimum 44px height on mobile
- **Sidebars**: Collapsible on mobile, fixed on desktop

## Implementation Notes

- Use CSS custom properties for all tokens
- Build a design tokens file to share across components
- Test with real medical data (patient names, appointment times, vital signs)
- Ensure forms work with keyboard navigation only
- Support reduced motion preference via `prefers-reduced-motion`