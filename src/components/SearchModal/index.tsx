import React, { useState, useEffect, useRef, useCallback } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useHistory } from "@docusaurus/router";
import styles from "./styles.module.css";

interface SearchModalProps {
  isOpen: boolean;
  onClose: () => void;
}

interface SearchResult {
  id: string;
  title: string;
  description: string;
  url: string;
  type: "page" | "doc" | "blog" | "tutorial";
  tags: string[];
  lastModified?: string;
  relevance: number;
}

export default function SearchModal({
  isOpen,
  onClose,
}: SearchModalProps): React.JSX.Element | null {
  const [query, setQuery] = useState("");
  const [isFocused, setIsFocused] = useState(false);
  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  const [isSearching, setIsSearching] = useState(false);
  const [searchHistory, setSearchHistory] = useState<string[]>([]);
  const { siteConfig } = useDocusaurusContext();
  const history = useHistory();
  const searchInputRef = useRef<HTMLInputElement>(null);
  const modalRef = useRef<HTMLDivElement>(null);
  const searchTimeoutRef = useRef<NodeJS.Timeout>();

  // Focus search input when modal opens
  useEffect(() => {
    if (isOpen && searchInputRef.current) {
      searchInputRef.current.focus();
      setIsFocused(true);
    }
  }, [isOpen]);

  // Handle escape key to close modal
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        onClose();
      }
    };

    if (isOpen) {
      document.addEventListener("keydown", handleKeyDown);
      // Prevent body scroll when modal is open
      document.body.style.overflow = "hidden";
    }

    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      document.body.style.overflow = "unset";
    };
  }, [isOpen, onClose]);

  // Handle click outside modal to close
  const handleBackdropClick = (event: React.MouseEvent) => {
    if (event.target === modalRef.current) {
      onClose();
    }
  };

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) {
      // For now, navigate to search page with query
      // Later we can implement inline search results
      history.push(`/search?q=${encodeURIComponent(query.trim())}`);
      onClose();
    }
  };

  // Define performSearch function first
  const performSearch = useCallback(
    async (searchQuery: string) => {
      try {
        // Simulate search API call - in real implementation, this would call your search backend
        const results = await searchContent(searchQuery);

        setSearchResults(results);

        // Add to search history
        if (searchQuery && !searchHistory.includes(searchQuery)) {
          setSearchHistory((prev) => [searchQuery, ...prev.slice(0, 9)]);
        }
      } catch (error) {
        console.error("Search failed:", error);
        setSearchResults([]);
      } finally {
        setIsSearching(false);
      }
    },
    [searchHistory]
  );

  // Real-time search with debouncing
  useEffect(() => {
    if (searchTimeoutRef.current) {
      clearTimeout(searchTimeoutRef.current);
    }

    if (query.trim().length > 2) {
      setIsSearching(true);
      searchTimeoutRef.current = setTimeout(() => {
        performSearch(query.trim());
      }, 300);
    } else {
      setSearchResults([]);
      setIsSearching(false);
    }

    return () => {
      if (searchTimeoutRef.current) {
        clearTimeout(searchTimeoutRef.current);
      }
    };
  }, [query, performSearch]);

  const searchContent = async (query: string): Promise<SearchResult[]> => {
    // Real client-side search through actual page content
    const searchQuery = query.toLowerCase();
    const results: SearchResult[] = [];

    try {
      // Search through all navigation links and page content
      const searchableElements = document.querySelectorAll(
        'a[href^="/docs/"], a[href^="/"], h1, h2, h3, h4, h5, h6, p, li'
      );

      const processedUrls = new Set<string>();

      searchableElements.forEach((element) => {
        const text = element.textContent?.toLowerCase() || "";
        const href = (element as HTMLAnchorElement).href;

        if (text.includes(searchQuery) && href && !processedUrls.has(href)) {
          processedUrls.add(href);

          // Extract title from heading or link text
          let title = "";
          let description = "";

          if (element.tagName.match(/^H[1-6]$/)) {
            title = element.textContent || "";
            // Get next paragraph or list item for description
            const nextElement = element.nextElementSibling;
            if (
              nextElement &&
              (nextElement.tagName === "P" || nextElement.tagName === "LI")
            ) {
              description = nextElement.textContent || "";
            }
          } else if (element.tagName === "A") {
            title = element.textContent || "";
            // Get parent heading for context
            const parentHeading = element.closest("h1, h2, h3, h4, h5, h6");
            if (parentHeading) {
              description = parentHeading.textContent || "";
            }
          }

          if (title && title.length > 3) {
            // Calculate relevance based on match quality
            let relevance = 0;
            if (title.toLowerCase().includes(searchQuery)) relevance += 0.6;
            if (description.toLowerCase().includes(searchQuery))
              relevance += 0.3;
            if (href.includes(searchQuery)) relevance += 0.1;

            // Determine content type
            let type: "page" | "doc" | "blog" | "tutorial" = "page";
            if (href.includes("/docs/")) type = "doc";
            if (href.includes("/blog/")) type = "blog";
            if (href.includes("/tutorial/")) type = "tutorial";

            // Extract tags from URL path
            const pathParts = href.split("/").filter((part) => part.length > 0);
            const tags = pathParts.slice(1, 4); // Take up to 3 path segments as tags

            results.push({
              id: href,
              title: title.trim(),
              description: description.trim() || `Content from ${href}`,
              url: href,
              type,
              tags,
              relevance: Math.min(relevance, 1.0),
            });
          }
        }
      });

      // Sort by relevance and limit results
      return results.sort((a, b) => b.relevance - a.relevance).slice(0, 8);
    } catch (error) {
      console.error("Client-side search failed:", error);
      return [];
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
  };

  const handleFocus = () => setIsFocused(true);
  const handleBlur = () => setIsFocused(false);

  if (!isOpen) return null;

  return (
    <div
      className={styles.modalOverlay}
      ref={modalRef}
      onClick={handleBackdropClick}
    >
      <div className={styles.modalContent}>
        <div className={styles.searchHeader}>
          <SearchIcon className={styles.searchIcon} />
          <form onSubmit={handleSearch} className={styles.searchForm}>
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
          </form>
          <button
            onClick={onClose}
            className={styles.closeButton}
            aria-label="Close search"
          >
            <CloseIcon />
          </button>
        </div>

        <div className={styles.searchResults}>
          {query ? (
            <>
              {isSearching ? (
                <div className={styles.searchingIndicator}>
                  <div className={styles.spinner}></div>
                  <p>Searching...</p>
                </div>
              ) : searchResults.length > 0 ? (
                <div className={styles.resultsList}>
                  {searchResults.map((result) => (
                    <div key={result.id} className={styles.resultItem}>
                      <div className={styles.resultHeader}>
                        <h4 className={styles.resultTitle}>
                          <a href={result.url} onClick={() => onClose()}>
                            {result.title}
                          </a>
                        </h4>
                        <span className={styles.resultType}>{result.type}</span>
                      </div>
                      <p className={styles.resultDescription}>
                        {result.description}
                      </p>
                      <div className={styles.resultMeta}>
                        <div className={styles.resultTags}>
                          {result.tags.map((tag) => (
                            <span key={tag} className={styles.resultTag}>
                              {tag}
                            </span>
                          ))}
                        </div>
                        <span className={styles.resultRelevance}>
                          {Math.round(result.relevance * 100)}% match
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className={styles.noResults}>
                  <p>
                    No results found for "<strong>{query}</strong>"
                  </p>
                  <p>Try different keywords or check your spelling</p>
                </div>
              )}
            </>
          ) : (
            <div className={styles.searchTips}>
              <h3>Search Tips</h3>
              <ul>
                <li>Use keywords to find specific content</li>
                <li>Try searching for programming concepts</li>
                <li>Look for course names or topics</li>
              </ul>
              {searchHistory.length > 0 && (
                <div className={styles.searchHistory}>
                  <h4>Recent Searches</h4>
                  <div className={styles.historyItems}>
                    {searchHistory.map((term, index) => (
                      <button
                        key={index}
                        className={styles.historyItem}
                        onClick={() => setQuery(term)}
                      >
                        {term}
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>

        <div className={styles.keyboardShortcuts}>
          <div className={styles.shortcut}>
            <kbd>⌘</kbd> + <kbd>K</kbd> to open search
          </div>
          <div className={styles.shortcut}>
            <kbd>Esc</kbd> to close
          </div>
        </div>
      </div>
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

function CloseIcon(): JSX.Element {
  return (
    <svg
      width="16"
      height="16"
      viewBox="0 0 16 16"
      fill="currentColor"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.75.75 0 1 1 1.06 1.06L9.06 8l3.22 3.22a.75.75 0 1 1-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 0 1-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z" />
    </svg>
  );
}
