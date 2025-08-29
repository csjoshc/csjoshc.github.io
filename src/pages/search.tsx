import React from "react";
import Layout from "@theme/Layout";
import ModernSearchBar from "../components/ModernSearchBar";

export default function SearchPage(): JSX.Element {
  return (
    <Layout title="Search" description="Search the site">
      <main className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset--2">
            <h1>Search</h1>
            <div style={{ marginBottom: "2rem" }}>
              <ModernSearchBar />
            </div>
            <p>Use the search bar above to find content on this site.</p>
          </div>
        </div>
      </main>
    </Layout>
  );
}
