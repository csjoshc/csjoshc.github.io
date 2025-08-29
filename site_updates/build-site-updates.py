#!/usr/bin/env python3
"""
Build Site Updates - Complete Pipeline
This script handles the complete build process for site updates:
1. Adds navigation fragments to all .md files
2. Converts .md files to .html files
3. Updates latest post links
"""

import os
import re
import subprocess
from pathlib import Path

def add_navigation_fragment(file_path):
    """Add navigation fragment to a markdown file if it doesn't already have it"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if navigation fragment already exists
    if '[🏠 Back to Home]' in content:
        print(f"  ✅ {file_path.name} already has navigation fragment")
        return False
    
    # Create navigation fragment based on file depth
    relative_depth = len(file_path.parts) - 1  # site_updates is depth 0
    
    if relative_depth == 1:  # Directly in site_updates
        nav_fragment = '''[🏠 Back to Home](../)

[📋 Back to Site Updates Portal](base)

'''
    elif relative_depth == 2:  # In year subdirectory
        nav_fragment = '''[🏠 Back to Home](../../)

[📋 Back to Site Updates Portal](../base)

'''
    else:  # Deeper nesting
        nav_fragment = '''[🏠 Back to Home](../../../)

[📋 Back to Site Updates Portal](../../base)

'''
    
    # Add navigation fragment at the beginning
    new_content = nav_fragment + content
    
    # Write the updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✅ Added navigation fragment to {file_path.name}")
    return True

def clean_markdown_for_docusaurus(file_path):
    """Clean markdown file by removing any HTML artifacts for Docusaurus compatibility"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove HTML artifacts that cause MDX compilation errors
    cleaned_content = content
    
    # Remove HTML head tags and meta tags
    cleaned_content = re.sub(r'<head[^>]*>.*?</head>', '', cleaned_content, flags=re.DOTALL)
    cleaned_content = re.sub(r'<meta[^>]*>', '', cleaned_content)
    cleaned_content = re.sub(r'<link[^>]*>', '', cleaned_content)
    
    # Remove HTML anchor tags and convert to markdown links
    cleaned_content = re.sub(r'<a href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', cleaned_content)
    
    # Remove any remaining HTML tags
    cleaned_content = re.sub(r'<[^>]+>', '', cleaned_content)
    
    # Clean up extra whitespace
    cleaned_content = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned_content)
    
    # Write the cleaned content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"  🧹 Cleaned {file_path.name} for Docusaurus compatibility")
    return True

def convert_md_to_html(md_file_path):
    """Convert a markdown file to HTML using pandoc"""
    html_file_path = md_file_path.with_suffix('.html')
    
    # Check if HTML file already exists and is newer
    if html_file_path.exists():
        md_mtime = md_file_path.stat().st_mtime
        html_mtime = html_file_path.stat().st_mtime
        if html_mtime >= md_mtime:
            print(f"  ⏭️  {md_file_path.name} -> {html_file_path.name} (already up to date)")
            return False
    
    try:
        # Use pandoc to convert markdown to HTML
        cmd = [
            'pandoc',
            str(md_file_path),
            '-o', str(html_file_path),
            '--standalone',
            '--metadata', 'title=' + md_file_path.stem,
            '--css', 'styles.css'
        ]
        
        # Add CSS link if styles.css exists
        if Path('styles.css').exists():
            cmd.extend(['--css', 'styles.css'])
        
        # Run pandoc from the current directory (site_updates)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path('.'))
        
        if result.returncode == 0:
            print(f"  ✅ {md_file_path.name} -> {html_file_path.name}")
            return True
        else:
            print(f"  ❌ Failed to convert {md_file_path.name}: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print(f"  ❌ Pandoc not found. Please install pandoc: https://pandoc.org/installing.html")
        return False
    except Exception as e:
        print(f"  ❌ Error converting {md_file_path.name}: {e}")
        return False

def add_html_boilerplate(html_file_path):
    """Add HTML boilerplate and styling to the converted file"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it already has our custom HTML structure
        if 'class="nav-links"' in content:
            return False
        
        # Create HTML boilerplate
        boilerplate = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html_file_path.stem}</title>
    <link rel="stylesheet" href="../styles.css">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }}
        .nav-links {{
            background: #f8f9fa;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            border-left: 4px solid #007bff;
        }}
        .nav-links a {{
            color: #007bff;
            text-decoration: none;
            margin-right: 15px;
        }}
        .nav-links a:hover {{
            text-decoration: underline;
        }}
        h1, h2, h3 {{
            color: #333;
        }}
        code {{
            background: #f1f3f4;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', monospace;
        }}
        pre {{
            background: #f1f3f4;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="nav-links">
        {extract_navigation_links(content)}
    </div>
    
    <div class="content">
        {content}
    </div>
</body>
</html>'''
        
        # Write the updated content
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(boilerplate)
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error adding boilerplate to {html_file_path.name}: {e}")
        return False

def extract_navigation_links(content):
    """Extract navigation links from the content and format them nicely"""
    nav_links = []
    
    # Look for navigation links in the content
    link_pattern = r'<a href="([^"]+)">([^<]+)</a>'
    matches = re.findall(link_pattern, content)
    
    for href, text in matches:
        if 'index.html' in href:
            nav_links.append(f'<a href="{href}">🏠 {text}</a>')
        elif 'base.html' in href:
            nav_links.append(f'<a href="{href}">📋 {text}</a>')
        else:
            nav_links.append(f'<a href="{href}">🔗 {text}</a>')
    
    return '\n        '.join(nav_links)

def sync_to_docs_directory():
    """Sync site updates to docs/site_updates directory for Docusaurus"""
    print("\n📁 Step 3: Syncing to docs directory...")
    
    # Get the project root directory (parent of site_updates)
    project_root = Path.cwd().parent
    site_updates_dir = project_root / 'site_updates'
    docs_site_updates = project_root / 'docs' / 'site_updates'
    
    # Ensure docs/site_updates directory exists
    docs_site_updates.mkdir(parents=True, exist_ok=True)
    
    # Copy all .md files from site_updates to docs/site_updates
    md_files = list(site_updates_dir.rglob('*.md'))
    copied_count = 0
    
    for md_file in md_files:
        # Calculate relative path from site_updates
        relative_path = md_file.relative_to(site_updates_dir)
        target_path = docs_site_updates / relative_path
        
        # Ensure target directory exists
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy the file
        import shutil
        shutil.copy2(md_file, target_path)
        
        # Clean the copied file for Docusaurus compatibility
        clean_markdown_for_docusaurus(target_path)
        
        print(f"  📋 Copied and cleaned {relative_path} to docs/site_updates/")
        copied_count += 1
    
    print(f"  ✅ Synced and cleaned {copied_count} files to docs/site_updates/")
    return True

def build_site_updates():
    """Complete build process for site updates"""
    print("🚀 Building site updates...")
    
    # Check if pandoc is available
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Pandoc is required but not found.")
        print("Please install pandoc: https://pandoc.org/installing.html")
        return False
    
    # Step 1: Add navigation fragments
    print("\n📝 Step 1: Adding navigation fragments...")
    # Only process files in the current site_updates directory, not recursively
    md_files = list(Path('.').glob('*.md')) + list(Path('.').glob('*/*.md'))
    
    if md_files:
        print(f"Found {len(md_files)} .md files")
        nav_updated = 0
        for md_file in md_files:
            if add_navigation_fragment(md_file):
                nav_updated += 1
        print(f"Updated {nav_updated} files with navigation fragments")
    else:
        print("No .md files found")
    
    # Step 2: Convert markdown to HTML
    print("\n🔄 Step 2: Converting markdown to HTML...")
    converted_count = 0
    boilerplate_count = 0
    
    for md_file in md_files:
        print(f"\nProcessing {md_file.name}...")
        
        # Convert markdown to HTML
        if convert_md_to_html(md_file):
            converted_count += 1
            
            # Add HTML boilerplate
            html_file = md_file.with_suffix('.html')
            if add_html_boilerplate(html_file):
                boilerplate_count += 1
    
    print(f"\n📊 HTML Conversion Summary:")
    print(f"  - Converted: {converted_count} files")
    print(f"  - Added boilerplate: {boilerplate_count} files")
    print(f"  - Total .md files: {len(md_files)}")
    
    # Step 3: Sync to docs directory
    sync_to_docs_directory()
    
    # Step 4: Generate base page
    print("\n📋 Step 4: Generating base page...")
    try:
        result = subprocess.run(['python3', 'generate-base-page.py'], 
                              capture_output=True, text=True, check=True)
        print("  ✅ Base page generated successfully")
        print(f"  📝 Output: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to generate base page: {e}")
        print(f"  📝 Error: {e.stderr.strip()}")
        return False
    
    # Step 5: Update main page link to most recent post
    print("\n🔗 Step 5: Updating main page link...")
    try:
        # Run from the project root directory
        result = subprocess.run(['python3', 'site_updates/update-main-page-link.py'], 
                              capture_output=True, text=True, check=True, cwd='..')
        print("  ✅ Main page link updated successfully")
        print(f"  📝 Output: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to update main page link: {e}")
        print(f"  📝 Error: {e.stderr.strip()}")
        return False
    
    return True

def main():
    """Main function"""
    print("🔧 Site Updates Build Pipeline")
    print("=" * 40)
    
    # Change to the site_updates directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Run the complete build process
    if build_site_updates():
        print("\n✅ Site updates build complete!")
        print("\nNext steps:")
        print("1. Run 'just update-latest-post' to update latest post links")
        print("2. Check the generated HTML files")
        print("3. Test navigation in your browser")
    else:
        print("\n❌ Build failed. Please check the errors above.")

if __name__ == "__main__":
    main()
