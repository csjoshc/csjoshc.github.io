import React from "react";
import Layout from "@theme-original/Layout";
import type LayoutType from "@theme/Layout";
import type { WrapperProps } from "@docusaurus/types";
import { ThemeProvider } from "../../components/ThemeProvider";
import ResponsiveNav from "../../components/ResponsiveNav";

type Props = WrapperProps<typeof LayoutType>;

export default function LayoutWrapper(props: Props): React.ReactElement {
  return (
    <ThemeProvider defaultTheme="system" storageKey="csjoshc-theme">
      <div className="min-h-screen bg-background">
        <ResponsiveNav />
        <Layout {...props} />
      </div>
    </ThemeProvider>
  );
}
