#!/usr/bin/env python3
"""
Convert Markdown to HTML for Site Updates
This script converts all .md files in site_updates to .html files
"""

import os
import re
import subprocess
from pathlib import Path

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
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=md_file_path.parent)
        
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
        
        # Check if it already has HTML structure
        if '<!DOCTYPE html>' in content or '<html' in content:
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

def process_directory(directory):
    """Process all .md files in a directory and convert them to HTML"""
    directory_path = Path(directory)
    md_files = list(directory_path.rglob('*.md'))
    
    if not md_files:
        print(f"No .md files found in {directory}")
        return
    
    print(f"Found {len(md_files)} .md files in {directory}")
    
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
    
    print(f"\n📊 Conversion Summary:")
    print(f"  - Converted: {converted_count} files")
    print(f"  - Added boilerplate: {boilerplate_count} files")
    print(f"  - Total .md files: {len(md_files)}")

def main():
    """Main function"""
    print("🔄 Converting site updates markdown files to HTML...")
    
    # Check if pandoc is available
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Pandoc is required but not found.")
        print("Please install pandoc: https://pandoc.org/installing.html")
        print("\nAlternative: You can manually convert files using:")
        print("  pandoc input.md -o output.html --standalone --css styles.css")
        return
    
    # Process the site_updates directory
    process_directory('site_updates')
    
    print("\n✅ HTML conversion complete!")

if __name__ == "__main__":
    main()
