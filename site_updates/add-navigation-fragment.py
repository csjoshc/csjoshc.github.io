#!/usr/bin/env python3
"""
Add Navigation Fragment to Site Updates Markdown Files
This script adds the standard navigation fragment to all .md files in site_updates
"""

import os
import re
from pathlib import Path

def add_navigation_fragment(file_path):
    """Add navigation fragment to a markdown file if it doesn't already have it"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if navigation fragment already exists
    if '<a href="../../index.html">Go back to index</a>' in content:
        print(f"  ✅ {file_path.name} already has navigation fragment")
        return False
    
    # Create navigation fragment based on file depth
    relative_depth = len(file_path.parts) - 1  # site_updates is depth 0
    
    if relative_depth == 1:  # Directly in site_updates
        nav_fragment = '''<a href="../index.html">Go back to index</a>

<a href="base.html">Go back to site update portal</a>

<head>
  
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

'''
    elif relative_depth == 2:  # In year subdirectory
        nav_fragment = '''<a href="../../index.html">Go back to index</a>

<a href="../base.html">Go back to site update portal</a>

<head>
  
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

'''
    else:  # Deeper nesting
        nav_fragment = '''<a href="../../../index.html">Go back to index</a>

<a href="../../base.html">Go back to site update portal</a>

<head>
  
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

'''
    
    # Add navigation fragment at the beginning
    new_content = nav_fragment + content
    
    # Write the updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✅ Added navigation fragment to {file_path.name}")
    return True

def process_directory(directory):
    """Process all .md files in a directory and its subdirectories"""
    directory_path = Path(directory)
    md_files = list(directory_path.rglob('*.md'))
    
    if not md_files:
        print(f"No .md files found in {directory}")
        return
    
    print(f"Found {len(md_files)} .md files in {directory}")
    
    updated_count = 0
    for md_file in md_files:
        if add_navigation_fragment(md_file):
            updated_count += 1
    
    print(f"\nUpdated {updated_count} out of {len(md_files)} files")

def main():
    """Main function"""
    print("🔧 Adding navigation fragments to site updates markdown files...")
    
    # Process the site_updates directory
    process_directory('site_updates')
    
    print("\n✅ Navigation fragment addition complete!")

if __name__ == "__main__":
    main()
