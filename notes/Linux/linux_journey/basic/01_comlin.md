<a href="../../../../index.html">Go back to index</a>

<a href = "../linux_journey_toc.html"> Go back to Linux Journey topic portal </a>
<head>
  <link rel="stylesheet" href="../../../../cssthemes/github.css">
</head>

**Using linux mint based on ubuntu**

# Command Line 

## `echo` and `pwd`
* `echo Hello World` - prints out text arguments to display
* `pwd` - prints working directory

## `cd` - changing directory

I noticed this earlier when specifying links with `[]()` syntax. Using `/` in front of a directory means **absolute path**, while starting without a slash means the folder should be in the current working directory. There are also a few arguments for cd:

* `.` for current directory 
* `..` to go one up 
* `~` to go to home directory
* `-` to go to previous directory. 

## `ls` - listing directories

* defaults to working directory but you specify a folder path to list a specific directory
  * `ls /` lists everything in the home directory
  * `ls -a` lists hidden files and folders (`.name`)
* `ls -l` use this flag to list detailed info about files/folders in a directory:
```
ls -l notes
total 0
drwxrwxrwx 1 jcmint jcmint   0 Mar  2 00:20 Devops
drwxrwxrwx 1 jcmint jcmint   0 Mar  2 00:20 Github
drwxrwxrwx 1 jcmint jcmint 456 Mar  2 21:06 Linux
```
Finally, combine flags in any order such as `ls -al` 

##  `touch` - create new files

`touch filename` 

* also updates timestamps on files/dirs:
```
touch linuxtextfile
ls -l
-rwxrwxrwx 1 jcmint jcmint    0 Mar  2 22:19 linuxtextfile
touch linuxtextfile
-rwxrwxrwx 1 jcmint jcmint    0 Mar  2 22:21 linuxtextfile
```

## `file` - inspect files

This describes a file's contents. 
```
file linuxtextfile
file todo.md
linuxtextfile: empty
todo.md: HTML document, ASCII text
```

##  `cat` (concatenate) - combine file contents 

Intended for short files. For two files containing `Hello` and `World` (without spaces):
```
cat test1 test2 
HelloWorld
```

##  `less` - get truncated preview

View large text files

**Commands**: `q` to quit, Arrow keys to navigate, `g` go to start, `G` go to end, search using /wordhere

## `history` - past commands 

* returns a list of all past commands
* Besides using arrows, you can use `!!` to run past commands. 
* `ctrl-R` to search past commands
* clear this list with `clear`
* **Tab Completion**: when entering a file name, if there is only one that works then pressing tab will autocomplete the name (useful if long)

## `cp` - Copy

* moves one or muiltiple files in one directory to one target directory

```
jcmint@jcmint:/media/jcmint/Data Volume/csjoshc.github.io$ PROMPT_DIRTRIM=1
jcmint@jcmint:.../csjoshc.github.io$ touch test1
jcmint@jcmint:.../csjoshc.github.io$ touch test2
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.html  notes  site_updates  test1  test2  testing  todo.html  todo.md
jcmint@jcmint:.../csjoshc.github.io$ ls testing
jcmint@jcmint:.../csjoshc.github.io$ cp test1 test2 testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
test1  test2
```

### Regex `cp` with `*`, `?` and `[]`
* Use `cp *.ext` to copy all files with that extension
* Use * to represent all characters and strings
* Use ? to represent one character 
* Use [] to match a set of characters

```
jcmint@jcmint:.../csjoshc.github.io$ cp *.html testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
index.html  test1  test2  todo.html

jcmint@jcmint:.../csjoshc.github.io$ cp [a-z]???.md testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
index.html  test1  test2  todo.html  todo.md
```

### Recursive & interactive `cp` with `-i` and `-r`
```
jcmint@jcmint:.../csjoshc.github.io$ cp -r notes testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
index.html  notes  test1  test2  todo.html  todo.md
jcmint@jcmint:.../csjoshc.github.io$ ls testing/notes
Devops  Github  Linux  Python
```
* -r flag is necessary to recursively copy the directory and its subdirectories
* Use the -i flag to be prompted when about to overwrite files
```
jcmint@jcmint:.../csjoshc.github.io$ cp -r -i notes testing
cp: overwrite 'testing/notes/Python/General/virtenv_jupyter_nb.ipynb'? y
cp: overwrite 'testing/notes/Python/General/virtenv_jupyter_nb.html'? y
```

## `mv` - Move & rename files
* largely identical to cp 

### Renaming
```
jcmint@jcmint:.../csjoshc.github.io$ mv test1 one
jcmint@jcmint:.../csjoshc.github.io$ mv test2 two
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.html  notes  one  site_updates  testing  todo.html  todo.md  two
```
* identical syntax for renaming folders

### Moving
```
jcmint@jcmint:.../csjoshc.github.io$ mv one two testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
index.html  notes  one  test1  test2  todo.html  todo.md  two
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.html  notes  site_updates  testing  todo.html  todo.md
```

* Similar process for moving directories - no `-r` required:

```
jcmint@jcmint:.../testing$ ls
index.html  mynote  one  test1  test2  todo.html  todo.md  two
jcmint@jcmint:.../testing$ mv mynote ..
jcmint@jcmint:.../testing$ ls
index.html  one  test1  test2  todo.html  todo.md  two
jcmint@jcmint:.../testing$ cd ..
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.html  mynote  notes  site_updates  testing  todo.html  todo.md
jcmint@jcmint:.../csjoshc.github.io$ ls mynote
Devops  Github  Linux  Python
```

* `-b`: Move and backup files that would've been overwritten:

```
jcmint@jcmint:.../csjoshc.github.io$ cd testing
jcmint@jcmint:.../testing$ ls
index.html  one  test1  test2  todo.html  todo.md  two
jcmint@jcmint:.../testing$ mv -b two three
jcmint@jcmint:.../testing$ ls 
index.html  one  test1  test2  three  todo.html  todo.md
jcmint@jcmint:.../testing$ mv -b one three
jcmint@jcmint:.../testing$ ls
index.html  test1  test2  three  three~  todo.html  todo.md
```
* there was no overwriting on the first `mv`

## `mkdir` - make directories and subdirectories
* use `-p` to allow making subdirectories
* multiple at once

```
jcmint@jcmint:.../mynote$ ls
Devops  Github  Linux  Python
jcmint@jcmint:.../mynote$ mkdir -p one two three/four/five
jcmint@jcmint:.../mynote$ ls
Devops  Github  Linux  one  Python  three  two
jcmint@jcmint:.../mynote$ ls three
four
```

## `rm` and `rmdir` - delete files and directories

* Be careful deleting files
* `-f` flag forces removal of protected files without prompting 
* `-i` will prompt at each file being removed
  
```
jcmint@jcmint:.../testing$ ls
index.html  mynote  test1  test2  three  three~  todo.html  todo.md
jcmint@jcmint:.../testing$ rm t*
jcmint@jcmint:.../testing$ ls
index.html  mynote

jcmint@jcmint:.../testing$ rm index.html -i
rm: remove regular file 'index.html'? y

jcmint@jcmint:.../testing$ ls
mynote
jcmint@jcmint:.../testing$ rm mynote
rm: cannot remove 'mynote': Is a directory
jcmint@jcmint:.../testing$ rm -r mynote
```

* `rmdir` can remove directories without additional flags:
  
```
jcmint@jcmint:.../testing$ cd ..
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.html  notes  site_updates  testing  todo.html  todo.md
jcmint@jcmint:.../csjoshc.github.io$ rmdir testing
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.html  notes  site_updates  todo.html  todo.md
```
