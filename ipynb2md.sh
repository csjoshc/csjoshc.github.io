find . -name "*.ipynb" -mtime -30  -exec jupyter nbconvert --to markdown {} \;
