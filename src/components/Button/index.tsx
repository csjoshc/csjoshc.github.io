import React from "react";
import styles from "./styles.module.css";

interface ButtonProps {
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "outline";
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  className?: string;
  href?: string;
  onClick?: () => void;
  type?: "button" | "submit" | "reset";
}

export default function Button({
  children,
  variant = "primary",
  size = "md",
  disabled = false,
  className = "",
  href,
  onClick,
  type = "button",
}: ButtonProps) {
  const buttonClasses = [
    styles.btn,
    styles[`btn-${variant}`],
    styles[`btn-${size}`],
    disabled && styles.disabled,
    className,
  ]
    .filter(Boolean)
    .join(" ");

  const commonProps = {
    className: buttonClasses,
    disabled,
    "aria-disabled": disabled,
  };

  if (href && !disabled) {
    return (
      <a href={href} {...commonProps}>
        {children}
      </a>
    );
  }

  return (
    <button type={type} onClick={onClick} {...commonProps}>
      {children}
    </button>
  );
}
