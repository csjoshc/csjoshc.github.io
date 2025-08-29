# Python for Data Science - Notebooks

This directory contains Jupyter notebooks for learning Python data science concepts.

## 🚀 **Quick Start**

### 1. Activate the Virtual Environment

```bash
# From the repository root (csjoshc.github.io/)
source .venv/bin/activate

# Or navigate to this directory and activate from root
cd notes/Python/PythonforDataScience
source ../../.venv/bin/activate
```

### 2. Start Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook

# Or start Jupyter Lab (recommended)
jupyter lab
```

### 3. Deactivate When Done

```bash
deactivate
```

## 📚 **Complete Setup Documentation**

**For full setup instructions, see the main Python setup guide:**

- **[🐍 Complete Python Setup Guide](../../../PYTHON_SETUP.md)** - Virtual environment, packages, and Cursor integration
- **[📦 Package Requirements](../../../requirements.txt)** - All required Python packages
- **[🔧 Environment Setup Script](../../../setup_venv.sh)** - Automated environment creation

## 🎯 **Why Repository Root Setup?**

- **Cursor Integration**: Cursor automatically detects `.venv` at repo root
- **Global Access**: All Python files use the same environment
- **Consistency**: Single source of truth for Python packages
- **IDE Support**: Better integration with VS Code, PyCharm, etc.

## 📁 **Notebook Contents**

### Core Data Science

- **Introduction** (`1_Introduction.ipynb`) - Getting started with Python
- **Basics** (`2_Basics.ipynb`) - Python fundamentals
- **NumPy** (`3_Numpy.ipynb`) - Numerical computing
- **Pandas Series** (`4_Pandas.ipynb`) - Data structures
- **DataFrames** (`4_Pandas2.ipynb`, `4_Pandas3.ipynb`, `4_Pandas4.ipynb`) - Data manipulation
- **Strings & Timestamps** (`4_Pandas5.ipynb`) - Text and time data
- **Visualization** (`5_Matplotlib.ipynb`) - Plotting and charts

### Machine Learning

- **Overview** (`7_ML.ipynb`) - ML concepts and workflow
- **Regression** (`7_ML_Reg.ipynb`) - Linear and polynomial regression
- **Decision Trees** (`7_ML_DT.ipynb`) - Classification with trees
- **Clustering** (`7_ML_Clust.ipynb`) - Unsupervised learning

## 🔧 **Troubleshooting**

### If packages are missing:

```bash
# Ensure you're using the repository root environment
source ../../../.venv/bin/activate

# Verify packages
pip list | grep pandas
```

### If you get import errors:

- Check that the virtual environment is activated
- Verify you're using the repository root `.venv`
- Ensure all packages are installed: `pip install -r ../../../requirements.txt`

## 📖 **Learning Path**

1. Start with **Introduction** and **Basics**
2. Learn **NumPy** for numerical operations
3. Master **Pandas** for data manipulation
4. Explore **Matplotlib** for visualization
5. Dive into **Machine Learning** concepts

## 🎉 **Ready to Learn!**

Your Python data science environment is fully configured at the repository root. Start with the notebooks and happy learning! 🐍📊
