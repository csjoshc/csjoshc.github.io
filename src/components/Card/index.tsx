import React from "react";
import styles from "./styles.module.css";

interface CardProps {
  title?: string;
  children: React.ReactNode;
  className?: string;
  href?: string;
  onClick?: () => void;
}

export default function Card({
  title,
  children,
  className = "",
  href,
  onClick,
}: CardProps) {
  const cardContent = (
    <div className={`${styles.card} ${className}`}>
      {title && <div className={styles.cardHeader}>{title}</div>}
      <div className={styles.cardBody}>{children}</div>
    </div>
  );

  if (href) {
    return (
      <a href={href} className={styles.cardLink}>
        {cardContent}
      </a>
    );
  }

  if (onClick) {
    return (
      <button onClick={onClick} className={styles.cardButton}>
        {cardContent}
      </button>
    );
  }

  return cardContent;
}
