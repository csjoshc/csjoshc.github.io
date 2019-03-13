
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

    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas2.ipynb to markdown
    [NbConvertApp] Writing 5224 bytes to ./notes/Python/PythonforDataScience/4_Pandas2.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas3.ipynb to markdown
    [NbConvertApp] Writing 4902 bytes to ./notes/Python/PythonforDataScience/4_Pandas3.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas4.ipynb to markdown
    [NbConvertApp] Support files will be in 4_Pandas4_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/4_Pandas4_files
    [NbConvertApp] Writing 20271 bytes to ./notes/Python/PythonforDataScience/4_Pandas4.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_pandas5.ipynb to markdown
    [NbConvertApp] Writing 6371 bytes to ./notes/Python/PythonforDataScience/4_pandas5.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/5_visualization.ipynb to markdown
    [NbConvertApp] Writing 1026 bytes to ./notes/Python/PythonforDataScience/5_visualization.md
    [NbConvertApp] Converting notebook ./utils/01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 3956 bytes to ./utils/01_BatchConversions.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -f markdown -t html  -o  ${0%.md}.html' {} \;
```

      1157236      4 -rwxrwxrwx   1 jcmint   jcmint       1017 Mar 11 22:56 ./notes/Python/base.md
      1157209      8 -rwxrwxrwx   1 jcmint   jcmint       7559 Mar 11 22:57 ./notes/Python/ProbabilityandStatistics/2_Sets.md
      1157223      8 -rwxrwxrwx   1 jcmint   jcmint       4475 Mar 11 22:57 ./notes/Python/PythonforDataScience/2_Basics.md
      1157226      8 -rwxrwxrwx   1 jcmint   jcmint       7857 Mar 11 22:57 ./notes/Python/PythonforDataScience/3_Numpy.md
      1157229      8 -rwxrwxrwx   1 jcmint   jcmint       7689 Mar 11 22:57 ./notes/Python/PythonforDataScience/4_Pandas.md
      1157232      8 -rwxrwxrwx   1 jcmint   jcmint       5224 Mar 12 22:39 ./notes/Python/PythonforDataScience/4_Pandas2.md
      1157386      8 -rwxrwxrwx   1 jcmint   jcmint       4902 Mar 12 22:39 ./notes/Python/PythonforDataScience/4_Pandas3.md
      1154906     20 -rwxrwxrwx   1 jcmint   jcmint      20273 Mar 12 22:39 ./notes/Python/PythonforDataScience/4_Pandas4.md
      1154907      8 -rwxrwxrwx   1 jcmint   jcmint       6371 Mar 12 22:39 ./notes/Python/PythonforDataScience/4_pandas5.md
      1157457      4 -rwxrwxrwx   1 jcmint   jcmint       1026 Mar 12 22:39 ./notes/Python/PythonforDataScience/5_visualization.md
      1157554      4 -rwxrwxrwx   1 jcmint   jcmint       3956 Mar 12 22:39 ./utils/01_BatchConversions.md
      1157584      1 -rwxrwxrwx   1 jcmint   jcmint        252 Mar 11 23:12 ./utils/base.md

