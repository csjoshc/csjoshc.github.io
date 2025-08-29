#!/usr/bin/env python3
"""
Update Latest Post Link - Build Process Integration
This script updates the main site updates page to point to the most recent post
and embeds the JavaScript directly into the HTML during the build process.
"""

import os
import re
from pathlib import Path
from datetime import datetime
import argparse

def find_latest_post():
    """Find the most recent post by scanning the directory structure"""
    site_updates_dir = Path('.')
    latest_post = None
    latest_date = None
    
    # Find all year directories (directories that contain years)
    year_dirs = []
    for item in site_updates_dir.iterdir():
        if item.is_dir():
            # Extract year from directory names like "3_2019", "8_2025"
            year_match = re.search(r'_(\d{4})$', item.name)
            if year_match:
                year = year_match.group(1)
                year_dirs.append((int(year), item.name))
    
    # Sort year directories (newest first)
    year_dirs.sort(key=lambda x: x[0], reverse=True)
    
    # Find the most recent post in the newest year
    for year, year_dir in year_dirs:
        year_path = site_updates_dir / year_dir
        
        # Find all HTML and MD files in the year directory
        for file_path in year_path.glob('*.html'):
            post_info = extract_post_info(file_path)
            if post_info and (latest_date is None or post_info['date'] > latest_date):
                latest_post = post_info
                latest_date = post_info['date']
        
        for file_path in year_path.glob('*.md'):
            post_info = extract_post_info(file_path)
            if post_info and (latest_date is None or post_info['date'] > latest_date):
                latest_post = post_info
                latest_date = post_info['date']
        
        # Only check the first (newest) year
        break
    
    return latest_post

def extract_post_info(filepath):
    """Extract post information from a file path"""
    filename = filepath.name
    date_match = re.match(r'(\d+)_(\d+)_(\d+)', filename)
    if not date_match:
        return None
    
    day, month, year = date_match.groups()
    date_str = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    
    # Try to extract title from the file content
    title = filename.replace('.html', '').replace('.md', '')
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if first_line.startswith('# '):
                title = first_line[2:].strip()
            elif first_line.startswith('<h1'):
                # Extract text from HTML h1 tag
                title_match = re.search(r'<h1[^>]*>(.*?)</h1>', first_line)
                if title_match:
                    title = title_match.group(1).strip()
    except Exception:
        pass
    
    return {
        'filename': filename,
        'date': date_str,
        'title': title,
        'path': str(filepath.relative_to(Path('.')))
    }

def update_base_html(latest_post):
    """Update the base.html file with the latest post link and embedded JavaScript"""
    base_html_path = Path('base.html')
    if not base_html_path.exists():
        print("base.html not found, skipping HTML update")
        return
    
    # Read the current HTML content
    with open(base_html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Update the first post link to point to the latest post
    if latest_post:
        # Add the August 2025 section if it doesn't exist
        if 'August 2025' not in html_content:
            # Find the project ideas section and add August 2025 after it
            project_section = re.search(r'(<h2 id="project-ideas">Project ideas</h2>\s*<ul>\s*<li><a href="[^"]*">[^<]*</a></li>\s*</ul>)', html_content)
            if project_section:
                august_section = f'''
    <h2 id="august-2025">August 2025</h2>
    <ul>
      <li><a href="{latest_post["path"]}">{latest_post["title"]} (Latest)</a></li>
    </ul>'''
                html_content = html_content.replace(project_section.group(1), project_section.group(1) + august_section)
        
        # Update the first post link in the first month section to indicate it's the latest
        # Look for the first <li><a href=...> pattern and update it
        first_link_pattern = r'(<li><a href="[^"]*">)([^<]*?)(\s*\(Latest\))*(\s*</a></li>)'
        def replace_first_link(match):
            href = match.group(1)
            text = match.group(2).strip()
            closing = match.group(4)
            return f"{href}{text} (Latest){closing}"
        
        # Replace only the first occurrence
        html_content = re.sub(first_link_pattern, replace_first_link, html_content, count=1)
    
    # Embed the JavaScript directly into the HTML
    js_file_path = Path('latest-post-inline.js')
    if js_file_path.exists():
        with open(js_file_path, 'r', encoding='utf-8') as f:
            js_content = f.read()
        
        # Remove the script tag if it exists
        html_content = re.sub(r'<script src="latest-post\.js"></script>', '', html_content)
        
        # Add the embedded JavaScript
        embedded_js = f'<script>\n{js_content}\n</script>'
        
        # Insert before closing body tag
        if '</body>' in html_content:
            html_content = html_content.replace('</body>', f'{embedded_js}\n</body>')
        else:
            # Fallback: add at the end
            html_content += f'\n{embedded_js}'
    
    # Write the updated HTML
    with open(base_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Updated base.html with latest post: {latest_post['title'] if latest_post else 'None'}")

def update_base_md(latest_post):
    """Update the base.md file with the latest post link"""
    base_md_path = Path('base.md')
    if not base_md_path.exists():
        print("base.md not found, skipping MD update")
        return
    
    # Read the current markdown content
    with open(base_md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    if latest_post:
        # Update the first post link to point to the latest post
        # Look for pattern like: * [August 28, 2025](8_2025/28_8_2025.html)
        old_pattern = r'(\* \[)[^\]]*(\][^)]*\([^)]*\))(\s*\(Latest\))*'
        new_link = f'* [{latest_post["title"]}]({latest_post["path"]}) (Latest)'
        
        # Replace the first occurrence (most recent post)
        md_content = re.sub(old_pattern, new_link, md_content, count=1)
    
    # Write the updated markdown
    with open(base_md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Updated base.md with latest post: {latest_post['title'] if latest_post else 'None'}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Update latest post links in site updates')
    parser.add_argument('--html-only', action='store_true', help='Only update HTML files')
    parser.add_argument('--md-only', action='store_true', help='Only update Markdown files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be updated without making changes')
    
    args = parser.parse_args()
    
    print("🔍 Finding latest post...")
    latest_post = find_latest_post()
    
    if latest_post:
        print(f"✅ Found latest post: {latest_post['title']} ({latest_post['date']})")
        print(f"   Path: {latest_post['path']}")
    else:
        print("⚠️  No latest post found")
    
    if args.dry_run:
        print("\n🔍 DRY RUN - No changes will be made")
        return
    
    print("\n📝 Updating files...")
    
    if not args.md_only:
        update_base_html(latest_post)
    
    if not args.html_only:
        update_base_md(latest_post)
    
    print("✅ Update complete!")

if __name__ == "__main__":
    main()
