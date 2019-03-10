
<a href="../index.html">Go back to index</a>
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

    [NbConvertApp] Converting notebook ./notes/Python/General/.ipynb_checkpoints/virtenv_jupyter_nb-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 3978 bytes to ./notes/Python/General/.ipynb_checkpoints/virtenv_jupyter_nb-checkpoint.md
    [NbConvertApp] Converting notebook ./notes/Python/General/virtenv_jupyter_nb.ipynb to markdown
    [NbConvertApp] Writing 3978 bytes to ./notes/Python/General/virtenv_jupyter_nb.md
    [NbConvertApp] Converting notebook ./notes/Python/ProbabilityandStatistics/1_Introduction.ipynb to markdown
    [NbConvertApp] Writing 1645 bytes to ./notes/Python/ProbabilityandStatistics/1_Introduction.md
    [NbConvertApp] Converting notebook ./notes/Python/ProbabilityandStatistics/2_Sets.ipynb to markdown
    [NbConvertApp] Writing 7509 bytes to ./notes/Python/ProbabilityandStatistics/2_Sets.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/1_Introduction.ipynb to markdown
    [NbConvertApp] Writing 3734 bytes to ./notes/Python/PythonforDataScience/1_Introduction.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/2_Basics.ipynb to markdown
    [NbConvertApp] Writing 3964 bytes to ./notes/Python/PythonforDataScience/2_Basics.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/3_Numpy.ipynb to markdown
    [NbConvertApp] Writing 7337 bytes to ./notes/Python/PythonforDataScience/3_Numpy.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas.ipynb to markdown
    [NbConvertApp] Writing 7197 bytes to ./notes/Python/PythonforDataScience/4_Pandas.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/4_Pandas2.ipynb to markdown
    [NbConvertApp] Writing 2112 bytes to ./notes/Python/PythonforDataScience/4_Pandas2.md
    [NbConvertApp] Converting notebook ./notes/Python/PythonforDataScience/5_visualization.ipynb to markdown
    [NbConvertApp] Writing 1012 bytes to ./notes/Python/PythonforDataScience/5_visualization.md
    [NbConvertApp] Converting notebook ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.ipynb to markdown
    [NbConvertApp] Writing 118 bytes to ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
    [NbConvertApp] Converting notebook ./utils/01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 6253 bytes to ./utils/01_BatchConversions.md


## Converting from `.md` to `.html`

The final step is convering all `.md` files that were recently modified. 


```python
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -f markdown -t html  -o  ${0%.md}.html' {} \;
```

      1157163      1 -rwxrwxrwx   1 jcmint   jcmint        464 Mar 10 15:14 ./notes/Devops/base.md
      1157165      4 -rwxrwxrwx   1 jcmint   jcmint       2531 Mar 10 15:14 ./notes/Devops/roadmap_notes.md
      1157168      4 -rwxrwxrwx   1 jcmint   jcmint        687 Mar 10 15:14 ./notes/Github/bugs_gh.md
      1157170      4 -rwxrwxrwx   1 jcmint   jcmint       2913 Mar 10 15:14 ./notes/Github/intro_gh.md
      1157173      4 -rwxrwxrwx   1 jcmint   jcmint       1241 Mar 10 15:14 ./notes/Linux/base.md
      1157177     12 -rwxrwxrwx   1 jcmint   jcmint       8258 Mar 10 15:14 ./notes/Linux/linux_journey/basic/01_comlin.md
      1157179      4 -rwxrwxrwx   1 jcmint   jcmint        681 Mar 10 15:14 ./notes/Linux/linux_journey/linux_journey_toc.md
      1157236      4 -rwxrwxrwx   1 jcmint   jcmint        874 Mar 10 15:14 ./notes/Python/base.md
      1157186      4 -rwxrwxrwx   1 jcmint   jcmint       3982 Mar 10 16:31 ./notes/Python/General/.ipynb_checkpoints/virtenv_jupyter_nb-checkpoint.md
      1157198      4 -rwxrwxrwx   1 jcmint   jcmint       3982 Mar 10 16:31 ./notes/Python/General/virtenv_jupyter_nb.md
      1157206      4 -rwxrwxrwx   1 jcmint   jcmint       1649 Mar 10 16:31 ./notes/Python/ProbabilityandStatistics/1_Introduction.md
      1157209      8 -rwxrwxrwx   1 jcmint   jcmint       7523 Mar 10 16:31 ./notes/Python/ProbabilityandStatistics/2_Sets.md
      1157456      4 -rwxrwxrwx   1 jcmint   jcmint       3734 Mar 10 16:31 ./notes/Python/PythonforDataScience/1_Introduction.md
      1157223      4 -rwxrwxrwx   1 jcmint   jcmint       3964 Mar 10 16:31 ./notes/Python/PythonforDataScience/2_Basics.md
      1157226      8 -rwxrwxrwx   1 jcmint   jcmint       7337 Mar 10 16:31 ./notes/Python/PythonforDataScience/3_Numpy.md
      1157229      8 -rwxrwxrwx   1 jcmint   jcmint       7197 Mar 10 16:31 ./notes/Python/PythonforDataScience/4_Pandas.md
      1157232      4 -rwxrwxrwx   1 jcmint   jcmint       2112 Mar 10 16:31 ./notes/Python/PythonforDataScience/4_Pandas2.md
      1157457      4 -rwxrwxrwx   1 jcmint   jcmint       1012 Mar 10 16:31 ./notes/Python/PythonforDataScience/5_visualization.md
      1157240      4 -rwxrwxrwx   1 jcmint   jcmint        866 Mar 10 15:14 ./site_updates/3_2019/2_3_2019.md
      1157241      1 -rwxrwxrwx   1 jcmint   jcmint        367 Mar 10 15:09 ./site_updates/3_2019/9_3_2019.md
      1157243      1 -rwxrwxrwx   1 jcmint   jcmint        255 Mar 10 15:14 ./site_updates/base.md
      1157245      4 -rwxrwxrwx   1 jcmint   jcmint       1419 Mar 10 15:14 ./todo.md
      1157553      1 -rwxrwxrwx   1 jcmint   jcmint        118 Mar 10 16:31 ./utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
      1157554      8 -rwxrwxrwx   1 jcmint   jcmint       6253 Mar 10 16:31 ./utils/01_BatchConversions.md


Oddly enough, this file may not be included in its most updated form, since the ipynb is compiled to md before the bash output is all printed, so I just save the file here and convert it again.


```python
%notebook 01_BatchConversions.ipynb
!jupyter nbconvert --to markdown "01_BatchConversions.ipynb"
!pandoc "01_BatchConversions.md" -f markdown -t html  -o  "01_BatchConversions.html"
```

    [NbConvertApp] Converting notebook 01_BatchConversions.ipynb to markdown
    [NbConvertApp] Writing 3220 bytes to 01_BatchConversions.md


## Output to Git
For convenisnce sake, automate the 4 git commands


```python
! git add .; git status; git commit -a -m "%Y_%m_%d__%H_%M"; git push origin master
```

    On branch master
    Your branch is up to date with 'origin/master'.
    
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)
    
    	[32mnew file:   .ipynb_checkpoints/01_BatchConversions-checkpoint.html[m
    	[32mnew file:   .ipynb_checkpoints/01_BatchConversions-checkpoint.ipynb[m
    	[32mnew file:   .ipynb_checkpoints/01_BatchConversions-checkpoint.md[m
    	[32mnew file:   01_BatchConversions.html[m
    	[32mnew file:   01_BatchConversions.ipynb[m
    	[32mnew file:   01_BatchConversions.md[m
    	[32mnew file:   base.md[m
    
    Changes not staged for commit:
      (use "git add/rm <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)
    
    	[31mmodified:   ../index.html[m
    	[31mmodified:   ../notes/Devops/base.html[m
    	[31mmodified:   ../notes/Devops/roadmap_notes.html[m
    	[31mmodified:   ../notes/Github/bugs_gh.html[m
    	[31mmodified:   ../notes/Github/intro_gh.html[m
    	[31mmodified:   ../notes/Linux/base.html[m
    	[31mmodified:   ../notes/Linux/linux_journey/basic/01_comlin.html[m
    	[31mmodified:   ../notes/Linux/linux_journey/linux_journey_toc.html[m
    	[31mdeleted:    ../notes/Python/.ipynb_checkpoints/base-checkpoint.html[m
    	[31mmodified:   ../notes/Python/General/virtenv_jupyter_nb.html[m
    	[31mmodified:   ../notes/Python/General/virtenv_jupyter_nb.md[m
    	[31mdeleted:    ../notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/1_Introduction-checkpoint.ipynb[m
    	[31mdeleted:    ../notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/2_Sets-checkpoint.ipynb[m
    	[31mdeleted:    ../notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/2_Sets-checkpoint.md[m
    	[31mmodified:   ../notes/Python/ProbabilityandStatistics/1_Introduction.html[m
    	[31mmodified:   ../notes/Python/ProbabilityandStatistics/1_Introduction.md[m
    	[31mmodified:   ../notes/Python/ProbabilityandStatistics/2_Sets.html[m
    	[31mmodified:   ../notes/Python/ProbabilityandStatistics/2_Sets.md[m
    	[31mdeleted:    ../notes/Python/PythonforDataScience/.ipynb_checkpoints/1_Introduction-checkpoint.ipynb[m
    	[31mdeleted:    ../notes/Python/PythonforDataScience/.ipynb_checkpoints/1_Introduction-checkpoint.md[m
    	[31mdeleted:    ../notes/Python/PythonforDataScience/.ipynb_checkpoints/2_Basics-checkpoint.ipynb[m
    	[31mdeleted:    ../notes/Python/PythonforDataScience/.ipynb_checkpoints/3_Numpy-checkpoint.ipynb[m
    	[31mdeleted:    ../notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas-checkpoint.ipynb[m
    	[31mdeleted:    ../notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas2-checkpoint.ipynb[m
    	[31mdeleted:    ../notes/Python/PythonforDataScience/.ipynb_checkpoints/5_visualization-checkpoint.ipynb[m
    	[31mmodified:   ../notes/Python/PythonforDataScience/2_Basics.html[m
    	[31mmodified:   ../notes/Python/PythonforDataScience/2_Basics.md[m
    	[31mmodified:   ../notes/Python/PythonforDataScience/3_Numpy.html[m
    	[31mmodified:   ../notes/Python/PythonforDataScience/3_Numpy.md[m
    	[31mmodified:   ../notes/Python/PythonforDataScience/4_Pandas.html[m
    	[31mmodified:   ../notes/Python/PythonforDataScience/4_Pandas.md[m
    	[31mmodified:   ../notes/Python/PythonforDataScience/4_Pandas2.html[m
    	[31mmodified:   ../notes/Python/PythonforDataScience/4_Pandas2.md[m
    	[31mmodified:   ../notes/Python/base.html[m
    	[31mmodified:   ../site_updates/3_2019/2_3_2019.html[m
    	[31mmodified:   ../site_updates/base.html[m
    	[31mmodified:   ../todo.html[m
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    
    	[31m../notes/Python/General/.ipynb_checkpoints/virtenv_jupyter_nb-checkpoint.html[m
    	[31m../notes/Python/PythonforDataScience/1_Introduction.html[m
    	[31m../notes/Python/PythonforDataScience/1_Introduction.md[m
    	[31m../notes/Python/PythonforDataScience/5_visualization.html[m
    	[31m../notes/Python/PythonforDataScience/5_visualization.md[m
    	[31m../site_updates/3_2019/9_3_2019.html[m
    
    [master b4fe274] %Y_%m_%d__%H_%M
     44 files changed, 1755 insertions(+), 4817 deletions(-)
     rewrite notes/Devops/base.html (88%)
     rewrite notes/Linux/base.html (74%)
     rewrite notes/Linux/linux_journey/linux_journey_toc.html (65%)
     delete mode 100644 notes/Python/.ipynb_checkpoints/base-checkpoint.html
     delete mode 100644 notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/1_Introduction-checkpoint.ipynb
     delete mode 100644 notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/2_Sets-checkpoint.ipynb
     delete mode 100644 notes/Python/ProbabilityandStatistics/.ipynb_checkpoints/2_Sets-checkpoint.md
     rewrite notes/Python/ProbabilityandStatistics/1_Introduction.html (71%)
     rewrite notes/Python/ProbabilityandStatistics/2_Sets.html (68%)
     delete mode 100644 notes/Python/PythonforDataScience/.ipynb_checkpoints/1_Introduction-checkpoint.ipynb
     delete mode 100644 notes/Python/PythonforDataScience/.ipynb_checkpoints/1_Introduction-checkpoint.md
     delete mode 100644 notes/Python/PythonforDataScience/.ipynb_checkpoints/2_Basics-checkpoint.ipynb
     delete mode 100644 notes/Python/PythonforDataScience/.ipynb_checkpoints/3_Numpy-checkpoint.ipynb
     delete mode 100644 notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas-checkpoint.ipynb
     delete mode 100644 notes/Python/PythonforDataScience/.ipynb_checkpoints/4_Pandas2-checkpoint.ipynb
     delete mode 100644 notes/Python/PythonforDataScience/.ipynb_checkpoints/5_visualization-checkpoint.ipynb
     rewrite notes/Python/PythonforDataScience/2_Basics.html (66%)
     rewrite notes/Python/PythonforDataScience/3_Numpy.html (73%)
     rewrite notes/Python/PythonforDataScience/4_Pandas.html (66%)
     rewrite notes/Python/PythonforDataScience/4_Pandas2.html (71%)
     rewrite notes/Python/base.html (69%)
     rewrite site_updates/3_2019/2_3_2019.html (63%)
     rewrite site_updates/base.html (86%)
     create mode 100644 utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.html
     create mode 100644 utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.ipynb
     create mode 100644 utils/.ipynb_checkpoints/01_BatchConversions-checkpoint.md
     create mode 100644 utils/01_BatchConversions.html
     create mode 100644 utils/01_BatchConversions.ipynb
     create mode 100644 utils/01_BatchConversions.md
     create mode 100644 utils/base.md
    Counting objects: 47, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (47/47), done.
    Writing objects: 100% (47/47), 16.30 KiB | 2.72 MiB/s, done.
    Total 47 (delta 26), reused 0 (delta 0)
    remote: Resolving deltas: 100% (26/26), completed with 25 local objects.[K
    To github.com:csjoshc/csjoshc.github.io.git
       fa8a907..b4fe274  master -> master



```python

```
