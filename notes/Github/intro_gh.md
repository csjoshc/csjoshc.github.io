
[Intro to using Github](#intro-to-using-github)

[Updating an existing repository](#updating-an-existing-repository) 

[Adding from remote](#adding-from-remote) 

[Good to know:](#good-to-know)

[Formatting](#formatting)

[Compiling .md to html using task build in vscode](#compiling-md-to-html-using-task-build-in-vscode)

<head>
  <link rel="stylesheet" href="css_gh.css">
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

`git add .`

`git checkout -b v1` 

* change v1 as appropriate
* maybe dd.mm.yy branch name? 



`git commit -a -m "Message here"`

`git push -u origin v1` 

`git push origin master` - Pushes to master


# Adding from remote

`git clone repo.url`

# Good to know: 

`url = git@github.com:csjoshc/csjoshc.github.io.git`

## Formatting 

Now using [premade css](https://gist.github.com/tuzz/3331384), [github.css](github.css) in same directory..

## Compiling .md to html using task build in vscode

Important step even though process isn't automated. Since I'm not changing too many .md too frequently, ctrl-shift-b and Build Task is ok. 

```
"command": "markdown-it",
"args": [
    "${relativeFile}",
    "-o",
    "${fileDirname}/${fileBasenameNoExtension}.html"
],
```