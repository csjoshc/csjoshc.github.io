#!/usr/bin/env python3
"""
Rebuild Queue Manager for Josh's Learning Notes
Manages which files need to be rebuilt and processes them efficiently.
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path
import subprocess
import json

class RebuildQueueManager:
    def __init__(self, queue_file="rebuild_queue.txt"):
        self.queue_file = queue_file
        self.project_root = Path(__file__).parent
        
    def add_to_queue(self, file_path, action="both"):
        """Add a file to the rebuild queue"""
        timestamp = datetime.now().isoformat()
        entry = f"{file_path}|{action}|{timestamp}\n"
        
        # Read existing queue
        queue_entries = self.read_queue()
        
        # Check if file already exists in queue
        existing_entry = None
        for i, entry_line in enumerate(queue_entries):
            if entry_line.startswith(f"{file_path}|"):
                existing_entry = i
                break
        
        if existing_entry is not None:
            # Update existing entry
            queue_entries[existing_entry] = entry
        else:
            # Add new entry
            queue_entries.append(entry)
        
        # Write back to queue file with proper formatting
        with open(self.queue_file, 'w') as f:
            f.write("# Rebuild Queue - Files that need to be converted/rebuilt\n")
            f.write("# Format: file_path|action|timestamp\n")
            f.write("# Actions: ipynb_to_md, md_to_html, both\n")
            f.write("# This file is automatically managed by Cursor rules and build scripts\n\n")
            for entry in queue_entries:
                # Ensure each entry ends with a newline
                if not entry.endswith('\n'):
                    entry = entry + '\n'
                f.write(entry)
        
        print(f"✅ Added to rebuild queue: {file_path} ({action})")
        return True
    
    def read_queue(self):
        """Read the current rebuild queue"""
        if not os.path.exists(self.queue_file):
            return []
        
        with open(self.queue_file, 'r') as f:
            content = f.read()
        
        # Split by lines and filter out comments and empty lines
        lines = content.split('\n')
        return [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
    
    def clear_queue(self):
        """Clear the rebuild queue"""
        with open(self.queue_file, 'w') as f:
            f.write("# Rebuild Queue - Files that need to be converted/rebuilt\n")
            f.write("# Format: file_path|action|timestamp\n")
            f.write("# Actions: ipynb_to_md, md_to_html, both\n")
            f.write("# This file is automatically managed by Cursor rules and build scripts\n\n")
        print("🧹 Rebuild queue cleared")
    
    def process_queue(self, dry_run=False):
        """Process all files in the rebuild queue"""
        queue_entries = self.read_queue()
        
        if not queue_entries:
            print("📭 Rebuild queue is empty - nothing to process")
            return
        
        print(f"🔄 Processing {len(queue_entries)} files in rebuild queue...")
        
        processed_files = []
        failed_files = []
        
        for entry in queue_entries:
            try:
                file_path, action, timestamp = entry.split('|')
                
                if dry_run:
                    print(f"  📋 Would process: {file_path} ({action})")
                    continue
                
                success = self._process_file(file_path, action)
                if success:
                    processed_files.append(file_path)
                    print(f"  ✅ Processed: {file_path}")
                else:
                    failed_files.append(file_path)
                    print(f"  ❌ Failed: {file_path}")
                    
            except ValueError as e:
                print(f"  ⚠️  Invalid queue entry: {entry} - {e}")
                continue
        
        if not dry_run:
            # Clear the queue after processing
            self.clear_queue()
            
            print(f"\n📊 Processing complete:")
            print(f"  ✅ Successfully processed: {len(processed_files)}")
            print(f"  ❌ Failed: {len(failed_files)}")
            
            if failed_files:
                print(f"  📝 Failed files: {', '.join(failed_files)}")
    
    def _process_file(self, file_path, action):
        """Process a single file based on the action"""
        try:
            if action == "ipynb_to_md" or action == "both":
                if file_path.endswith('.ipynb'):
                    # Convert notebook to markdown
                    success = self._convert_notebook_to_markdown(file_path)
                    if not success:
                        return False
            
            if action == "md_to_html" or action == "both":
                if file_path.endswith('.md'):
                    # Convert markdown to HTML (this will be handled by mkdocs)
                    print(f"    📝 Markdown file {file_path} will be processed by mkdocs")
            
            return True
            
        except Exception as e:
            print(f"    ❌ Error processing {file_path}: {e}")
            return False
    
    def _convert_notebook_to_markdown(self, notebook_path):
        """Convert a Jupyter notebook to markdown"""
        try:
            # Ensure the notebook exists
            if not os.path.exists(notebook_path):
                print(f"    ⚠️  Notebook not found: {notebook_path}")
                return False
            
            # Convert using jupyter nbconvert
            cmd = [
                "jupyter", "nbconvert", 
                "--to", "markdown",
                "--output-dir", "docs",
                notebook_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            
            if result.returncode == 0:
                print(f"    📓 Converted {notebook_path} to markdown")
                return True
            else:
                print(f"    ❌ Failed to convert {notebook_path}: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"    ❌ Error converting notebook {notebook_path}: {e}")
            return False
    
    def show_queue(self):
        """Show the current rebuild queue"""
        queue_entries = self.read_queue()
        
        if not queue_entries:
            print("📭 Rebuild queue is empty")
            return
        
        print(f"📋 Current rebuild queue ({len(queue_entries)} files):")
        for i, entry in enumerate(queue_entries, 1):
            try:
                file_path, action, timestamp = entry.split('|')
                print(f"  {i}. {file_path} ({action}) - {timestamp}")
            except ValueError:
                print(f"  {i}. Invalid entry: {entry}")

def main():
    """Main function for command line usage"""
    if len(sys.argv) < 2:
        print("Usage: python3 manage_rebuild_queue.py [command] [options]")
        print("Commands:")
        print("  add <file_path> [action]  - Add file to rebuild queue")
        print("  show                       - Show current queue")
        print("  process                    - Process all files in queue")
        print("  dry-run                    - Show what would be processed")
        print("  clear                      - Clear the queue")
        return
    
    manager = RebuildQueueManager()
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("❌ Error: Please provide a file path")
            return
        file_path = sys.argv[2]
        action = sys.argv[3] if len(sys.argv) > 3 else "both"
        manager.add_to_queue(file_path, action)
        
    elif command == "show":
        manager.show_queue()
        
    elif command == "process":
        manager.process_queue()
        
    elif command == "dry-run":
        manager.process_queue(dry_run=True)
        
    elif command == "clear":
        manager.clear_queue()
        
    else:
        print(f"❌ Unknown command: {command}")
        print("Use 'python3 manage_rebuild_queue.py help' for usage information")

if __name__ == "__main__":
    main()
