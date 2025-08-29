# 🧭 Navigation Template System
This directory contains reusable navigation templates that can be automatically inserted into markdown files to provide consistent navigation across the site.
## 📁 Available Templates
### **nav_python_datascience.md**
- **Use for**: Python for Data Science, IntroCompThinkDataSci, IntroCompSciPython, ProbabilityandStatistics, and General Python pages
- **Navigation**: Index + Python Portal
- **Path structure**: `../../../index.md` and `../base.md`
### **nav_python_portal.md**
- **Use for**: Python portal base pages
- **Navigation**: Index + Python Portal
- **Path structure**: `../../../index.md` and `../base.md`
### **nav_site_updates.md**
- **Use for**: Site update pages (3_2019, 4_2019, 5_2019, 6_2019)
- **Navigation**: Index only
- **Path structure**: `../../index.md`
### **nav_general.md**
- **Use for**: General, Devops, Github, Linux pages
- **Navigation**: Index only
- **Path structure**: `../../index.md`
### **nav_utils.md**
- **Use for**: Utility pages
- **Navigation**: Index only
- **Path structure**: `../index.md`
## 🚀 Usage
### **Automatic Insertion (Recommended)**
Use the provided Python scripts to automatically insert navigation templates:
#### **1. Insert Navigation into Existing Markdown Files**
```bash
# Dry run to see what would be changed
python3 insert_navigation.py --dry-run
# Apply changes with backup
python3 insert_navigation.py --backup
# Apply changes without backup
python3 insert_navigation.py
```
#### **2. Convert Jupyter Notebooks with Navigation**
```bash
# Convert notebooks and insert navigation
python3 ipynb2md_with_nav.py docs/Python --backup
# Dry run to see what would be converted
python3 ipynb2md_with_nav.py docs/Python --dry-run
```
### **Manual Insertion**
If you prefer to manually insert navigation, copy the appropriate template content and place it at the top of your markdown file:
```markdown


  Go back to index
  Go back to Python Portal


# Your Page Title
Your page content...
```
## 🔧 Template Customization
### **Adding New Templates**
1. Create a new template file in this directory
2. Follow the naming convention: `nav_[context].md`
3. Update the pattern matching in the Python scripts
4. Test with a few files before applying broadly
### **Template Structure**
Each template should include:
- HTML container with `return-navigation` class
- Navigation buttons with appropriate `nav-button` classes
- Relative paths that work from the target file's location
- Clear comments for maintainability
### **CSS Classes**
The templates use these CSS classes for styling:
- `.return-navigation` - Container for navigation buttons
- `.nav-button` - Base button styling
- `.index-button` - Index navigation button
- `.portal-button` - Portal navigation button
- `.section-button` - Section navigation button
## 📍 Path Calculation
### **Understanding Relative Paths**
The templates use relative paths based on the file's location in the directory structure:
- **Root level files** (e.g., `docs/index.md`): `index.md`
- **One level deep** (e.g., `docs/utils/file.md`): `../index.md`
- **Two levels deep** (e.g., `docs/General/file.md`): `../../index.md`
- **Three levels deep** (e.g., `docs/Python/file.md`): `../../../index.md`
### **Path Examples**
| File Location                              | To Index              | To Portal      |
| ------------------------------------------ | --------------------- | -------------- |
| `docs/index.md`                            | `index.md`          | N/A            |
| `docs/utils/file.md`                       | `../index.md`       | N/A            |
| `docs/General/file.md`                     | `../../index.md`    | N/A            |
| `docs/Python/file.md`                      | `../../../index.md` | `../base.md` |
| `docs/Python/PythonforDataScience/file.md` | `../../../index.md` | `../base.md` |
## 🧪 Testing
### **Before Applying to All Files**
1. **Test with dry-run**: Use `--dry-run` flag to see what would change
2. **Test with backup**: Use `--backup` flag to create backup files
3. **Test a few files**: Apply to a small subset first
4. **Verify rendering**: Check that navigation works correctly in the browser
### **Validation Checklist**
- [ ] Navigation buttons appear at the top of the page
- [ ] Links work correctly and navigate to expected pages
- [ ] Styling is consistent with the site theme
- [ ] No broken links or 404 errors
- [ ] Navigation is visible in both light and dark modes
## 🔄 Maintenance
### **Updating Templates**
When updating navigation templates:
1. **Test changes** on a few files first
2. **Update all affected files** using the automation scripts
3. **Verify consistency** across the site
4. **Update documentation** if needed
### **Adding New Navigation Patterns**
When adding new content types:
1. **Create appropriate template** in this directory
2. **Update pattern matching** in the Python scripts
3. **Test with sample files**
4. **Apply to all relevant files**
## 📚 Related Files
- **insert_navigation.py** - Script to insert navigation into existing markdown files
- **ipynb2md_with_nav.py** - Script to convert notebooks with navigation
- **Custom CSS** - Styling for navigation buttons in `docs/stylesheets/custom.css`
---
**Note**: Always test navigation changes before applying them broadly. Use the dry-run and backup options to ensure safe updates.
