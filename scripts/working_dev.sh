#!/bin/bash

# Working Development Server for csjoshc.github.io
# Enhanced with faster incremental builds and smart file watching

echo "🚀 Starting Enhanced Development Server..."
echo "========================================="
echo ""

# Function to clean up on exit
cleanup() {
    echo ""
    echo "🛑 Stopping development server..."
    pkill -f "mkdocs serve"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Check if port 8000 is available
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Port 8000 is already in use. Stopping existing process..."
    pkill -f "mkdocs serve"
    sleep 2
fi

echo "🌐 Starting MkDocs server at http://localhost:8000"
echo "📱 Live reload enabled - changes will auto-refresh your browser"
echo "🔄 Dirty reload enabled - faster rebuilds"
echo "👀 Smart file watching enabled"
echo ""
echo "⏳ Initial build may take 10-15 seconds (converting notebooks)..."
echo "💡 To stop the server, press Ctrl+C"
echo ""

# Start MkDocs with enhanced incremental build settings
python3 -m mkdocs serve \
    --livereload \
    --dirtyreload \
    --dev-addr=127.0.0.1:8000 \
    --watch docs \
    --watch mkdocs.yml \
    --watch docs/stylesheets

# If we get here, something went wrong
echo "❌ Server stopped unexpectedly"
cleanup
