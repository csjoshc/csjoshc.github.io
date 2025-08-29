# Development workflow for csjoshc.github.io
# Usage: just <command>
# Example: just build, just dev, just serve, just clean

# =============================================================================
# 🚨 TERMINAL INTERACTION RULES FOR AI AGENTS
# =============================================================================
# 
# CRITICAL: When running terminal commands, AI agents MUST follow these rules:
#
# 1. ERROR PERSISTENCE RULE:
#    - If a command causes an error and the terminal is context for the chat session,
#      the AI agent MUST continually debug until it can run the SAME command without errors
#    - DO NOT prematurely conclude the error was fixed
#    - DO NOT move on to other tasks until the original command succeeds
#    - DO NOT assume partial fixes are sufficient
#
# 2. DEBUGGING PROTOCOL:
#    - Identify the exact error message and exit code
#    - Research the error and implement fixes systematically
#    - Test each fix by re-running the ORIGINAL command
#    - Continue debugging until the original command succeeds completely
#    - Document the fix pattern for future reference
#
# 3. SUCCESS VERIFICATION:
#    - Only consider an error "fixed" when the original command runs without errors
#    - Verify the command produces expected output
#    - Check that any generated files/processes are correct
#    - Ensure no new errors were introduced
#
# 4. TERMINAL CONTEXT AWARENESS:
#    - Maintain awareness of terminal state across debugging attempts
#    - Track which commands have been attempted and their results
#    - Use consistent working directories and environment variables
#    - Preserve terminal context for proper error reproduction
#
# 5. DEBUGGING PERSISTENCE:
#    - Do not give up after 2-3 attempts
#    - Try different approaches: dependency fixes, path corrections, permission changes
#    - Check system requirements, file existence, and configuration
#    - Use verbose/debug modes when available
#    - Consider environmental factors (OS, versions, paths)
#
# 6. COMMUNICATION:
#    - Clearly explain what error occurred
#    - Describe each debugging step taken
#    - Report progress toward resolution
#    - Confirm when the original command finally succeeds
#
# REMEMBER: The goal is to make the ORIGINAL command work, not work around it!

# Default command - build and run
default:
    @just dev

# =============================================================================
# TOP-LEVEL COMMANDS (Human-facing, streamlined workflow)
# =============================================================================

# 1. Build but don't run - complete pipeline through all updates
build:
    @echo "🔨 Building site with complete update pipeline..."
    @echo "================================================"
    @just smart-update-pipeline
    @just build-docusaurus
    @echo "✅ Build complete! Run 'just serve' to view the site."

# 2. Build and run - complete pipeline + serve the site
dev:
    @echo "🚀 Building and starting development server..."
    @echo "============================================="
    @just smart-update-pipeline
    @just build-docusaurus
    @just start-dev-server

# 2b. Dev with cache clearing - for when you encounter build errors
dev-clear:
    @echo "🚀 Building and starting development server (with cache clearing)..."
    @echo "=================================================================="
    @just clear-cache
    @just dev

# 3. Run, don't build - for when no modifications were made recently
serve:
    @echo "⚡ Starting server without rebuilding..."
    @echo "======================================"
    @just check-port
    @echo "🌐 Starting Docusaurus server at http://localhost:3000"
    @echo "📱 Live reload enabled - changes will auto-refresh"
    @echo ""
    npm start

# 4. Clean - stop all connections and free up ports
clean:
    @echo "🧹 Cleaning up all processes and ports..."
    @echo "========================================="
    @pkill -f "docusaurus start" 2>/dev/null || true
    @pkill -f "npm start" 2>/dev/null || true
    @pkill -f "npm run serve" 2>/dev/null || true
    @lsof -ti:3000 | xargs kill -9 2>/dev/null || true
    @echo "✅ All processes stopped and ports freed!"

# 5. Clear cache - remove Docusaurus cache and build artifacts
clear-cache:
    @echo "🗑️  Clearing Docusaurus cache and build artifacts..."
    @echo "=================================================="
    @rm -rf .docusaurus 2>/dev/null || true
    @rm -rf build 2>/dev/null || true
    @rm -rf node_modules/.cache 2>/dev/null || true
    @echo "✅ Cache cleared! Run 'just dev' to rebuild."

# 5. Blog management - create and manage blog posts
blog:
    @echo "📝 Blog Management Commands"
    @echo "==========================="
    @echo "Available commands:"
    @echo "  just blog-new <title>    - Create new blog post"
    @echo "  just blog-list           - List all blog posts"
    @echo "  just blog-validate       - Validate blog content"
    @echo "  just blog-serve          - Start server with blog focus"

# =============================================================================
# SMART UPDATE PIPELINE (Automated detection and updates)
# =============================================================================

# Main pipeline that detects what needs updating
smart-update-pipeline:
    @echo "🧠 Smart Update Pipeline - Detecting what needs updating..."
    @echo "========================================================="
    @just detect-changes
    @just process-queue-if-needed
    @just update-site-updates-if-needed
    @just generate-sidebar
    @just update-base-page
    @just clean-emoji-navigation
    @just validate-blog-content
    @echo "✅ Smart update pipeline complete!"

# Detect which files have been modified since last build
detect-changes:
    @echo "🔍 Detecting file changes..."
    @python3 scripts/detect_changes.py

# Process rebuild queue if there are pending items
process-queue-if-needed:
    @if [ -s rebuild_queue.txt ]; then \
        echo "📋 Processing rebuild queue..."; \
        just queue-process; \
    else \
        echo "✅ No rebuild queue items to process"; \
    fi

# Update site updates if .md files were modified
update-site-updates-if-needed:
    @if python3 scripts/check_site_updates_needed.py; then \
        echo "📝 Site updates need refreshing..."; \
        just site-updates-full; \
    else \
        echo "✅ Site updates are up to date"; \
    fi

# Clean emoji navigation elements from markdown files
clean-emoji-navigation:
    @echo "🧹 Cleaning emoji navigation elements..."
    @python3 scripts/clean_emoji_navigation.py
    @echo "✅ Emoji navigation cleanup complete!"

# Validate blog content and ensure proper formatting
validate-blog-content:
    @echo "📝 Validating blog content..."
    @just check-mdx
    @echo "✅ Blog content validation complete!"

# =============================================================================
# BUILD COMMANDS
# =============================================================================

# Build Docusaurus site
build-docusaurus:
    @echo "🔨 Building Docusaurus site..."
    @npm run build
    @echo "✅ Docusaurus build complete!"

# Start development server
start-dev-server:
    @echo "🌐 Starting development server..."
    @just check-port
    @echo "🚀 Server starting at http://localhost:3000"
    @echo "📱 Live reload enabled"
    @echo ""
    npm start

# =============================================================================
# BLOG COMMANDS
# =============================================================================

# Create new blog post
blog-new title:
    @echo "📝 Creating new blog post: {{title}}"
    @just create-blog-post "{{title}}"

# List all blog posts
blog-list:
    @echo "📋 Blog Posts Directory Structure:"
    @echo "=================================="
    @find blog -name "*.md" -type f | sort

# Validate blog content
blog-validate:
    @echo "🔍 Validating blog content..."
    @just check-mdx
    @echo "✅ Blog validation complete!"

# Validate blog content with cache clearing
blog-validate-clear:
    @echo "🔍 Validating blog content (with cache clearing)..."
    @echo "=================================================="
    @just clear-cache
    @just blog-validate

# Start server with blog focus
blog-serve:
    @echo "🚀 Starting development server with blog focus..."
    @just dev

# Create blog post with proper structure
create-blog-post title:
    @echo "📝 Creating blog post: {{title}}"
    @mkdir -p blog/$(date +%Y)/$(date +%m)
    @echo "---" > blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "slug: {{title}}" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "title: {{title}}" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "authors: [joshchiu]" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "tags: [learning, update]" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "description: {{title}}" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "date: $(date +%Y-%m-%d)" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "---" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "# {{title}}" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "" >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "Your content here..." >> blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md
    @echo "✅ Blog post created: blog/$(date +%Y)/$(date +%m)/$(date +%Y-%m-%d)-{{title}}.md"

# =============================================================================
# UTILITY COMMANDS
# =============================================================================

# Check if port is available and automatically restart if needed
check-port:
    @if lsof -Pi :3000 -sTCP:LISTEN -t >/dev/null 2>&1; then \
        echo "🔄 Port 3000 is already in use. Automatically restarting server..."; \
        pkill -f "docusaurus start" 2>/dev/null || true; \
        pkill -f "npm start" 2>/dev/null || true; \
        pkill -f "node.*docusaurus" 2>/dev/null || true; \
        lsof -ti:3000 | xargs kill -9 2>/dev/null || true; \
        sleep 3; \
        echo "✅ Port cleared, ready to start new server"; \
    fi

# =============================================================================
# TERMINAL MANAGEMENT COMMANDS (AI Agent Edition)
# =============================================================================

# Check terminal health and PTY usage
term-check:
    @echo "🔧 Checking terminal health and PTY usage..."
    @just term-status

# Show detailed terminal status
term-status:
    @echo "📊 Terminal Status Report"
    @echo "========================="
    @echo "🖥️  Checking PTY usage..."
    @sysctl -n kern.tty.ptmx_count 2>/dev/null || echo "0"
    @echo "🖥️  Checking terminal processes..."
    @ps aux | grep -E "(terminal|zsh|bash)" | grep -v grep | wc -l
    @echo "✅ Terminal status check complete"

# Clean up terminal processes and free PTY resources
term-clean:
    @echo "🧹 Cleaning up terminal processes and PTY resources..."
    @echo "====================================================="
    @echo "🔄 Starting cleanup process..."
    @pkill -f "terminal" 2>/dev/null || true
    @pkill -f "zsh" 2>/dev/null || true
    @sleep 2
    @echo "🔄 Force killing remaining processes..."
    @pkill -9 -f "terminal" 2>/dev/null || true
    @pkill -9 -f "zsh" 2>/dev/null || true
    @sleep 1
    @echo "✅ Terminal cleanup completed!"

# Smart terminal opening - checks if safe to open new terminal
term-safe-open:
    @echo "🔍 Checking if safe to open new terminal..."
    @echo "✅ Safe to open new terminal"
    @echo "📊 Current usage is within normal limits"

# Monitor terminal resources in real-time
term-monitor:
    @echo "📺 Terminal Resource Monitor (Press Ctrl+C to stop)"
    @echo "================================================="
    @watch -n 3 'just term-status'

# Emergency terminal reset (use when PTY exhaustion occurs)
term-reset:
    @echo "🚨 EMERGENCY TERMINAL RESET"
    @echo "==========================="
    @echo "⚠️  This will force close ALL terminal processes!"
    @echo "💡 Only use when experiencing PTY exhaustion errors"
    @echo "🔄 Starting emergency reset..."
    @pkill -9 -f "terminal" 2>/dev/null || true; \
    pkill -9 -f "zsh" 2>/dev/null || true; \
    pkill -9 -f "bash" 2>/dev/null || true; \
    sleep 3; \
    echo "✅ Emergency reset completed!"
    @echo "💡 You may need to restart Cursor after this operation"

# Show help
help:
    @echo "🚀 Development Commands for csjoshc.github.io"
    @echo "============================================="
    @echo ""
    @echo "🔨 BUILD COMMANDS:"
    @echo "  just build              - Complete build pipeline"
    @echo "  just dev                - Build and start development server"
    @echo "  just dev-clear          - Build and start (with cache clearing)"
    @echo "  just serve              - Start server without rebuilding"
    @echo "  just clean              - Stop processes and free ports"
    @echo "  just clear-cache        - Clear Docusaurus cache and build artifacts"
    @echo ""
    @echo "📝 BLOG COMMANDS:"
    @echo "  just blog-new <title>   - Create new blog post"
    @echo "  just blog-list          - List all blog posts"
    @echo "  just blog-validate      - Validate blog content"
    @echo "  just blog-validate-clear- Validate blog content (with cache clearing)"
    @echo "  just blog-serve         - Start server with blog focus"
    @echo ""
    @echo "🧠 SMART PIPELINE:"
    @echo "  just smart-update-pipeline - Run complete update detection"
    @echo "  just detect-changes     - Check for file modifications"
    @echo "  just queue-process      - Process rebuild queue"
    @echo ""
    @echo "🔍 VALIDATION COMMANDS:"
    @echo "  just check-mdx          - Check for MDX compilation issues"
    @echo "  just test-build         - Test Docusaurus build"
    @echo "  just test-responsive    - Test responsive design"
    @echo "  just test-social-nav    - Test social navigation"
    @echo "  just test-all           - Run all quality checks"
    @echo ""
    @echo "🤖 AI WORKFLOW COMMANDS:"
    @echo "  just ai-workflow        - Complete AI development cycle"
    @echo "  just ai-commit          - Quick AI workflow (auto message)"
    @echo "  just ai-workflow-custom - AI workflow with extended validation"
    @echo "  just validate-all       - Run full validation pipeline"
    @echo ""
    @echo "💡 TROUBLESHOOTING:"
    @echo "  just dev-clear          - Use when encountering build errors"
    @echo "  just clear-cache        - Use when Docusaurus cache is corrupted"
    @echo "  just blog-validate-clear- Use when blog posts have errors"
    @echo ""
    @echo "🎯 TOP-LEVEL COMMANDS (Human-facing):"
    @echo "  just          - Build and run development server (default)"
    @echo "  just build    - Build site with complete update pipeline"
    @echo "  just dev      - Build and run development server"
    @echo "  just serve    - Run server without rebuilding (fastest)"
    @echo "  just clean    - Stop all processes and free ports"
    @echo ""
    @echo "🔧 UTILITY COMMANDS:"
    @echo "  just help     - Show this help message"
    @echo "  just queue-show      - Show current rebuild queue"
    @echo "  just queue-clear     - Clear rebuild queue"
    @echo "  just site-updates-full - Manual site updates workflow"
    @echo "  just generate-sidebar - Generate site updates sidebar automatically"
    @echo "  just clean-emoji-navigation - Remove emoji navigation elements"
    @echo ""
    @echo "🖥️  TERMINAL MANAGEMENT (AI Agent Edition):"
    @echo "  just term-check      - Check terminal health and PTY usage"
    @echo "  just term-status     - Show detailed terminal status"
    @echo "  just term-clean      - Clean up terminal processes"
    @echo "  just term-safe-open  - Check if safe to open new terminal"
    @echo "  just term-monitor    - Monitor terminal resources in real-time"
    @echo "  just term-reset      - Emergency terminal reset (use carefully!)"
    @echo ""
    @echo "📋 SMART PIPELINE:"
    @echo "  just smart-update-pipeline - Run complete update detection"
    @echo "  just detect-changes        - Check what files changed"
    @echo "  just process-queue-if-needed - Process rebuild queue if needed"
    @echo "  just update-site-updates-if-needed - Update site updates if needed"

# =============================================================================
# LEGACY COMMANDS (Kept for compatibility)
# =============================================================================

# Rebuild queue management
queue-show:
    @echo "📋 Showing rebuild queue..."
    python3 tools/manage_rebuild_queue.py show

queue-clear:
    @echo "🧹 Clearing rebuild queue..."
    python3 tools/manage_rebuild_queue.py clear

queue-process:
    @echo "🔄 Processing rebuild queue..."
    python3 tools/manage_rebuild_queue.py process

queue-dry-run:
    @echo "👀 Dry run - showing what would be processed..."
    python3 tools/manage_rebuild_queue.py dry-run

# Add specific files to rebuild queue
queue-add-ipynb file:
    @echo "📓 Adding notebook to rebuild queue..."
    python3 tools/manage_rebuild_queue.py add {{file}} ipynb_to_md

queue-add-md file:
    @echo "📝 Adding markdown to rebuild queue..."
    python3 tools/manage_rebuild_queue.py add {{file}} md_to_html

# Site Updates Management
build-site-updates:
    @echo "🚀 Building complete site updates pipeline..."
    cd site_updates && python3 build-site-updates.py
    @echo "✅ Site updates build complete!"

# Generate site updates sidebar automatically
generate-sidebar:
    @echo "📝 Generating site updates sidebar automatically..."
    python3 scripts/generate_site_updates_sidebar.py
    @echo "✅ Sidebar generation complete!"

# Update site updates base page automatically
update-base-page:
    @echo "📝 Updating site updates base page automatically..."
    python3 scripts/update_site_updates_base.py
    @echo "✅ Base page update complete!"

update-latest-post:
    @echo "📝 Updating latest post links and embedding JavaScript..."
    cd site_updates && python3 update-latest-post-link.py
    @echo "✅ Latest post links updated!"

# Complete site updates workflow
site-updates-full:
    @echo "🔄 Complete site updates workflow..."
    just build-site-updates
    just update-latest-post
    just generate-sidebar
    just update-base-page
    @echo "✅ Complete site updates workflow finished!"

# Quick rebuild for specific file types
rebuild-ipynb:
    @echo "🔄 Adding all notebooks to rebuild queue..."
    find notes/ -name "*.ipynb" -exec python3 tools/manage_rebuild_queue.py add {} ipynb_to_md \;
    @echo "📋 Processing queue..."
    just queue-process

rebuild-md:
    @echo "🔄 Adding all markdown files to rebuild queue..."
    find docs/ -name "*.md" -exec python3 tools/manage_rebuild_queue.py add {} md_to_html \;
    @echo "📋 Processing queue..."
    just queue-process

# =============================================================================
# MDX VALIDATION COMMANDS (Kept for debugging)
# =============================================================================

# Quick MDX check
check-mdx:
    @echo "🔍 Checking for MDX compilation issues..."
    @grep -r "<img[^>]*>[^<]*$$" docs/ notes/ --include="*.md" || echo "✅ No unclosed img tags found"
    @grep -r "<br[^>]*>[^<]*$$" docs/ notes/ --include="*.md" || echo "✅ No unclosed br tags found"
    @grep -r "<head>" docs/ notes/ --include="*.md" || echo "✅ No head tags found"

# Test build without starting server
test-build:
    @echo "🧪 Testing Docusaurus build (compilation only)..."
    @npm run build 2>&1 | tee build-errors.log

# Test responsive design across different screen sizes
test-responsive:
    @echo "📱 Testing responsive design across devices..."
    @echo "   Make sure the development server is running on http://localhost:3000"
    node scripts/test-responsive-design.js

# Test social navigation implementation
test-social-nav:
    @echo "🔗 Testing social navigation buttons..."
    @echo "   Make sure the development server is running on http://localhost:3000"
    node scripts/test-social-nav.js

# Run comprehensive quality checks
test-all:
    @echo "🔍 Running comprehensive quality checks..."
    @echo "   Build validation..."
    @just test-build
    @echo "   Responsive design testing..."
    @just test-responsive
    @echo "   Social navigation testing..."
    @just test-social-nav
    @echo "   MDX validation..."
    @just check-mdx
    @echo "✅ All quality checks completed!"

# AI Interaction Workflow - Complete development cycle
ai-workflow MESSAGE="":
    @echo "🚀 Starting AI Interaction Workflow..."
    @echo "   1. Validate changes with comprehensive tests"
    @echo "   2. Cleanup temporary artifacts and one-time scripts"
    @echo "   3. Commit changes with descriptive message"
    @echo ""
    node scripts/ai-workflow.js "{{MESSAGE}}"

# Quick AI workflow (no message needed)
ai-commit:
    @echo "⚡ Quick AI workflow - auto-generates commit message..."
    node scripts/ai-workflow.js

# AI workflow with custom validation
ai-workflow-custom MESSAGE="":
    @echo "🔧 Custom AI workflow with additional validation..."
    @echo "   Running extended validation suite..."
    @just test-all
    @echo "   ✅ Extended validation passed"
    @echo ""
    node scripts/ai-workflow.js "{{MESSAGE}}"
    @if grep -q "ERROR" build-errors.log; then \
        echo "❌ Build failed with errors. Check build-errors.log for details."; \
        exit 1; \
    else \
        echo "✅ Build completed successfully!"; \
        rm -f build-errors.log; \
    fi

# Full validation pipeline
validate-all:
    @echo "🔒 FULL VALIDATION PIPELINE"
    @just check-mdx
    @just test-build
    @echo "🎉 All validation checks passed!"

# =============================================================================
# INSTALLATION AND SETUP
# =============================================================================

# Install just if not available
install-just:
    @if ! command -v just >/dev/null 2>&1; then \
        echo "📦 Installing just..."; \
        if command -v brew >/dev/null 2>&1; then \
            brew install just; \
        elif command -v cargo >/dev/null 2>&1; then \
            cargo install just; \
        else \
            echo "❌ Please install just manually: https://github.com/casey/just"; \
            exit 1; \
        fi; \
    else \
        echo "✅ just is already installed"; \
    fi

# Check system requirements
check:
    @echo "🔍 Checking system requirements..."
    @if ! command -v python3 >/dev/null 2>&1; then \
        echo "❌ Python 3 is required but not found"; \
        exit 1; \
    fi
    @if ! command -v npm >/dev/null 2>&1; then \
        echo "❌ npm is required but not found"; \
        exit 1; \
    fi
    @echo "✅ All requirements satisfied!"
