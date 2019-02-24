[Intro to using Github](#intro-to-using-github)

[Updating an existing repository](#updating-an-existing-repository)
<head>
  <link rel="stylesheet" type="text/css" href="css_gh.css">
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

`cd /../../media/jcmint/'Data Volume'/Site` 

`git checkout -b v1` 

* change v1 as appropriate
* maybe dd.mm.yy branch name? 

`git add .`

`git commit -a -m "Message here"`

`git push origin v1`