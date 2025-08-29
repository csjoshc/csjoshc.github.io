import React, { createContext, useContext, useState, useEffect } from "react";
import SearchModal from "../SearchModal";

interface SearchContextType {
  isSearchOpen: boolean;
  openSearch: () => void;
  closeSearch: () => void;
}

const SearchContext = createContext<SearchContextType | undefined>(undefined);

export function useSearch(): SearchContextType {
  const context = useContext(SearchContext);
  if (context === undefined) {
    throw new Error("useSearch must be used within a SearchProvider");
  }
  return context;
}

interface SearchProviderProps {
  children: React.ReactNode;
}

export default function SearchProvider({
  children,
}: SearchProviderProps): JSX.Element {
  const [isSearchOpen, setIsSearchOpen] = useState(false);

  const openSearch = () => setIsSearchOpen(true);
  const closeSearch = () => setIsSearchOpen(false);

  // Handle global keyboard shortcuts
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      // Open search with Cmd+K (Mac) or Ctrl+K (Windows/Linux)
      if ((event.metaKey || event.ctrlKey) && event.key === "k") {
        event.preventDefault();
        setIsSearchOpen(true);
      }
    };

    document.addEventListener("keydown", handleKeyDown);

    // Expose openSearch function globally for HTML navbar item
    (window as any).openSearch = openSearch;

    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      delete (window as any).openSearch;
    };
  }, [openSearch]);

  const value: SearchContextType = {
    isSearchOpen,
    openSearch,
    closeSearch,
  };

  return (
    <SearchContext.Provider value={value}>
      {children}
      <SearchModal isOpen={isSearchOpen} onClose={closeSearch} />
    </SearchContext.Provider>
  );
}
