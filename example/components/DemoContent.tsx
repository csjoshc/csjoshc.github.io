import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';

export default function DemoContent() {
  return (
    <div className="container mx-auto px-4 py-8 space-y-8">
      {/* Hero Section */}
      <div className="text-center space-y-4">
        <h1 className="text-4xl lg:text-6xl font-bold text-foreground">
          csjoshc.github.io
        </h1>
        <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
          Docusaurus-inspired responsive navigation demonstration with custom behaviors
        </p>
      </div>

      {/* Feature Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Dynamic Labels</CardTitle>
            <CardDescription>
              Navigation labels change based on screen size
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              At 996px breakpoint, navigation items switch from full labels to icon-only mode while maintaining functionality.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Persistent Elements</CardTitle>
            <CardDescription>
              Social links and search stay visible on mobile
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              Unlike standard mobile navigation, social icons and search remain accessible on the main navigation bar.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Custom Dropdown</CardTitle>
            <CardDescription>
              Hamburger menu drops below navigation
            </CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              The mobile menu appears below the main navigation instead of overlaying it, maintaining visibility of persistent elements.
            </p>
          </CardContent>
        </Card>
      </div>

      {/* Technical Specifications */}
      <Card>
        <CardHeader>
          <CardTitle>Technical Specifications</CardTitle>
          <CardDescription>
            Implementation details for the responsive navigation
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <h4 className="font-medium mb-2">Breakpoint</h4>
              <p className="text-sm text-muted-foreground">
                996px (Docusaurus standard) - lg: prefix in Tailwind
              </p>
            </div>
            <div>
              <h4 className="font-medium mb-2">Mobile Behavior</h4>
              <p className="text-sm text-muted-foreground">
                Non-overlay dropdown maintains main nav visibility
              </p>
            </div>
            <div>
              <h4 className="font-medium mb-2">Responsive Elements</h4>
              <p className="text-sm text-muted-foreground">
                Home, GitHub, LinkedIn buttons with dynamic labels
              </p>
            </div>
            <div>
              <h4 className="font-medium mb-2">Persistent Features</h4>
              <p className="text-sm text-muted-foreground">
                Search bar and social icons remain accessible
              </p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Testing Instructions */}
      <Card>
        <CardHeader>
          <CardTitle>Testing the Navigation</CardTitle>
          <CardDescription>
            How to verify the responsive behavior
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-sm font-medium">
                1
              </div>
              <div>
                <p className="font-medium">Resize Browser Window</p>
                <p className="text-sm text-muted-foreground">
                  Drag the browser window to test the 996px breakpoint behavior
                </p>
              </div>
            </div>
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-sm font-medium">
                2
              </div>
              <div>
                <p className="font-medium">Observe Label Changes</p>
                <p className="text-sm text-muted-foreground">
                  Watch how "Site Home", "GitHub", and "LinkedIn" labels appear/disappear
                </p>
              </div>
            </div>
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-sm font-medium">
                3
              </div>
              <div>
                <p className="font-medium">Test Mobile Menu</p>
                <p className="text-sm text-muted-foreground">
                  Click the hamburger menu to see the custom dropdown behavior
                </p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}