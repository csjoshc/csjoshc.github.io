#!/usr/bin/env python3
"""
Template Processing Script for Navigation
This script processes markdown files and adds consistent navigation templates.
"""

import os
import re
import glob
from pathlib import Path

# Navigation templates for different sections
NAVIGATION_TEMPLATES = {
    'python_datascience': {
        'pattern': r'Python/PythonforDataScience/',
        'template': '''<!-- Python Data Science Navigation Template -->
<!-- This template provides navigation for Python data science pages -->

<div class="return-navigation">
  <a href="../../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="../base.html" class="nav-button portal-button">🐍 Python</a>
</div>

<!-- Content starts here -->

'''
    },
    'python_datascience_notebook': {
        'pattern': r'Python/PythonforDataScience/.*\.ipynb',
        'template': '''<!-- Python Data Science Notebook Navigation Template -->
<!-- This template provides navigation for Python Data Science notebook pages -->

<div class="return-navigation">
  <a href="../../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="../base.html" class="nav-button portal-button">🐍 Python</a>
  <a href="base.html" class="nav-button section-button">📊 Data Science</a>
</div>

<!-- Content starts here -->

'''
    },
    'python_general': {
        'pattern': r'Python/General/',
        'template': '''<!-- Python General Navigation Template -->
<!-- This template provides navigation for Python General pages -->

<div class="return-navigation">
  <a href="../../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="../base.html" class="nav-button portal-button">🐍 Python</a>
</div>

<!-- Content starts here -->

'''
    },
    'python_general_notebook': {
        'pattern': r'Python/General/.*\.ipynb',
        'template': '''<!-- Python General Notebook Navigation Template -->
<!-- This template provides navigation for Python General notebook pages -->

<div class="return-navigation">
  <a href="../../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="../base.html" class="nav-button portal-button">🐍 Python</a>
  <a href="base.html" class="nav-button section-button">🔧 General</a>
</div>

<!-- Content starts here -->

'''
    },
    'python_probability_notebook': {
        'pattern': r'Python/ProbabilityandStatistics/.*\.ipynb',
        'template': '''<!-- Python Probability & Statistics Notebook Navigation Template -->
<!-- This template provides navigation for Python Probability & Statistics notebook pages -->

<div class="return-navigation">
  <a href="../../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="../base.html" class="nav-button portal-button">🐍 Python</a>
  <a href="base.html" class="nav-button section-button">📈 Probability & Stats</a>
</div>

<!-- Content starts here -->

'''
    },
    'python_portal': {
        'pattern': r'Python/',
        'template': '''<!-- Python Portal Navigation Template -->
<!-- This template provides navigation for Python Portal pages -->

<div class="return-navigation">
  <a href="../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="base.html" class="nav-button portal-button">🐍 Python</a>
</div>

<!-- Content starts here -->

'''
    },
    'general': {
        'pattern': r'General/',
        'template': '''<!-- General Navigation Template -->
<!-- This template provides navigation for General topic pages -->

<div class="return-navigation">
  <a href="../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="base.html" class="nav-button portal-button">📚 General</a>
</div>

<!-- Content starts here -->

'''
    },
    'linux': {
        'pattern': r'Linux/',
        'template': '''<!-- Linux Navigation Template -->
<!-- This template provides navigation for Linux pages -->

<div class="return-navigation">
  <a href="../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="base.html" class="nav-button portal-button">🐧 Linux</a>
</div>

<!-- Content starts here -->

'''
    },
    'devops': {
        'pattern': r'Devops/',
        'template': '''<!-- Devops Navigation Template -->
<!-- This template provides navigation for Devops pages -->

<div class="return-navigation">
  <a href="../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="base.html" class="nav-button portal-button">⚙️ Devops</a>
</div>

<!-- Content starts here -->

'''
    },
    'github': {
        'pattern': r'Github/',
        'template': '''<!-- Github Navigation Template -->
<!-- This template provides navigation for Github pages -->

<div class="return-navigation">
  <a href="../../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="base.html" class="nav-button portal-button">🐙 Github</a>
</div>

<!-- Content starts here -->

'''
    },
    'utils': {
        'pattern': r'utils/',
        'template': '''<!-- Utilities Navigation Template -->
<!-- This template provides navigation for Utilities pages -->

<div class="return-navigation">
  <a href="../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="base.html" class="nav-button portal-button">🛠️ Utilities</a>
</div>

<!-- Content starts here -->

'''
    },
    'site_updates': {
        'pattern': r'site_updates/',
        'template': '''<!-- Site Updates Navigation Template -->
<!-- This template provides navigation for site update pages -->

<div class="return-navigation">
  <a href="../index.html" class="nav-button index-button">🏠 Home</a>
  <a href="base.html" class="nav-button portal-button">📝 Site Updates</a>
</div>

<!-- Content starts here -->

'''
    }
}

def get_navigation_template(file_path):
    """Determine which navigation template to use based on file path."""
    # Sort templates by specificity (longer patterns first)
    sorted_templates = sorted(NAVIGATION_TEMPLATES.items(), 
                            key=lambda x: len(x[1]['pattern']), reverse=True)
    
    for section, config in sorted_templates:
        if re.search(config['pattern'], file_path):
            return config['template']
    return None

def add_navigation_to_file(file_path):
    """Add navigation template to a markdown file if it doesn't already have it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has navigation
        if '<!-- Content starts here -->' in content:
            print(f"✓ {file_path} already has navigation")
            return False
        
        # Get appropriate navigation template
        template = get_navigation_template(file_path)
        if not template:
            print(f"⚠ {file_path} - no template found")
            return False
        
        # Add navigation at the beginning
        new_content = template + content
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ Added navigation to {file_path}")
        return True
        
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def process_all_files(docs_dir):
    """Process all markdown files in the docs directory."""
    markdown_files = glob.glob(os.path.join(docs_dir, '**/*.md'), recursive=True)
    
    # Filter out template files and README files
    markdown_files = [f for f in markdown_files 
                     if not f.endswith('README.md') 
                     and '_templates' not in f
                     and not f.endswith('base.md')]
    
    print(f"Found {len(markdown_files)} markdown files to process")
    
    processed_count = 0
    for file_path in markdown_files:
        if add_navigation_to_file(file_path):
            processed_count += 1
    
    print(f"\nProcessing complete! Added navigation to {processed_count} files.")

if __name__ == "__main__":
    docs_dir = "."  # Current directory
    process_all_files(docs_dir)
