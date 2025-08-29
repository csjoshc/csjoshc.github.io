#!/bin/bash
# Script to update all PNG image references to WebP throughout the project
# This script handles HTML files, markdown files, and any other text files

echo "🔄 Updating image references from PNG to WebP..."

# Function to update file references
update_file() {
    local file="$1"
    local temp_file="${file}.tmp"
    
    # Update PNG references to WebP in the file
    sed 's/\.png/\.webp/g' "$file" > "$temp_file"
    
    # Check if any changes were made
    if ! cmp -s "$file" "$temp_file"; then
        mv "$temp_file" "$file"
        echo "✅ Updated: $file"
    else
        rm "$temp_file"
        echo "⏭️  No changes needed: $file"
    fi
}

# Update HTML files
echo "📄 Processing HTML files..."
find . -name "*.html" -type f | while read -r file; do
    update_file "$file"
done

# Update markdown files
echo "📝 Processing markdown files..."
find . -name "*.md" -type f | while read -r file; do
    update_file "$file"
done

# Update any other text files that might contain image references
echo "📋 Processing other text files..."
find . -name "*.txt" -o -name "*.py" -o -name "*.js" -o -name "*.css" | while read -r file; do
    update_file "$file"
done

echo "🎉 Image reference update complete!"
echo ""
echo "📊 Summary of changes:"
echo "  - PNG extensions changed to WebP in HTML files"
echo "  - PNG extensions changed to WebP in markdown files"
echo "  - PNG extensions changed to WebP in other text files"
echo ""
echo "⚠️  Note: You'll need to rebuild the site for the new WebP images to be generated."
echo "   Run: ./build.sh"
