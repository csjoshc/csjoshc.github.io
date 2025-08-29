#!/usr/bin/env python3
"""
Update Site Updates Base Page
This script automatically updates the site updates base.md file to include links to all available site update posts.
"""

import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

def get_site_update_files(docs_dir: Path) -> Dict[int, List[Tuple[str, str, Tuple[int, int, int]]]]:
    """Get all site update files organized by year"""
    site_updates = {}
    
    # Look for site update files in various directories
    search_patterns = [
        docs_dir / "site_updates" / "*" / "*.md",
        docs_dir / "*_2019" / "*.md",
        docs_dir / "*_2020" / "*.md",
        docs_dir / "*_2021" / "*.md",
        docs_dir / "*_2022" / "*.md",
        docs_dir / "*_2023" / "*.md",
        docs_dir / "*_2024" / "*.md",
        docs_dir / "*_2025" / "*.md",
    ]
    
    for pattern in search_patterns:
        for file_path in docs_dir.glob(str(pattern.relative_to(docs_dir))):
            if file_path.is_file() and file_path.name != 'base.md' and file_path.name != 'README.md':
                # Extract year from directory name or filename
                year = None
                month = None
                day = None
                
                # Try to get year from directory name first
                for part in file_path.parts:
                    if part.endswith('_2019') or part.endswith('_2020') or \
                       part.endswith('_2021') or part.endswith('_2022') or \
                       part.endswith('_2023') or part.endswith('_2024') or \
                       part.endswith('_2025'):
                        year = int(part.split('_')[-1])
                        break
                
                # Always try to parse month and day from filename
                if '_' in file_path.name:
                    parts = file_path.name.replace('.md', '').split('_')
                    if len(parts) >= 3:
                        try:
                            day = int(parts[0])
                            month = int(parts[1])
                            if year is None:
                                year = int(parts[2])
                        except ValueError:
                            pass
                
                if year and month and day:
                    if year not in site_updates:
                        site_updates[year] = []
                    
                    # Calculate relative path for the link
                    # Since we're in docs/site_updates/base.md, we need to go up one level
                    # to reach the docs directory, then reference the file
                    relative_path = file_path.relative_to(docs_dir)
                    link_path = str(relative_path).replace('.md', '')
                    
                    # Fix the link path to be relative to docs/site_updates/base.md
                    # We need to go up one level (../) to reach the docs directory
                    # For files in site_updates subdirectories, we need to go up two levels
                    if link_path.startswith('site_updates/'):
                        # Remove the 'site_updates/' prefix since we're already in that directory
                        link_path = link_path.replace('site_updates/', '')
                    else:
                        # For files in year directories, we need to go up one level
                        link_path = '../' + link_path
                    
                    # Generate label from date
                    try:
                        date_obj = datetime(year, month, day)
                        label = date_obj.strftime("%B %d, %Y")
                    except ValueError:
                        label = f"{month}/{day}/{year}"
                    
                    site_updates[year].append((link_path, label, (year, month, day)))
    
    # Sort files within each year by date
    for year in site_updates:
        site_updates[year].sort(key=lambda x: x[2])
    
    return site_updates

def generate_base_content(site_updates: Dict[int, List[Tuple[str, str, Tuple[int, int, int]]]]) -> str:
    """Generate the content for the base.md file"""
    if not site_updates:
        return """# Site update portal

Here I want to post occasional summaries of site updates.

*No site updates found.*"""
    
    # Sort years in descending order (newest first)
    sorted_years = sorted(site_updates.keys(), reverse=True)
    
    content_lines = [
        "# Site update portal",
        "",
        "Here I want to post occasional summaries of site updates.",
        ""
    ]
    
    for year in sorted_years:
        content_lines.append(f"## {year}")
        content_lines.append("")
        
        for link_path, label, (y, m, d) in site_updates[year]:
            content_lines.append(f"- [{label}]({link_path})")
        
        content_lines.append("")
    
    return "\n".join(content_lines)

def update_base_file(base_path: Path, new_content: str) -> bool:
    """Update the base.md file with new content"""
    try:
        with open(base_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"❌ Error updating base.md: {e}")
        return False

def main():
    """Main function"""
    print("🔧 Updating Site Updates Base Page")
    print("=" * 40)
    
    # Get project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    docs_dir = project_root / "docs"
    base_path = docs_dir / "site_updates" / "base.md"
    
    if not docs_dir.exists():
        print("❌ docs directory not found")
        return False
    
    if not base_path.exists():
        print("❌ base.md not found")
        return False
    
    print(f"📁 Scanning {docs_dir} for site update files...")
    
    # Get all site update files
    site_updates = get_site_update_files(docs_dir)
    
    if not site_updates:
        print("❌ No site update files found")
        return False
    
    print(f"✅ Found site updates for {len(site_updates)} year(s):")
    for year in sorted(site_updates.keys(), reverse=True):
        count = len(site_updates[year])
        print(f"  📅 {year}: {count} update(s)")
    
    # Generate base content
    print("\n📝 Generating base page content...")
    base_content = generate_base_content(site_updates)
    
    # Update base.md file
    print("🔄 Updating base.md...")
    if update_base_file(base_path, base_content):
        print("✅ Base.md updated successfully!")
        print("\n📋 Next steps:")
        print("1. Run 'just build' to rebuild the site")
        print("2. Check that all site updates appear in the base page")
        return True
    else:
        print("❌ Failed to update base.md")
        return False

if __name__ == "__main__":
    main()
