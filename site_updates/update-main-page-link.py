#!/usr/bin/env python3
"""
Update the main page to link the Site Updates button to the most recent post.
This script scans for the most recent DD_MM_YYYY.md file and updates the HomepageFeatures component accordingly.
"""

import os
import re
from pathlib import Path
from datetime import datetime

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

def find_most_recent_post():
    """Find the most recent post based on filename dates"""
    docs_site_updates = Path('docs/site_updates')
    
    if not docs_site_updates.exists():
        print("❌ docs/site_updates directory not found")
        return None
    
    most_recent = None
    most_recent_date = None
    
    # Scan all subdirectories for .md files
    for md_file in docs_site_updates.rglob('*.md'):
        if md_file.name == 'base.md':
            continue  # Skip the base page
        
        date_info = parse_date_from_filename(md_file.name)
        if date_info:
            year, month, day = date_info
            file_date = datetime(year, month, day)
            
            if most_recent_date is None or file_date > most_recent_date:
                most_recent_date = file_date
                most_recent = md_file
    
    if most_recent:
        # Convert to relative path from docs directory
        relative_path = most_recent.relative_to(Path('docs'))
        # Convert to Docusaurus doc ID format (remove .md extension)
        doc_id = str(relative_path).replace('.md', '')
        print(f"✅ Most recent post: {most_recent.name} ({most_recent_date.strftime('%B %d, %Y')})")
        print(f"📝 Doc ID: {doc_id}")
        return doc_id
    
    return None

def update_homepage_features_link(most_recent_doc_id):
    """Update the HomepageFeatures component to link to the most recent post"""
    # Get the project root directory (where the script is called from)
    project_root = Path.cwd()
    homepage_features = project_root / 'src' / 'components' / 'HomepageFeatures' / 'index.tsx'
    
    if not homepage_features.exists():
        print("❌ src/components/HomepageFeatures/index.tsx not found")
        print(f"   Looked in: {homepage_features}")
        return False
    
    # Read the current content
    with open(homepage_features, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Site Updates section and update the link
    # Look for either the base pattern or an existing post pattern
    base_pattern = r'link: "/docs/site_updates/base"'
    post_pattern = r'link: "/docs/site_updates/\d+_\d+/\d+_\d+_\d+"'
    
    # Check if we need to update from base or from an existing post
    if base_pattern in content:
        old_pattern = base_pattern
        print("  🔄 Updating from base link...")
    elif re.search(post_pattern, content):
        old_pattern = re.search(post_pattern, content).group(0)
        print("  🔄 Updating from existing post link...")
    else:
        print("❌ Could not find Site Updates link pattern in HomepageFeatures")
        return False
    
    new_link = f'link: "/docs/{most_recent_doc_id}"'
    updated_content = content.replace(old_pattern, new_link)
    
    # Also update the description to indicate it's the latest post
    # Create the new description with human-readable date format
    filename_date = most_recent_doc_id.split('/')[-1]  # e.g., "28_8_2025"
    try:
        # Parse the filename date and format it nicely
        day, month, year = filename_date.split('_')
        month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        month_name = month_names[int(month) - 1]  # Convert month number to name
        human_readable_date = f"{month_name} {int(day)}, {year}"
    except (ValueError, IndexError):
        # Fallback to simple format if parsing fails
        human_readable_date = filename_date.replace('_', ' ')
    
    new_desc = f"Latest update: {human_readable_date}. View the most recent site updates and changes."
    
    # Replace the description (handle both old and new formats)
    old_desc_patterns = [
        f'        From basic programming concepts to advanced topics like DevOps and\n        Linux, find all your learning materials in one organized platform.',
        f'        Latest update: .*\. View the most recent site updates and changes\.'
    ]
    
    for old_desc_pattern in old_desc_patterns:
        if re.search(old_desc_pattern, updated_content):
            updated_content = re.sub(old_desc_pattern, f'        {new_desc}', updated_content)
            break
    
    # Write the updated content
    with open(homepage_features, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Updated HomepageFeatures to link to: /docs/{most_recent_doc_id}")
    print(f"📝 Updated description: {new_desc}")
    return True

def main():
    """Main function to update the main page link"""
    print("🔗 Updating main page Site Updates link...")
    
    # Find the most recent post
    most_recent_doc_id = find_most_recent_post()
    
    if not most_recent_doc_id:
        print("❌ No recent posts found")
        return False
    
    # Update the HomepageFeatures component
    success = update_homepage_features_link(most_recent_doc_id)
    
    if success:
        print("🎉 HomepageFeatures updated successfully!")
        print(f"📱 Site Updates button now links to: /docs/{most_recent_doc_id}")
    else:
        print("❌ Failed to update HomepageFeatures")
    
    return success

if __name__ == "__main__":
    main()
