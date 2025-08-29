# Social Navigation Implementation

## Overview

The social navigation feature adds GitHub and LinkedIn buttons to the navbar with the following behavior:

- **Wide screens (>996px)**: Shows both icons and text labels
- **Narrow screens (≤996px)**: Shows only icons, text labels are hidden
- **Mobile menu**: Social buttons remain in the top navbar (not moved to mobile menu)

## Implementation Details

### Navbar Configuration

The social navigation items are defined in `docusaurus.config.ts`:

```typescript
{
  type: "html",
  position: "right",
  value: `<a href="https://github.com/csjoshc/csjoshc.github.io"
           class="social-nav-item github-nav-item"
           aria-label="GitHub" title="Visit GitHub">
           <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor">
             <!-- GitHub SVG path -->
           </svg>
           <span class="social-label">GitHub</span>
         </a>`
}
```

### CSS Styling

Social navigation items are styled in `src/css/components.css`:

```css
.social-nav-item {
  display: inline-flex;
  align-items: center;
  gap: var(--ifm-spacing-sm);
  /* ... base styling */
}

.social-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

/* Responsive behavior */
@media (max-width: 996px) {
  .social-label {
    opacity: 0;
    width: 0;
    margin: 0;
    overflow: hidden;
  }

  .social-nav-item {
    gap: 0;
    padding: var(--ifm-spacing-sm);
    min-width: 44px;
    justify-content: center;
  }
}
```

### Responsive Behavior

1. **Desktop (>996px)**:

   - Full buttons with icons and text
   - Hover effects with background color changes
   - Proper spacing and alignment

2. **Tablet/Narrow (≤996px)**:

   - Icons remain visible
   - Text labels are hidden with `opacity: 0` and `width: 0`
   - Buttons maintain touch-friendly 44px minimum size
   - Smooth transitions between states

3. **Mobile Menu**:
   - Social buttons stay in top navbar
   - Not moved to mobile hamburger menu
   - Maintain consistent positioning with search button

## Accessibility Features

- **ARIA labels**: `aria-label="GitHub"` and `aria-label="LinkedIn"`
- **Titles**: Descriptive tooltips on hover
- **Focus management**: Proper focus indicators
- **Keyboard navigation**: Full keyboard support
- **Screen reader support**: Semantic HTML structure

## Customization

### Adding New Social Platforms

1. Add to `docusaurus.config.ts`:

```typescript
{
  type: "html",
  position: "right",
  value: `<a href="YOUR_URL" class="social-nav-item YOUR_PLATFORM-nav-item">
           <svg class="social-icon"><!-- Your SVG --></svg>
           <span class="social-label">Your Platform</span>
         </a>`
}
```

2. Add platform-specific styling in `src/css/components.css`:

```css
.YOUR_PLATFORM-nav-item .social-icon {
  color: YOUR_BRAND_COLOR;
}
```

### Adjusting Breakpoints

Modify the responsive breakpoint in CSS:

```css
/* Change from 996px to 768px for example */
@media (max-width: 768px) {
  .social-label {
    opacity: 0;
    width: 0;
    /* ... */
  }
}
```

## Testing

Test the implementation with:

```bash
# Test social navigation specifically
just test-social-nav

# Run all tests including social navigation
just test-all
```

The test script validates:

- Icons are present and visible
- Links work correctly
- Responsive text hiding works
- Accessibility features are implemented
- Buttons remain in navbar on narrow screens

## Browser Support

- **Modern browsers**: Full feature support
- **IE11**: Limited support (no CSS custom properties)
- **Mobile browsers**: Full support with touch optimization

## Performance Considerations

- **Minimal CSS**: Efficient selectors and properties
- **Optimized SVGs**: Inline SVG icons for better performance
- **Smooth transitions**: Hardware-accelerated animations
- **Bundle size**: Minimal impact on overall bundle

## Troubleshooting

### Icons Not Showing

- Check SVG paths are valid
- Verify `viewBox` attribute is correct
- Ensure `fill="currentColor"` for theme support

### Text Not Hiding on Narrow Screens

- Check CSS media query breakpoint
- Verify `.social-label` class is applied
- Test with browser dev tools responsive mode

### Buttons Moving to Mobile Menu

- Check responsive navbar CSS overrides
- Ensure `.social-nav-item` has proper `display: inline-flex !important`
- Verify responsive breakpoint matches

## Future Enhancements

- **Icon animations**: Hover animations for icons
- **Custom icons**: Support for custom social platform icons
- **Theme variants**: Different icon styles for light/dark themes
- **Analytics**: Click tracking for social navigation
- **Progressive enhancement**: Fallback for no-JS environments
