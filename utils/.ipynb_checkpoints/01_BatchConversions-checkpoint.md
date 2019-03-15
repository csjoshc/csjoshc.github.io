
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
# -mtime -1 ipynb
```

    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas4-checkpoint.ipynb to markdown
    [NbConvertApp] Support files will be in 4_Pandas4-checkpoint_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas4-checkpoint_files
    [NbConvertApp] Writing 24686 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas4-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/.ipynb_checkpoints/5_visualization-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 3379 bytes to ./notes/Python/PythonforDataScience/.ipynb_checkpoints/5_visualization-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas4.ipynb to markdown
    [NbConvertApp] Writing 25617 bytes to ./notes/Python/PythonforDataScience/4_Pandas4.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/5_visualization.ipynb to markdown
    [NbConvertApp] Writing 3379 bytes to ./notes/Python/PythonforDataScience/5_visualization.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/w5visual/.ipynb_checkpoints/05a_Matplotlib_Notebook-checkpoint.ipynb to markdown
    [NbConvertApp] Support files will be in 05a_Matplotlib_Notebook-checkpoint_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/.ipynb_checkpoints/05a_Matplotlib_Notebook-checkpoint_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/.ipynb_checkpoints/05a_Matplotlib_Notebook-checkpoint_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/.ipynb_checkpoints/05a_Matplotlib_Notebook-checkpoint_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/.ipynb_checkpoints/05a_Matplotlib_Notebook-checkpoint_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/.ipynb_checkpoints/05a_Matplotlib_Notebook-checkpoint_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/.ipynb_checkpoints/05a_Matplotlib_Notebook-checkpoint_files
    [NbConvertApp] Writing 16787 bytes to ./notes/Python/PythonforDataScience/w5visual/.ipynb_checkpoints/05a_Matplotlib_Notebook-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/w5visual/05a_Matplotlib_Notebook.ipynb to markdown
    [NbConvertApp] Support files will be in 05a_Matplotlib_Notebook_files/
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/05a_Matplotlib_Notebook_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/05a_Matplotlib_Notebook_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/05a_Matplotlib_Notebook_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/05a_Matplotlib_Notebook_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/05a_Matplotlib_Notebook_files
    [NbConvertApp] Making directory ./notes/Python/PythonforDataScience/w5visual/05a_Matplotlib_Notebook_files
    [NbConvertApp] Writing 16655 bytes to ./notes/Python/PythonforDataScience/w5visual/05a_Matplotlib_Notebook.md
    [NbConvertApp] Converting notebook ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 8029 bytes to ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
    [NbConvertApp] Converting notebook ./utils/01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 8029 bytes to ./utils/01_BatchConversions.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
# ! cd ..;  find ./ -iname "*.ipynb" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s -M -o ${0%.ipynb}.md' {} \;
```


```python
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -s --toc --highlight-style breezedark -M date="`date "+%B %e, %Y"`" -f markdown_strict+backtick_code_blocks  -t html  -o  ${0%.md}.html' {} \;
# -mtime -1
```

      1157198      4 -rwxrwxrwx   1 jcmint   jcmint       3981 Mar 14 21:10 ./notes/Python/General/virtenv_jupyter_nb.md
      1157206      4 -rwxrwxrwx   1 jcmint   jcmint       1519 Mar 14 21:10 ./notes/Python/ProbabilityandStatistics/1_Introduction.md
      1157209      8 -rwxrwxrwx   1 jcmint   jcmint       6467 Mar 14 21:10 ./notes/Python/ProbabilityandStatistics/2_Sets.md
      1156698     28 -rwxrwxrwx   1 jcmint   jcmint      24688 Mar 14 23:44 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas4-checkpoint.md
      1154608      4 -rwxrwxrwx   1 jcmint   jcmint       3379 Mar 14 23:44 ./notes/Python/PythonforDataScience/.ipynb_checkpoints/5_visualization-checkpoint.md
      1157456      4 -rwxrwxrwx   1 jcmint   jcmint       3492 Mar 14 21:10 ./notes/Python/PythonforDataScience/1_Introduction.md
      1157223      4 -rwxrwxrwx   1 jcmint   jcmint       3660 Mar 14 21:10 ./notes/Python/PythonforDataScience/2_Basics.md
      1157226      8 -rwxrwxrwx   1 jcmint   jcmint       6568 Mar 14 21:10 ./notes/Python/PythonforDataScience/3_Numpy.md
      1157229      8 -rwxrwxrwx   1 jcmint   jcmint       6931 Mar 14 21:10 ./notes/Python/PythonforDataScience/4_Pandas.md
      1157232      8 -rwxrwxrwx   1 jcmint   jcmint       4482 Mar 14 21:10 ./notes/Python/PythonforDataScience/4_Pandas2.md
      1157386      8 -rwxrwxrwx   1 jcmint   jcmint       4238 Mar 14 21:10 ./notes/Python/PythonforDataScience/4_Pandas3.md
      1154906     28 -rwxrwxrwx   1 jcmint   jcmint      25619 Mar 14 23:44 ./notes/Python/PythonforDataScience/4_Pandas4.md
      1155433      8 -rwxrwxrwx   1 jcmint   jcmint       6373 Mar 14 21:10 ./notes/Python/PythonforDataScience/4_Pandas5.md
      1157457      4 -rwxrwxrwx   1 jcmint   jcmint       3379 Mar 14 23:44 ./notes/Python/PythonforDataScience/5_visualization.md
      1155544     20 -rwxrwxrwx   1 jcmint   jcmint      16787 Mar 14 23:44 ./notes/Python/PythonforDataScience/w5visual/.ipynb_checkpoints/05a_Matplotlib_Notebook-checkpoint.md
       735941     20 -rwxrwxrwx   1 jcmint   jcmint      16655 Mar 14 23:44 ./notes/Python/PythonforDataScience/w5visual/05a_Matplotlib_Notebook.md
       910780     16 -rwxrwxrwx   1 jcmint   jcmint      14187 Mar 14 21:10 ./notes/Python/PythonforDataScience/w5visual/05b_Exploring\ Indicator's\ Across\ Countries.md
    pandoc: ./notes/Python/PythonforDataScience/w5visual/05b_Exploring: openFile: does not exist (No such file or directory)
       916644      4 -rwxrwxrwx   1 jcmint   jcmint       2625 Mar 14 21:10 ./notes/Python/PythonforDataScience/w5visual/05c_Folium_Notebook.md
      1155480      4 -rwxrwxrwx   1 jcmint   jcmint       1071 Mar 14 22:28 ./site_updates/3_2019/16_3_2019.md
       916648      8 -rwxrwxrwx   1 jcmint   jcmint       8029 Mar 14 23:44 ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
      1157554      8 -rwxrwxrwx   1 jcmint   jcmint       8029 Mar 14 23:44 ./utils/01_BatchConversions.md

