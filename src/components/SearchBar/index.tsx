import React, { useState, useEffect } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useHistory } from "@docusaurus/router";
import styles from "./styles.module.css";

export default function SearchBar(): JSX.Element {
  const [query, setQuery] = useState("");
  const [isVisible, setIsVisible] = useState(false);
  const { siteConfig } = useDocusaurusContext();
  const history = useHistory();

  // Add keyboard shortcut (Ctrl/Cmd + K) to focus search
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if ((event.ctrlKey || event.metaKey) && event.key === "k") {
        event.preventDefault();
        const searchInput = document.querySelector(
          `.${styles.searchInput}`
        ) as HTMLInputElement;
        if (searchInput) {
          searchInput.focus();
        }
      }

      // Escape key to clear search
      if (event.key === "Escape") {
        setQuery("");
        const searchInput = document.querySelector(
          `.${styles.searchInput}`
        ) as HTMLInputElement;
        if (searchInput) {
          searchInput.blur();
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
    setIsVisible(e.target.value.length > 0);
  };

  return (
    <div className={styles.searchBarContainer}>
      <form onSubmit={handleSearch} className={styles.searchForm}>
        <input
          type="search"
          placeholder="Search learning content... (Ctrl+K)"
          value={query}
          onChange={handleInputChange}
          className={styles.searchInput}
          aria-label="Search"
        />
        <button
          type="submit"
          className={styles.searchButton}
          aria-label="Search"
        >
          <SearchIcon />
        </button>
      </form>

      {/* Keyboard shortcut hint */}
      <div className={styles.keyboardHint}>
        <kbd>Ctrl</kbd> + <kbd>K</kbd>
      </div>
    </div>
  );
}

function SearchIcon(): JSX.Element {
  return (
    <svg
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
