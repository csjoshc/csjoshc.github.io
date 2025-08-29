#!/usr/bin/env python3
"""
Test script that mimics exactly what the notebook does.
"""

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

# Add current directory to Python path to find utils.py
current_dir = os.getcwd()
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
    print(f"Added {current_dir} to Python path")

# Import from utils module
from utils import setup_pandas_notebook
print("✓ Successfully imported setup_pandas_notebook")

# Setup notebook environment (sets working directory and verifies tags.csv)
working_dir = setup_pandas_notebook()

# Load the data
tags = pd.read_csv("tags.csv")
print(f"✓ Data loaded successfully! Shape: {tags.shape}")
print(f"✓ First few rows:")
print(tags.head())
