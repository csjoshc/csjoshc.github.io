# Cursor Rules Directory

This directory contains rule files that guide AI agent behavior and provide contextual information for different file types and development workflows.

## 📁 File Organization

### Rule Categories (by number prefix):

| Range     | Category          | Purpose                              |
| --------- | ----------------- | ------------------------------------ |
| **01**    | Context Detection | Smart rule application system        |
| **10-19** | General Standards | Universal development practices      |
| **20-29** | CSS Rules         | Styling and frontend guidelines      |
| **30-39** | Python Rules      | Python development standards         |
| **40-49** | Jupyter Rules     | Notebook-specific guidelines         |
| **50-59** | File Management   | Build and synchronization rules      |
| **60-69** | AI Interaction    | Agent behavior and workflow patterns |
| **70-79** | HTML Rules        | Markup and accessibility standards   |
| **80-89** | JavaScript Rules  | JS/TS development guidelines         |
| **90-99** | Terminal Rules    | Command-line and shell safety        |
| **91**    | Git Standards     | Commit message and attribution rules |

## 🎯 How Rules Are Applied

### Context-Aware Rule Selection

#### **Smart Rule Application**

- **Context Analysis**: Rules analyze query/task type BEFORE applying standards
- **File Type Matching**: Applied based on `globs` patterns in YAML frontmatter
- **Context-Aware Filtering**: Development rules only apply to development tasks
- **Query Classification**: Automatically detects informational vs development queries
- **Conditional Application**: Development rules use `alwaysApply: false` + context checking

#### **Rule Application Hierarchy**

1. **Context Detection** (01-context-detection.mdc) - Determines applicable rules
2. **Relevant Standards** - Only contextually-appropriate rules
3. **Safety Protocols** - Always apply for terminal operations

#### **Context Types**

- **Informational**: "what files are here?", "show me the rules"
- **Development**: "write code", "fix this function", "create component"
- **Operational**: "run build", "deploy", "check status"
- **Documentation**: "write docs", "create guide", "update README"

### Example Rule Structure:

```yaml
---
description: CSS quality standards and validation requirements
globs:
  - "*.css"
  - "*.module.css"
alwaysApply: true
---
# Rule content here...
```

## 📋 Current Rule Coverage

| Context Type            | Active Rules                          | Count   |
| ----------------------- | ------------------------------------- | ------- |
| **All Contexts**        | 01 (Context Detection)                | 1 rule  |
| **Informational**       | 10, 60, 90 (General + AI + Terminal)  | 3 rules |
| **Development**         | All relevant standards + safety       | varies  |
| `*.css`, `*.module.css` | 21-26 (CSS Standards)                 | 6 rules |
| `*.py`                  | 31-34 + 51,52,54 (Python + File Mgmt) | 7 rules |
| `*.js`, `*.ts`, `*.tsx` | 60, 70, 80 (AI + HTML + JS)           | 3 rules |
| `*.ipynb`               | 40 + 51,52,54 (Jupyter + File Mgmt)   | 4 rules |
| `*.md`, `*.mdc`         | 10, 60 (General + AI)                 | 2 rules |
| `*.html`, `*.htm`       | 70 (HTML Standards)                   | 1 rule  |
| Shell scripts           | 90 (Terminal Management)              | 1 rule  |
| Git operations          | 91 (Git Commit Standards)             | 1 rule  |

### **Rule Application Strategy**

| Rule Type             | `alwaysApply` | `contextAware` | When Applied                             |
| --------------------- | ------------- | -------------- | ---------------------------------------- |
| **Context Detection** | `true`        | N/A            | Always (priority 1)                      |
| **Development Rules** | `false`       | `true`         | Only in development/operational contexts |
| **General Rules**     | `true`        | N/A            | Always apply                             |
| **Safety Rules**      | `true`        | N/A            | Always apply for protection              |

## 🔧 Rule File Format

Each `.mdc` file contains:

1. **YAML Frontmatter**: Metadata and configuration
2. **Markdown Content**: Guidelines, standards, and best practices
3. **Structured Sections**: Clear headings and organized content

## 🚀 Best Practices

### Writing New Rules:

- Use consistent numbering scheme
- Include clear `description` in frontmatter
- Set `alwaysApply` appropriately (usually `true` for standards)
- Use specific `globs` patterns for targeted application

### Rule Maintenance:

- Keep rules focused and concise
- Update when development practices change
- Test rule application with different file types

## 📊 Validation

Run validation to ensure rules are properly formatted:

```bash
# Check all rules have valid YAML
find .cursor/rules -name "*.mdc" -exec head -5 {} \; | grep -A2 "^---$"
```

## 🎯 AI Agent Integration

The rules in this directory provide:

- **Contextual Guidance**: File-type specific development standards
- **Workflow Optimization**: Streamlined development processes
- **Quality Assurance**: Consistent code and documentation standards
- **Safety Protocols**: Terminal and command-line best practices

---

**Last Updated**: December 2024
**Total Rules**: 22 files (including context detection)
**Coverage**: Context-aware application for all major file types and workflows
