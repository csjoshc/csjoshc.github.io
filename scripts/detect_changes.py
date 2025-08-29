#!/usr/bin/env python3
"""
Detect Changes - Smart File Change Detection
This script detects which files have been modified since the last build
and automatically adds them to the rebuild queue.
"""

import os
import json
import time
from pathlib import Path
from datetime import datetime, timedelta

# Configuration
BUILD_STATE_FILE = ".build_state.json"
REBUILD_QUEUE_FILE = "rebuild_queue.txt"
NOTES_DIR = "notes"
DOCS_DIR = "docs"
SITE_UPDATES_DIR = "site_updates"

def load_build_state():
    """Load the last build state from file"""
    if os.path.exists(BUILD_STATE_FILE):
        try:
            with open(BUILD_STATE_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    
    # Default state if no file exists
    return {
        "last_build": None,
        "file_timestamps": {},
        "last_site_updates_build": None
    }

def save_build_state(state):
    """Save the current build state to file"""
    with open(BUILD_STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def get_file_modification_time(file_path):
    """Get the modification time of a file"""
    try:
        return os.path.getmtime(file_path)
    except OSError:
        return 0

def scan_directory_for_changes(directory, extensions, last_build_time):
    """Scan a directory for files that have changed since last build"""
    changed_files = []
    
    if not os.path.exists(directory):
        return changed_files
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                mod_time = get_file_modification_time(file_path)
                
                if last_build_time is None or mod_time > last_build_time:
                    changed_files.append(file_path)
    
    return changed_files

def add_to_rebuild_queue(file_path, action):
    """Add a file to the rebuild queue"""
    timestamp = datetime.now().isoformat()
    queue_entry = f"{file_path}|{action}|{timestamp}\n"
    
    with open(REBUILD_QUEUE_FILE, 'a') as f:
        f.write(queue_entry)

def detect_notebook_changes(last_build_time):
    """Detect changes in Jupyter notebooks"""
    print("🔍 Scanning for notebook changes...")
    
    # Convert timestamp string to float if needed
    if last_build_time and isinstance(last_build_time, str):
        try:
            last_build_dt = datetime.fromisoformat(last_build_time)
            last_build_timestamp = last_build_dt.timestamp()
        except ValueError:
            last_build_timestamp = None
    else:
        last_build_timestamp = last_build_time
    
    changed_notebooks = scan_directory_for_changes(
        NOTES_DIR, 
        ['.ipynb'], 
        last_build_timestamp
    )
    
    if changed_notebooks:
        print(f"  📓 Found {len(changed_notebooks)} changed notebooks:")
        for notebook in changed_notebooks:
            print(f"    - {notebook}")
            add_to_rebuild_queue(notebook, 'ipynb_to_md')
    else:
        print("  ✅ No notebook changes detected")
    
    return changed_notebooks

def detect_markdown_changes(last_build_time):
    """Detect changes in markdown files"""
    print("🔍 Scanning for markdown changes...")
    
    # Convert timestamp string to float if needed
    if last_build_time and isinstance(last_build_time, str):
        try:
            last_build_dt = datetime.fromisoformat(last_build_time)
            last_build_timestamp = last_build_dt.timestamp()
        except ValueError:
            last_build_timestamp = None
    else:
        last_build_timestamp = last_build_time
    
    changed_markdown = scan_directory_for_changes(
        DOCS_DIR, 
        ['.md'], 
        last_build_timestamp
    )
    
    if changed_markdown:
        print(f"  📝 Found {len(changed_markdown)} changed markdown files:")
        for md_file in changed_markdown:
            print(f"    - {md_file}")
            add_to_rebuild_queue(md_file, 'md_to_html')
    else:
        print("  ✅ No markdown changes detected")
    
    return changed_markdown

def detect_site_updates_changes(last_build_time):
    """Detect changes in site updates"""
    print("🔍 Scanning for site updates changes...")
    
    # Convert timestamp string to float if needed
    if last_build_time and isinstance(last_build_time, str):
        try:
            last_build_dt = datetime.fromisoformat(last_build_time)
            last_build_timestamp = last_build_dt.timestamp()
        except ValueError:
            last_build_timestamp = None
    else:
        last_build_timestamp = last_build_time
    
    changed_site_updates = scan_directory_for_changes(
        SITE_UPDATES_DIR, 
        ['.md'], 
        last_build_timestamp
    )
    
    if changed_site_updates:
        print(f"  📋 Found {len(changed_site_updates)} changed site update files:")
        for file in changed_site_updates:
            print(f"    - {file}")
    else:
        print("  ✅ No site updates changes detected")
    
    return changed_site_updates

def main():
    """Main function"""
    print("🧠 Smart Change Detection")
    print("=" * 40)
    
    # Load last build state
    build_state = load_build_state()
    last_build_time = build_state.get('last_build')
    
    if last_build_time:
        last_build_dt = datetime.fromisoformat(last_build_time)
        print(f"📅 Last build: {last_build_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("📅 No previous build detected - will process all files")
    
    # Detect changes in different file types
    notebook_changes = detect_notebook_changes(last_build_time)
    markdown_changes = detect_markdown_changes(last_build_time)
    site_updates_changes = detect_site_updates_changes(last_build_time)
    
    # Update build state
    current_time = datetime.now().isoformat()
    build_state['last_build'] = current_time
    
    # Record file timestamps for future comparisons
    all_files = []
    all_files.extend(notebook_changes)
    all_files.extend(markdown_changes)
    all_files.extend(site_updates_changes)
    
    for file_path in all_files:
        build_state['file_timestamps'][file_path] = get_file_modification_time(file_path)
    
    # Save updated build state
    save_build_state(build_state)
    
    # Summary
    total_changes = len(notebook_changes) + len(markdown_changes) + len(site_updates_changes)
    
    if total_changes > 0:
        print(f"\n📊 Summary: {total_changes} files need processing")
        print("  - Notebooks:", len(notebook_changes))
        print("  - Markdown:", len(markdown_changes))
        print("  - Site Updates:", len(site_updates_changes))
        
        if notebook_changes or markdown_changes:
            print("\n🔄 Files have been added to the rebuild queue")
            print("   Run 'just queue-process' to process them")
        
        if site_updates_changes:
            print("\n📝 Site updates need refreshing")
            print("   Run 'just site-updates-full' to update them")
    else:
        print("\n✅ No changes detected - everything is up to date!")
    
    print(f"\n📅 Build state updated: {current_time}")

if __name__ == "__main__":
    main()
