find . -name "*.ipynb" -mtime -7  -exec jupyter nbconvert --to markdown {} \;
