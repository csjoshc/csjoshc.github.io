#!/usr/bin/env python3
"""
Unified Development Script for csjoshc.github.io
Combines all development functionality into one Python script
Usage: python3 dev.py [mode]
Modes: simple, enhanced, ultra, build, clean
"""

import os
import sys
import signal
import subprocess
import time
import psutil
from pathlib import Path

# Colors for output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color

def print_status(message):
    """Print colored status message"""
    print(f"{Colors.GREEN}✅ {message}{Colors.NC}")

def print_warning(message):
    """Print colored warning message"""
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.NC}")

def print_error(message):
    """Print colored error message"""
    print(f"{Colors.RED}❌ {message}{Colors.NC}")

def print_info(message):
    """Print colored info message"""
    print(f"{Colors.BLUE}ℹ️  {message}{Colors.NC}")

def print_success(message):
    """Print colored success message"""
    print(f"{Colors.GREEN}🚀 {message}{Colors.NC}")

def show_usage():
    """Display usage information"""
    print("🚀 Unified Development Script for csjoshc.github.io")
    print("==================================================")
    print("")
    print("Usage: python3 dev.py [mode]")
    print("")
    print("Modes:")
    print("  simple    - Basic MkDocs server (fastest startup)")
    print("  enhanced  - Enhanced with file watching (recommended)")
    print("  ultra     - Maximum performance with verbose logging")
    print("  build     - Build site without serving")
    print("  clean     - Clean up all processes and temporary files")
    print("  help      - Show this help message")
    print("")
    print("Examples:")
    print("  python3 dev.py              # Default: enhanced mode")
    print("  python3 dev.py simple       # Simple development server")
    print("  python3 dev.py ultra        # Ultra-fast with verbose logging")
    print("  python3 dev.py build        # Build site only")
    print("  python3 dev.py clean        # Clean up everything")

def check_port(port):
    """Check if port is available and kill existing processes if needed"""
    try:
        # Check if port is in use
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['cmdline'] and any('mkdocs' in cmd for cmd in proc.info['cmdline']):
                    print_warning(f"Port {port} is already in use. Stopping existing process...")
                    proc.terminate()
                    proc.wait(timeout=5)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                pass
        time.sleep(2)
    except Exception as e:
        print_warning(f"Could not check port {port}: {e}")

def clean_all():
    """Clean up all development processes and temporary files"""
    print_info("Cleaning up development environment...")
    
    try:
        # Kill MkDocs processes
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['cmdline'] and any('mkdocs' in cmd for cmd in proc.info['cmdline']):
                    proc.terminate()
                    proc.wait(timeout=5)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                pass
        
        # Kill any background watchers
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['cmdline'] and any(watcher in ' '.join(proc.info['cmdline']) 
                                              for watcher in ['smart_watcher', 'simple_watcher']):
                    proc.terminate()
                    proc.wait(timeout=5)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                pass
        
        # Remove temporary files
        temp_files = ['.dev_pid', '.watcher_pid']
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        
        print_success("Cleanup complete!")
    except Exception as e:
        print_error(f"Error during cleanup: {e}")

def build_site():
    """Build site without serving"""
    print_info("Building site...")
    try:
        result = subprocess.run(['python3', '-m', 'mkdocs', 'build'], 
                              capture_output=True, text=True, check=True)
        print_success("Site built successfully!")
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print_error(f"Build failed: {e}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        sys.exit(1)

def start_simple():
    """Start simple development server"""
    print_info("Starting Simple Development Server...")
    print("=========================================")
    
    check_port(8000)
    
    print_info("Starting MkDocs server at http://localhost:8000")
    print_info("Live reload enabled - changes will auto-refresh your browser")
    print_info("Dirty reload enabled - faster rebuilds")
    print("")
    print_warning("Initial build may take 10-15 seconds (converting notebooks)...")
    print_info("To stop the server, press Ctrl+C")
    print("")
    
    try:
        subprocess.run(['python3', '-m', 'mkdocs', 'serve',
                       '--livereload', '--dirtyreload', '--dev-addr=127.0.0.1:8000'])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print_error(f"Server error: {e}")

def start_enhanced():
    """Start enhanced development server"""
    print_info("Starting Enhanced Development Server...")
    print("==========================================")
    
    check_port(8000)
    
    print_info("Starting MkDocs server at http://localhost:8000")
    print_info("Live reload enabled - changes will auto-refresh your browser")
    print_info("Dirty reload enabled - faster rebuilds")
    print_info("Smart file watching enabled")
    print("")
    print_warning("Initial build may take 10-15 seconds (converting notebooks)...")
    print_info("To stop the server, press Ctrl+C")
    print("")
    
    try:
        subprocess.run(['python3', '-m', 'mkdocs', 'serve',
                       '--livereload', '--dirtyreload', '--dev-addr=127.0.0.1:8000',
                       '--watch', 'docs', '--watch', 'mkdocs.yml', '--watch', 'docs/stylesheets'])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print_error(f"Server error: {e}")

def start_ultra():
    """Start ultra-fast development server"""
    print_info("Starting Ultra-Fast Development Server...")
    print("=============================================")
    
    check_port(8000)
    
    print_info("Starting MkDocs server at http://localhost:8000")
    print_info("Ultra-fast incremental builds enabled")
    print_info("Live reload enabled")
    print_info("Dirty reload enabled")
    print_info("Smart file watching enabled")
    print_info("Optimized for development speed")
    print("")
    print_warning("Initial build may take 10-15 seconds (converting notebooks)...")
    print_info("To stop the server, press Ctrl+C")
    print("")
    
    try:
        subprocess.run(['python3', '-m', 'mkdocs', 'serve',
                       '--livereload', '--dirtyreload', '--dev-addr=127.0.0.1:8000',
                       '--watch', 'docs', '--watch', 'mkdocs.yml', '--watch', 'docs/stylesheets',
                       '--verbose'])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print_error(f"Server error: {e}")

def main():
    """Main function to handle command line arguments"""
    # Get mode from command line arguments
    mode = sys.argv[1] if len(sys.argv) > 1 else 'enhanced'
    
    # Handle different modes
    if mode in ['simple', 'basic']:
        start_simple()
    elif mode in ['enhanced', 'recommended']:
        start_enhanced()
    elif mode in ['ultra', 'fast', 'performance']:
        start_ultra()
    elif mode == 'build':
        build_site()
    elif mode == 'clean':
        clean_all()
    elif mode in ['help', '-h', '--help']:
        show_usage()
    else:
        print_error(f"Unknown mode: {mode}")
        print("")
        show_usage()
        sys.exit(1)

if __name__ == "__main__":
    # Set up signal handlers for graceful shutdown
    def signal_handler(signum, frame):
        print("\n🛑 Shutting down gracefully...")
        clean_all()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Run main function
    main()
