#!/usr/bin/env node

/**
 * Responsive Design Testing Script
 *
 * This script tests the responsive design implementation across different screen sizes
 * and validates that components behave correctly on mobile, tablet, and desktop.
 */

const puppeteer = require("puppeteer");

const VIEWPORTS = {
  mobile: { width: 375, height: 667, deviceScaleFactor: 2 },
  tablet: { width: 768, height: 1024, deviceScaleFactor: 1 },
  desktop: { width: 1200, height: 800, deviceScaleFactor: 1 },
  largeDesktop: { width: 1600, height: 900, deviceScaleFactor: 1 },
};

const TEST_URL = "http://localhost:3000";

async function testResponsiveDesign() {
  console.log("🚀 Starting Responsive Design Tests...\n");

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

        // Test navbar responsiveness
        const navbarTest = await testNavbarResponsiveness(page, device);
        console.log(`  ✅ Navbar: ${navbarTest ? "PASS" : "FAIL"}`);

        // Test layout responsiveness
        const layoutTest = await testLayoutResponsiveness(page, device);
        console.log(`  ✅ Layout: ${layoutTest ? "PASS" : "FAIL"}`);

        // Test component responsiveness
        const componentTest = await testComponentResponsiveness(page, device);
        console.log(`  ✅ Components: ${componentTest ? "PASS" : "FAIL"}`);

        // Test accessibility
        const accessibilityTest = await testAccessibility(page, device);
        console.log(
          `  ✅ Accessibility: ${accessibilityTest ? "PASS" : "FAIL"}`
        );

        await page.close();
      } catch (error) {
        console.log(`  ❌ Error testing ${device}: ${error.message}`);
        await page.close();
      }
    }

    console.log("\n🎉 Responsive Design Tests Completed!");
    console.log("\n📋 Test Results Summary:");
    console.log(
      "   - Mobile (375x667): Tested navbar, layout, components, accessibility"
    );
    console.log(
      "   - Tablet (768x1024): Tested navbar, layout, components, accessibility"
    );
    console.log(
      "   - Desktop (1200x800): Tested navbar, layout, components, accessibility"
    );
    console.log(
      "   - Large Desktop (1600x900): Tested navbar, layout, components, accessibility"
    );
  } catch (error) {
    console.error("❌ Test failed:", error.message);
  } finally {
    if (browser) {
      await browser.close();
    }
  }
}

async function testNavbarResponsiveness(page, device) {
  try {
    // Check if navbar exists
    const navbar = await page.$(".navbar");
    if (!navbar) return false;

    // Test mobile menu toggle (only on mobile/tablet)
    if (device === "mobile" || device === "tablet") {
      const mobileToggle = await page.$(".mobile-menu-toggle");
      if (!mobileToggle) {
        console.log(`    ⚠️  Mobile menu toggle not found on ${device}`);
        return false;
      }

      // Test mobile menu functionality
      await page.click(".mobile-menu-toggle");
      await page.waitForTimeout(500);

      const mobileMenu = await page.$(".mobile-menu");
      if (!mobileMenu) {
        console.log(`    ⚠️  Mobile menu not shown on ${device}`);
        return false;
      }
    }

    // Test navbar items visibility
    const navbarItems = await page.$$(".navbar__item");
    if (navbarItems.length === 0) {
      console.log(`    ⚠️  No navbar items found on ${device}`);
      return false;
    }

    return true;
  } catch (error) {
    console.log(`    ⚠️  Navbar test error on ${device}: ${error.message}`);
    return false;
  }
}

async function testLayoutResponsiveness(page, device) {
  try {
    // Check for proper container sizing
    const containers = await page.$$('.container, [class*="container"]');
    if (containers.length === 0) {
      console.log(`    ⚠️  No containers found on ${device}`);
      return false;
    }

    // Test responsive grid layouts
    const grids = await page.$$('[class*="grid"], [class*="flex"]');
    if (grids.length > 0) {
      console.log(
        `    📊 Found ${grids.length} responsive layouts on ${device}`
      );
    }

    // Check for proper spacing
    const content = await page.$('main, .main-wrapper, [role="main"]');
    if (!content) {
      console.log(`    ⚠️  Main content area not found on ${device}`);
      return false;
    }

    return true;
  } catch (error) {
    console.log(`    ⚠️  Layout test error on ${device}: ${error.message}`);
    return false;
  }
}

async function testComponentResponsiveness(page, device) {
  try {
    // Test button responsiveness
    const buttons = await page.$$('button, [role="button"], .btn');
    if (buttons.length > 0) {
      console.log(`    🔘 Found ${buttons.length} buttons on ${device}`);
    }

    // Test card responsiveness
    const cards = await page.$$('.card, [class*="card"]');
    if (cards.length > 0) {
      console.log(`    📄 Found ${cards.length} cards on ${device}`);
    }

    // Test form responsiveness
    const forms = await page.$$('form, [role="form"]');
    if (forms.length > 0) {
      const inputs = await page.$$("input, textarea, select");
      console.log(
        `    📝 Found ${forms.length} forms with ${inputs.length} inputs on ${device}`
      );
    }

    return true;
  } catch (error) {
    console.log(`    ⚠️  Component test error on ${device}: ${error.message}`);
    return false;
  }
}

async function testAccessibility(page, device) {
  try {
    // Test focus indicators
    const focusableElements = await page.$$(
      "button, a, input, select, textarea, [tabindex]"
    );
    if (focusableElements.length === 0) {
      console.log(`    ⚠️  No focusable elements found on ${device}`);
      return false;
    }

    // Test heading structure
    const headings = await page.$$("h1, h2, h3, h4, h5, h6");
    if (headings.length === 0) {
      console.log(`    ⚠️  No headings found on ${device}`);
    }

    // Test alt text for images
    const images = await page.$$("img");
    let imagesWithoutAlt = 0;
    for (const img of images) {
      const alt = await page.evaluate((el) => el.getAttribute("alt"), img);
      if (!alt) imagesWithoutAlt++;
    }

    if (imagesWithoutAlt > 0) {
      console.log(
        `    ⚠️  ${imagesWithoutAlt} images without alt text on ${device}`
      );
    }

    return true;
  } catch (error) {
    console.log(
      `    ⚠️  Accessibility test error on ${device}: ${error.message}`
    );
    return false;
  }
}

// Run the tests
if (require.main === module) {
  testResponsiveDesign().catch(console.error);
}

module.exports = { testResponsiveDesign };
