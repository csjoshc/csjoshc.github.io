#!/bin/bash
# Modern build script for MkDocs Material website
# Replaces the old pandoc-based conversion pipeline

echo "🚀 Building Josh's Learning Notes website..."

# Check if rebuild queue has files to process
if [ -s rebuild_queue.txt ] && ! grep -q "^#" rebuild_queue.txt; then
    echo "📋 Processing rebuild queue..."
    python3 manage_rebuild_queue.py process
    
    if [ $? -eq 0 ]; then
        echo "✅ Rebuild queue processed successfully"
    else
        echo "❌ Error processing rebuild queue"
        exit 1
    fi
else
    echo "📭 No files in rebuild queue - skipping notebook conversion"
fi

# Build the site using MkDocs
echo "🏗️ Building static site with MkDocs Material..."
python3 -m mkdocs build

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Build completed successfully!"
    echo "📁 Static files are in the 'site/' directory"
    echo "🌐 To serve locally, run: python3 -m mkdocs serve"
else
    echo "❌ Build failed! Check the error messages above."
    exit 1
fi
