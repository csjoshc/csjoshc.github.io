
<a href="../../index.html">Go back to index</a>

<head>
  <link rel="stylesheet" href="../../css_themes/github.css">
</head>

# Intro to using Github

* create new respository on github 
* create new folder under Notebooks
* change data directory in vscode
* create sample note md files
* follow directions on [this](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line) link

`# in console, cd to folder above`

`git init`

`git add.`

`git commit -m "First commit"`

Then, **copy** the git url

`git remote add origin <url>`

`git remote -v`

`git push origin master`

# Updating an existing repository

`cd /../../media/jcmint/'Data Volume'/csjoshc.github.io` 

## The confusion
I was having a lot of trouble managing the staging, commit and push to branch process. [This](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners) *maybe* cleared it up for me. 

**As a summary**, after any file change you want to eventually push, you must do 
`git add .

git status 

git commit -a -m "new change"`

**the first and third must be used together after any change**

### git add 
git add stages the current version of a file, or the current version of all the files. Therefore, this needs to be run after all changes you are intending to package together are made. 

`git add .`

### git status
This is good to run after git add .
* this will make sure you are committing what you think you are.

### git commit 
`git commit` adds those changes to the index of changes to be sent off

`git commit -a -m "Message here"`

* change v1 as appropriate
* maybe dd.mm.yy branch name? 

### git checkout
This creates a new branch for tracking code changes that won't affect the state of the master or other branch (so you could switch back to that branch and push that branch as a separate project state from the new branch). At least that's how I understand it. This might not be that necessary, since I don't really have a dev vs production version of my notes.
`git checkout -b v1` 

### git push (to a new branch)
I guess I can push and automatically create a new remote branch at the same time
`git push origin v1` 
* adding `-u` as an argument is questionable 


`git push origin master` - Pushes to master


# Adding from remote

`git clone repo.url`

# Good to know: 

`url = git@github.com:csjoshc/csjoshc.github.io.git`

## Formatting 

Now using [premade css](https://gist.github.com/tuzz/3331384) in a folder in the root directory. 

## Compiling .md to html using task build in vscode

Important step even though process isn't automated. Since I'm not changing too many .md too frequently, ctrl-shift-b and Build Task is ok. 
`tasks.json`:

```
"command": "markdown-it",
"args": [
    "${relativeFile}",
    "-o",
    "${fileDirname}/${fileBasenameNoExtension}.html"
],
```