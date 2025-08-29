#!/usr/bin/env python3
"""
Check Site Updates Needed - Smart Detection for Site Updates
This script checks if site updates need refreshing by comparing
file modification dates with the last build.
"""

import os
import json
from pathlib import Path
from datetime import datetime

# Configuration
BUILD_STATE_FILE = ".build_state.json"
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
        "last_site_updates_build": None
    }

def get_latest_site_updates_modification():
    """Get the latest modification time of any .md file in site_updates"""
    latest_time = 0
    
    if not os.path.exists(SITE_UPDATES_DIR):
        return latest_time
    
    for root, dirs, files in os.walk(SITE_UPDATES_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    mod_time = os.path.getmtime(file_path)
                    latest_time = max(latest_time, mod_time)
                except OSError:
                    continue
    
    return latest_time

def check_site_updates_needed():
    """Check if site updates need refreshing"""
    build_state = load_build_state()
    last_site_updates_build = build_state.get('last_site_updates_build')
    
    # Get the latest modification time of site updates
    latest_mod_time = get_latest_site_updates_modification()
    
    if last_site_updates_build is None:
        # First time running - need to build
        return True
    
    # Convert to datetime for comparison
    try:
        last_build_dt = datetime.fromisoformat(last_site_updates_build)
        last_build_timestamp = last_build_dt.timestamp()
        
        # Check if any .md files are newer than the last build
        if latest_mod_time > last_build_timestamp:
            return True
        
        return False
    except (ValueError, TypeError):
        # Invalid timestamp format - need to rebuild
        return True

def main():
    """Main function - returns exit code 0 if updates needed, 1 if not"""
    if check_site_updates_needed():
        print("📝 Site updates need refreshing")
        exit(0)  # Updates needed
    else:
        print("✅ Site updates are up to date")
        exit(1)  # No updates needed

if __name__ == "__main__":
    main()
