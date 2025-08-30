import React from 'react';
import { ThemeProvider } from './ThemeProvider';
import ResponsiveNav from './ResponsiveNav';

type RootLayoutProps = {
  children: React.ReactNode;
};

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <ThemeProvider defaultTheme="system" storageKey="csjoshc-theme">
      <div className="min-h-screen bg-background">
        <ResponsiveNav />
        <main className="flex-1">
          {children}
        </main>
      </div>
    </ThemeProvider>
  );
}
