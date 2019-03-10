import os
import subprocess
import sys


os.chdir("/media/jcmint/Data Volume/csjoshc.github.io")
os.getcwd()

getipynb = "find . -mtime -1 -name *.ipynb".split(" ")
my_out = subprocess.check_output(getipynb)
p_getipynb = subprocess.Popen(getipynb, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out_getipynb, err_getipynb = p_getipynb.communicate()
out_getipynb

subprocess.Popen(["jupyter", "nbconvert", "--to", "markdown", out_getipynb])

getmd = getipynb
getmd[5] = ".md"

p_getmd = subprocess.Popen(getmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out_getmd, err_getmd = p_getmd.communicate()
out_getmd

