#!/usr/bin/env python3
"""
Generate Site Updates Sidebar
This script automatically generates the site updates section of the Docusaurus sidebars.ts file
based on the actual markdown files present in the docs directory.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

def parse_date_from_filename(filename: str) -> Tuple[int, int, int]:
    """Parse date from filename like '28_8_2025.md' -> (2025, 8, 28)"""
    # Remove .md extension
    name = filename.replace('.md', '')
    
    # Handle different date formats
    if '_' in name:
        parts = name.split('_')
        if len(parts) >= 3:
            try:
                day = int(parts[0])
                month = int(parts[1])
                year = int(parts[2])
                return (year, month, day)
            except ValueError:
                pass
    
    # Fallback: try to extract date from filename
    date_match = re.search(r'(\d{1,2})[_-](\d{1,2})[_-](\d{4})', name)
    if date_match:
        day, month, year = map(int, date_match.groups())
        return (year, month, day)
    
    return (0, 0, 0)

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
                parsed_year, parsed_month, parsed_day = parse_date_from_filename(file_path.name)
                if parsed_year == 0:  # Invalid date
                    continue
                
                # Use year from directory if available, otherwise from filename
                if year is None:
                    year = parsed_year
                
                month, day = parsed_month, parsed_day
                
                # Calculate relative path for Docusaurus
                relative_path = file_path.relative_to(docs_dir)
                doc_id = str(relative_path).replace('.md', '')
                
                # Generate label from date
                if year and month and day:
                    try:
                        date_obj = datetime(year, month, day)
                        label = date_obj.strftime("%B %d, %Y")
                    except ValueError:
                        label = f"{month}/{day}/{year}"
                else:
                    label = file_path.stem
                

                
                if year not in site_updates:
                    site_updates[year] = []
                
                site_updates[year].append((doc_id, label, (year, month, day)))
    
    # Sort files within each year by date
    for year in site_updates:
        site_updates[year].sort(key=lambda x: x[2])
    
    return site_updates

def generate_sidebar_content(site_updates: Dict[int, List[Tuple[str, str, Tuple[int, int, int]]]]) -> str:
    """Generate the sidebar content for site updates"""
    if not site_updates:
        return ""
    
    # Sort years in descending order (newest first)
    sorted_years = sorted(site_updates.keys(), reverse=True)
    
    sidebar_items = []
    
    for year in sorted_years:
        year_items = []
        for doc_id, label, (y, m, d) in site_updates[year]:
            year_items.append(f"""            {{
              type: "doc",
              id: "{doc_id}",
              label: "{label}",
            }},""")
        
        # Add year category
        sidebar_items.append(f"""        {{
          type: "category",
          label: "{year}",
          items: [
{chr(10).join(year_items)}
          ],
        }},""")
    
    return f"""    {{
      type: "category",
      label: "📝 Site Updates",
      link: {{
        type: "doc",
        id: "site_updates/base",
      }},
      items: [
{chr(10).join(sidebar_items)}
      ],
    }},"""

def update_sidebars_file(sidebars_path: Path, new_site_updates_content: str) -> bool:
    """Update the sidebars.ts file with new site updates content"""
    try:
        with open(sidebars_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the site updates section
        start_pattern = r'(\s*{\s*type:\s*"category",\s*label:\s*"📝 Site Updates",\s*link:\s*{\s*type:\s*"doc",\s*id:\s*"site_updates/base",\s*},\s*items:\s*\[)'
        end_pattern = r'(\s*],\s*},\s*)'
        
        start_match = re.search(start_pattern, content, re.MULTILINE | re.DOTALL)
        end_match = re.search(end_pattern, content, re.MULTILINE | re.DOTALL)
        
        if start_match and end_match:
            start_pos = start_match.start(1)
            end_pos = end_match.end(1)
            
            # Replace the entire site updates section
            new_content = content[:start_pos] + new_site_updates_content + content[end_pos:]
            
            with open(sidebars_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        else:
            print("❌ Could not find site updates section in sidebars.ts")
            return False
            
    except Exception as e:
        print(f"❌ Error updating sidebars.ts: {e}")
        return False

def main():
    """Main function"""
    print("🔧 Generating Site Updates Sidebar")
    print("=" * 40)
    
    # Get project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    docs_dir = project_root / "docs"
    sidebars_path = project_root / "config" / "sidebars.ts"
    
    if not docs_dir.exists():
        print("❌ docs directory not found")
        return False
    
    if not sidebars_path.exists():
        print("❌ sidebars.ts not found")
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
    
    # Generate sidebar content
    print("\n📝 Generating sidebar content...")
    sidebar_content = generate_sidebar_content(site_updates)
    
    # Update sidebars.ts file
    print("🔄 Updating sidebars.ts...")
    if update_sidebars_file(sidebars_path, sidebar_content):
        print("✅ Sidebars.ts updated successfully!")
        print("\n📋 Next steps:")
        print("1. Run 'just build' to rebuild the site")
        print("2. Check that all site updates appear in the navigation")
        return True
    else:
        print("❌ Failed to update sidebars.ts")
        return False

if __name__ == "__main__":
    main()
