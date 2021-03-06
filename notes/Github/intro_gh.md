
<a href="../../index.html">Go back to index</a>

<head>
  <link rel="stylesheet" href="../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>




# Intro to using Github

* create new respository on github 
* create new folder under Notebooks
* change data directory in vscode
* create sample note md files
* follow directions on [this](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line) link

```
# in console, cd to folder above
git init
git add.
git commit -m "First commit"
# Then, **copy** the git url
git remote add origin <url>
git remote -v
git push origin master
```

## Updating an existing repository

`cd /../../media/jcmint/'Data Volume'/csjoshc.github.io `
I was having a lot of trouble managing the staging, commit and push to branch process. [This](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners) *maybe* cleared it up for me. 
**As a summary**, after any file change you want to eventually push, you must do 
```
git add .
git status 
git commit -a -m "new change"
git push origin master
```
**the first and third must be used together after any change**.
`git add .` stages the current version of a file, or the current version of all the files. Therefore, this needs to be run after all changes you are intending to package together are made. 
`git status` good to run after git add. This will make sure you are committing what you think you are. `git commit` adds those changes to the index of changes to be sent off, and `git push origin master` is fine when working on own repository 

`git push origin v1 ` - When pushing to branch
* adding -u as an argument is questionable 

## Adding from remote
`git clone repo.url` 
url = git@github.com:csjoshc/csjoshc.github.io.git

## git checkout
This creates a new branch for tracking code changes that won't affect the state of the master or other branch (so you could switch back to that branch and push that branch as a separate project state from the new branch). At least that's how I understand it. This might not be that necessary, since I don't really have a dev vs production version of my notes.

## Formatting 
Now using [premade css](https://gist.github.com/tuzz/3331384) in a folder in the root directory. 

## Compiling .md to html using task build in vscode
Important step even though process isn't automated. Since I'm not changing too many .md too frequently, ctrl-shift-b and Build Task is ok. 
tasks.json:

```
"command": "markdown-it",
"args": [
    "${relativeFile}",
    "-o",
    "${fileDirname}/${fileBasenameNoExtension}.html"
],
```