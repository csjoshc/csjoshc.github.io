
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
! cd ..; find . -name "*.ipynb" -mtime -1 -exec jupyter nbconvert --to markdown {} \;
```

    [NbConvertApp] Converting notebook ./notes/Python/General/virtenv_jupyter_nb.ipynb to markdown
    [NbConvertApp] Writing 3977 bytes to ./notes/Python/General/virtenv_jupyter_nb.md
    [NbConvertApp] Converting notebook ./notes/Python/ProbabilityandStatistics/1_Introduction.ipynb to markdown
    [NbConvertApp] Writing 1645 bytes to ./notes/Python/ProbabilityandStatistics/1_Introduction.md
    [NbConvertApp] Converting notebook ./notes/Python/ProbabilityandStatistics/2_Sets.ipynb to markdown
    [NbConvertApp] Writing 7509 bytes to ./notes/Python/ProbabilityandStatistics/2_Sets.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/1_Introduction.ipynb to markdown
    [NbConvertApp] Writing 3733 bytes to ./notes/Python/PythonforDataScience/1_Introduction.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/2_Basics.ipynb to markdown
    [NbConvertApp] Writing 3963 bytes to ./notes/Python/PythonforDataScience/2_Basics.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/3_Numpy.ipynb to markdown
    [NbConvertApp] Writing 7336 bytes to ./notes/Python/PythonforDataScience/3_Numpy.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas.ipynb to markdown
    [NbConvertApp] Writing 7192 bytes to ./notes/Python/PythonforDataScience/4_Pandas.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas2.ipynb to markdown
    [NbConvertApp] Writing 2111 bytes to ./notes/Python/PythonforDataScience/4_Pandas2.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/5_visualization.ipynb to markdown
    [NbConvertApp] Writing 1011 bytes to ./notes/Python/PythonforDataScience/5_visualization.md
    [NbConvertApp] Converting notebook ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 5607 bytes to ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
    [NbConvertApp] Converting notebook ./utils/01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 5607 bytes to ./utils/01_BatchConversions.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -f markdown -t html  -o  ${0%.md}.html' {} \;
```
