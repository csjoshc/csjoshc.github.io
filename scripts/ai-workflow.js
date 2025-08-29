#!/usr/bin/env node

/**
 * AI Interaction Workflow
 *
 * Comprehensive workflow for AI-assisted development that includes:
 * 1. Validation and testing
 * 2. Cleanup of temporary artifacts
 * 3. Git commit with descriptive messages
 */

const { execSync, spawn } = require("child_process");
const fs = require("fs");
const path = require("path");

class AIWorkflow {
  constructor() {
    this.changes = [];
    this.tempFiles = [];
    this.commitMessage = "";
  }

  /**
   * Step 1: Validate changes with tests
   */
  async validateChanges() {
    console.log("🔍 Step 1: Validating Changes...\n");

    try {
      // Run build test
      console.log("📦 Testing build...");
      execSync("npm run build", { stdio: "inherit" });
      console.log("✅ Build successful\n");

      // Run social navigation test
      console.log("🔗 Testing social navigation...");
      execSync("node scripts/test-social-nav.js", { stdio: "inherit" });
      console.log("✅ Social navigation test passed\n");

      // Run responsive design test
      console.log("📱 Testing responsive design...");
      execSync("node scripts/test-responsive-design.js", { stdio: "inherit" });
      console.log("✅ Responsive design test completed\n");

      console.log("🎉 All validations passed!\n");
      return true;
    } catch (error) {
      console.error("❌ Validation failed:", error.message);
      return false;
    }
  }

  /**
   * Step 2: Cleanup temporary artifacts
   */
  async cleanupArtifacts() {
    console.log("🧹 Step 2: Cleaning up temporary artifacts...\n");

    const tempPatterns = [
      // Debug scripts (keep for development but clean old ones)
      "scripts/debug-*.js",
      // Temporary test files
      "*.tmp",
      "*.temp",
      // Build artifacts that shouldn't be committed
      "build/",
      ".docusaurus/",
      // Cache files
      ".cache/",
      "node_modules/.cache/",
      // Log files
      "*.log",
      // OS files
      ".DS_Store",
      "Thumbs.db",
    ];

    let cleanedCount = 0;

    for (const pattern of tempPatterns) {
      try {
        const files = this.glob(pattern);
        for (const file of files) {
          if (fs.existsSync(file)) {
            // Only remove if it's not in .gitignore or if it's truly temporary
            const isIgnored = this.isGitIgnored(file);
            if (isIgnored || file.includes(".tmp") || file.includes(".temp")) {
              fs.unlinkSync(file);
              console.log(`  🗑️  Removed: ${file}`);
              cleanedCount++;
            }
          }
        }
      } catch (error) {
        // Ignore errors for files that don't exist
      }
    }

    // Clean empty directories
    this.cleanEmptyDirs("scripts/");
    this.cleanEmptyDirs("src/components/");

    console.log(`✅ Cleaned up ${cleanedCount} temporary files\n`);
  }

  /**
   * Step 3: Analyze changes and create commit
   */
  async analyzeAndCommit(message) {
    console.log("📝 Step 3: Analyzing changes and creating commit...\n");

    try {
      // Check git status
      const status = execSync("git status --porcelain", { encoding: "utf8" });
      if (!status.trim()) {
        console.log("ℹ️  No changes to commit\n");
        return true;
      }

      console.log("📋 Changes detected:");
      console.log(status);

      // Analyze the changes
      const changes = this.analyzeChanges(status);

      // Create descriptive commit message
      const commitMessage = message || this.generateCommitMessage(changes);

      // Stage and commit
      console.log("📦 Staging files...");
      execSync("git add .", { stdio: "inherit" });

      console.log("💾 Creating commit...");
      execSync(`git commit -m "${commitMessage}"`, { stdio: "inherit" });

      console.log("✅ Changes committed successfully!");
      console.log(`📝 Commit message: ${commitMessage}\n`);

      return true;
    } catch (error) {
      console.error("❌ Commit failed:", error.message);
      return false;
    }
  }

  /**
   * Main workflow execution
   */
  async execute(message = "") {
    console.log("🚀 Starting AI Interaction Workflow...\n");

    const steps = [
      { name: "Validation", method: this.validateChanges.bind(this) },
      { name: "Cleanup", method: this.cleanupArtifacts.bind(this) },
      { name: "Commit", method: () => this.analyzeAndCommit(message) },
    ];

    let success = true;

    for (const step of steps) {
      try {
        console.log(`\n${"=".repeat(50)}`);
        console.log(`Step: ${step.name}`);
        console.log(`${"=".repeat(50)}\n`);

        const result = await step.method();
        if (!result) {
          success = false;
          break;
        }
      } catch (error) {
        console.error(`❌ ${step.name} failed:`, error.message);
        success = false;
        break;
      }
    }

    console.log(`\n${"=".repeat(50)}`);
    if (success) {
      console.log("🎉 AI Interaction Workflow Completed Successfully!");
      console.log("📊 Summary:");
      console.log("   ✅ Validation passed");
      console.log("   ✅ Cleanup completed");
      console.log("   ✅ Changes committed");
    } else {
      console.log("❌ AI Interaction Workflow Failed");
    }
    console.log(`${"=".repeat(50)}\n`);

    return success;
  }

  // Helper methods
  glob(pattern) {
    // Simple glob implementation for common patterns
    const files = [];

    if (pattern.includes("*")) {
      const dir = pattern.split("*")[0];
      if (fs.existsSync(dir)) {
        const items = fs.readdirSync(dir);
        for (const item of items) {
          if (item.includes(pattern.split("*")[1] || "")) {
            files.push(path.join(dir, item));
          }
        }
      }
    } else if (fs.existsSync(pattern)) {
      files.push(pattern);
    }

    return files;
  }

  isGitIgnored(file) {
    try {
      execSync(`git check-ignore "${file}"`, { stdio: "pipe" });
      return true;
    } catch {
      return false;
    }
  }

  cleanEmptyDirs(dir) {
    if (!fs.existsSync(dir)) return;

    const items = fs.readdirSync(dir);
    for (const item of items) {
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);

      if (stat.isDirectory()) {
        this.cleanEmptyDirs(fullPath);
        // Check if directory is now empty
        try {
          const remaining = fs.readdirSync(fullPath);
          if (remaining.length === 0) {
            fs.rmdirSync(fullPath);
            console.log(`  🗑️  Removed empty directory: ${fullPath}`);
          }
        } catch {
          // Directory might have been removed already
        }
      }
    }
  }

  analyzeChanges(status) {
    const changes = {
      added: [],
      modified: [],
      deleted: [],
      renamed: [],
    };

    const lines = status.split("\n").filter((line) => line.trim());

    for (const line of lines) {
      const status = line.substring(0, 2);
      const file = line.substring(3);

      if (status[0] === "A" || status[1] === "A") {
        changes.added.push(file);
      } else if (status[0] === "M" || status[1] === "M") {
        changes.modified.push(file);
      } else if (status[0] === "D" || status[1] === "D") {
        changes.deleted.push(file);
      } else if (status[0] === "R" || status[1] === "R") {
        changes.renamed.push(file);
      }
    }

    return changes;
  }

  generateCommitMessage(changes) {
    const parts = [];

    if (changes.added.length > 0) {
      parts.push(`Add ${changes.added.length} file(s)`);
    }

    if (changes.modified.length > 0) {
      parts.push(`Update ${changes.modified.length} file(s)`);
    }

    if (changes.deleted.length > 0) {
      parts.push(`Remove ${changes.deleted.length} file(s)`);
    }

    if (changes.renamed.length > 0) {
      parts.push(`Rename ${changes.renamed.length} file(s)`);
    }

    // Add context based on file types
    const allFiles = [...changes.added, ...changes.modified];
    const categories = this.categorizeFiles(allFiles);

    if (categories.css > 0) {
      parts.push(`${categories.css} CSS file(s)`);
    }

    if (categories.js > 0) {
      parts.push(`${categories.js} JS file(s)`);
    }

    if (categories.react > 0) {
      parts.push(`${categories.react} React component(s)`);
    }

    if (categories.test > 0) {
      parts.push(`${categories.test} test file(s)`);
    }

    return parts.join(", ") || "Update files";
  }

  categorizeFiles(files) {
    const categories = {
      css: 0,
      js: 0,
      react: 0,
      test: 0,
      other: 0,
    };

    for (const file of files) {
      if (file.endsWith(".css")) {
        categories.css++;
      } else if (file.endsWith(".js") || file.endsWith(".ts")) {
        categories.js++;
      } else if (file.endsWith(".tsx") || file.endsWith(".jsx")) {
        categories.react++;
      } else if (file.includes("test") || file.includes("spec")) {
        categories.test++;
      } else {
        categories.other++;
      }
    }

    return categories;
  }
}

// CLI interface
if (require.main === module) {
  const args = process.argv.slice(2);
  const message = args.join(" ") || "";

  const workflow = new AIWorkflow();
  workflow.execute(message).then((success) => {
    process.exit(success ? 0 : 1);
  });
}

module.exports = AIWorkflow;
