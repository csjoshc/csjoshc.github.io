
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

    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/7_ML_Clust.ipynb to markdown
    [NbConvertApp] Support files will be in 7_ML_Clust_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/7_ML_Clust_files
    [NbConvertApp] Writing 45557 bytes to ./notes/Python/PythonforDataScience/7_ML_Clust.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/Week-7-MachineLearning/Weather Data Clustering using k-Means.ipynb to markdown
    [NbConvertApp] Support files will be in Weather Data Clustering using k-Means_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/Week-7-MachineLearning/Weather Data Clustering using k-Means_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/Week-7-MachineLearning/Weather Data Clustering using k-Means_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/Week-7-MachineLearning/Weather Data Clustering using k-Means_files
    [NbConvertApp] Writing 30548 bytes to ./notes/Python/PythonforDataScience/Week-7-MachineLearning/Weather Data Clustering using k-Means.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
# ! cd ..;  find ./ -iname "*.ipynb" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s -M -o ${0%.ipynb}.md' {} \;
```


```python
! cd ..;  find ./ -iname "*.md" -mtime -7 -ls -exec sh -c 'pandoc ${0} -s --toc --highlight-style breezedark -M date="`date "+%B %e, %Y"`" -f markdown_strict+backtick_code_blocks+auto_identifiers  -t html  -o  ${0%.md}.html' {} \;
# -mtime -1
```

      1157236      4 -rwxrwxrwx   1 jcmint   jcmint       2050 Apr 13 23:20 ./notes/Python/base.md
      1159156      8 -rwxrwxrwx   1 jcmint   jcmint       6165 Apr 14 21:14 ./notes/Python/IntroCompThinkDataSci/unit1/problemset1.md
      1158591      8 -rwxrwxrwx   1 jcmint   jcmint       6308 Apr 13 22:42 ./notes/Python/IntroCompThinkDataSci/unit1/unit1.md
      1159201      4 -rwxrwxrwx   1 jcmint   jcmint        790 Apr 13 23:26 ./site_updates/4_2019/13_4_2019.md
      1157243      1 -rwxrwxrwx   1 jcmint   jcmint        442 Apr 13 23:27 ./site_updates/base.md

