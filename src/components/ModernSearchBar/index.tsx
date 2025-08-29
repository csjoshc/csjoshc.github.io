import React, { useState, useEffect, useRef } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useHistory } from "@docusaurus/router";
import styles from "./styles.module.css";

export default function ModernSearchBar(): JSX.Element {
  const [query, setQuery] = useState("");
  const [isFocused, setIsFocused] = useState(false);
  const { siteConfig } = useDocusaurusContext();
  const history = useHistory();
  const searchInputRef = useRef<HTMLInputElement>(null);

  // Add keyboard shortcut (Ctrl/Cmd + K) to focus search
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if ((event.ctrlKey || event.metaKey) && event.key === "k") {
        event.preventDefault();
        if (searchInputRef.current) {
          searchInputRef.current.focus();
        }
      }

      // Escape key to clear search and blur
      if (event.key === "Escape") {
        setQuery("");
        if (searchInputRef.current) {
          searchInputRef.current.blur();
        }
      }
    };

    document.addEventListener("keydown", handleKeyDown);
    return () => document.removeEventListener("keydown", handleKeyDown);
  }, []);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      // Navigate to search results page
      history.push(`/search?q=${encodeURIComponent(query.trim())}`);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
  };

  const handleFocus = () => {
    setIsFocused(true);
  };

  const handleBlur = () => {
    setIsFocused(false);
  };

  return (
    <div className={styles.searchContainer}>
      <form onSubmit={handleSearch} className={styles.searchForm}>
        <div className={`${styles.searchWrapper} ${isFocused ? styles.focused : ""}`}>
          <SearchIcon className={styles.searchIcon} />
          <input
            ref={searchInputRef}
            type="search"
            placeholder="Search or jump to..."
            value={query}
            onChange={handleInputChange}
            onFocus={handleFocus}
            onBlur={handleBlur}
            className={styles.searchInput}
            aria-label="Search"
          />
          <div className={styles.keyboardShortcut}>
            <kbd>⌘</kbd>
            <kbd>K</kbd>
          </div>
        </div>
      </form>
    </div>
  );
}

function SearchIcon({ className }: { className?: string }): JSX.Element {
  return (
    <svg
      className={className}
      width="16"
      height="16"
      viewBox="0 0 16 16"
      fill="currentColor"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        fillRule="evenodd"
        d="M10.442 10.442a.75.75 0 0 1 1.061 0l3.768 3.768a.75.75 0 0 1-1.061 1.061l-3.768-3.768a.75.75 0 0 1 0-1.061Z"
        clipRule="evenodd"
      />
      <path
        fillRule="evenodd"
        d="M6.5 12a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11ZM13 6.5a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0Z"
        clipRule="evenodd"
      />
    </svg>
  );
}
