import React from "react";
import Layout from "@theme/Layout";
import ModernLanding from "../components/ModernLanding";

export default function Home(): React.JSX.Element {
  return (
    <Layout
      title="Welcome to Josh's demo site"
      description="Continually evolving with my learning journey"
    >
      <ModernLanding />
    </Layout>
  );
}
