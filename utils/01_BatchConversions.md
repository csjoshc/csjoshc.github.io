

```
! cd
```


```
! pwd
```


```
! pwd
! cd ../../..
```


```
! pwd
! cd ../../..
! pwd
```


```
! pwd
!cd ".."
! pwd
```


```
! pwd
!cd /
! pwd
```


```
! pwd
!cd / ls
! pwd
```


```
! pwd
!{cd / ls}
! pwd
```


```
! pwd
! cd ../cssthemes
! pwd
```


```
! pwd
! cd ../cssthemes
! ls ..
```


```
! pwd
! cd .. ls
! ls ..
```


```
! pwd
! cd .. ls
```


```
! pwd
! cd ..; ls
```


```
! cd ..; ls

! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -f markdown -t html  -o  ${0%.md}.html' {} \;
```


```
!find . -name "*.ipynb" -mtime -1 -exec jupyter nbconvert --to html {} \;
```


```
! cd ..; find . -name "*.ipynb" -mtime -1 -exec jupyter nbconvert --to html {} \;
```


```
! cd ..; find . -name "*.ipynb" -mtime -1 -exec jupyter nbconvert --to md {} \;
```


```
! cd ..; find . -name "*.ipynb" -mtime -1 -exec jupyter nbconvert --to markdown {} \;
```


```
! cd ..;  'find ./ -iname "*.md" -mtime -1 -ls -exec sh -c' 'pandoc ${0} -f markdown -t html  -o  ${0%.md}.html' {} \;
```


```
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -f markdown -t html  -o  ${0%.md}.html' {} \;
```


```
import sys
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```


```
! cd ..; find . -name "*.ipynb" -mtime -1 -exec jupyter nbconvert --to markdown {} \;
```


```
! cd ..;  find ./ -iname "*.md" -mtime -1 -ls -exec sh -c 'pandoc ${0} -f markdown -t html  -o  ${0%.md}.html' {} \;
```


```
!jupyter nbconvert --to markdown {}
!pandoc 01_BatchConversions.md -f markdown -t html  -o  01_BatchConversions.html
```


```
!jupyter nbconvert --to markdown "01_BatchConversions.md"
!pandoc 01_BatchConversions.md -f markdown -t html  -o  01_BatchConversions.html
```


```
!jupyter nbconvert --to markdown "01_BatchConversions.md"
!pandoc "01_BatchConversions.md" -f markdown -t html  -o  "01_BatchConversions.html"
```


```
!jupyter nbconvert --to markdown "01_BatchConversions.md"
```


```
!jupyter nbconvert --to markdown "01_BatchConversions.ipynb"
!pandoc "01_BatchConversions.md" -f markdown -t html  -o  "01_BatchConversions.html"
```


```
!jupyter nbconvert --to markdown "01_BatchConversions.ipynb"
!pandoc "01_BatchConversions.md" -f markdown -t html  -o  "01_BatchConversions.html"
```


```javascript
%%javascript
IPython.notebook.save_notebook()

!jupyter nbconvert --to markdown "01_BatchConversions.ipynb"
!pandoc "01_BatchConversions.md" -f markdown -t html  -o  "01_BatchConversions.html"
```


```

IPython.notebook.save_notebook()

!jupyter nbconvert --to markdown "01_BatchConversions.ipynb"
!pandoc "01_BatchConversions.md" -f markdown -t html  -o  "01_BatchConversions.html"
```


```javascript
%%javascript
IPython.notebook.save_notebook()
```


```
import sys, IPython
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```


```javascript
%%javascript
IPython.notebook.save_notebook()
```


```
%notebook 01_BatchConversions.ipynb

!jupyter nbconvert --to markdown "01_BatchConversions.ipynb"
!pandoc "01_BatchConversions.md" -f markdown -t html  -o  "01_BatchConversions.html"
```
