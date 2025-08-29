#!/usr/bin/env node

/**
 * Social Navigation Test Script
 *
 * Tests that GitHub and LinkedIn buttons have proper icons and responsive behavior
 */

const puppeteer = require("puppeteer");

const VIEWPORTS = {
  desktop: { width: 1200, height: 800 },
  narrow: { width: 800, height: 600 }, // Below 996px breakpoint
  mobile: { width: 375, height: 667 },
};

const TEST_URL = "http://localhost:3000";

async function testSocialNavigation() {
  console.log("🔗 Testing Social Navigation Implementation...\n");

  let browser;
  try {
    browser = await puppeteer.launch({
      headless: true,
      args: ["--no-sandbox", "--disable-setuid-sandbox"],
    });

    for (const [device, viewport] of Object.entries(VIEWPORTS)) {
      console.log(
        `📱 Testing ${device} (${viewport.width}x${viewport.height})`
      );

      const page = await browser.newPage();
      await page.setViewport(viewport);

      try {
        await page.goto(TEST_URL, {
          waitUntil: "networkidle0",
          timeout: 30000,
        });

        // Test GitHub button
        const githubTest = await testSocialButton(page, device, "github");
        console.log(`  ✅ GitHub: ${githubTest ? "PASS" : "FAIL"}`);

        // Test LinkedIn button
        const linkedinTest = await testSocialButton(page, device, "linkedin");
        console.log(`  ✅ LinkedIn: ${linkedinTest ? "PASS" : "FAIL"}`);

        // Test Search button
        const searchTest = await testSearchButton(page, device);
        console.log(`  ✅ Search: ${searchTest ? "PASS" : "FAIL"}`);

        // Test responsive behavior
        const responsiveTest = await testResponsiveBehavior(page, device);
        console.log(`  ✅ Responsive: ${responsiveTest ? "PASS" : "FAIL"}`);

        await page.close();
      } catch (error) {
        console.log(`  ❌ Error testing ${device}: ${error.message}`);
        await page.close();
      }
    }

    console.log("\n🎉 Social Navigation Tests Completed!");
  } catch (error) {
    console.error("❌ Test failed:", error.message);
  } finally {
    if (browser) {
      await browser.close();
    }
  }
}

async function testSocialButton(page, device, platform) {
  try {
    const selector = `.${platform}-nav-item`;
    const button = await page.$(selector);

    if (!button) {
      console.log(`    ⚠️  ${platform} button not found on ${device}`);
      return false;
    }

    // Check if icon exists
    const icon = await page.$(`${selector} .social-icon`);
    if (!icon) {
      console.log(`    ⚠️  ${platform} icon not found on ${device}`);
      return false;
    }

    // Check if link works (basic check)
    const href = await page.evaluate((el) => el.href, button);
    if (!href || !href.includes(platform)) {
      console.log(`    ⚠️  ${platform} link not working on ${device}`);
      return false;
    }

    // Check responsive text behavior
    if (device === "narrow" || device === "mobile") {
      const label = await page.$(`${selector} .social-label`);
      if (label) {
        const opacity = await page.evaluate(
          (el) => getComputedStyle(el).opacity,
          label
        );
        if (parseFloat(opacity) > 0.1) {
          console.log(
            `    ⚠️  ${platform} label should be hidden on ${device}`
          );
          return false;
        }
      }
    }

    return true;
  } catch (error) {
    console.log(
      `    ⚠️  ${platform} test error on ${device}: ${error.message}`
    );
    return false;
  }
}

async function testSearchButton(page, device) {
  try {
    const button = await page.$(".search-nav-item");

    if (!button) {
      console.log(`    ⚠️  Search button not found on ${device}`);
      return false;
    }

    // Check if icon exists
    const icon = await page.$(".search-nav-item .search-icon");
    if (!icon) {
      console.log(`    ⚠️  Search icon not found on ${device}`);
      return false;
    }

    // Check responsive behavior
    if (device === "narrow" || device === "mobile") {
      const labels = await page.$$(
        ".search-nav-item .search-label, .search-nav-item .search-shortcut"
      );

      for (const label of labels) {
        const isVisible = await page.evaluate((el) => {
          const style = getComputedStyle(el);
          const rect = el.getBoundingClientRect();
          return (
            style.display !== "none" &&
            style.visibility !== "hidden" &&
            parseFloat(style.opacity) > 0.1 &&
            rect.width > 0 &&
            rect.height > 0
          );
        }, label);

        if (isVisible) {
          console.log(
            `    ⚠️  Search label/shortcut should be hidden on ${device}`
          );
          return false;
        }
      }
    }

    return true;
  } catch (error) {
    console.log(`    ⚠️  Search test error on ${device}: ${error.message}`);
    return false;
  }
}

async function testResponsiveBehavior(page, device) {
  try {
    // Check that social items are visible in navbar (only count visible ones)
    const allSocialItems = await page.$$(".social-nav-item");
    const visibleSocialItems = [];

    for (const item of allSocialItems) {
      const isVisible = await page.evaluate((el) => {
        const style = getComputedStyle(el);
        return (
          style.display !== "none" &&
          style.visibility !== "hidden" &&
          style.opacity !== "0"
        );
      }, item);

      if (isVisible) {
        visibleSocialItems.push(item);
      }
    }

    console.log(
      `    📊 Found ${visibleSocialItems.length} visible social items on ${device} (from ${allSocialItems.length} total)`
    );

    // We expect exactly 2 visible social items (GitHub + LinkedIn)
    if (visibleSocialItems.length !== 2) {
      console.log(
        `    ⚠️  Expected 2 visible social items, found ${visibleSocialItems.length} on ${device}`
      );
      return false;
    }

    // Check that search is visible
    const searchItem = await page.$(".search-nav-item");
    if (!searchItem) {
      console.log(`    ⚠️  Search item not visible on ${device}`);
      return false;
    }

    // On narrow/mobile, check that mobile menu toggle exists
    if (device === "narrow" || device === "mobile") {
      const mobileToggle = await page.$(".mobile-menu-toggle");
      if (!mobileToggle) {
        console.log(`    ⚠️  Mobile menu toggle not found on ${device}`);
        return false;
      }

      // Check that social items are still in the top navbar (not moved to mobile menu)
      const navbarSocialItems = await page.$$(".navbar .social-nav-item");
      const visibleNavbarSocialItems = [];

      for (const item of navbarSocialItems) {
        const isVisible = await page.evaluate((el) => {
          const style = getComputedStyle(el);
          return (
            style.display !== "none" &&
            style.visibility !== "hidden" &&
            style.opacity !== "0"
          );
        }, item);

        if (isVisible) {
          visibleNavbarSocialItems.push(item);
        }
      }

      if (visibleNavbarSocialItems.length !== 2) {
        console.log(
          `    ⚠️  Expected 2 visible social items in navbar, found ${visibleNavbarSocialItems.length} on ${device}`
        );
        return false;
      }
    }

    return true;
  } catch (error) {
    console.log(`    ⚠️  Responsive test error on ${device}: ${error.message}`);
    return false;
  }
}

// Run the tests
if (require.main === module) {
  testSocialNavigation().catch(console.error);
}

module.exports = { testSocialNavigation };
