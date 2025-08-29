#!/bin/bash

# Setup virtual environment for Python development at repository root

echo "Setting up virtual environment for Python development..."

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python 3 not found. Please install Python 3.8+ first."
    exit 1
fi

echo "Using Python: $($PYTHON_CMD --version)"

# Create virtual environment at repository root
echo "Creating virtual environment at repository root..."
$PYTHON_CMD -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

echo ""
echo "Virtual environment setup complete!"
echo ""
echo "Virtual environment location: .venv/ (repository root)"
echo "Python path: $(which python)"
echo ""
echo "To activate the environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To deactivate, run:"
echo "  deactivate"
echo ""
echo "To start Jupyter notebook, run:"
echo "  jupyter notebook"
echo ""
echo "Or to start Jupyter lab:"
echo "  jupyter lab"
echo ""
echo "Note: This environment is now at the repository root and will be"
echo "automatically detected by Cursor and other IDEs."
