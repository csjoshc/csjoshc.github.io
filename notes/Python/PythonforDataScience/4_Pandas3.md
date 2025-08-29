
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>

  



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
first_df
last_df
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
      <th>1</th>
      <td>1</td>
      <td>29</td>
      <td>3.5</td>
      <td>1112484676</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>32</td>
      <td>3.5</td>
      <td>1112484819</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>47</td>
      <td>3.5</td>
      <td>1112484727</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>50</td>
      <td>3.5</td>
      <td>1112484580</td>
    </tr>
  </tbody>
</table>
</div>






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
      <th>20000258</th>
      <td>138493</td>
      <td>68954</td>
      <td>4.5</td>
      <td>1258126920</td>
    </tr>
    <tr>
      <th>20000259</th>
      <td>138493</td>
      <td>69526</td>
      <td>4.5</td>
      <td>1259865108</td>
    </tr>
    <tr>
      <th>20000260</th>
      <td>138493</td>
      <td>69644</td>
      <td>3.0</td>
      <td>1260209457</td>
    </tr>
    <tr>
      <th>20000261</th>
      <td>138493</td>
      <td>70286</td>
      <td>5.0</td>
      <td>1258126944</td>
    </tr>
    <tr>
      <th>20000262</th>
      <td>138493</td>
      <td>71619</td>
      <td>2.5</td>
      <td>1255811136</td>
    </tr>
  </tbody>
</table>
</div>



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
first_df[['rating', 'normalized']]
```

    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.





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
      <th>rating</th>
      <th>normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>3.5</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.5</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.5</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.5</td>
      <td>0.7</td>
    </tr>
  </tbody>
</table>
</div>



### Add row by index location


```python
first_df.loc[3] = ["test", "test2", "test3", False, True]
first_df
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
      <th>normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>29</td>
      <td>3.5</td>
      <td>1112484676</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>32</td>
      <td>3.5</td>
      <td>1112484819</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>test</td>
      <td>test2</td>
      <td>test3</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>50</td>
      <td>3.5</td>
      <td>1112484580</td>
      <td>0.7</td>
    </tr>
  </tbody>
</table>
</div>



### Drop row by index location


```python
first_df = first_df.drop(3)
first_df
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
      <th>normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>29</td>
      <td>3.5</td>
      <td>1112484676</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>32</td>
      <td>3.5</td>
      <td>1112484819</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>50</td>
      <td>3.5</td>
      <td>1112484580</td>
      <td>0.7</td>
    </tr>
  </tbody>
</table>
</div>



### Drop column - **del**


```python
del first_df['timestamp']
first_df
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
      <th>normalized</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>29</td>
      <td>3.5</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>32</td>
      <td>3.5</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>50</td>
      <td>3.5</td>
      <td>0.7</td>
    </tr>
  </tbody>
</table>
</div>


