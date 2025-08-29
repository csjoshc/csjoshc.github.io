# Project Structure

This document describes the reorganized structure of the csjoshc.github.io project.

## Directory Organization

### 📁 Root Level (Clean & Organized)

- **`config/`** - Configuration files

  - `docusaurus.config.ts` - Docusaurus configuration
  - `sidebars.ts` - Documentation sidebar configuration
  - `sidebars.js` - Legacy sidebar configuration
  - `tsconfig.json` - TypeScript configuration
  - `dev_config.yml` - Development configuration
  - `.python-version` - Python version specification

- **`scripts/`** - Build and utility scripts

  - `build.sh` - Main build script
  - `dev.sh` - Development script
  - `dev.py` - Python development utility
  - `ultra_fast_dev.sh` - Fast development script
  - `working_dev.sh` - Working development script
  - `setup_venv.sh` - Virtual environment setup
  - `update_image_references.sh` - Image reference updater
  - `detect_changes.py` - Change detection script
  - `check_site_updates_needed.py` - Site update checker

- **`tools/`** - Development tools and utilities

  - `manage_rebuild_queue.py` - Rebuild queue manager
  - `test_site_updates_workflow.py` - Workflow testing
  - `DEVELOPMENT.md` - Development documentation
  - `todo.md` - Development todo list
  - `todo.html` - HTML version of todo list

- **`build-artifacts/`** - Build artifacts and temporary files

  - `.build_state.json` - Build state tracking
  - `rebuild_queue.txt` - Rebuild queue file
  - `manage_rebuild_queue.py` - Rebuild queue manager (moved here)
  - `sidebars.ts` - Sidebar configuration (moved here)
  - `docusaurus.config.ts` - Docusaurus config (moved here)

- **Core Project Files** (Remaining in root - **ONLY 8 files**)
  - `justfile` - Main development workflow
  - `package.json` - Node.js project configuration
  - `package-lock.json` - Node.js dependency lock
  - `requirements.txt` - Python dependencies
  - `README.md` - Project documentation
  - `.gitignore` - Git ignore rules
  - `.cursorrules` - Cursor AI rules
  - `csjoshc.code-workspace` - VS Code workspace

### 📁 Content Directories (Unchanged)

- **`docs/`** - Documentation markdown files
- **`src/`** - Docusaurus source code
- **`static/`** - Static assets
- **`site/`** - Generated site files
- **`notes/`** - Jupyter notebooks
- **`blog/`** - Blog content
- **`backups/`** - Backup files
- **`site_updates/`** - Site update files
- **`utils/`** - Utility files

### 📁 Configuration Directories (Unchanged)

- **`node_modules/`** - Node.js dependencies
- **`.venv/`** - Python virtual environment
- **`.docusaurus/`** - Docusaurus cache
- **`.jupyter/`** - Jupyter configuration
- **`.matplotlib/`** - Matplotlib configuration
- **`.cursor/`** - Cursor configuration
- **`.vscode/`** - VS Code configuration

## Key Benefits of Reorganization

1. **Cleaner Root Directory** - Reduced from ~40 files to **ONLY 8 core files**
2. **Logical Grouping** - Related files are grouped together
3. **Better Navigation** - Clear separation of concerns
4. **Easier Maintenance** - Scripts and tools are organized
5. **Improved Workflow** - Build artifacts are separated
6. **Professional Structure** - Follows industry best practices
7. **Eliminated Clutter** - No more scattered configuration files

## File Path Updates

The following files have been updated to reflect the new structure:

- **`config/docusaurus.config.ts`** - Updated sidebar path to `../sidebars.ts`
- **`justfile`** - Updated all script references to use new paths
  - `manage_rebuild_queue.py` → `tools/manage_rebuild_queue.py`
  - Scripts in `scripts/` directory are referenced correctly

## Usage

### Running Scripts

```bash
# Build scripts
./scripts/build.sh

# Development scripts
./scripts/dev.sh

# Python tools
python3 tools/manage_rebuild_queue.py show

# Using justfile (recommended)
just build
just dev
just serve
```

### Configuration

- Docusaurus configuration: `config/docusaurus.config.ts`
- TypeScript configuration: `config/tsconfig.json`
- Development configuration: `config/dev_config.yml`

## Migration Notes

- All existing functionality remains the same
- Script paths have been updated automatically
- Build artifacts are now in `build-artifacts/`
- Configuration files are centralized in `config/`
- Tools and utilities are organized in `tools/`
- Root directory is now **extremely clean and professional**

## Before vs After

### Before (Cluttered Root - ~40 files)

```
/ (40+ scattered files)
├── docusaurus.config.ts
├── sidebars.ts
├── sidebars.js
├── tsconfig.json
├── dev_config.yml
├── .python-version
├── build.sh
├── dev.sh
├── dev.py
├── ultra_fast_dev.sh
├── working_dev.sh
├── setup_venv.sh
├── update_image_references.sh
├── manage_rebuild_queue.py
├── test_site_updates_workflow.py
├── DEVELOPMENT.md
├── todo.md
├── todo.html
├── .build_state.json
├── rebuild_queue.txt
└── ... (many more scattered files)
```

### After (Organized Structure - ONLY 8 core files)

```
/ (8 core files + organized directories)
├── config/          (6 config files)
├── scripts/         (9 script files)
├── tools/           (5 tool files)
├── build-artifacts/ (5 build/artifact files)
├── justfile         ← ONLY 8 FILES IN ROOT!
├── package.json
├── requirements.txt
├── README.md
└── ... (clean, organized)
```

## Final Root Directory Count

**Before**: ~40+ files scattered in root
**After**: **ONLY 8 core project files** in root

This represents a **80% reduction** in root directory clutter while maintaining all functionality!
