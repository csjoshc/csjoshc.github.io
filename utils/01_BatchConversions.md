
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

    [NbConvertApp] Converting notebook ./notes/Python/ProbabilityandStatistics/2_Sets.ipynb to markdown
    [NbConvertApp] Support files will be in 2_Sets_files/
    [NbConvertApp] Making directory ./notes/Python/ProbabilityandStatistics/2_Sets_files
    [NbConvertApp] Writing 7545 bytes to ./notes/Python/ProbabilityandStatistics/2_Sets.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas3-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 0 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas3-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/2_Basics.ipynb to markdown
    [NbConvertApp] Writing 4475 bytes to ./notes/Python/PythonforDataScience/2_Basics.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/3_Numpy.ipynb to markdown
    [NbConvertApp] Writing 7857 bytes to ./notes/Python/PythonforDataScience/3_Numpy.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas.ipynb to markdown
    [NbConvertApp] Writing 7689 bytes to ./notes/Python/PythonforDataScience/4_Pandas.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas2.ipynb to markdown
    [NbConvertApp] Writing 5224 bytes to ./notes/Python/PythonforDataScience/4_Pandas2.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas3.ipynb to markdown
    [NbConvertApp] Writing 4235 bytes to ./notes/Python/PythonforDataScience/4_Pandas3.md
    [NbConvertApp] Converting notebook ./utils/01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 3956 bytes to ./utils/01_BatchConversions.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -f markdown -t html  -o  ${0%.md}.html' {} \;
```

      1157236      4 -rwxrwxrwx   1 jcmint   jcmint       1016 Mar 11 21:53 ./notes/Python/base.md
      1157209      8 -rwxrwxrwx   1 jcmint   jcmint       7559 Mar 11 22:53 ./notes/Python/ProbabilityandStatistics/2_Sets.md
      1157384      0 -rwxrwxrwx   1 jcmint   jcmint          0 Mar 11 22:53 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas3-checkpoint.md
      1157223      8 -rwxrwxrwx   1 jcmint   jcmint       4475 Mar 11 22:53 ./notes/Python/PythonforDataScience/2_Basics.md
      1157226      8 -rwxrwxrwx   1 jcmint   jcmint       7857 Mar 11 22:53 ./notes/Python/PythonforDataScience/3_Numpy.md
      1157229      8 -rwxrwxrwx   1 jcmint   jcmint       7689 Mar 11 22:53 ./notes/Python/PythonforDataScience/4_Pandas.md
      1157232      8 -rwxrwxrwx   1 jcmint   jcmint       5224 Mar 11 22:53 ./notes/Python/PythonforDataScience/4_Pandas2.md
      1157386      8 -rwxrwxrwx   1 jcmint   jcmint       4235 Mar 11 22:53 ./notes/Python/PythonforDataScience/4_Pandas3.md
      1157554      4 -rwxrwxrwx   1 jcmint   jcmint       3956 Mar 11 22:53 ./utils/01_BatchConversions.md

