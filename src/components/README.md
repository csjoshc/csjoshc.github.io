# Component Library

This directory contains reusable React components built following Docusaurus best practices and modern CSS methodologies.

## Architecture

### CSS Organization

The CSS is organized into modular files for maintainability:

- **`utilities.css`** - CSS custom properties, utility classes, and responsive utilities
- **`components.css`** - Reusable component styles (buttons, cards, forms, etc.)
- **`custom.css`** - Main CSS file that imports modular files and provides global overrides

### Component Structure

Each component follows a consistent pattern:

```
ComponentName/
├── index.tsx          # Main component file
├── styles.module.css  # Component-specific styles
└── README.md         # Component documentation (optional)
```

## Available Components

### Button Component

A versatile button component with multiple variants and sizes.

```tsx
import Button from '@site/src/components/Button';

// Basic usage
<Button>Click me</Button>

// With variants
<Button variant="primary">Primary</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="outline">Outline</Button>

// With sizes
<Button size="sm">Small</Button>
<Button size="md">Medium</Button>
<Button size="lg">Large</Button>

// As link
<Button href="/docs">Go to Docs</Button>

// With click handler
<Button onClick={() => console.log('clicked')}>Action</Button>
```

**Props:**

- `children`: ReactNode - Button content
- `variant`: 'primary' | 'secondary' | 'outline' - Button style variant
- `size`: 'sm' | 'md' | 'lg' - Button size
- `disabled`: boolean - Disable button interaction
- `className`: string - Additional CSS classes
- `href`: string - Convert to link
- `onClick`: () => void - Click handler
- `type`: 'button' | 'submit' | 'reset' - Button type

### Card Component

A flexible card component for displaying content.

```tsx
import Card from '@site/src/components/Card';

// Basic card
<Card>
  <p>Card content goes here</p>
</Card>

// Card with title
<Card title="Card Title">
  <p>Card content with a title</p>
</Card>

// Card as link
<Card title="Clickable Card" href="/docs">
  <p>This card is a link</p>
</Card>

// Card with click handler
<Card title="Interactive Card" onClick={() => alert('Clicked!')}>
  <p>This card responds to clicks</p>
</Card>
```

**Props:**

- `title`: string - Card header title
- `children`: ReactNode - Card content
- `className`: string - Additional CSS classes
- `href`: string - Convert to link
- `onClick`: () => void - Click handler

## CSS Best Practices

### 1. CSS Custom Properties (Variables)

Use CSS custom properties for consistent theming:

```css
/* Colors */
--ifm-color-primary: #0969da;
--text-primary: #24292f;
--border-light: #e1e4e8;

/* Spacing */
--ifm-spacing-xs: 0.25rem;
--ifm-spacing-sm: 0.5rem;
--ifm-spacing-md: 1rem;

/* Responsive breakpoints */
--breakpoint-mobile: 996px;
--breakpoint-tablet: 768px;
--breakpoint-desktop: 1200px;
```

### 2. Mobile-First Responsive Design

Always design for mobile first, then enhance for larger screens:

```css
/* Mobile styles */
.component {
  padding: var(--ifm-spacing-sm);
}

/* Tablet and up */
@media (min-width: 768px) {
  .component {
    padding: var(--ifm-spacing-md);
  }
}

/* Desktop and up */
@media (min-width: 996px) {
  .component {
    padding: var(--ifm-spacing-lg);
  }
}
```

### 3. CSS Modules

Use CSS modules for component-specific styles:

```css
/* styles.module.css */
.component {
  background: var(--ifm-background-color);
  border-radius: var(--ifm-radius-md);
}

.component:hover {
  transform: translateY(-2px);
}
```

### 4. Dark Mode Support

Always provide dark mode variants:

```css
.component {
  background: var(--ifm-background-color);
  color: var(--text-primary);
}

[data-theme="dark"] .component {
  /* Dark mode specific styles */
  background: var(--ifm-background-color);
}
```

### 5. Focus and Accessibility

Ensure proper focus states and accessibility:

```css
.component:focus {
  outline: 2px solid var(--ifm-color-primary);
  outline-offset: 2px;
}

.component:focus-visible {
  outline: 2px solid var(--ifm-color-primary);
  outline-offset: 2px;
}
```

## Responsive Breakpoints

Following Docusaurus conventions:

- **Mobile**: < 996px (default)
- **Tablet**: 768px - 995px
- **Desktop**: ≥ 996px
- **Large Desktop**: ≥ 1200px

## Utility Classes

Common utility classes are available in `utilities.css`:

### Spacing

- `.m-0`, `.mt-1`, `.mb-2`, `.ml-3`, `.mr-4`
- `.p-0`, `.pt-1`, `.pb-2`, `.pl-3`, `.pr-4`
- `.mx-auto`, `.my-2`

### Display

- `.d-none`, `.d-block`, `.d-flex`, `.d-inline-flex`
- `.d-md-none`, `.d-lg-block` (responsive)

### Flexbox

- `.justify-content-center`, `.justify-content-between`
- `.align-items-center`, `.align-items-start`

### Colors

- `.text-primary`, `.text-secondary`, `.text-muted`
- `.bg-primary`, `.bg-light`

### Borders and Shadows

- `.border`, `.border-top`, `.border-none`
- `.rounded`, `.rounded-sm`, `.rounded-lg`
- `.shadow-sm`, `.shadow-md`, `.shadow-lg`

## Component Development Guidelines

### 1. Component Structure

```tsx
interface ComponentProps {
  // Define props interface
  children?: React.ReactNode;
  className?: string;
  // ... other props
}

export default function Component({
  children,
  className = "",
  ...props
}: ComponentProps) {
  return <div className={`${styles.component} ${className}`}>{children}</div>;
}
```

### 2. CSS Module Naming

Use BEM-like naming convention:

```css
/* styles.module.css */
.component {
}
.component__header {
}
.component__body {
}
.component--large {
}
.component--disabled {
}
```

### 3. Prop Handling

```tsx
// Good: Allow customization
function Component({ className = "", style, ...props }) {
  return (
    <div
      className={`${styles.component} ${className}`}
      style={style}
      {...props}
    >
      {/* content */}
    </div>
  );
}
```

### 4. TypeScript Support

Always use TypeScript for type safety:

```tsx
interface ButtonProps {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "outline";
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  onClick?: () => void;
}
```

## Testing Components

Test components across different screen sizes and themes:

```tsx
// Example test
describe("Button", () => {
  it("renders correctly", () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole("button")).toBeInTheDocument();
  });

  it("handles click events", () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    fireEvent.click(screen.getByRole("button"));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
});
```

## Performance Considerations

### 1. CSS Optimization

- Use CSS custom properties instead of hardcoded values
- Minimize CSS specificity conflicts
- Use CSS modules to avoid global scope pollution

### 2. Component Optimization

- Use React.memo for expensive components
- Avoid unnecessary re-renders
- Use lazy loading for heavy components

### 3. Bundle Size

- Import only what you need
- Use tree shaking friendly imports
- Consider code splitting for large components

## Contributing

When adding new components:

1. Follow the established file structure
2. Include comprehensive TypeScript types
3. Provide CSS modules for styling
4. Add responsive design support
5. Include accessibility features
6. Write documentation and examples
7. Test across different screen sizes and themes

## Migration Guide

To migrate existing components to this new structure:

1. Create the component directory structure
2. Move component logic to `index.tsx`
3. Extract styles to `styles.module.css`
4. Update imports throughout the codebase
5. Test thoroughly for regressions
