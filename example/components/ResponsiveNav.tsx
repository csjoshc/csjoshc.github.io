import React, { useState } from 'react';
import { Search, Menu, X, Github, Linkedin, Home } from 'lucide-react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { ThemeToggle } from './ThemeToggle';

export default function ResponsiveNav() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <nav className="w-full bg-background border-b border-border sticky top-0 z-50">
      {/* Main Navigation Bar */}
      <div className="w-full px-4 lg:px-6">
        <div className="flex items-center justify-between h-16">
          {/* Left Section - Home */}
          <div className="flex items-center">
            <Button variant="ghost" className="flex items-center gap-2 px-3">
              <Home className="w-5 h-5" />
              <span className="hidden lg:block">Site Home</span>
            </Button>
          </div>

          {/* Center Section - Main Nav Links (hidden on mobile) */}
          <div className="hidden lg:flex items-center space-x-8">
            <Button variant="ghost">Research</Button>
            <Button variant="ghost">Publications</Button>
            <Button variant="ghost">Projects</Button>
            <Button variant="ghost">Teaching</Button>
            <Button variant="ghost">About</Button>
          </div>

          {/* Right Section - Social Links, Search, and Mobile Menu */}
          <div className="flex items-center gap-2 lg:gap-4">
            {/* Social Links - Always visible but with responsive labels */}
            <Button 
              variant="ghost" 
              className="flex items-center gap-2 px-3"
              onClick={() => window.open('https://github.com/csjoshc', '_blank')}
            >
              <Github className="w-5 h-5" />
              <span className="hidden lg:block">GitHub</span>
            </Button>
            
            <Button 
              variant="ghost" 
              className="flex items-center gap-2 px-3"
              onClick={() => window.open('https://linkedin.com/in/csjoshc', '_blank')}
            >
              <Linkedin className="w-5 h-5" />
              <span className="hidden lg:block">LinkedIn</span>
            </Button>

            {/* Search Bar - Always visible but responsive sizing */}
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-muted-foreground" />
              <Input
                type="search"
                placeholder="Search..."
                className="pl-10 w-32 lg:w-64 h-9 bg-input-background"
              />
            </div>

            {/* Theme Toggle */}
            <ThemeToggle />

            {/* Mobile Menu Button - Only visible on mobile */}
            <Button
              variant="ghost"
              size="icon"
              className="lg:hidden"
              onClick={toggleMobileMenu}
            >
              {isMobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </Button>
          </div>
        </div>
      </div>

      {/* Mobile Dropdown Menu - Appears below main nav, not as overlay */}
      {isMobileMenuOpen && (
        <div className="lg:hidden bg-background border-t border-border">
          <div className="px-4 py-2 space-y-1">
            <Button variant="ghost" className="w-full justify-start text-left">
              Research
            </Button>
            <Button variant="ghost" className="w-full justify-start text-left">
              Publications
            </Button>
            <Button variant="ghost" className="w-full justify-start text-left">
              Projects
            </Button>
            <Button variant="ghost" className="w-full justify-start text-left">
              Teaching
            </Button>
            <Button variant="ghost" className="w-full justify-start text-left">
              About
            </Button>
          </div>
        </div>
      )}
    </nav>
  );
}