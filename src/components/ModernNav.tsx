import React, { useState, useEffect } from "react";
import {
  Search,
  Menu,
  X,
  Github,
  Linkedin,
  Home,
  BookOpen,
  Server,
  Code,
} from "lucide-react";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { ThemeToggle } from "./ThemeToggle";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useLocation } from "@docusaurus/router";

export default function ModernNav() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const { siteConfig } = useDocusaurusContext();
  const location = useLocation();

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  // Close mobile menu when route changes
  useEffect(() => {
    setIsMobileMenuOpen(false);
  }, [location]);

  const navigationItems = [
    {
      to: "/docs/Python/base",
      label: "Python",
      icon: <Code className="w-4 h-4" />,
    },
    {
      to: "/docs/Devops/roadmap_notes",
      label: "DevOps",
      icon: <Server className="w-4 h-4" />,
    },
    {
      to: "/docs/General/base",
      label: "General",
      icon: <BookOpen className="w-4 h-4" />,
    },
    {
      to: "/docs/Linux/base",
      label: "Linux",
      icon: <Server className="w-4 h-4" />,
    },
    {
      to: "/docs/Github/intro_gh",
      label: "GitHub",
      icon: <Github className="w-4 h-4" />,
    },
  ];

  return (
    <nav className="w-full bg-background border-b border-border sticky top-0 z-50">
      {/* Main Navigation Bar */}
      <div className="w-full px-4 lg:px-6">
        <div className="flex items-center justify-between h-16">
          {/* Left Section - Logo/Home */}
          <div className="flex items-center">
            <Button
              variant="ghost"
              className="flex items-center gap-2 px-3 text-lg font-bold"
              onClick={() => (window.location.href = "/")}
            >
              <Home className="w-5 h-5" />
              <span className="hidden lg:block">{siteConfig.title}</span>
            </Button>
          </div>

          {/* Center Section - Main Nav Links (hidden on mobile) */}
          <div className="hidden lg:flex items-center space-x-2">
            {navigationItems.map((item) => (
              <Button
                key={item.to}
                variant="ghost"
                className="flex items-center gap-2"
                onClick={() => (window.location.href = item.to)}
              >
                {item.icon}
                {item.label}
              </Button>
            ))}
          </div>

          {/* Right Section - Social Links, Search, and Mobile Menu */}
          <div className="flex items-center gap-2 lg:gap-4">
            {/* Social Links */}
            <Button
              variant="ghost"
              className="flex items-center gap-2 px-3"
              onClick={() =>
                window.open("https://github.com/csjoshc", "_blank")
              }
            >
              <Github className="w-5 h-5" />
              <span className="hidden lg:block">GitHub</span>
            </Button>

            <Button
              variant="ghost"
              className="flex items-center gap-2 px-3"
              onClick={() =>
                window.open("https://linkedin.com/in/csjoshc", "_blank")
              }
            >
              <Linkedin className="w-5 h-5" />
              <span className="hidden lg:block">LinkedIn</span>
            </Button>

            {/* Search Bar */}
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

            {/* Mobile Menu Button */}
            <Button
              variant="ghost"
              size="icon"
              className="lg:hidden"
              onClick={toggleMobileMenu}
            >
              {isMobileMenuOpen ? (
                <X className="w-5 h-5" />
              ) : (
                <Menu className="w-5 h-5" />
              )}
            </Button>
          </div>
        </div>
      </div>

      {/* Mobile Dropdown Menu */}
      {isMobileMenuOpen && (
        <div className="lg:hidden bg-background border-t border-border">
          <div className="px-4 py-2 space-y-1">
            {navigationItems.map((item) => (
              <Button
                key={item.to}
                variant="ghost"
                className="w-full justify-start text-left flex items-center gap-3"
                onClick={() => (window.location.href = item.to)}
              >
                {item.icon}
                {item.label}
              </Button>
            ))}
          </div>
        </div>
      )}
    </nav>
  );
}
