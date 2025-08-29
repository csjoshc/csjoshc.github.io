import React from "react";
import styles from "./styles.module.css";

interface LayoutProps {
  children: React.ReactNode;
  className?: string;
  containerClassName?: string;
  maxWidth?: "sm" | "md" | "lg" | "xl" | "full";
  padding?: "none" | "sm" | "md" | "lg";
}

export default function Layout({
  children,
  className = "",
  containerClassName = "",
  maxWidth = "lg",
  padding = "md",
}: LayoutProps) {
  const layoutClasses = [
    styles.layout,
    styles[`max-width-${maxWidth}`],
    styles[`padding-${padding}`],
    className,
  ]
    .filter(Boolean)
    .join(" ");

  const containerClasses = [styles.container, containerClassName]
    .filter(Boolean)
    .join(" ");

  return (
    <div className={layoutClasses}>
      <div className={containerClasses}>{children}</div>
    </div>
  );
}
