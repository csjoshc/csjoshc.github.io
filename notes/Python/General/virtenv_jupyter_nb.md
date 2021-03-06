
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>

<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>


# Introduction

Having coded in Python for 6 months or so already, I had always used Spyder and pip install mindlessly (so I guess no virtual env either). I heard about virtual env from a colleague and looked into it, and then decided to implement it on my Linux machine.

## Setting up a virtual env (Anaconda Navigator)

After Anaconda was installed, I created a new virtual env for learning purposes using the GUI: 

![](https://i.imgur.com/VyaA3yh.png)

Options included python 3.7 and MRO for R

## Setting up Jupyter with my new env
```
conda activate learningenv
#
source activate learningenv
# output:
(learningenv) jcmint@jcmint:/media/jcmint/Data Volume/csjoshc.github.io$
```

Next, I installed a few packages inside my learningenv

```
conda info --envs
# conda environments: # just to be sure im not install packages into my github repository...
#
base                     /home/jcmint/anaconda3
learningenv           *  /home/jcmint/anaconda3/envs/learningenv


conda install jupyter 
conda install ipykernel
conda install nb_conda


```

## Kernel selection
Jupyter notebook needs to be started **inside** of a virtualenv. A notebook created outside of it can still be used inside of it, if you close Jupyter and activate the correct env. 

In the bash Terminal:

```
jcmint@jcmint:~$ source activate learningenv
(learningenv) jcmint@jcmint:~$ jupyter notebook
[I 22:35:27.784 NotebookApp] [nb_conda_kernels] enabled, 1 kernels found
[I 22:35:27.967 NotebookApp] [nb_conda] enabled
```

**Incorrect**

```
import sys
print(sys.executable)


# /home/jcmint/anaconda3/bin/python
```



```python
# This code block verifies correct env selection 
# Correct (if switched env before running jupyter notebook in bash)
import sys
sys.executable
```




    '/home/jcmint/anaconda3/envs/learningenv/bin/python'



The code block above should match the image below:

![](https://i.imgur.com/n8J3HcA.png)

## Other points about Jupyter, kernel and virtual env

You can see the list of available kernels in a jupyter notebook session in the `Conda` tab. Notebooks are not created within an environment, really. Rather, they can be created and run in any environment (although dependent code will obviously break if the package dependencies are unmet in different environments). 

![](https://i.imgur.com/Wo2Q3lT.png)

Basically, the kernel and environment that a jupyter session are in are not persistent once you close the session. It's therefore necessary to be disciplined and use `source activate learningenv` before `jupyter notebook` on the Terminal. 

## Previews and formatting

The in-session formatting of jupyter has nothing to do with css. Also, downloading as HTML also doesn't use the embedded CSS stylesheet. Converting to markdown, then to html, will use the stylesheet. However, this  means that I will need to copy and paste each .md from Downloads to the repository and then compile into HTML using vscode. The only way to get the formatting right for good is to override the default css by adding a file to the directory below [(according to this guide)](https://stackoverflow.com/questions/32156248/how-do-i-set-custom-css-for-my-ipython-ihaskell-jupyter-notebook/32158550#32158550)


```python
import jupyter_core
jupyter_core.paths.jupyter_config_dir()


```




    '/home/jcmint/.jupyter'




```python
!ls /media/jcmint/'Data Volume'/csjoshc.github.io/css_themes
!ls /home/jcmint/.jupyter
!mkdir /home/jcmint/.jupyter/custom
!cp /media/jcmint/'Data Volume'/csjoshc.github.io/css_themes/github.css /home/jcmint/.jupyter/custom/custom.css
!ls /home/jcmint/.jupyter/custom

```

    css_gh.css  github.css	vscode.css
    custom	jupyter_notebook_config.py  lab  migrated
    mkdir: cannot create directory ‘/home/jcmint/.jupyter/custom’: File exists
    custom.css

