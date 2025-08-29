# 🚀 Streamlined Justfile Workflow

## 🎯 **Top-Level Commands (Human-facing)**

The justfile has been completely redesigned to provide **exactly 4 main commands** that humans need to run:

### 1. **`just build`** - Build but don't run
- **Complete pipeline** through all updates
- **Smart detection** of what needs updating
- **Automatic queue management** for changed files
- **Site updates integration** when needed
- **Docusaurus build** with error detection
- **Result**: Site is built and ready, but not served

### 2. **`just dev`** - Build and run (DEFAULT)
- **Complete pipeline** through all updates
- **Smart detection** of what needs updating
- **Automatic queue management** for changed files
- **Site updates integration** when needed
- **Docusaurus build** with error detection
- **Development server** starts automatically
- **Result**: Site is built and served at http://localhost:3000

### 3. **`just serve`** - Run, don't build
- **Fast startup** - no rebuilding
- **Uses existing build** if available
- **Perfect for** when no modifications were made recently
- **Result**: Server starts immediately (if build exists)

### 4. **`just clean`** - Stop all connections
- **Stops all processes** (docusaurus, npm, etc.)
- **Frees up ports** (especially port 3000)
- **Clean shutdown** for development
- **Result**: All processes stopped, ports freed

---

## 🧠 **Smart Update Pipeline (Automatic)**

The system automatically detects what needs updating based on **file modification dates**:

### **File Change Detection**
- **Jupyter Notebooks** (`.ipynb`) → Added to rebuild queue as `ipynb_to_md`
- **Markdown Files** (`.md`) → Added to rebuild queue as `md_to_html`
- **Site Updates** (`.md` in `site_updates/`) → Triggers site updates workflow

### **Smart Logic**
1. **Scans all directories** for modified files since last build
2. **Compares timestamps** to determine what changed
3. **Adds files to queue** automatically
4. **Processes queue** if items exist
5. **Updates site updates** if `.md` files changed
6. **Builds Docusaurus** with complete pipeline

### **Build State Tracking**
- **`.build_state.json`** tracks last build time
- **File timestamps** recorded for future comparisons
- **Incremental updates** - only process what changed
- **No unnecessary work** - skip unchanged files

---

## 🔧 **How It Works**

### **When you run `just dev` or `just build`:**

1. **🧠 Smart Detection**
   ```bash
   just detect-changes
   # Scans notebooks, markdown, site updates
   # Adds changed files to rebuild queue
   # Updates build state
   ```

2. **📋 Queue Processing** (if needed)
   ```bash
   just process-queue-if-needed
   # Processes ipynb_to_md conversions
   # Processes md_to_html conversions
   # Clears queue when done
   ```

3. **📝 Site Updates** (if needed)
   ```bash
   just update-site-updates-if-needed
   # Adds navigation fragments to .md files
   # Converts .md to .html with pandoc
   # Updates latest post links
   # Embeds JavaScript
   ```

4. **🔨 Docusaurus Build**
   ```bash
   just build-docusaurus
   # Builds the complete site
   # Catches compilation errors
   # Creates production-ready build
   ```

5. **🌐 Server Start** (only for `just dev`)
   ```bash
   just start-dev-server
   # Starts development server
   # Live reload enabled
   # Serves at http://localhost:3000
   ```

---

## 📊 **Example Workflow**

### **Scenario 1: No Changes**
```bash
$ just dev
🧠 Smart Update Pipeline - Detecting what needs updating...
🔍 Detecting file changes...
✅ No changes detected - everything is up to date!
✅ Smart update pipeline complete!
🔨 Building Docusaurus site...
✅ Docusaurus build complete!
🌐 Starting development server...
🚀 Server starting at http://localhost:3000
```

### **Scenario 2: Notebook Modified**
```bash
$ just dev
🧠 Smart Update Pipeline - Detecting what needs updating...
🔍 Detecting file changes...
📓 Found 1 changed notebook:
  - notes/Python/example.ipynb
🔄 Files have been added to the rebuild queue
📋 Processing rebuild queue...
✅ Processed: notes/Python/example.ipynb
✅ Smart update pipeline complete!
🔨 Building Docusaurus site...
✅ Docusaurus build complete!
🌐 Starting development server...
```

### **Scenario 3: Site Updates Modified**
```bash
$ just dev
🧠 Smart Update Pipeline - Detecting what needs updating...
🔍 Detecting file changes...
📋 Found 2 changed site update files:
  - site_updates/new_post.md
📝 Site updates need refreshing
🔄 Complete site updates workflow...
✅ Site updates build complete!
✅ Smart update pipeline complete!
🔨 Building Docusaurus site...
✅ Docusaurus build complete!
🌐 Starting development server...
```

---

## 🎯 **Usage Patterns**

### **Daily Development**
```bash
# Start development (builds everything needed)
just dev

# Make changes to files...

# Restart server (no rebuild needed)
just clean
just serve
```

### **Production Build**
```bash
# Build everything for deployment
just build

# Check build output
ls build/
```

### **Quick Testing**
```bash
# Test existing build without rebuilding
just serve

# Stop when done
just clean
```

---

## 🔍 **Utility Commands**

### **Queue Management**
```bash
just queue-show      # Show current rebuild queue
just queue-clear     # Clear rebuild queue
```

### **Manual Workflows**
```bash
just site-updates-full  # Manual site updates workflow
just smart-update-pipeline  # Run complete update detection
```

### **Help**
```bash
just help  # Show all available commands
```

---

## 🚨 **Error Detection & Recovery**

### **Build Errors**
- **MDX compilation errors** are caught during build
- **Broken links** are reported with specific file paths
- **Build fails** if critical errors are found
- **Error logs** saved to `build-errors.log`

### **Queue Failures**
- **Individual file failures** don't stop the pipeline
- **Failed files** are logged with specific errors
- **Successful files** are processed normally
- **Queue is cleared** after processing

### **Recovery**
- **Run `just clean`** to stop all processes
- **Fix the specific error** in the reported file
- **Run `just dev`** again to retry
- **System automatically** detects what needs updating

---

## ✨ **Benefits**

### **🚀 Streamlined Workflow**
- **Only 4 main commands** to remember
- **Automatic detection** of what needs updating
- **No manual queue management** required
- **Smart incremental builds** - only process changed files

### **🧠 Intelligent Automation**
- **File modification tracking** for efficient builds
- **Automatic queue management** for conversions
- **Site updates integration** when needed
- **Error detection** and reporting

### **⚡ Performance**
- **Skip unchanged files** automatically
- **Parallel processing** where possible
- **Incremental builds** for faster development
- **Smart caching** of build state

### **🔧 Developer Experience**
- **One command** (`just dev`) handles everything
- **Clear error messages** with specific file paths
- **Automatic recovery** from common issues
- **Consistent workflow** across all file types

---

## 🎉 **Success!**

You now have a **streamlined, intelligent build system** that:

1. **Automatically detects** what needs updating
2. **Manages the rebuild queue** intelligently
3. **Integrates site updates** seamlessly
4. **Provides exactly 4 commands** you need to remember
5. **Handles errors gracefully** with clear reporting
6. **Optimizes performance** by skipping unchanged files

**Just run `just dev` and let the system handle everything else!** 🚀
