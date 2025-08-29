import React from "react";
import type { Props } from "@theme/Root";
import SearchProvider from "../../components/SearchProvider";

export default function Root({ children }: Props): JSX.Element {
  return (
    <SearchProvider>
      {children}
    </SearchProvider>
  );
}
