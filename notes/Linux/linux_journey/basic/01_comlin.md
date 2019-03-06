<a href="../../../../index.html">Go back to index</a>

<a href = "../linux_journey_toc.html"> Go back to Linux Journey topic portal </a>
<head>
  <link rel="stylesheet" href="../../../../css_themes/github.css">
</head>

- [Command Line](#command-line)
  - [echo and pwd](#echo-and-pwd)
  - [Changing directory with `cd`](#changing-directory-with-cd)
  - [Listing directories with `ls`](#listing-directories-with-ls)
  - [create new file with `touch`](#create-new-file-with-touch)
  - [inspect files with `file`](#inspect-files-with-file)
  - [combine file contents with `cat` (concatenate)](#combine-file-contents-with-cat-concatenate)
  - [get truncated preview with `less`](#get-truncated-preview-with-less)
  - [past commands with `history`](#past-commands-with-history)

# Command Line

## echo and pwd

* Using linux mint based on ubuntu
* `echo Hello World` - prints out text arguments to display
* `pwd` - prints working directory

## Changing directory with `cd`

I noticed this earlier when specifying links with `[]()` syntax. Using `/` in front of a directory means **absolute path**, while starting without a slash means the folder should be in the current working directory. There are also a few arguments for cd:

* `.` for current directory 
* `..` to go one up 
* `~` to go to home directory
* `-` to go to previous directory. 

## Listing directories with `ls`

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

## create new file with `touch` 

`touch filename` 

* also updates timestamps on files/dirs:
```
touch linuxtextfile
ls -l
-rwxrwxrwx 1 jcmint jcmint    0 Mar  2 22:19 linuxtextfile
touch linuxtextfile
-rwxrwxrwx 1 jcmint jcmint    0 Mar  2 22:21 linuxtextfile
```

## inspect files with `file`

This describes a file's contents. 
```
file linuxtextfile
file todo.md
linuxtextfile: empty
todo.md: HTML document, ASCII text
```

## combine file contents with `cat` (concatenate)

Intended for short files. For two files containing `Hello` and `World` (without spaces):
```
cat test1 test2 
HelloWorld
```

## get truncated preview with `less` 

View large text files

**Commands**: `q` to quit, Arrow keys to navigate, `g` go to start, `G` go to end, search using /wordhere

## past commands with `history`

* returns a list of all past commands
* Besides using arrows, you can use `!!` to run past commands. 
* `ctrl-R` to search past commands
* clear this list with `clear`
* **Tab Completion**: when entering a file name, if there is only one that works then pressing tab will autocomplete the name (useful if long)

- [Command Line](#command-line)
  - [echo and pwd](#echo-and-pwd)
  - [Changing directory with `cd`](#changing-directory-with-cd)
  - [Listing directories with `ls`](#listing-directories-with-ls)
  - [create new file with `touch`](#create-new-file-with-touch)
  - [inspect files with `file`](#inspect-files-with-file)
  - [combine file contents with `cat` (concatenate)](#combine-file-contents-with-cat-concatenate)
  - [get truncated preview with `less`](#get-truncated-preview-with-less)
  - [past commands with `history`](#past-commands-with-history)