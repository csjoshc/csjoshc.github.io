#!/usr/bin/env node

/**
 * Debug Navbar Elements Script
 *
 * Helps debug what navbar elements are present and their classes
 */

const puppeteer = require("puppeteer");

const VIEWPORTS = {
  desktop: { width: 1200, height: 800 },
  narrow: { width: 800, height: 600 },
  mobile: { width: 375, height: 667 },
};

const TEST_URL = "http://localhost:3000";

async function debugNavbar() {
  console.log("🔍 Debugging Navbar Elements...\n");

  let browser;
  try {
    browser = await puppeteer.launch({
      headless: true,
      args: ["--no-sandbox", "--disable-setuid-sandbox"],
    });

    for (const [device, viewport] of Object.entries(VIEWPORTS)) {
      console.log(`📱 ${device} (${viewport.width}x${viewport.height})`);

      const page = await browser.newPage();
      await page.setViewport(viewport);

      try {
        await page.goto(TEST_URL, {
          waitUntil: "networkidle0",
          timeout: 30000,
        });

        // Debug all navbar items
        const navbarItems = await page.$$(
          ".navbar__item, .navbar__link, .social-nav-item, .search-nav-item"
        );
        console.log(`  📊 Total navbar elements: ${navbarItems.length}`);

        for (let i = 0; i < navbarItems.length; i++) {
          const classes = await page.evaluate(
            (el) => el.className,
            navbarItems[i]
          );
          const text = await page.evaluate(
            (el) => el.textContent?.trim() || "",
            navbarItems[i]
          );
          console.log(`    ${i + 1}. Classes: "${classes}" | Text: "${text}"`);
        }

        // Debug social items specifically
        const socialItems = await page.$$(".social-nav-item");
        console.log(`  🔗 Social items: ${socialItems.length}`);

        for (let i = 0; i < socialItems.length; i++) {
          const classes = await page.evaluate(
            (el) => el.className,
            socialItems[i]
          );
          const text = await page.evaluate(
            (el) => el.textContent?.trim() || "",
            socialItems[i]
          );
          console.log(`    ${i + 1}. Classes: "${classes}" | Text: "${text}"`);
        }

        // Debug search item
        const searchItem = await page.$(".search-nav-item");
        if (searchItem) {
          const searchClasses = await page.evaluate(
            (el) => el.className,
            searchItem
          );
          const searchText = await page.evaluate(
            (el) => el.textContent?.trim() || "",
            searchItem
          );
          console.log(
            `  🔍 Search item: Classes: "${searchClasses}" | Text: "${searchText}"`
          );

          // Check if labels are hidden
          const labels = await page.$$(
            ".search-nav-item .search-label, .search-nav-item .search-shortcut"
          );
          console.log(`  📝 Search labels found: ${labels.length}`);
          for (let i = 0; i < labels.length; i++) {
            const labelText = await page.evaluate(
              (el) => el.textContent?.trim() || "",
              labels[i]
            );
            const opacity = await page.evaluate(
              (el) => getComputedStyle(el).opacity,
              labels[i]
            );
            console.log(
              `    Label ${i + 1}: "${labelText}" | Opacity: ${opacity}`
            );
          }
        } else {
          console.log(`  ❌ Search item not found`);
        }

        console.log("");

        await page.close();
      } catch (error) {
        console.log(`  ❌ Error on ${device}: ${error.message}`);
        await page.close();
      }
    }

    console.log("🎉 Debug Complete!");
  } catch (error) {
    console.error("❌ Debug failed:", error.message);
  } finally {
    if (browser) {
      await browser.close();
    }
  }
}

// Run the debug
if (require.main === module) {
  debugNavbar().catch(console.error);
}

module.exports = { debugNavbar };
