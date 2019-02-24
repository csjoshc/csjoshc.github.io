<!-- toc -->

- [Intro to using Github](#Intro-to-using-Github)
- [Updating an existing notebook](#Updating-an-existing-notebook)

<!-- tocstop -->
---
title: Intro to using Github
created: '2019-02-23T03:43:08.733Z'
modified: '2019-02-23T04:20:16.597Z'
---

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

# Updating an existing notebook

`git checkout -b v1` 

* change v1 as appropraite
* maybe dd.mm.yy branch name? 

`git add .`

`git commit -a -m "Message here"`

`git push origin v1`