#!/usr/bin/env python3
"""
Test Site Updates Workflow
This script creates a minimal test example to verify the site updates workflow works correctly.
"""

import os
import shutil
import tempfile
from pathlib import Path
from datetime import datetime
import subprocess

def create_test_post():
    """Create a minimal test post for testing the workflow"""
    # Create test directory structure
    test_year = "9_2025"  # Future year to ensure it becomes the latest
    test_dir = Path("site_updates") / test_year
    test_dir.mkdir(exist_ok=True)

    # Create a simple test post
    test_date = "01_9_2025"  # September 1, 2025
    test_md_file = test_dir / f"{test_date}.md"

    test_content = f"""<a href="../../index.html">Go back to index</a>

<a href="../base.html">Go back to site update portal</a>

<head>

  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

# September 1, 2025 - Test Post

This is a test post to verify the site updates workflow.

## Testing Features

- Navigation links
- Latest post detection
- Proper ordering
- HTML conversion

**Test completed successfully!**
"""

    # Write the test file
    with open(test_md_file, 'w', encoding='utf-8') as f:
        f.write(test_content)

    print(f"✅ Created test post: {test_md_file}")
    return test_md_file

def run_build_workflow():
    """Run the complete build workflow"""
    print("\n🔨 Running build workflow...")

    # Change to site_updates directory and run build
    site_updates_dir = Path("site_updates")
    original_dir = os.getcwd()

    try:
        os.chdir(site_updates_dir)
        print("📝 Building site updates...")

        # Run build-site-updates.py
        result = subprocess.run(['python3', 'build-site-updates.py'],
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Build failed: {result.stderr}")
            return False

        print("✅ Site updates build completed")

        # Run update-latest-post-link.py
        result = subprocess.run(['python3', 'update-latest-post-link.py'],
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Update latest post failed: {result.stderr}")
            return False

        print("✅ Latest post links updated")

    finally:
        os.chdir(original_dir)

    return True

def verify_latest_post():
    """Verify that the test post is correctly identified as the latest"""
    print("\n🔍 Verifying latest post detection...")

    base_md = Path("site_updates/base.md")
    if not base_md.exists():
        print("❌ base.md not found")
        return False

    with open(base_md, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if our test post is marked as latest
    if "September 1, 2025" in content and "(Latest)" in content:
        print("✅ Test post correctly identified as latest")
        return True
    else:
        print("❌ Test post not identified as latest")
        print("Current content:")
        print(content)
        return False

def update_navigation_template():
    """Update the navigation template to link to the latest post"""
    print("\n📝 Updating navigation template...")

    nav_template = Path("docs/_templates/nav_site_updates.md")
    if not nav_template.exists():
        print("❌ Navigation template not found")
        return False

    # Read current template
    with open(nav_template, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update to link to the latest post (which should be our test post)
    new_content = content.replace(
        "📝 Site Updates",
        '<a href="../site_updates/base.html">📝 Site Updates</a>'
    )

    with open(nav_template, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ Navigation template updated")
    return True

def cleanup_test_post():
    """Clean up the test post"""
    test_dir = Path("site_updates/9_2025")
    if test_dir.exists():
        shutil.rmtree(test_dir)
        print("🧹 Test post cleaned up")

def main():
    """Main test function"""
    print("🧪 Testing Site Updates Workflow")
    print("=" * 40)

    try:
        # Step 1: Create test post
        print("\n1. Creating test post...")
        test_file = create_test_post()

        # Step 2: Run build workflow
        print("\n2. Running build workflow...")
        if not run_build_workflow():
            return False

        # Step 3: Verify latest post detection
        print("\n3. Verifying latest post...")
        if not verify_latest_post():
            return False

        # Step 4: Update navigation template
        print("\n4. Updating navigation template...")
        if not update_navigation_template():
            return False

        print("\n✅ All tests passed!")
        print("\n📋 Test Results:")
        print("- Test post created and detected as latest")
        print("- Build workflow completed successfully")
        print("- Navigation template updated")
        print("\n🎯 Next steps:")
        print("1. Run 'just build' to see the complete workflow")
        print("2. Check http://localhost:3000/docs/site_updates/base")
        print("3. Verify the 'Site Updates' button links correctly")

        return True

    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False

    finally:
        # Clean up test post
        print("\n5. Cleaning up...")
        cleanup_test_post()

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
