import React, { useState, useEffect } from "react";
import styles from "./styles.module.css";

interface SearchAnalyticsProps {
  searchTerm: string;
  resultsCount: number;
  searchTime: number;
}

interface SearchStats {
  totalSearches: number;
  popularTerms: { term: string; count: number }[];
  averageResults: number;
  averageSearchTime: number;
}

export default function SearchAnalytics({
  searchTerm,
  resultsCount,
  searchTime,
}: SearchAnalyticsProps): JSX.Element {
  const [stats, setStats] = useState<SearchStats>({
    totalSearches: 0,
    popularTerms: [],
    averageResults: 0,
    averageSearchTime: 0,
  });

  useEffect(() => {
    // Load search statistics from localStorage
    loadSearchStats();
  }, []);

  useEffect(() => {
    // Update stats when search is performed
    if (searchTerm) {
      updateSearchStats(searchTerm, resultsCount, searchTime);
    }
  }, [searchTerm, resultsCount, searchTime]);

  const loadSearchStats = () => {
    try {
      const stored = localStorage.getItem("searchAnalytics");
      if (stored) {
        setStats(JSON.parse(stored));
      }
    } catch (error) {
      console.error("Failed to load search stats:", error);
    }
  };

  const updateSearchStats = (term: string, count: number, time: number) => {
    try {
      const newStats = { ...stats };

      // Update total searches
      newStats.totalSearches += 1;

      // Update popular terms
      const existingTerm = newStats.popularTerms.find((t) => t.term === term);
      if (existingTerm) {
        existingTerm.count += 1;
      } else {
        newStats.popularTerms.push({ term, count: 1 });
      }

      // Sort popular terms by count
      newStats.popularTerms.sort((a, b) => b.count - a.count);
      newStats.popularTerms = newStats.popularTerms.slice(0, 10); // Keep top 10

      // Update averages
      newStats.averageResults = Math.round(
        (newStats.averageResults * (newStats.totalSearches - 1) + count) /
          newStats.totalSearches
      );
      newStats.averageSearchTime = Math.round(
        (newStats.averageSearchTime * (newStats.totalSearches - 1) + time) /
          newStats.totalSearches
      );

      setStats(newStats);
      localStorage.setItem("searchAnalytics", JSON.stringify(newStats));
    } catch (error) {
      console.error("Failed to update search stats:", error);
    }
  };

  if (!searchTerm) return null;

  return (
    <div className={styles.analyticsContainer}>
      <div className={styles.searchMetrics}>
        <div className={styles.metric}>
          <span className={styles.metricLabel}>Results:</span>
          <span className={styles.metricValue}>{resultsCount}</span>
        </div>
        <div className={styles.metric}>
          <span className={styles.metricLabel}>Time:</span>
          <span className={styles.metricValue}>{searchTime}ms</span>
        </div>
      </div>

      <div className={styles.globalStats}>
        <h4>Search Statistics</h4>
        <div className={styles.statsGrid}>
          <div className={styles.statItem}>
            <span className={styles.statValue}>{stats.totalSearches}</span>
            <span className={styles.statLabel}>Total Searches</span>
          </div>
          <div className={styles.statItem}>
            <span className={styles.statValue}>{stats.averageResults}</span>
            <span className={styles.statLabel}>Avg Results</span>
          </div>
          <div className={styles.statItem}>
            <span className={styles.statValue}>
              {stats.averageSearchTime}ms
            </span>
            <span className={styles.statLabel}>Avg Time</span>
          </div>
        </div>

        {stats.popularTerms.length > 0 && (
          <div className={styles.popularTerms}>
            <h5>Popular Search Terms</h5>
            <div className={styles.termsList}>
              {stats.popularTerms.slice(0, 5).map((term, index) => (
                <div key={index} className={styles.termItem}>
                  <span className={styles.termText}>{term.term}</span>
                  <span className={styles.termCount}>{term.count}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
