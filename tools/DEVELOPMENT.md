# Development Workflow Guide

## 📚 **Development Logs & Documentation**

All major development changes, features, and improvements are documented in the organized `DEVELOPMENT_LOG/` directory.

- **📋 [Development Log Index](DEVELOPMENT_LOG/README.md)** - Master index of all development entries and documentation
- **🚀 [Latest: Streamlined Justfile](DEVELOPMENT_LOG/2025-08-28_23-15_STREAMLINED_JUSTFILE.md)** - Complete justfile redesign

### **📁 Organized Documentation**

- **Features** - [Feature Documentation](DEVELOPMENT_LOG/features/) - New capabilities and implementations
- **Systems** - [System Architecture](DEVELOPMENT_LOG/systems/) - System design and architecture
- **Workflows** - [Development Workflows](DEVELOPMENT_LOG/workflows/) - Development processes and commands

---

## 🚀 **Automatic File Watching & Incremental Builds**

This project includes several tools for automatic file watching and incremental builds during development.

## 📋 **Available Scripts**

### **1. Working Development Server (Recommended)**

```bash
./working_dev.sh
```

**What it does:**

- Starts MkDocs with live reload and dirty reload
- Handles initial build time (10-15 seconds for notebooks)
- Provides reliable development server
- Automatically handles port conflicts

### **2. Simple Development Server**

```bash
./simple_dev.sh
```

**What it does:**

- Basic MkDocs server with live reload
- Good for simple development needs
- Reliable and straightforward

### **3. Simple File Watcher (Optional)**

```bash
python3 simple_watcher.py
```

**What it does:**

- Works alongside MkDocs server
- Provides additional file change notifications
- Lightweight and non-intrusive

## 🔄 **How It Works**

### **File Watching**

- **Automatic Detection**: MkDocs watches `docs/` and `mkdocs.yml` by default
- **Live Reload**: Browser automatically refreshes on changes
- **Dirty Reload**: Only rebuilds changed files for faster updates

### **Initial Build Time**

- **First Start**: Takes 10-15 seconds to convert all Jupyter notebooks
- **Subsequent Changes**: Very fast (1-2 seconds) due to incremental builds
- **Notebook Conversion**: Happens automatically in the background

### **Live Reload**

- **Browser Auto-refresh**: Changes automatically appear in your browser
- **Instant Feedback**: See changes immediately without manual refresh
- **Smart Reloading**: Only reloads what's necessary

## 🎯 **Usage Examples**

### **Start Development Environment**

```bash
# Start working development server (recommended)
./working_dev.sh

# Or start simple server
./simple_dev.sh

# Optional: Add file watcher in another terminal
python3 simple_watcher.py
```

### **Make Changes**

1. **Edit any file** in `docs/`, `notes/`, or `docs/stylesheets/`
2. **Save the file** - changes are automatically detected
3. **Watch terminal** - you'll see build progress
4. **Browser refreshes** automatically with new content

### **File Types Supported**

- ✅ **Markdown** (`.md`) - Documentation files
- ✅ **Jupyter Notebooks** (`.ipynb`) - Code and explanations
- ✅ **CSS** (`.css`) - Styling changes
- ✅ **YAML** (`.yml`, `.yaml`) - Configuration files

## ⚙️ **Configuration**

### **MkDocs Configuration**

The main `mkdocs.yml` file controls:

- Site structure and navigation
- Theme and styling
- Plugin configuration
- Build settings

### **Development Settings**

- **Port**: Default 8000 (automatically handled)
- **Live Reload**: Enabled by default
- **Dirty Reload**: Enabled for faster builds
- **File Watching**: Automatic for docs and config

## 🛠️ **Troubleshooting**

### **Port Already in Use**

```bash
# The scripts automatically handle this, but if needed:
pkill -f "mkdocs serve"
```

### **Initial Build Taking Long**

```bash
# This is normal for first startup
# Wait 10-15 seconds for notebook conversion
# Subsequent changes will be much faster
```

### **File Changes Not Detected**

```bash
# Check if server is running
ps aux | grep "mkdocs serve"

# Restart the development server
./working_dev.sh
```

### **Build Failures**

```bash
# Check MkDocs configuration
python3 -m mkdocs build --verbose

# Verify file syntax
python3 -m mkdocs serve --dirtyreload
```

## 🔍 **Monitoring & Debugging**

### **View Active Processes**

```bash
# Check what's running
ps aux | grep -E "(mkdocs|smart_watcher)"

# Check port usage
lsof -i :8000
```

### **Log Files**

- **MkDocs**: Check terminal output for build logs
- **File Watcher**: Check terminal output for change detection
- **Browser Console**: Check for any JavaScript errors

## 📚 **Advanced Features**

### **Incremental Builds**

- **Configuration Changes**: Full site rebuild when `mkdocs.yml` changes
- **Content Changes**: Incremental rebuild for markdown and notebook files
- **Notebook Conversion**: Automatic `.ipynb` to `.md` conversion

### **Performance Optimization**

- **Dirty Reload**: Only rebuilds changed files
- **Live Reload**: Instant browser updates
- **Smart Watching**: Efficient file change detection

## 🎉 **Benefits**

1. **Instant Feedback**: See changes immediately
2. **No Manual Refreshing**: Browser updates automatically
3. **Efficient Builds**: Only rebuilds what changed
4. **Professional Workflow**: Industry-standard development practices
5. **Time Saving**: Focus on content, not manual processes

## 🚀 **Getting Started**

1. **Clone the repository** (if not already done)
2. **Make scripts executable**: `chmod +x *.sh`
3. **Start development**: `./working_dev.sh`
4. **Wait for initial build** (10-15 seconds)
5. **Open browser**: Navigate to `http://localhost:8000`
6. **Make changes**: Edit any file and watch auto-reload
7. **Enjoy development**: Focus on content, not process!

## ⚠️ **Important Notes**

- **Initial Build**: First startup takes 10-15 seconds due to notebook conversion
- **Port 8000**: Default port, automatically managed by scripts
- **File Watching**: MkDocs handles most file watching automatically
- **Live Reload**: Works out of the box with no additional configuration

---

**Happy Developing! 🎯✨**
