#!/usr/bin/env python3
"""
Test script to simulate running the first cell of the notebook interactively
"""

print("=== SIMULATING JUPYTER INTERACTIVE EXECUTION ===")

import sys
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plte 
import os, sys

# Import and use utility functions
import sys
import os

# Multiple strategies to find utils.py
notebook_dir_candidates = [
    os.getcwd(),  # Current working directory
    '/Users/joshchiu/repos/csjoshc.github.io/notes/Python/PythonforDataScience',  # Absolute path to notebook directory
    os.path.dirname(os.path.abspath('4_Pandas5.ipynb')) if os.path.exists('4_Pandas5.ipynb') else None,  # Directory of this notebook
]

# Remove None values
notebook_dir_candidates = [d for d in notebook_dir_candidates if d is not None]

print(f"Current working directory: {os.getcwd()}")
print(f"Searching for utils.py in:")

utils_found = False
utils_dir = None

for candidate_dir in notebook_dir_candidates:
    utils_path = os.path.join(candidate_dir, 'utils.py')
    print(f"  {candidate_dir} -> utils.py exists: {os.path.exists(utils_path)}")
    
    if os.path.exists(utils_path) and not utils_found:
        utils_dir = candidate_dir
        utils_found = True
        print(f"  ✓ Found utils.py in: {utils_dir}")

if utils_found and utils_dir not in sys.path:
    sys.path.insert(0, utils_dir)
    print(f"Added {utils_dir} to Python path")
elif not utils_found:
    print("⚠ utils.py not found in any candidate directories")
    print("Available files in current directory:", os.listdir('.'))

# Clear any cached imports to avoid stale import errors
if 'utils' in sys.modules:
    del sys.modules['utils']
    print("Cleared cached utils module")

# Import from utils module
try:
    from utils import setup_pandas_notebook
    print("✓ Successfully imported setup_pandas_notebook")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print(f"Current sys.path first 3 entries: {sys.path[:3]}")
    print(f"utils module in sys.modules: {'utils' in sys.modules}")
    print(f"Files in current directory: {[f for f in os.listdir('.') if f.endswith('.py')]}")
    raise

# Setup notebook environment (sets working directory and verifies tags.csv)
working_dir = setup_pandas_notebook()

# Load the data
tags = pd.read_csv("tags.csv")
print(f"✓ Data loaded successfully! Shape: {tags.shape}")
