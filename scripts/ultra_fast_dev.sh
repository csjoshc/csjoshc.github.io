#!/bin/bash

# Ultra-Fast Development Server for csjoshc.github.io
# Maximizes incremental build performance

echo "⚡ Starting Ultra-Fast Development Server..."
echo "==========================================="
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
    sleep 1
fi

echo "🌐 Starting MkDocs server at http://localhost:8000"
echo "⚡ Ultra-fast incremental builds enabled"
echo "📱 Live reload enabled"
echo "🔄 Dirty reload enabled"
echo "👀 Smart file watching enabled"
echo "🚀 Optimized for development speed"
echo ""
echo "⏳ Initial build may take 10-15 seconds (converting notebooks)..."
echo "💡 To stop the server, press Ctrl+C"
echo ""

# Start MkDocs with maximum incremental build performance
python3 -m mkdocs serve \
    --livereload \
    --dirtyreload \
    --dev-addr=127.0.0.1:8000 \
    --watch docs \
    --watch mkdocs.yml \
    --watch docs/stylesheets \
    --verbose

# If we get here, something went wrong
echo "❌ Server stopped unexpectedly"
cleanup
