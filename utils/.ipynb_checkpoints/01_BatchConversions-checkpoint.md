
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
    [NbConvertApp] Converting notebook ./notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/2_Sets-checkpoint.ipynb to markdown
    [NbConvertApp] Support files will be in 2_Sets-checkpoint_files/
    [NbConvertApp] Making directory ./notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/2_Sets-checkpoint_files
    [NbConvertApp] Writing 7567 bytes to ./notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/2_Sets-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/ProbabilityandStatistics/1_Introduction.ipynb to markdown
    [NbConvertApp] Writing 1645 bytes to ./notes/Python/ProbabilityandStatistics/1_Introduction.md
    [NbConvertApp] Converting notebook ./notes/Python/ProbabilityandStatistics/2_Sets.ipynb to markdown
    [NbConvertApp] Support files will be in 2_Sets_files/
    [NbConvertApp] Making directory ./notes/Python/ProbabilityandStatistics/2_Sets_files
    [NbConvertApp] Writing 7549 bytes to ./notes/Python/ProbabilityandStatistics/2_Sets.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/1_Introduction-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 3733 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/1_Introduction-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/2_Basics-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 4475 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/2_Basics-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/3_Numpy-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 7857 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/3_Numpy-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 7689 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas2-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 5224 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas2-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas3-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 4908 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas3-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas4-checkpoint.ipynb to markdown
    [NbConvertApp] Support files will be in 4_Pandas4-checkpoint_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas4-checkpoint_files
    [NbConvertApp] Writing 21190 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas4-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas5-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 7491 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas5-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/1_Introduction.ipynb to markdown
    [NbConvertApp] Writing 3733 bytes to ./notes/Python/PythonforDataScience/1_Introduction.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/2_Basics.ipynb to markdown
    [NbConvertApp] Writing 3675 bytes to ./notes/Python/PythonforDataScience/2_Basics.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/3_Numpy.ipynb to markdown
    [NbConvertApp] Writing 6579 bytes to ./notes/Python/PythonforDataScience/3_Numpy.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas.ipynb to markdown
    [NbConvertApp] Writing 7689 bytes to ./notes/Python/PythonforDataScience/4_Pandas.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas2.ipynb to markdown
    [NbConvertApp] Writing 4467 bytes to ./notes/Python/PythonforDataScience/4_Pandas2.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas3.ipynb to markdown
    [NbConvertApp] Writing 4248 bytes to ./notes/Python/PythonforDataScience/4_Pandas3.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas4.ipynb to markdown
    [NbConvertApp] Support files will be in 4_Pandas4_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/4_Pandas4_files
    [NbConvertApp] Writing 20243 bytes to ./notes/Python/PythonforDataScience/4_Pandas4.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas5.ipynb to markdown
    [NbConvertApp] Writing 6391 bytes to ./notes/Python/PythonforDataScience/4_Pandas5.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/5_visualization.ipynb to markdown
    [NbConvertApp] Writing 1026 bytes to ./notes/Python/PythonforDataScience/5_visualization.md
    [NbConvertApp] Converting notebook ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 3615 bytes to ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
    [NbConvertApp] Converting notebook ./utils/01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 7012 bytes to ./utils/01_BatchConversions.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
! cd ..;  find ./ -iname "*.md" -ls -exec sh -c 'pandoc ${0} -s --highlight-style breezedark -f markdown -t html  -o  ${0%.md}.html' {} \;
```

      1157163      1 -rwxrwxrwx   1 jcmint   jcmint        464 Mar 10 15:14 ./notes/Devops/base.md
      1157165      4 -rwxrwxrwx   1 jcmint   jcmint       2531 Mar 10 15:14 ./notes/Devops/roadmap_notes.md
      1157168      4 -rwxrwxrwx   1 jcmint   jcmint        687 Mar 10 15:14 ./notes/Github/bugs_gh.md
      1157170      4 -rwxrwxrwx   1 jcmint   jcmint       2913 Mar 10 15:14 ./notes/Github/intro_gh.md
      1157173      4 -rwxrwxrwx   1 jcmint   jcmint       1241 Mar 10 15:14 ./notes/Linux/base.md
      1157177     12 -rwxrwxrwx   1 jcmint   jcmint       8258 Mar 10 15:14 ./notes/Linux/linux_journey/basic/01_comlin.md
      1157179      4 -rwxrwxrwx   1 jcmint   jcmint        681 Mar 10 15:14 ./notes/Linux/linux_journey/linux_journey_toc.md
      1157236      4 -rwxrwxrwx   1 jcmint   jcmint       1172 Mar 12 22:53 ./notes/Python/base.md
      1157198      4 -rwxrwxrwx   1 jcmint   jcmint       3981 Mar 12 23:50 ./notes/Python/General/virtenv_jupyter_nb.md
      1155650      8 -rwxrwxrwx   1 jcmint   jcmint       7581 Mar 12 23:50 ./notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/2_Sets-checkpoint.md
      1157206      4 -rwxrwxrwx   1 jcmint   jcmint       1649 Mar 12 23:50 ./notes/Python/ProbabilityandStatistics/1_Introduction.md
      1157209      8 -rwxrwxrwx   1 jcmint   jcmint       7563 Mar 12 23:50 ./notes/Python/ProbabilityandStatistics/2_Sets.md
      1155651      4 -rwxrwxrwx   1 jcmint   jcmint       3733 Mar 12 23:50 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/1_Introduction-checkpoint.md
      1155652      8 -rwxrwxrwx   1 jcmint   jcmint       4475 Mar 12 23:50 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/2_Basics-checkpoint.md
      1155653      8 -rwxrwxrwx   1 jcmint   jcmint       7857 Mar 12 23:50 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/3_Numpy-checkpoint.md
      1155654      8 -rwxrwxrwx   1 jcmint   jcmint       7689 Mar 12 23:50 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas-checkpoint.md
      1155655      8 -rwxrwxrwx   1 jcmint   jcmint       5224 Mar 12 23:50 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas2-checkpoint.md
      1155632      8 -rwxrwxrwx   1 jcmint   jcmint       4908 Mar 12 23:50 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas3-checkpoint.md
      1155635     24 -rwxrwxrwx   1 jcmint   jcmint      21192 Mar 12 23:50 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas4-checkpoint.md
      1155636      8 -rwxrwxrwx   1 jcmint   jcmint       7491 Mar 12 23:50 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas5-checkpoint.md
      1157456      4 -rwxrwxrwx   1 jcmint   jcmint       3733 Mar 12 23:50 ./notes/Python/PythonforDataScience/1_Introduction.md
      1157223      4 -rwxrwxrwx   1 jcmint   jcmint       3675 Mar 12 23:50 ./notes/Python/PythonforDataScience/2_Basics.md
      1157226      8 -rwxrwxrwx   1 jcmint   jcmint       6579 Mar 12 23:50 ./notes/Python/PythonforDataScience/3_Numpy.md
      1157229      8 -rwxrwxrwx   1 jcmint   jcmint       7689 Mar 12 23:50 ./notes/Python/PythonforDataScience/4_Pandas.md
      1157232      8 -rwxrwxrwx   1 jcmint   jcmint       4467 Mar 12 23:50 ./notes/Python/PythonforDataScience/4_Pandas2.md
      1157386      8 -rwxrwxrwx   1 jcmint   jcmint       4248 Mar 12 23:50 ./notes/Python/PythonforDataScience/4_Pandas3.md
      1154906     20 -rwxrwxrwx   1 jcmint   jcmint      20245 Mar 12 23:50 ./notes/Python/PythonforDataScience/4_Pandas4.md
      1155433      8 -rwxrwxrwx   1 jcmint   jcmint       6391 Mar 12 23:50 ./notes/Python/PythonforDataScience/4_Pandas5.md
      1157457      4 -rwxrwxrwx   1 jcmint   jcmint       1026 Mar 12 23:50 ./notes/Python/PythonforDataScience/5_visualization.md
      1155480      1 -rwxrwxrwx   1 jcmint   jcmint        509 Mar 12 23:01 ./site_updates/3_2019/16_3_2019.md
      1157240      4 -rwxrwxrwx   1 jcmint   jcmint        866 Mar 10 15:14 ./site_updates/3_2019/2_3_2019.md
      1157241      1 -rwxrwxrwx   1 jcmint   jcmint        528 Mar 10 18:40 ./site_updates/3_2019/9_3_2019.md
      1157243      1 -rwxrwxrwx   1 jcmint   jcmint        297 Mar 10 18:39 ./site_updates/base.md
      1157245      4 -rwxrwxrwx   1 jcmint   jcmint       1282 Mar 12 22:59 ./todo.md
      1158314      4 -rwxrwxrwx   1 jcmint   jcmint       3615 Mar 12 23:50 ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
      1157554      8 -rwxrwxrwx   1 jcmint   jcmint       7012 Mar 12 23:50 ./utils/01_BatchConversions.md
      1157584      1 -rwxrwxrwx   1 jcmint   jcmint        252 Mar 11 23:12 ./utils/base.md

