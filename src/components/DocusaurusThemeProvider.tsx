import React, { createContext, useContext, useEffect, useState } from "react";

type Theme = "dark" | "light" | "system";

type DocusaurusThemeProviderProps = {
  children: React.ReactNode;
  defaultTheme?: Theme;
  storageKey?: string;
};

type DocusaurusThemeProviderState = {
  theme: Theme;
  setTheme: (theme: Theme) => void;
};

const initialState: DocusaurusThemeProviderState = {
  theme: "system",
  setTheme: () => null,
};

const DocusaurusThemeProviderContext =
  createContext<DocusaurusThemeProviderState>(initialState);

export function DocusaurusThemeProvider({
  children,
  defaultTheme = "system",
  storageKey = "csjoshc-theme",
  ...props
}: DocusaurusThemeProviderProps) {
  const [theme, setTheme] = useState<Theme>(() => {
    // Check localStorage first
    const stored = localStorage.getItem(storageKey) as Theme;
    if (stored && ["dark", "light", "system"].includes(stored)) {
      return stored;
    }

    // Check Docusaurus theme preference
    const docusaurusTheme = document.documentElement.getAttribute("data-theme");
    if (docusaurusTheme === "dark" || docusaurusTheme === "light") {
      return docusaurusTheme;
    }

    return defaultTheme;
  });

  useEffect(() => {
    const root = window.document.documentElement;
    const docusaurusRoot = window.document.documentElement;

    // Remove existing theme classes
    root.classList.remove("light", "dark");
    docusaurusRoot.classList.remove("theme-light", "theme-dark");

    if (theme === "system") {
      const systemTheme = window.matchMedia("(prefers-color-scheme: dark)")
        .matches
        ? "dark"
        : "light";

      root.classList.add(systemTheme);
      docusaurusRoot.classList.add(`theme-${systemTheme}`);
      return;
    }

    // Apply theme to both our system and Docusaurus
    root.classList.add(theme);
    docusaurusRoot.classList.add(`theme-${theme}`);

    // Update Docusaurus theme attribute
    docusaurusRoot.setAttribute("data-theme", theme);
  }, [theme]);

  // Listen for Docusaurus theme changes
  useEffect(() => {
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (
          mutation.type === "attributes" &&
          mutation.attributeName === "data-theme"
        ) {
          const docusaurusTheme =
            document.documentElement.getAttribute("data-theme");
          if (docusaurusTheme && docusaurusTheme !== theme) {
            setTheme(docusaurusTheme as Theme);
          }
        }
      });
    });

    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-theme"],
    });

    return () => observer.disconnect();
  }, [theme]);

  const value = {
    theme,
    setTheme: (newTheme: Theme) => {
      localStorage.setItem(storageKey, newTheme);
      setTheme(newTheme);
    },
  };

  return (
    <DocusaurusThemeProviderContext.Provider {...props} value={value}>
      {children}
    </DocusaurusThemeProviderContext.Provider>
  );
}

export const useDocusaurusTheme = () => {
  const context = useContext(DocusaurusThemeProviderContext);

  if (context === undefined)
    throw new Error(
      "useDocusaurusTheme must be used within a DocusaurusThemeProvider"
    );

  return context;
};

// Hook to sync with Docusaurus theme system
export const useDocusaurusThemeSync = () => {
  const { theme, setTheme } = useDocusaurusTheme();

  useEffect(() => {
    // Sync with Docusaurus theme toggle if it exists
    const docusaurusToggle = document.querySelector("[data-theme-toggle]");
    if (docusaurusToggle) {
      const handleDocusaurusToggle = () => {
        const currentTheme =
          document.documentElement.getAttribute("data-theme");
        if (currentTheme && currentTheme !== theme) {
          setTheme(currentTheme as Theme);
        }
      };

      docusaurusToggle.addEventListener("click", handleDocusaurusToggle);
      return () =>
        docusaurusToggle.removeEventListener("click", handleDocusaurusToggle);
    }
  }, [theme, setTheme]);

  return { theme, setTheme };
};
