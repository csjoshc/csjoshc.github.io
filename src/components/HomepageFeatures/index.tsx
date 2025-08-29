import type { ReactNode } from "react";
import clsx from "clsx";
import Heading from "@theme/Heading";
import Link from "@docusaurus/Link";
import styles from "./styles.module.css";

type FeatureItem = {
  title: string;
  description: ReactNode;
  link: string;
};

const FeatureList: FeatureItem[] = [
  {
    title: "Python",
    description: (
      <>
        Comprehensive Python learning materials covering data science, machine
        learning, and programming fundamentals with interactive Jupyter
        notebooks.
      </>
    ),
    link: "/docs/Python/base",
  },
  {
    title: "Interactive Learning",
    description: (
      <>
        Learn through hands-on examples and interactive content. All materials
        are organized and easy to navigate for self-paced learning.
      </>
    ),
    link: "/docs/Devops/roadmap_notes",
  },
  {
    title: "Site Updates",
    description: (
      <>
        Latest update: August 28, 2025. View the most recent site updates and changes.
      </>
    ),
    link: "/docs/site_updates/8_2025/28_8_2025",
  },
];

function Feature({ title, description, link }: FeatureItem) {
  return (
    <div className={clsx("col col--4")}>
      <Link
        to={link}
        className={styles.featureLink}
        aria-label={`Navigate to ${title} section`}
        role="button"
        tabIndex={0}
      >
        <div className="text--center padding-horiz--md">
          <Heading as="h3">{title}</Heading>
          <p>{description}</p>
        </div>
      </Link>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
