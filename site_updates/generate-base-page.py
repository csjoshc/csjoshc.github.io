#!/usr/bin/env python3
"""
Generate the site updates base page automatically.
This script scans the docs/site_updates/ directory and generates
a properly formatted base.md file with month headers and post listings.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def parse_date_from_filename(filename):
    """Extract date from filename like '28_8_2025' -> (2025, 8, 28)"""
    # Remove .md extension
    name = filename.replace('.md', '')
    
    # Pattern: day_month_year (e.g., 28_8_2025)
    match = re.match(r'(\d+)_(\d+)_(\d+)', name)
    if match:
        day, month, year = map(int, match.groups())
        return (year, month, day)
    
    return None

def get_month_name(month):
    """Convert month number to month name"""
    months = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    return months.get(month, f"Month {month}")

def format_post_title(filename):
    """Convert filename to readable title"""
    # Remove .md extension
    name = filename.replace('.md', '')
    
    # Pattern: day_month_year
    match = re.match(r'(\d+)_(\d+)_(\d+)', name)
    if match:
        day, month, year = match.groups()
        month_name = get_month_name(int(month))
        return f"{month_name} {day}, {year}"
    
    return name

def scan_site_updates():
    """Scan the docs/site_updates directory for posts"""
    docs_path = Path('../docs/site_updates')
    if not docs_path.exists():
        print(f"❌ Directory {docs_path} not found")
        return {}
    
    posts_by_month = defaultdict(list)
    seen_posts = set()  # Track seen posts to avoid duplicates
    
    # Scan all directories recursively for .md files
    for md_file in docs_path.rglob('*.md'):
        if md_file.name != 'base.md' and md_file.name != 'README.md':  # Skip base files
            date_info = parse_date_from_filename(md_file.name)
            if date_info:
                year, month, day = date_info
                
                # Create a unique key for this post
                post_key = f"{year}_{month}_{day}"
                
                # Only add if we haven't seen this post before
                if post_key not in seen_posts:
                    seen_posts.add(post_key)
                    
                    # Calculate relative path from docs/site_updates
                    rel_path = md_file.relative_to(docs_path)
                    
                    posts_by_month[(year, month)].append({
                        'filename': md_file.name,
                        'path': str(rel_path),
                        'date': date_info,
                        'title': format_post_title(md_file.name)
                    })
    
    # Also check for project_ideas and other special directories
    project_ideas_path = docs_path / 'project_ideas'
    if project_ideas_path.exists():
        for md_file in project_ideas_path.glob('*.md'):
            if md_file.name != 'base.md':
                posts_by_month[('special', 'project_ideas')].append({
                    'filename': md_file.name,
                    'path': f"project_ideas/{md_file.name}",
                    'date': None,
                    'title': md_file.name.replace('.md', '').replace('_', ' ').title()
                })
    
    return posts_by_month

def generate_base_content(posts_by_month):
    """Generate the base.md content"""
    content = """🏠 Home
📝 Site Updates

# Site update portal

Here I want to post occasional summaries of site updates.

"""
    
    # Add project ideas section first
    if ('special', 'project_ideas') in posts_by_month:
        content += "## Project ideas\n\n"
        for post in posts_by_month[('special', 'project_ideas')]:
            content += f"- [{post['title']}]({post['path']})\n"
        content += "\n"
    
    # Sort months by year (descending) then by month (descending)
    sorted_months = sorted(
        [(year, month) for year, month in posts_by_month.keys() 
         if year != 'special'],
        reverse=True
    )
    
    # Generate month sections
    for year, month in sorted_months:
        month_name = get_month_name(month)
        content += f"## {month_name} {year}\n\n"
        
        # Sort posts within month by day (descending)
        month_posts = sorted(
            posts_by_month[(year, month)],
            key=lambda x: x['date'][2],  # Sort by day
            reverse=True
        )
        
        for post in month_posts:
            content += f"- [{post['title']}]({post['path']})\n"
        
        content += "\n"
    
    return content

def main():
    """Main function"""
    print("🔍 Scanning site updates directory...")
    
    # Change to the site_updates directory
    os.chdir(Path(__file__).parent)
    
    posts_by_month = scan_site_updates()
    
    if not posts_by_month:
        print("❌ No posts found")
        return
    
    print(f"📝 Found posts in {len(posts_by_month)} month(s)")
    
    # Generate content
    content = generate_base_content(posts_by_month)
    
    # Write to base.md
    base_path = Path('base.md')
    with open(base_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Generated {base_path}")
    print(f"📊 Total posts: {sum(len(posts) for posts in posts_by_month.values())}")
    
    # Also update the docs version
    docs_base_path = Path('../docs/site_updates/base.md')
    if docs_base_path.exists():
        with open(docs_base_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {docs_base_path}")

if __name__ == "__main__":
    main()
