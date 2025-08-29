#!/usr/bin/env python3
"""
Utility functions for Jupyter notebooks.
"""

import os
import sys
from pathlib import Path

def set_notebook_working_directory():
    """
    Set the working directory to the location of the current notebook.
    
    Returns:
        str: The path of the working directory that was set
    """
    try:
        # Method 1: Try to get notebook path from Jupyter environment
        from IPython import get_ipython
        ipython = get_ipython()
        
        if ipython and hasattr(ipython, "kernel"):
            # Get the notebook path from kernel info
            try:
                kernel_info = ipython.kernel.kernel_info()
                if isinstance(kernel_info, dict) and "notebook_path" in kernel_info:
                    notebook_path = os.path.dirname(kernel_info["notebook_path"])
                    os.chdir(notebook_path)
                    print(f"✓ Changed to notebook directory: {os.getcwd()}")
                    return os.getcwd()
            except Exception as e:
                print(f"  (Could not get kernel info: {e})")
        
        # Method 2: Try to get from Jupyter environment variables
        if 'JUPYTER_SERVER_ROOT' in os.environ:
            jupyter_root = os.environ['JUPYTER_SERVER_ROOT']
            current_dir = os.getcwd()
            if jupyter_root in current_dir:
                # We're in a Jupyter environment, use current directory
                print(f"✓ Using Jupyter environment directory: {current_dir}")
                return current_dir
        
        # Method 3: Fallback to current directory
        current_dir = os.getcwd()
        print(f"✓ Using current directory: {current_dir}")
        return current_dir
        
    except Exception as e:
        # Final fallback: use current directory
        current_dir = os.getcwd()
        print(f"✓ Using current directory: {current_dir}")
        print(f"  (Could not determine notebook path: {e})")
        return current_dir

def verify_data_file(filename, required=True):
    """
    Verify that a data file exists in the current working directory.
    
    Args:
        filename (str): Name of the file to check
        required (bool): If True, raises FileNotFoundError if file doesn't exist
    
    Returns:
        bool: True if file exists, False otherwise
        
    Raises:
        FileNotFoundError: If required=True and file doesn't exist
    """
    if os.path.exists(filename):
        print(f"✓ {filename} found in current directory")
        return True
    else:
        print(f"⚠ {filename} not found in current directory")
        print(f"  Current directory: {os.getcwd()}")
        print(f"  Current directory contents: {os.listdir('.')}")
        
        if required:
            raise FileNotFoundError(f"Required data file '{filename}' not found in {os.getcwd()}")
        return False

def setup_notebook_environment(data_files=None):
    """
    Complete setup function for notebooks.
    
    Args:
        data_files (list): List of required data file names
    
    Returns:
        str: The working directory that was set
    """
    print("Setting up notebook environment...")
    
    # Set working directory
    working_dir = set_notebook_working_directory()
    
    # Verify data files if specified
    if data_files:
        for filename in data_files:
            verify_data_file(filename, required=True)
    
    print("✓ Notebook environment setup complete!")
    return working_dir

def setup_pandas_notebook():
    """
    Setup function specifically for pandas notebooks with tags.csv
    """
    return setup_notebook_environment(data_files=['tags.csv'])

# Debug function to help troubleshoot import issues
def debug_import():
    """Debug function to help troubleshoot import issues"""
    print("=== DEBUG INFO ===")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python path: {sys.path}")
    print(f"utils.py location: {os.path.abspath(__file__)}")
    print(f"utils.py exists: {os.path.exists(__file__)}")
    print("=== END DEBUG ===")

# Test if this module can be imported
if __name__ == "__main__":
    print("utils.py module loaded successfully!")
    debug_import()
