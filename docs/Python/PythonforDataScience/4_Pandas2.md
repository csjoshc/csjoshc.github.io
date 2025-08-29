
  🏠 Home
  🐍 Python

```python

print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0

```
    /home/jcmint/anaconda3/envs/learningenv/bin/python
# Dataframes - Introduction
Starting out with data in .csv form, with several files for this unit. Just putting the dataframe to terminal doesn't properly print when exporting to .md or .md (although it works fine in .iypnb) so I have to use `tabulate` or the default print. 
```python

import os, sys
os.chdir(sys.path[0]) # Change dir to the folder this .ipynb file is in
print(os.listdir('../../../../data/w4pd'))
movies = pd.read_csv('../../../../data/w4pd/movies.csv')
tags = pd.read_csv('../../../../data/w4pd/tags.csv')
ratings = pd.read_csv('../../../../data/w4pd/ratings.csv')
movies.head()
```
    ['genome-scores.csv', 'genome-tags.csv', 'Icon\r', 'links.csv', 'movies.csv', 'ratings.csv', 'README.txt', 'tags.csv']

|  | movieId | title | genres |
| --- | --- | --- | --- |
| 0 | 1 | Toy Story (1995) | Adventure|Animation|Children|Comedy|Fantasy |
| 1 | 2 | Jumanji (1995) | Adventure|Children|Fantasy |
| 2 | 3 | Grumpier Old Men (1995) | Comedy|Romance |
| 3 | 4 | Waiting to Exhale (1995) | Comedy|Drama|Romance |
| 4 | 5 | Father of the Bride Part II (1995) | Comedy |

## Accessing rows
**Code:** `df.iloc(n)`
```python
row_0 = movies.iloc[0]
row_0
```
    movieId                                              1
    title                                 Toy Story (1995)
    genres     Adventure|Animation|Children|Comedy|Fantasy
    Name: 0, dtype: object
## Listing columns
**Code:** `df.columns`
```python
tags.columns
```
    Index(['userId', 'movieId', 'tag', 'timestamp'], dtype='object')
## List summary statistics
**Code:** `df.describe()` - count, std, quartiles
```python
ratings.describe()
```

|  | userId | movieId | rating | timestamp |
| --- | --- | --- | --- | --- |
| count | 2.000026e+07 | 2.000026e+07 | 2.000026e+07 | 2.000026e+07 |
| mean | 6.904587e+04 | 9.041567e+03 | 3.525529e+00 | 1.100918e+09 |
| std | 4.003863e+04 | 1.978948e+04 | 1.051989e+00 | 1.621694e+08 |
| min | 1.000000e+00 | 1.000000e+00 | 5.000000e-01 | 7.896520e+08 |
| 25% | 3.439500e+04 | 9.020000e+02 | 3.000000e+00 | 9.667977e+08 |
| 50% | 6.914100e+04 | 2.167000e+03 | 3.500000e+00 | 1.103556e+09 |
| 75% | 1.036370e+05 | 4.770000e+03 | 4.000000e+00 | 1.225642e+09 |
| max | 1.384930e+05 | 1.312620e+05 | 5.000000e+00 | 1.427784e+09 |

## List correlations amongst variables
**Code:** `df.corr()`
```python
ratings.corr()
```

|  | userId | movieId | rating | timestamp |
| --- | --- | --- | --- | --- |
| userId | 1.000000 | -0.000850 | 0.001175 | -0.003101 |
| movieId | -0.000850 | 1.000000 | 0.002606 | 0.459096 |
| rating | 0.001175 | 0.002606 | 1.000000 | -0.000512 |
| timestamp | -0.003101 | 0.459096 | -0.000512 | 1.000000 |

## Other aggregate functions
**Code:** `df.min(), max(), std(), mean()`
```python
ratings.mode()
```

|  | userId | movieId | rating | timestamp |
| --- | --- | --- | --- | --- |
| 0 | 118205 | 296 | 4.0 | 825638400 |

## Test logical conditionals
**Code:** `any(df['col1'] > n), all(df['col1'] > n)`

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