
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

    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas3.ipynb to markdown
    [NbConvertApp] Writing 9008 bytes to ./notes/Python/PythonforDataScience/4_Pandas3.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/1_Introduction.ipynb to markdown
    [NbConvertApp] Writing 3532 bytes to ./notes/Python/PythonforDataScience/1_Introduction.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas.ipynb to markdown
    [NbConvertApp] Writing 10915 bytes to ./notes/Python/PythonforDataScience/4_Pandas.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas2.ipynb to markdown
    [NbConvertApp] Writing 6952 bytes to ./notes/Python/PythonforDataScience/4_Pandas2.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas4.ipynb to markdown
    [NbConvertApp] Support files will be in 4_Pandas4_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/4_Pandas4_files
    [NbConvertApp] Writing 25861 bytes to ./notes/Python/PythonforDataScience/4_Pandas4.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas5.ipynb to markdown
    [NbConvertApp] Writing 12749 bytes to ./notes/Python/PythonforDataScience/4_Pandas5.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/5_Matplotlib.ipynb to markdown
    [NbConvertApp] Support files will be in 5_Matplotlib_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/5_Matplotlib_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/5_Matplotlib_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/5_Matplotlib_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/5_Matplotlib_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/5_Matplotlib_files
    [NbConvertApp] Writing 14271 bytes to ./notes/Python/PythonforDataScience/5_Matplotlib.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/7_ML.ipynb to markdown
    [NbConvertApp] Writing 3025 bytes to ./notes/Python/PythonforDataScience/7_ML.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/7_ML_DT.ipynb to markdown
    [NbConvertApp] Support files will be in 7_ML_DT_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_DT_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_DT_files
    [NbConvertApp] Writing 19994 bytes to ./notes/Python/PythonforDataScience/7_ML_DT.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/Week-7-MachineLearning/European Soccer Regression Analysis using scikit-learn.ipynb to markdown
    [NbConvertApp] Writing 4974 bytes to ./notes/Python/PythonforDataScience/Week-7-MachineLearning/European Soccer Regression Analysis using scikit-learn.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/Week-7-MachineLearning/Weather Data Classification using Decision Trees.ipynb to markdown
    [NbConvertApp] Writing 39084 bytes to ./notes/Python/PythonforDataScience/Week-7-MachineLearning/Weather Data Classification using Decision Trees.md
    [NbConvertApp] Converting notebook ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 8036 bytes to ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
    [NbConvertApp] Converting notebook ./utils/01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 6531 bytes to ./utils/01_BatchConversions.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
# ! cd ..;  find ./ -iname "*.ipynb" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s -M -o ${0%.ipynb}.md' {} \;
```


```python
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s --toc --highlight-style breezedark -M date="`date "+%B %e, %Y"`" -f markdown_strict+backtick_code_blocks+auto_identifiers  -t html  -o  ${0%.md}.html' {} \;
# -mtime -1
```

      1157236      4 -rwxrwxrwx   1 jcmint   jcmint       1380 Mar 21 22:59 ./notes/Python/base.md
      1157456      4 -rwxrwxrwx   1 jcmint   jcmint       3532 Mar 21 23:02 ./notes/Python/PythonforDataScience/1_Introduction.md
      1157229     12 -rwxrwxrwx   1 jcmint   jcmint      10915 Mar 21 23:02 ./notes/Python/PythonforDataScience/4_Pandas.md
      1157232      8 -rwxrwxrwx   1 jcmint   jcmint       6952 Mar 21 23:02 ./notes/Python/PythonforDataScience/4_Pandas2.md
      1157386     12 -rwxrwxrwx   1 jcmint   jcmint       9008 Mar 21 23:02 ./notes/Python/PythonforDataScience/4_Pandas3.md
      1154906     28 -rwxrwxrwx   1 jcmint   jcmint      25863 Mar 21 23:02 ./notes/Python/PythonforDataScience/4_Pandas4.md
      1155433     16 -rwxrwxrwx   1 jcmint   jcmint      12749 Mar 21 23:02 ./notes/Python/PythonforDataScience/4_Pandas5.md
      1158996     16 -rwxrwxrwx   1 jcmint   jcmint      14271 Mar 21 23:02 ./notes/Python/PythonforDataScience/5_Matplotlib.md
      1158777      4 -rwxrwxrwx   1 jcmint   jcmint       3025 Mar 21 23:02 ./notes/Python/PythonforDataScience/7_ML.md
      1158781     20 -rwxrwxrwx   1 jcmint   jcmint      19994 Mar 21 23:02 ./notes/Python/PythonforDataScience/7_ML_DT.md
       916648      8 -rwxrwxrwx   1 jcmint   jcmint       8036 Mar 21 23:02 ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
      1157554      8 -rwxrwxrwx   1 jcmint   jcmint       6531 Mar 21 23:02 ./utils/01_BatchConversions.md

