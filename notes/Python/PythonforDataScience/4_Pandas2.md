
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>

<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
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


# Dataframes - Introduction

Starting out with data in .csv form, with several files for this unit. Just putting the dataframe to terminal doesn't properly print when exporting to .md or .html (although it works fine in .iypnb) so I have to use `tabulate` or the default print. 


```python
import pandas as pd
import os, sys

os.chdir(sys.path[0]) # Change dir to the folder this .ipynb file is in
print(os.listdir('../../../../data/w4pd'))
movies = pd.read_csv('../../../../data/w4pd/movies.csv')
tags = pd.read_csv('../../../../data/w4pd/tags.csv')
ratings = pd.read_csv('../../../../data/w4pd/ratings.csv')
movies.head()
```

    ['genome-scores.csv', 'genome-tags.csv', 'Icon\r', 'links.csv', 'movies.csv', 'ratings.csv', 'README.txt', 'tags.csv']





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children|Fantasy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Comedy|Drama|Romance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
    </tr>
  </tbody>
</table>
</div>



## `df.iloc(n)` - Accessing rows


```python
row_0 = movies.iloc[0]
row_0
```




    movieId                                              1
    title                                 Toy Story (1995)
    genres     Adventure|Animation|Children|Comedy|Fantasy
    Name: 0, dtype: object



## `df.columns` - Listing columns


```python
tags.columns
```




    Index(['userId', 'movieId', 'tag', 'timestamp'], dtype='object')



## `df.describe()` - List summary statistics (count, std, quartiles)


```python
ratings.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>movieId</th>
      <th>rating</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2.000026e+07</td>
      <td>2.000026e+07</td>
      <td>2.000026e+07</td>
      <td>2.000026e+07</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.904587e+04</td>
      <td>9.041567e+03</td>
      <td>3.525529e+00</td>
      <td>1.100918e+09</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.003863e+04</td>
      <td>1.978948e+04</td>
      <td>1.051989e+00</td>
      <td>1.621694e+08</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000e+00</td>
      <td>1.000000e+00</td>
      <td>5.000000e-01</td>
      <td>7.896520e+08</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.439500e+04</td>
      <td>9.020000e+02</td>
      <td>3.000000e+00</td>
      <td>9.667977e+08</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.914100e+04</td>
      <td>2.167000e+03</td>
      <td>3.500000e+00</td>
      <td>1.103556e+09</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.036370e+05</td>
      <td>4.770000e+03</td>
      <td>4.000000e+00</td>
      <td>1.225642e+09</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.384930e+05</td>
      <td>1.312620e+05</td>
      <td>5.000000e+00</td>
      <td>1.427784e+09</td>
    </tr>
  </tbody>
</table>
</div>



## `df.corr()` - List correlations amongst variables


```python
ratings.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>movieId</th>
      <th>rating</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>userId</th>
      <td>1.000000</td>
      <td>-0.000850</td>
      <td>0.001175</td>
      <td>-0.003101</td>
    </tr>
    <tr>
      <th>movieId</th>
      <td>-0.000850</td>
      <td>1.000000</td>
      <td>0.002606</td>
      <td>0.459096</td>
    </tr>
    <tr>
      <th>rating</th>
      <td>0.001175</td>
      <td>0.002606</td>
      <td>1.000000</td>
      <td>-0.000512</td>
    </tr>
    <tr>
      <th>timestamp</th>
      <td>-0.003101</td>
      <td>0.459096</td>
      <td>-0.000512</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Other aggregate functions: `df. min(), max(), std(), mean()`


```python
ratings.mode()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>userId</th>
      <th>movieId</th>
      <th>rating</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>118205</td>
      <td>296</td>
      <td>4.0</td>
      <td>825638400</td>
    </tr>
  </tbody>
</table>
</div>



## `any(df['col1'] > n), all(df['col1'] > n)` - Test logical conditionals
Test if any or all cells in a column fit a logical condition


```python
any(ratings['rating'] == 0), all(ratings['rating'] > 0)
```




    (False, True)



## Filtering columns (return boolean col)


```python
filter_1 = ratings['rating'] > 4
sum(filter_1)/len(ratings)
```




    0.22167128502260194



## Other useful commands

```python
pd.read.json()
pd.read_html()
pd.read_sql_query()
pd.read_sql_table()
os.chdir()
os.getcwd()
os.listdir()
```
