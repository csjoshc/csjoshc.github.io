
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
    [NbConvertApp] Writing 1515 bytes to ./notes/Python/ProbabilityandStatistics/1_Introduction.md
    [NbConvertApp] Converting notebook ./notes/Python/ProbabilityandStatistics/2_Sets.ipynb to markdown
    [NbConvertApp] Support files will be in 2_Sets_files/
    [NbConvertApp] Making directory ./notes/Python/ProbabilityandStatistics/2_Sets_files
    [NbConvertApp] Writing 6453 bytes to ./notes/Python/ProbabilityandStatistics/2_Sets.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/1_Introduction.ipynb to markdown
    [NbConvertApp] Writing 3492 bytes to ./notes/Python/PythonforDataScience/1_Introduction.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/2_Basics.ipynb to markdown
    [NbConvertApp] Writing 3660 bytes to ./notes/Python/PythonforDataScience/2_Basics.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/3_Numpy.ipynb to markdown
    [NbConvertApp] Writing 6568 bytes to ./notes/Python/PythonforDataScience/3_Numpy.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas.ipynb to markdown
    [NbConvertApp] Writing 6931 bytes to ./notes/Python/PythonforDataScience/4_Pandas.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas2.ipynb to markdown
    [NbConvertApp] Writing 4482 bytes to ./notes/Python/PythonforDataScience/4_Pandas2.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas3.ipynb to markdown
    [NbConvertApp] Writing 4238 bytes to ./notes/Python/PythonforDataScience/4_Pandas3.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas4.ipynb to markdown
    [NbConvertApp] Support files will be in 4_Pandas4_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/4_Pandas4_files
    [NbConvertApp] Writing 20232 bytes to ./notes/Python/PythonforDataScience/4_Pandas4.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas5.ipynb to markdown
    [NbConvertApp] Writing 6373 bytes to ./notes/Python/PythonforDataScience/4_Pandas5.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/5_visualization.ipynb to markdown
    [NbConvertApp] Writing 1026 bytes to ./notes/Python/PythonforDataScience/5_visualization.md
    [NbConvertApp] Converting notebook ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 7092 bytes to ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
    [NbConvertApp] Converting notebook ./utils/01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 7446 bytes to ./utils/01_BatchConversions.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
! cd ..;  find ./ -iname "*.md"  -mtime -1 -ls -exec sh -c 'pandoc ${0} -s --toc --highlight-style breezedark -M date="`date "+%B %e, %Y"`" -f markdown -t html  -o  ${0%.md}.html' {} \;
```

      1157163      1 -rwxrwxrwx   1 jcmint   jcmint        464 Mar 10 15:14 ./notes/Devops/base.md
      1157165      4 -rwxrwxrwx   1 jcmint   jcmint       2531 Mar 10 15:14 ./notes/Devops/roadmap_notes.md
      1157168      4 -rwxrwxrwx   1 jcmint   jcmint        687 Mar 10 15:14 ./notes/Github/bugs_gh.md
      1157170      4 -rwxrwxrwx   1 jcmint   jcmint       2577 Mar 13 21:35 ./notes/Github/intro_gh.md
      1157173      4 -rwxrwxrwx   1 jcmint   jcmint       1102 Mar 13 21:35 ./notes/Linux/base.md
      1157177      8 -rwxrwxrwx   1 jcmint   jcmint       7215 Mar 13 21:35 ./notes/Linux/linux_journey/basic/01_comlin.md
      1157179      1 -rwxrwxrwx   1 jcmint   jcmint        562 Mar 13 21:35 ./notes/Linux/linux_journey/linux_journey_toc.md
      1157236      4 -rwxrwxrwx   1 jcmint   jcmint       1172 Mar 12 22:53 ./notes/Python/base.md
      1157198      4 -rwxrwxrwx   1 jcmint   jcmint       3981 Mar 13 21:36 ./notes/Python/General/virtenv_jupyter_nb.md
      1157206      4 -rwxrwxrwx   1 jcmint   jcmint       1519 Mar 13 21:36 ./notes/Python/ProbabilityandStatistics/1_Introduction.md
      1157209      8 -rwxrwxrwx   1 jcmint   jcmint       6467 Mar 13 21:36 ./notes/Python/ProbabilityandStatistics/2_Sets.md
      1157456      4 -rwxrwxrwx   1 jcmint   jcmint       3492 Mar 13 21:36 ./notes/Python/PythonforDataScience/1_Introduction.md
      1157223      4 -rwxrwxrwx   1 jcmint   jcmint       3660 Mar 13 21:36 ./notes/Python/PythonforDataScience/2_Basics.md
      1157226      8 -rwxrwxrwx   1 jcmint   jcmint       6568 Mar 13 21:36 ./notes/Python/PythonforDataScience/3_Numpy.md
      1157229      8 -rwxrwxrwx   1 jcmint   jcmint       6931 Mar 13 21:36 ./notes/Python/PythonforDataScience/4_Pandas.md
      1157232      8 -rwxrwxrwx   1 jcmint   jcmint       4482 Mar 13 21:36 ./notes/Python/PythonforDataScience/4_Pandas2.md
      1157386      8 -rwxrwxrwx   1 jcmint   jcmint       4238 Mar 13 21:36 ./notes/Python/PythonforDataScience/4_Pandas3.md
      1154906     20 -rwxrwxrwx   1 jcmint   jcmint      20234 Mar 13 21:36 ./notes/Python/PythonforDataScience/4_Pandas4.md
      1155433      8 -rwxrwxrwx   1 jcmint   jcmint       6373 Mar 13 21:36 ./notes/Python/PythonforDataScience/4_Pandas5.md
      1157457      4 -rwxrwxrwx   1 jcmint   jcmint       1026 Mar 13 21:36 ./notes/Python/PythonforDataScience/5_visualization.md
      1155480      4 -rwxrwxrwx   1 jcmint   jcmint        662 Mar 13 00:09 ./site_updates/3_2019/16_3_2019.md
      1157240      4 -rwxrwxrwx   1 jcmint   jcmint        866 Mar 10 15:14 ./site_updates/3_2019/2_3_2019.md
      1157241      1 -rwxrwxrwx   1 jcmint   jcmint        528 Mar 10 18:40 ./site_updates/3_2019/9_3_2019.md
      1157243      1 -rwxrwxrwx   1 jcmint   jcmint        297 Mar 10 18:39 ./site_updates/base.md
      1157245      4 -rwxrwxrwx   1 jcmint   jcmint       1282 Mar 12 22:59 ./todo.md
      1154792      8 -rwxrwxrwx   1 jcmint   jcmint       7092 Mar 13 21:36 ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
      1157554      8 -rwxrwxrwx   1 jcmint   jcmint       7446 Mar 13 21:36 ./utils/01_BatchConversions.md
      1157584      1 -rwxrwxrwx   1 jcmint   jcmint        252 Mar 11 23:12 ./utils/base.md

