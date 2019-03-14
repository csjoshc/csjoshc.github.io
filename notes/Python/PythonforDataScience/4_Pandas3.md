
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>
<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
</head>



```python
import sys
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
import os, sys

os.chdir(sys.path[0]) # Change dir to the folder this .ipynb file is in
print(os.listdir('../../../../data/w4pd'))
movies = pd.read_csv('../../../../data/w4pd/movies.csv')
tags = pd.read_csv('../../../../data/w4pd/tags.csv')
ratings = pd.read_csv('../../../../data/w4pd/ratings.csv')
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python
    ['genome-scores.csv', 'genome-tags.csv', 'Icon\r', 'links.csv', 'movies.csv', 'ratings.csv', 'README.txt', 'tags.csv']


# Dataframes - Subsetting & Cleaning

## `df.copy()`
Certain ways of indexing will return a reference to the original object instead of a copy of an object. To make this explicit use `.copy()` when subsetting a df. 

## `df.shape, df.isnull().any(), df.dropna()`
* Find the shape
* Test if any values in each column are NA
* Drop ROWS with null values. 


```python
print(ratings.shape)
print(ratings.isnull().any())
```

    (20000263, 4)
    userId       False
    movieId      False
    rating       False
    timestamp    False
    dtype: bool


## Filling, Replacing, Imputations

Filling in Data
* Forward filling - take prior values to fill forward into missing values
 * `df.fillna(method = 'ffill')`
* Backward filling
 * `df.fillna(method = 'backfill')`

Replacing
* Replace one value with another
 * `df = pd.replace(9999, 0)`
 * Replace 9999 with 0

Dropping rows with missing values
* `df.dropna(axis = 0)`
 * default 0 drops rows
 
Linear interpolation (numeric) 
* fill in missing values based on averaging the value before and after
* `df.interpolate()`

## Data Operations - Slicing

### Subset rows


```python
first_df = ratings[1:5]
last_df = ratings[-5:]
print(first_df, "\n", last_df)
```

       userId  movieId  rating   timestamp
    1       1       29     3.5  1112484676
    2       1       32     3.5  1112484819
    3       1       47     3.5  1112484727
    4       1       50     3.5  1112484580 
               userId  movieId  rating   timestamp
    20000258  138493    68954     4.5  1258126920
    20000259  138493    69526     4.5  1259865108
    20000260  138493    69644     3.0  1260209457
    20000261  138493    70286     5.0  1258126944
    20000262  138493    71619     2.5  1255811136


### `df.value_counts()` - Frequency table
One column frequency table.


```python
ratings['rating'].value_counts()
```




    4.0    5561926
    3.0    4291193
    5.0    2898660
    3.5    2200156
    4.5    1534824
    2.0    1430997
    2.5     883398
    1.0     680732
    1.5     279252
    0.5     239125
    Name: rating, dtype: int64



### Create derived variable column


```python
first_df['normalized'] = first_df['rating']/5
print(first_df[['rating', 'normalized']])
```

       rating  normalized
    1     3.5         0.7
    2     3.5         0.7
    3     3.5         0.7
    4     3.5         0.7


### Add row by index location


```python
first_df.loc[3] = ["test", "test2", "test3", False, True]
print(first_df)
```

      userId movieId rating   timestamp normalized
    1      1      29    3.5  1112484676        0.7
    2      1      32    3.5  1112484819        0.7
    3   test   test2  test3       False       True
    4      1      50    3.5  1112484580        0.7


### Drop row by index location


```python
first_df = first_df.drop(3)
print(first_df)
```

      userId movieId rating   timestamp normalized
    1      1      29    3.5  1112484676        0.7
    2      1      32    3.5  1112484819        0.7
    4      1      50    3.5  1112484580        0.7


### Drop column - **del**


```python
del first_df['timestamp']
print(first_df)
```

      userId movieId rating normalized
    1      1      29    3.5        0.7
    2      1      32    3.5        0.7
    4      1      50    3.5        0.7

