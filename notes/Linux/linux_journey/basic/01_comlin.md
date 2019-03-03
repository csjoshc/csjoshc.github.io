<a href="../../../../index.html">Go back to index</a>

<a href = "../linux_journey_toc.html"> Go back to Linux Journey topic portal </a>
<head>
  <link rel="stylesheet" href="../../../../css_themes/vscode.css">
</head>

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

