
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>
<head>
  <link rel="stylesheet" href="../../../css_themes/github.css">
</head>



```python
import sys
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0
from tabulate import tabulate
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Dataframes

Starting out with data in .csv form, with several files for this unit. Just putting the dataframe to terminal doesn't properly print when exporting to .md or .html (although it works fine in .iypnb) so I have to use `tabulate`


```python
import pandas as pd
import os, sys

os.chdir(sys.path[0]) # Change dir to the folder this .ipynb file is in
print(os.listdir('../../../../data/w4pd'))
movies = pd.read_csv('../../../../data/w4pd/movies.csv')
print(tabulate(movies.head(), headers=movies.columns, tablefmt='psql'))
```

    ['genome-scores.csv', 'genome-tags.csv', 'Icon\r', 'links.csv', 'movies.csv', 'ratings.csv', 'README.txt', 'tags.csv']
    +----+-----------+------------------------------------+---------------------------------------------+
    |    |   movieId | title                              | genres                                      |
    |----+-----------+------------------------------------+---------------------------------------------|
    |  0 |         1 | Toy Story (1995)                   | Adventure|Animation|Children|Comedy|Fantasy |
    |  1 |         2 | Jumanji (1995)                     | Adventure|Children|Fantasy                  |
    |  2 |         3 | Grumpier Old Men (1995)            | Comedy|Romance                              |
    |  3 |         4 | Waiting to Exhale (1995)           | Comedy|Drama|Romance                        |
    |  4 |         5 | Father of the Bride Part II (1995) | Comedy                                      |
    +----+-----------+------------------------------------+---------------------------------------------+

