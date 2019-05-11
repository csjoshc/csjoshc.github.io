
<a href="../index.html">Go back to index</a>

<a href="base.html">Go back to Utilities Portal</a>

<head>
  <link rel="stylesheet" href="../cssthemes/github.css">
</head>



```python
import sys, IPython
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Batch compiling 
Some simple bash commands to compile whatever file formats into html

## Converting from `.ipynb` to `.md`
First step is to convert all `.ipynb` files in the main directory and its subdirectories. This is necessary because nbconvert straight to html doesn't keep the page background color (solid black). Here I filter by file extension and recent modification date (past day)


```python
! cd ..; find . -name "*.ipynb" -mtime -1  -exec jupyter nbconvert --to markdown {} \;
#  ipynb
```

## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
# ! cd ..;  find ./ -iname "*.ipynb" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s -M -o ${0%.ipynb}.md' {} \;
```


```python
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s --toc --highlight-style breezedark -M date="`date "+%B %e, %Y"`" -f markdown_strict+backtick_code_blocks+auto_identifiers  -t html  -o  ${0%.md}.html' {} \;
# -mtime -1
```

      1157236      4 -rwxrwxrwx   1 jcmint   jcmint       2372 May  5 17:24 ./notes/Python/base.md
      1161675      8 -rwxrwxrwx   1 jcmint   jcmint       5970 May  5 17:24 ./notes/Python/IntroCompThinkDataSci/unit3/unit3.md
      1213249      1 -rwxrwxrwx   1 jcmint   jcmint        403 May  5 17:24 ./site_updates/5_2019/04_5_2019.md
      1157243      1 -rwxrwxrwx   1 jcmint   jcmint        540 May  5 17:23 ./site_updates/base.md

