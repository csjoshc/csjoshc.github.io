<head>
  <link rel="stylesheet" href="css_themes/vscode.css">
</head>
<a href="index.html">Go back to index</a>

# To do list for site
* Need to add actual css although compiling md to html is ok for now
* Make topic portal pages
* automate the html compile process, make it a task in json...Its already tedious to compil
e each .md to .html by going through all of them just to be sure with just 5-6 pages
* add python notes from OneNote
* floating toc makes better use of widescreen 
* devops portal page has no href to return to index page
* picture for index page

# Notes
* adding links in markdown format are relative to the file itself if there is no backslash before the beginning of the folder directory:
* Set up keyboard shortcuts:
  * html compile with `cntr-space-p`
  * toc insertion with `cntr-space-t`
  * remapped preview output with `cntr-shift-v`, overriding default
* use `ctrl+shift+P` to get command palette in vscode. Useful tasks - insert or update TOC, open persistent preview tools in sidepane like so:
![](https://i.imgur.com/BNdiun3.png)


**This is relative to the .md file itself:**

`[test link](foldername/filename.extension)`

**This would be relative to the root directory (/csjoshc.github.io)**

`[rest link](/foldername/filename.extension)`

* html block links - haven't tried it out yet, but seems to default to relative to the .md as well 