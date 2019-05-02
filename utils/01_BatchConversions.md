
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
! cd ..; find . -name "*.ipynb" -mtime -7  -exec jupyter nbconvert --to markdown {} \;
#  ipynb
```

    [NbConvertApp] Converting notebook ./notes/Python/IntroCompThinkDataSci/unit2/.ipynb_checkpoints/ps2-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 2899 bytes to ./notes/Python/IntroCompThinkDataSci/unit2/.ipynb_checkpoints/ps2-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/IntroCompThinkDataSci/unit2/ps2.ipynb to markdown
    [NbConvertApp] Support files will be in ps2_files/
    [NbConvertApp] Making directory ./notes/Python/IntroCompThinkDataSci/unit2/ps2_files
    [NbConvertApp] Making directory ./notes/Python/IntroCompThinkDataSci/unit2/ps2_files
    [NbConvertApp] Writing 13272 bytes to ./notes/Python/IntroCompThinkDataSci/unit2/ps2.md
    [NbConvertApp] Converting notebook ./utils/01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 4100 bytes to ./utils/01_BatchConversions.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
# ! cd ..;  find ./ -iname "*.ipynb" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s -M -o ${0%.ipynb}.md' {} \;
```


```python
! cd ..;  find ./ -iname "*.md" -mtime -7 -ls -exec sh -c 'pandoc ${0} -s --toc --highlight-style breezedark -M date="`date "+%B %e, %Y"`" -f markdown_strict+backtick_code_blocks+auto_identifiers  -t html  -o  ${0%.md}.html' {} \;
# -mtime -1
```

      1157236      4 -rwxrwxrwx   1 jcmint   jcmint       2293 May  1 20:41 ./notes/Python/base.md
        33577      0 -rwxrwxrwx   1 jcmint   jcmint          0 Apr 25 21:57 ./notes/Python/IntroCompThinkDataSci/unit2/problemset2.md
      1159916     16 -rwxrwxrwx   1 jcmint   jcmint      13272 May  1 21:04 ./notes/Python/IntroCompThinkDataSci/unit2/ps2.md
      1157554      8 -rwxrwxrwx   1 jcmint   jcmint       4100 May  1 21:04 ./utils/01_BatchConversions.md



```python

```
