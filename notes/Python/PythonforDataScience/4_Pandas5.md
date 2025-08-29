
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
tags = pd.read_csv('../../../../data/w4pd/tags.csv')
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Dataframe data types - strings & timestamps

## String functions
Str functions don't seem to mutate the original dataframe

### `df['col1'].str.split(' ')` - Splitting columns of dataframe


```python
tags['tag'].str.split(' ').head()
```




    0      [Mark, Waters]
    1        [dark, hero]
    2        [dark, hero]
    3    [noir, thriller]
    4        [dark, hero]
    Name: tag, dtype: object



### `df['col'].str.contains(' ')` - Testing for string contents


```python
tags['isdark'] = tags['tag'].str.contains('dark') 
tags.head()
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
      <th>tag</th>
      <th>timestamp</th>
      <th>isdark</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>4141</td>
      <td>Mark Waters</td>
      <td>1240597180</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>65</td>
      <td>208</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65</td>
      <td>353</td>
      <td>dark hero</td>
      <td>1368150079</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>65</td>
      <td>521</td>
      <td>noir thriller</td>
      <td>1368149983</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>65</td>
      <td>592</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



### `df['col1].str.replace('from', 'to')` - Replace strings with other strings


```python
tags['light tag'] = tags['tag'].str.replace('dark', 'light').head()
tags.head()
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
      <th>tag</th>
      <th>timestamp</th>
      <th>isdark</th>
      <th>light tag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>4141</td>
      <td>Mark Waters</td>
      <td>1240597180</td>
      <td>False</td>
      <td>Mark Waters</td>
    </tr>
    <tr>
      <th>1</th>
      <td>65</td>
      <td>208</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>True</td>
      <td>light hero</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65</td>
      <td>353</td>
      <td>dark hero</td>
      <td>1368150079</td>
      <td>True</td>
      <td>light hero</td>
    </tr>
    <tr>
      <th>3</th>
      <td>65</td>
      <td>521</td>
      <td>noir thriller</td>
      <td>1368149983</td>
      <td>False</td>
      <td>noir thriller</td>
    </tr>
    <tr>
      <th>4</th>
      <td>65</td>
      <td>592</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>True</td>
      <td>light hero</td>
    </tr>
  </tbody>
</table>
</div>



### `df['col1'].str.extract('*')` - Match regex
Get the string that matches the reg expression


```python
tags['first tag'] = tags['tag'].str.extract('([a-zA-Z][A-Za-z])') 
tags.head()
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
      <th>tag</th>
      <th>timestamp</th>
      <th>isdark</th>
      <th>light tag</th>
      <th>first tag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>4141</td>
      <td>Mark Waters</td>
      <td>1240597180</td>
      <td>False</td>
      <td>Mark Waters</td>
      <td>Ma</td>
    </tr>
    <tr>
      <th>1</th>
      <td>65</td>
      <td>208</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>True</td>
      <td>light hero</td>
      <td>da</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65</td>
      <td>353</td>
      <td>dark hero</td>
      <td>1368150079</td>
      <td>True</td>
      <td>light hero</td>
      <td>da</td>
    </tr>
    <tr>
      <th>3</th>
      <td>65</td>
      <td>521</td>
      <td>noir thriller</td>
      <td>1368149983</td>
      <td>False</td>
      <td>noir thriller</td>
      <td>no</td>
    </tr>
    <tr>
      <th>4</th>
      <td>65</td>
      <td>592</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>True</td>
      <td>light hero</td>
      <td>da</td>
    </tr>
  </tbody>
</table>
</div>



### `df['col1'].str.split(' ', expand = True)` - Split str column


```python
output = tags['light tag'].str.split(' ', expand =True) 
output.head()
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
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mark</td>
      <td>Waters</td>
    </tr>
    <tr>
      <th>1</th>
      <td>light</td>
      <td>hero</td>
    </tr>
    <tr>
      <th>2</th>
      <td>light</td>
      <td>hero</td>
    </tr>
    <tr>
      <th>3</th>
      <td>noir</td>
      <td>thriller</td>
    </tr>
    <tr>
      <th>4</th>
      <td>light</td>
      <td>hero</td>
    </tr>
  </tbody>
</table>
</div>



### Cleanup


```python
tags.drop(tags.columns[4:7], axis = 1, inplace=True)
tags.head()
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
      <th>tag</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>4141</td>
      <td>Mark Waters</td>
      <td>1240597180</td>
    </tr>
    <tr>
      <th>1</th>
      <td>65</td>
      <td>208</td>
      <td>dark hero</td>
      <td>1368150078</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65</td>
      <td>353</td>
      <td>dark hero</td>
      <td>1368150079</td>
    </tr>
    <tr>
      <th>3</th>
      <td>65</td>
      <td>521</td>
      <td>noir thriller</td>
      <td>1368149983</td>
    </tr>
    <tr>
      <th>4</th>
      <td>65</td>
      <td>592</td>
      <td>dark hero</td>
      <td>1368150078</td>
    </tr>
  </tbody>
</table>
</div>



## Dealing with timestamps
Need to convert UNIX POSIX timestamp to Python format before using it. 

### `pd.to_datetime(df['col1'], unit = 's')` - Convert timestamp


```python
tags['parsed time'] = pd.to_datetime(tags['timestamp'], unit='s') 
tags.head()
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
      <th>tag</th>
      <th>timestamp</th>
      <th>parsed time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>4141</td>
      <td>Mark Waters</td>
      <td>1240597180</td>
      <td>2009-04-24 18:19:40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>65</td>
      <td>208</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>2013-05-10 01:41:18</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65</td>
      <td>353</td>
      <td>dark hero</td>
      <td>1368150079</td>
      <td>2013-05-10 01:41:19</td>
    </tr>
    <tr>
      <th>3</th>
      <td>65</td>
      <td>521</td>
      <td>noir thriller</td>
      <td>1368149983</td>
      <td>2013-05-10 01:39:43</td>
    </tr>
    <tr>
      <th>4</th>
      <td>65</td>
      <td>592</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>2013-05-10 01:41:18</td>
    </tr>
  </tbody>
</table>
</div>



### Using timestamp to filter


```python
tags['After Dec 31 2013'] = tags['parsed time'] > '2013-12-31' 
tags.head()
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
      <th>tag</th>
      <th>timestamp</th>
      <th>parsed time</th>
      <th>After Dec 31 2013</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>4141</td>
      <td>Mark Waters</td>
      <td>1240597180</td>
      <td>2009-04-24 18:19:40</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>65</td>
      <td>208</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>2013-05-10 01:41:18</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65</td>
      <td>353</td>
      <td>dark hero</td>
      <td>1368150079</td>
      <td>2013-05-10 01:41:19</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>65</td>
      <td>521</td>
      <td>noir thriller</td>
      <td>1368149983</td>
      <td>2013-05-10 01:39:43</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>65</td>
      <td>592</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>2013-05-10 01:41:18</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



### `df.sort_values(by ='col1', ascending = False)` Sort based on time 


```python
tags = tags.sort_values(by = 'parsed time', ascending =False) 
tags.head()
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
      <th>tag</th>
      <th>timestamp</th>
      <th>parsed time</th>
      <th>After Dec 31 2013</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>339178</th>
      <td>102853</td>
      <td>115149</td>
      <td>russian mafia</td>
      <td>1427771352</td>
      <td>2015-03-31 03:09:12</td>
      <td>True</td>
    </tr>
    <tr>
      <th>158780</th>
      <td>46072</td>
      <td>6058</td>
      <td>premonition</td>
      <td>1427760764</td>
      <td>2015-03-31 00:12:44</td>
      <td>True</td>
    </tr>
    <tr>
      <th>158763</th>
      <td>46072</td>
      <td>3409</td>
      <td>premonition</td>
      <td>1427760726</td>
      <td>2015-03-31 00:12:06</td>
      <td>True</td>
    </tr>
    <tr>
      <th>288375</th>
      <td>87797</td>
      <td>215</td>
      <td>Vienna</td>
      <td>1427755801</td>
      <td>2015-03-30 22:50:01</td>
      <td>True</td>
    </tr>
    <tr>
      <th>290535</th>
      <td>88044</td>
      <td>106782</td>
      <td>profanity</td>
      <td>1427754096</td>
      <td>2015-03-30 22:21:36</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


