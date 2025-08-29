
  🏠 Home
  🐧 Linux

**Using linux mint based on ubuntu**

# Command Line

## echo and pwd

**Code:** `echo` and `pwd`

- `echo Hello World` - prints out text arguments to display
- `pwd` - prints working directory

## cd - changing directory

**Code:** `cd`
I noticed this earlier when specifying links with `[]()` syntax. Using `/` in front of a directory means **absolute path**, while starting without a slash means the folder should be in the current working directory. There are also a few arguments for cd:

- `.` for current directory
- `..` to go one up
- `~` to go to home directory
- `-` to go to previous directory.

## ls - listing directories

**Code:** `ls`

- defaults to working directory but you specify a folder path to list a specific directory
  - `ls /` lists everything in the home directory
  - `ls -a` lists hidden files and folders (`.name`)
- `ls -l` use this flag to list detailed info about files/folders in a directory:

```
ls -l notes
total 0
drwxrwxrwx 1 jcmint jcmint   0 Mar  2 00:20 Devops
drwxrwxrwx 1 jcmint jcmint   0 Mar  2 00:20 Github
drwxrwxrwx 1 jcmint jcmint 456 Mar  2 21:06 Linux
```

Finally, combine flags in any order such as `ls -al`

## `touch` - create new files

`touch filename`

- also updates timestamps on files/dirs:

```

ls -l
-rwxrwxrwx 1 jcmint jcmint    0 Mar  2 22:19 linuxtextfile

-rwxrwxrwx 1 jcmint jcmint    0 Mar  2 22:21 linuxtextfile
```

## `file` - inspect files

This describes a file's contents.

```

file todo.md
linuxtextfile: empty
todo.md: HTML document, ASCII text
```

## `cat` (concatenate) - combine file contents

Intended for short files. For two files containing `Hello` and `World` (without spaces):

```
cat test1 test2

```

## `less` - get truncated preview

**Commands**: `q` to quit, Arrow keys to navigate, `g` go to start, `G` go to end, search using /wordhere

## history - past commands

**Code:** `history`

- returns a list of all past commands
- Besides using arrows, you can use `!!` to run past commands.
- `ctrl-R` to search past commands
- clear this list with `clear`
- **Tab Completion**: when entering a file name, if there is only one that works then pressing tab will autocomplete the name (useful if long)

## cp - Copy

**Code:** `cp`

- moves one or muiltiple files in one directory to one target directory

```
jcmint@jcmint:/media/jcmint/Data Volume/csjoshc.github.io$ PROMPT_DIRTRIM=1
jcmint@jcmint:.../csjoshc.github.io$ touch test1
jcmint@jcmint:.../csjoshc.github.io$ touch test2
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.md  notes  site_updates  test1  test2  testing  todo.md  todo.md
jcmint@jcmint:.../csjoshc.github.io$ ls testing
jcmint@jcmint:.../csjoshc.github.io$ cp test1 test2 testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
test1  test2
```

### Regex cp with wildcards

**Code:** `cp` with `*`, `?` and `[]`

- Use `cp *.ext` to copy all files with that extension
- Use \* to represent all characters and strings
- Use ? to represent one character
- Use [] to match a set of characters

```
jcmint@jcmint:.../csjoshc.github.io$ cp *.md testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
index.md  test1  test2  todo.md
jcmint@jcmint:.../csjoshc.github.io$ cp [a-z]???.md testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
index.md  test1  test2  todo.md  todo.md
```

### Recursive & interactive cp

**Code:** `cp` with `-i` and `-r`

```
jcmint@jcmint:.../csjoshc.github.io$ cp -r notes testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
index.md  notes  test1  test2  todo.md  todo.md
jcmint@jcmint:.../csjoshc.github.io$ ls testing/notes

```

- -r flag is necessary to recursively copy the directory and its subdirectories
- Use the -i flag to be prompted when about to overwrite files

```
jcmint@jcmint:.../csjoshc.github.io$ cp -r -i notes testing
cp: overwrite 'testing/notes/Python/General/virtenv_jupyter_nb.ipynb'? y
cp: overwrite 'testing/notes/Python/General/virtenv_jupyter_nb.md'? y
```

## mv - Move & rename files

**Code:** `mv`

- largely identical to cp

### Renaming

```
jcmint@jcmint:.../csjoshc.github.io$ mv test1 one
jcmint@jcmint:.../csjoshc.github.io$ mv test2 two
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.md  notes  one  site_updates  testing  todo.md  todo.md  two
```

- identical syntax for renaming folders

### Moving

```
jcmint@jcmint:.../csjoshc.github.io$ mv one two testing
jcmint@jcmint:.../csjoshc.github.io$ ls testing
index.md  notes  one  test1  test2  todo.md  todo.md  two
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.md  notes  site_updates  testing  todo.md  todo.md
```

- Similar process for moving directories - no `-r` required:

```
jcmint@jcmint:.../testing$ ls
index.md  mynote  one  test1  test2  todo.md  todo.md  two
jcmint@jcmint:.../testing$ mv mynote ..
jcmint@jcmint:.../testing$ ls
index.md  one  test1  test2  todo.md  todo.md  two
jcmint@jcmint:.../testing$ cd ..
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.md  mynote  notes  site_updates  testing  todo.md  todo.md
jcmint@jcmint:.../csjoshc.github.io$ ls mynote

```

- `-b`: Move and backup files that would've been overwritten:

```
jcmint@jcmint:.../csjoshc.github.io$ cd testing
jcmint@jcmint:.../testing$ ls
index.md  one  test1  test2  todo.md  todo.md  two
jcmint@jcmint:.../testing$ mv -b two three
jcmint@jcmint:.../testing$ ls
index.md  one  test1  test2  three  todo.md  todo.md
jcmint@jcmint:.../testing$ mv -b one three
jcmint@jcmint:.../testing$ ls
index.md  test1  test2  three  three~  todo.md  todo.md
```

- there was no overwriting on the first `mv`

## mkdir - make directories and subdirectories

**Code:** `mkdir`

- use `-p` to allow making subdirectories
- multiple at once

```
jcmint@jcmint:.../mynote$ ls

jcmint@jcmint:.../mynote$ mkdir -p one two three/four/five
jcmint@jcmint:.../mynote$ ls

jcmint@jcmint:.../mynote$ ls three

```

## rm and rmdir - delete files and directories

**Code:** `rm` and `rmdir`

- Be careful deleting files
- `-f` flag forces removal of protected files without prompting
- `-i` will prompt at each file being removed

```
jcmint@jcmint:.../testing$ ls
index.md  mynote  test1  test2  three  three~  todo.md  todo.md
jcmint@jcmint:.../testing$ rm t*
jcmint@jcmint:.../testing$ ls
index.md  mynote
jcmint@jcmint:.../testing$ rm index.md -i
rm: remove regular file 'index.md'? y
jcmint@jcmint:.../testing$ ls

jcmint@jcmint:.../testing$ rm mynote
rm: cannot remove 'mynote': Is a directory
jcmint@jcmint:.../testing$ rm -r mynote
```

- `rmdir` can remove directories without additional flags:

```
jcmint@jcmint:.../testing$ cd ..
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.md  notes  site_updates  testing  todo.md  todo.md
jcmint@jcmint:.../csjoshc.github.io$ rmdir testing
jcmint@jcmint:.../csjoshc.github.io$ ls
css_themes  index.md  notes  site_updates  todo.md  todo.md
```
