import React from "react";
import Layout from "@theme/Layout";

export default function SearchPage(): JSX.Element {
  return (
    <Layout title="Search" description="Search the site">
      <main className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset--2">
            <h1>Search</h1>
            <p>
              Use the search bar in the navigation to find content on this site.
            </p>
          </div>
        </div>
      </main>
    </Layout>
  );
}
