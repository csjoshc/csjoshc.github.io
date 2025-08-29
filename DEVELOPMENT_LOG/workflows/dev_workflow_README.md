# Development Workflow for csjoshc.github.io

## 🚀 **Quick Start**

### **Justfile-Based Development Commands**

We now use a `justfile` for clean, simple development commands:

```bash
# Start development server (enhanced mode - recommended)
just

# Start enhanced development server
just dev

# Start simple development server (fastest startup)
just simple

# Start ultra-fast development server (maximum performance)
just ultra

# Build site without serving
just build

# Clean up all processes
just clean

# Show help
just help
```

## 📋 **Available Commands**

### **1. Enhanced Mode (Default)**

```bash
just
# or
just dev
```

- **Features**: Live reload, dirty reload, smart file watching
- **Best for**: Daily development work
- **Performance**: Balanced speed and reliability
- **Initial build time**: ~10-15 seconds (notebook conversion)

### **2. Simple Mode**

```bash
just simple
```

- **Features**: Live reload, dirty reload
- **Best for**: Quick testing and simple changes
- **Performance**: Fastest startup
- **Initial build time**: ~10-15 seconds

### **3. Ultra Mode**

```bash
just ultra
```

- **Features**: Live reload, dirty reload, enhanced file watching
- **Best for**: Maximum performance during active development
- **Performance**: Fastest incremental builds
- **Initial build time**: ~10-15 seconds

### **4. Build Only**

```bash
just build
```

- **Features**: Builds the entire site without serving
- **Best for**: Production builds, CI/CD
- **Performance**: Full build (not incremental)

### **5. Cleanup**

```bash
just clean
```

- **Features**: Stops all running MkDocs processes
- **Best for**: When you need to free up port 8000

## 🔧 **System Requirements**

The justfile automatically checks for:

- **Python 3.6+**: For MkDocs and notebook processing
- **MkDocs**: For site generation
- **Just**: For running the commands

### **Installing Just**

```bash
# macOS (using Homebrew)
brew install just

# Linux/macOS (using Cargo)
cargo install just

# Manual installation
# https://github.com/casey/just
```

### **Installing MkDocs**

```bash
# Activate virtual environment first
source .venv/bin/activate

# Install MkDocs with Material theme
pip3 install mkdocs-material
```

## 🚀 **How Incremental Builds Work**

### **🔄 `--dirtyreload` (Enabled in all modes):**

- **Only rebuilds changed files** instead of the entire site
- **Skips unchanged pages** during rebuilds
- **Maintains navigation structure** from previous build

### **👀 File Watching (Ultra mode):**

- **`--watch docs`**: Monitors all content files
- **`--watch mkdocs.yml`**: Watches configuration changes
- **`--watch docs/stylesheets`**: Watches CSS changes

### **📱 `--livereload` (Enabled in all modes):**

- **Automatically refreshes browser** when files change
- **No manual refresh needed** during development

## 💡 **Development Tips**

### **First Time Setup:**

1. **Activate virtual environment**: `source .venv/bin/activate`
2. **Check requirements**: `just check`
3. **Start development**: `just dev`

### **Daily Development:**

1. **Start server**: `just dev`
2. **Make changes** to your `.md` or `.ipynb` files
3. **Browser auto-refreshes** when you save
4. **Stop server**: `Ctrl+C`

### **Troubleshooting:**

- **Port in use**: `just clean` then `just dev`
- **Slow builds**: Use `just ultra` for maximum performance
- **Check requirements**: `just check`

## 🔧 **VS Code Integration**

Add this to your `.vscode/launch.json` for easy debugging:

```json
{
  "name": "Start Dev Server",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/justfile",
  "args": ["dev"],
  "console": "integratedTerminal"
}
```

## 📁 **File Structure**

```
csjoshc.github.io/
├── justfile                    # Development commands
├── mkdocs.yml                 # MkDocs configuration
├── docs/                      # Source documentation
├── site/                      # Built site (auto-generated)
└── .venv/                     # Python virtual environment
```

## 🎯 **Why Justfile?**

- **✅ Simpler**: No Python dependencies, just shell commands
- **✅ Faster**: Direct execution, no Python startup time
- **✅ Cleaner**: Self-documenting commands with `just help`
- **✅ Portable**: Works on any system with just installed
- **✅ Maintainable**: Easy to modify and extend commands
