#!/usr/bin/env python3
"""
Clean emoji-based navigation elements from markdown files.

This script removes common emoji navigation patterns that can cause
MDX compilation issues or unwanted text-only div elements.
"""

import os
import re
import glob
from pathlib import Path

def clean_emoji_navigation(file_path):
    """Clean emoji navigation elements from a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Remove emoji navigation patterns
        # Pattern 1: Lines that are just emoji + text (like "🏠 Home")
        content = re.sub(r'^[🏠🐍📝⚙️🛠️🐙🐧📋⭐]*\s*[A-Za-z\s]+$', '', content, flags=re.MULTILINE)

        # Pattern 2: Navigation sections with emoji links
        content = re.sub(r'## Navigation\n\n(?:- \[🏠[^\]]*\]\([^\)]+\)\n)+', '', content, flags=re.MULTILINE)
        content = re.sub(r'## Navigation\n\n(?:- \[🐍[^\]]*\]\([^\)]+\)\n)+', '', content, flags=re.MULTILINE)

        # Pattern 3: Emoji headers (but preserve important ones like in frontmatter)
        # Only remove standalone emoji headers that are just navigation
        content = re.sub(r'^## [🏠🐍📝⚙️🛠️🐙🐧📋⭐]+\s*[A-Za-z\s]+$', '## Navigation', content, flags=re.MULTILINE)

        # Remove empty navigation sections
        content = re.sub(r'## Navigation\n\n##', '##', content)

        # Clean up multiple empty lines
        content = re.sub(r'\n\n\n+', '\n\n', content)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Cleaned: {file_path}")
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to clean all markdown files."""
    docs_dir = Path(__file__).parent.parent / 'docs'

    if not docs_dir.exists():
        print(f"Docs directory not found: {docs_dir}")
        return

    cleaned_count = 0

    # Find all markdown files
    for md_file in docs_dir.rglob('*.md'):
        if clean_emoji_navigation(md_file):
            cleaned_count += 1

    print(f"Processed {cleaned_count} files with emoji navigation cleanup")

if __name__ == '__main__':
    main()
