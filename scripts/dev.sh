#!/bin/bash

# Unified Development Script for csjoshc.github.io
# Combines all development functionality into one script
# Usage: ./dev.sh [mode]
# Modes: simple, enhanced, ultra, build, clean

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}🚀 $1${NC}"
}

# Function to clean up on exit
cleanup() {
    echo ""
    print_warning "Stopping development server..."
    pkill -f "mkdocs serve" 2>/dev/null || true
    pkill -f "python.*mkdocs" 2>/dev/null || true
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Function to check if port is available
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        print_warning "Port $port is already in use. Stopping existing process..."
        pkill -f "mkdocs serve" 2>/dev/null || true
        sleep 2
    fi
}

# Function to show usage
show_usage() {
    echo "🚀 Unified Development Script for csjoshc.github.io"
    echo "=================================================="
    echo ""
    echo "Usage: ./dev.sh [mode]"
    echo ""
    echo "Modes:"
    echo "  simple    - Basic MkDocs server (fastest startup)"
    echo "  enhanced  - Enhanced with file watching (recommended)"
    echo "  ultra     - Maximum performance with verbose logging"
    echo "  build     - Build site without serving"
    echo "  clean     - Clean up all processes and temporary files"
    echo "  help      - Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./dev.sh              # Default: enhanced mode"
    echo "  ./dev.sh simple       # Simple development server"
    echo "  ./dev.sh ultra        # Ultra-fast with verbose logging"
    echo "  ./dev.sh build        # Build site only"
    echo "  ./dev.sh clean        # Clean up everything"
}

# Function to clean up processes and files
clean_all() {
    print_info "Cleaning up development environment..."
    
    # Kill MkDocs processes
    pkill -f "mkdocs serve" 2>/dev/null || true
    pkill -f "python.*mkdocs" 2>/dev/null || true
    
    # Kill any background watchers
    pkill -f "smart_watcher" 2>/dev/null || true
    pkill -f "simple_watcher" 2>/dev/null || true
    
    # Remove temporary files
    rm -f .dev_pid 2>/dev/null || true
    rm -f .watcher_pid 2>/dev/null || true
    
    print_success "Cleanup complete!"
}

# Function to build site without serving
build_site() {
    print_info "Building site..."
    ./build.sh
    print_success "Site built successfully!"
}

# Function to start simple development server
start_simple() {
    print_info "Starting Simple Development Server..."
    echo "========================================="
    
    check_port 8000
    
    print_info "Starting MkDocs server at http://localhost:8000"
    print_info "Live reload enabled - changes will auto-refresh your browser"
    print_info "Dirty reload enabled - faster rebuilds"
    echo ""
    print_info "Using smart rebuild system - only changed files will be processed"
    print_info "To stop the server, press Ctrl+C"
    echo ""
    
    # Start MkDocs server directly (no initial build needed since we use smart rebuilds)
    python3 -m mkdocs serve \
        --livereload \
        --dirtyreload \
        --dev-addr=127.0.0.1:8000
}

# Function to start enhanced development server
start_enhanced() {
    print_info "Starting Enhanced Development Server..."
    echo "=========================================="
    
    check_port 8000
    
    print_info "Starting MkDocs server at http://localhost:8000"
    print_info "Live reload enabled - changes will auto-refresh your browser"
    print_info "Dirty reload enabled - faster rebuilds"
    print_info "Smart file watching enabled"
    echo ""
    print_info "Using smart rebuild system - only changed files will be processed"
    print_info "To stop the server, press Ctrl+C"
    echo ""
    
    python3 -m mkdocs serve \
        --livereload \
        --dirtyreload \
        --dev-addr=127.0.0.1:8000 \
        --watch docs \
        --watch mkdocs.yml \
        --watch docs/stylesheets
}

# Function to start ultra-fast development server
start_ultra() {
    print_info "Starting Ultra-Fast Development Server..."
    echo "============================================="
    
    check_port 8000
    
    print_info "Starting MkDocs server at http://localhost:8000"
    print_info "Ultra-fast incremental builds enabled"
    print_info "Live reload enabled"
    print_info "Dirty reload enabled"
    print_info "Smart file watching enabled"
    print_info "Optimized for development speed"
    echo ""
    print_info "Using smart rebuild system - only changed files will be processed"
    print_info "To stop the server, press Ctrl+C"
    echo ""
    
    python3 -m mkdocs serve \
        --livereload \
        --dirtyreload \
        --dev-addr=127.0.0.1:8000 \
        --watch docs \
        --watch mkdocs.yml \
        --watch docs/stylesheets \
        --verbose
}

# Main script logic
main() {
    local mode=${1:-enhanced}  # Default to enhanced mode
    
    case $mode in
        "simple"|"basic")
            start_simple
            ;;
        "enhanced"|"recommended")
            start_enhanced
            ;;
        "ultra"|"fast"|"performance")
            start_ultra
            ;;
        "build")
            build_site
            ;;
        "clean")
            clean_all
            ;;
        "help"|"-h"|"--help")
            show_usage
            ;;
        *)
            print_error "Unknown mode: $mode"
            echo ""
            show_usage
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"
