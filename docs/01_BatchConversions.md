```python
import sys, IPython
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```
    /home/jcmint/anaconda3/envs/learningenv/bin/python
# Batch compiling 

## Converting from `.ipynb` to `.md`
First step is to convert all `.ipynb` files in the main directory and its subdirectories. This is necessary because nbconvert straight to html doesn't keep the page background color (solid black). Here I filter by file extension and recent modification date (past day)
```python
! cd ..; find . -name "*.ipynb" -mtime -1  -exec jupyter nbconvert --to markdown {} \;
#  ipynb
```
## Converting from `.md` to `.md`
The final step is convering all `.md` files that were recently modified. 
```python
# ! cd ..;  find ./ -iname "*.ipynb" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s -M -o ${0%.ipynb}.md' {} \;
```
```python
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s --toc --highlight-style breezedark -M date="`date "+%B %e, %Y"`" -f markdown_strict+backtick_code_blocks+auto_identifiers  -t html  -o  ${0%.md}.md' {} \;
# -mtime -1
```
      1213322      4 -rwxrwxrwx   1 jcmint   jcmint       1450 May 10 04:03 ./notes/General/CS50x2019/basics.md
      1161675      8 -rwxrwxrwx   1 jcmint   jcmint       6494 May 11 00:43 ./notes/Python/IntroCompThinkDataSci/unit3/unit3.md
      1221583      4 -rwxrwxrwx   1 jcmint   jcmint       2028 May 10 04:31 ./site_updates/5_2019/11_5_2019.md
      1157243      1 -rwxrwxrwx   1 jcmint   jcmint        577 May 11 00:52 ./site_updates/base.md
      1157554      4 -rwxrwxrwx   1 jcmint   jcmint       1836 May 10 23:37 ./utils/01_BatchConversions.md
```python
```