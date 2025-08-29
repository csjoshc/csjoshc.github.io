import type { ReactNode } from "react";
import clsx from "clsx";
import Layout from "@theme/Layout";
import HomepageFeatures from "@site/src/components/HomepageFeatures";
import Heading from "@theme/Heading";

import styles from "./index.module.css";

function HomepageHeader() {
  return (
    <header className={clsx("hero hero--primary", styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          Welcome
        </Heading>
        <p className="hero__subtitle">A Portfolio and Blogging Platform</p>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout
      title="Welcome - Portfolio and Blogging Platform"
      description="A comprehensive learning platform covering Python, DevOps, and various technical topics with interactive content and resources."
    >
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
