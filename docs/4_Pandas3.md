```python

print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0

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

# Dataframes - Subsetting & Cleaning# Change dir to the folder this .ipynb file is in
print(os.listdir('../../../../data/w4pd'))
movies = pd.read_csv('../../../../data/w4pd/movies.csv')
tags = pd.read_csv('../../../../data/w4pd/tags.csv')
ratings = pd.read_csv('../../../../data/w4pd/ratings.csv')
```
/home/jcmint/anaconda3/envs/learningenv/bin/python
['genome-scores.csv', 'genome-tags.csv', 'Icon\r', 'links.csv', 'movies.csv', 'ratings.csv', 'README.txt', 'tags.csv']
# Dataframes - Subsetting & Cleaning
## Copy dataframe
**Code:** `df.copy()`Certain ways of indexing will return a reference to the original object instead of a copy of an object. To make this explicit use `.copy()` when subsetting a df. ## Dataframe inspection and cleaning
**Code:** `df.shape, df.isnull().any(), df.dropna()`* Find the shape* Test if any values in each column are NA* Drop ROWS with null values.

```python
print(ratings.shape)
print(ratings.isnull().any())
```

    (20000263, 4)

    dtype: bool

## Filling, Replacing, ImputationsFilling in Data* Forward filling - take prior values to fill forward into missing values * `df.fillna(method = 'ffill')`* Backward filling * `df.fillna(method = 'backfill')`Replacing* Replace one value with another * `df = pd.replace(9999, 0)` * Replace 9999 with 0Dropping rows with missing values* `df.dropna(axis = 0)` * default 0 drops rows Linear interpolation (numeric) * fill in missing values based on averaging the value before and after* `df.interpolate()`## Data Operations - Slicing### Subset rows

```python
first_df = ratings[1:5]
last_df = ratings[-5:]
first_df
last_df
```

|  | userId | movieId | rating | timestamp |
| --- | --- | --- | --- | --- |
| 1 | 1 | 29 | 3.5 | 1112484676 |
| 2 | 1 | 32 | 3.5 | 1112484819 |
| 3 | 1 | 47 | 3.5 | 1112484727 |
| 4 | 1 | 50 | 3.5 | 1112484580 |

|  | userId | movieId | rating | timestamp |
| --- | --- | --- | --- | --- |
| 20000258 | 138493 | 68954 | 4.5 | 1258126920 |
| 20000259 | 138493 | 69526 | 4.5 | 1259865108 |
| 20000260 | 138493 | 69644 | 3.0 | 1260209457 |
| 20000261 | 138493 | 70286 | 5.0 | 1258126944 |
| 20000262 | 138493 | 71619 | 2.5 | 1255811136 |

## Filling, Replacing, Imputations

* Forward filling - take prior values to fill forward into missing values
* `df.fillna(method = 'ffill')`
* Backward filling
* `df.fillna(method = 'backfill')`

* Replace one value with another
* `df = pd.replace(9999, 0)`
* Replace 9999 with 0

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
first_df
last_df
```

|  | userId | movieId | rating | timestamp |
| --- | --- | --- | --- | --- |
| 1 | 1 | 29 | 3.5 | 1112484676 |
| 2 | 1 | 32 | 3.5 | 1112484819 |
| 3 | 1 | 47 | 3.5 | 1112484727 |
| 4 | 1 | 50 | 3.5 | 1112484580 |

|  | userId | movieId | rating | timestamp |
| --- | --- | --- | --- | --- |
| 20000258 | 138493 | 68954 | 4.5 | 1258126920 |
| 20000259 | 138493 | 69526 | 4.5 | 1259865108 |
| 20000260 | 138493 | 69644 | 3.0 | 1260209457 |
| 20000261 | 138493 | 70286 | 5.0 | 1258126944 |
| 20000262 | 138493 | 71619 | 2.5 | 1255811136 |

### Frequency table
**Code:** `df.value_counts()`One column frequency table.

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
first_df[['rating', 'normalized']]
```

    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead

    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.

|  | rating | normalized |
| --- | --- | --- |
| 1 | 3.5 | 0.7 |
| 2 | 3.5 | 0.7 |
| 3 | 3.5 | 0.7 |
| 4 | 3.5 | 0.7 |

### Add row by index location

```python
first_df.loc[3] = ["test", "test2", "test3", False, True]
first_df
```

|  | userId | movieId | rating | timestamp | normalized |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 29 | 3.5 | 1112484676 | 0.7 |
| 2 | 1 | 32 | 3.5 | 1112484819 | 0.7 |
| 3 | test | test2 | test3 | False | True |
| 4 | 1 | 50 | 3.5 | 1112484580 | 0.7 |

### Drop row by index location

```python
first_df = first_df.drop(3)
first_df
```

|  | userId | movieId | rating | timestamp | normalized |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 29 | 3.5 | 1112484676 | 0.7 |
| 2 | 1 | 32 | 3.5 | 1112484819 | 0.7 |
| 4 | 1 | 50 | 3.5 | 1112484580 | 0.7 |

### Drop column - **del**

```python
del first_df['timestamp']
first_df
```

|  | userId | movieId | rating | normalized |
| --- | --- | --- | --- | --- |
| 1 | 1 | 29 | 3.5 | 0.7 |
| 2 | 1 | 32 | 3.5 | 0.7 |
| 4 | 1 | 50 | 3.5 | 0.7 |
