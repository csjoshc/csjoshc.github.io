import React from 'react';
import { ChevronRight, BookOpen, FileText, FolderOpen } from 'lucide-react';
import { Button } from './ui/button';
import { ScrollArea } from './ui/scroll-area';

interface SidebarItem {
  label: string;
  to?: string;
  children?: SidebarItem[];
  isActive?: boolean;
  isExpanded?: boolean;
}

interface ModernSidebarProps {
  items: SidebarItem[];
  className?: string;
}

export default function ModernSidebar({ items, className = '' }: ModernSidebarProps) {
  const [expandedItems, setExpandedItems] = React.useState<Set<string>>(new Set());

  const toggleExpanded = (label: string) => {
    const newExpanded = new Set(expandedItems);
    if (newExpanded.has(label)) {
      newExpanded.delete(label);
    } else {
      newExpanded.add(label);
    }
    setExpandedItems(newExpanded);
  };

  const renderSidebarItem = (item: SidebarItem, depth: number = 0) => {
    const hasChildren = item.children && item.children.length > 0;
    const isExpanded = expandedItems.has(item.label);
    const isActive = item.isActive;

    return (
      <div key={item.label} className="w-full">
        <div className="flex items-center">
          {hasChildren ? (
            <Button
              variant="ghost"
              size="sm"
              className={`w-full justify-start text-left h-8 px-2 ${
                isActive ? 'bg-accent text-accent-foreground' : 'hover:bg-accent/50'
              }`}
              onClick={() => toggleExpanded(item.label)}
            >
              <FolderOpen className="w-4 h-4 mr-2 flex-shrink-0" />
              <span className="truncate">{item.label}</span>
              <ChevronRight 
                className={`w-4 h-4 ml-auto transition-transform ${
                  isExpanded ? 'rotate-90' : ''
                }`}
              />
            </Button>
          ) : (
            <Button
              variant="ghost"
              size="sm"
              className={`w-full justify-start text-left h-8 px-2 ${
                isActive ? 'bg-accent text-accent-foreground' : 'hover:bg-accent/50'
              }`}
              onClick={() => item.to && (window.location.href = item.to)}
            >
              <FileText className="w-4 h-4 mr-2 flex-shrink-0" />
              <span className="truncate">{item.label}</span>
            </Button>
          )}
        </div>
        
        {hasChildren && isExpanded && (
          <div className="ml-4 mt-1 space-y-1">
            {item.children!.map((child) => renderSidebarItem(child, depth + 1))}
          </div>
        )}
      </div>
    );
  };

  return (
    <div className={`w-full h-full ${className}`}>
      <div className="p-4 border-b border-border">
        <div className="flex items-center gap-2">
          <BookOpen className="w-5 h-5 text-primary" />
          <h2 className="text-lg font-semibold text-foreground">Navigation</h2>
        </div>
      </div>
      
      <ScrollArea className="h-[calc(100vh-120px)] p-4">
        <div className="space-y-1">
          {items.map((item) => renderSidebarItem(item))}
        </div>
      </ScrollArea>
    </div>
  );
}

// Enhanced sidebar wrapper for Docusaurus integration
export function EnhancedDocusaurusSidebar({ 
  children, 
  className = '' 
}: { 
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <div className={`theme-doc-sidebar-container ${className}`}>
      <div className="theme-doc-sidebar-menu">
        <div className="modern-sidebar-wrapper">
          {children}
        </div>
      </div>
    </div>
  );
}
