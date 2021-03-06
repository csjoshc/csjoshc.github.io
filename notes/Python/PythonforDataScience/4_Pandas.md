
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
# print(tabulate(df, headers=df.columns, tablefmt='psql'))
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Pandas - Introduction
* Merge and join data sets
* Better visualizations
* Exploratory data analysis
* Time series data
* Data pivoting, sorting, cleaning

# Series
* One dimensional labeled array 
* Similar to fixed size dictionary 

Need to install pandas
```
conda activate learningenv
conda install pandas
```


```python
import pandas as pd
ser = pd.Series([1, 2, 3, "letter", "word"],['a', 'b', 'c', 'd', 'e'])
ser
```




    a         1
    b         2
    c         3
    d    letter
    e      word
    dtype: object



## Accessing values by key or index

### Listing keys


```python
ser.index
```




    Index(['a', 'b', 'c', 'd', 'e'], dtype='object')



### Access value by key or Index


```python
print(ser.loc['a'], ser['a']) #key
print(ser.iloc[2]) #Index
```

    1 1
    3


### Test if key is in Series


```python
1 in ser, 'a' in ser # test if key is in Series
```




    (False, True)



### Multiply numbers and strings


```python
ser*2 # Multiply
```




    a               2
    b               4
    c               6
    d    letterletter
    e        wordword
    dtype: object




```python
ser['b']**2 # Square
```




    4



# Dataframes
* Contains axes and columns for heterogenous data storage. 
* Easy way of creating a data table.
* Create series first, then load them into a new dataframe


```python
s1 = pd.Series([1., 2., 3.], index=['apple', 'ball', 'clock']) 
s2 = pd.Series([5., 10., 15., 20.], index=['apple', 'ball', 'cerill', 'nancy']) 
df = pd.DataFrame({'one': s1, 'two' : s2} ) 
df
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>apple</th>
      <td>1.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>ball</th>
      <td>2.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>cerill</th>
      <td>NaN</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>clock</th>
      <td>3.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>nancy</th>
      <td>NaN</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>



## Access & Operations

### Accessing Columns


```python
df['one']
```




    apple     1.0
    ball      2.0
    cerill    NaN
    clock     3.0
    nancy     NaN
    Name: one, dtype: float64



### Creating new columns


```python
df['product'] = df['one'] * df['two'] 
df['big'] = df['two'] > 10 
df
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
      <th>one</th>
      <th>two</th>
      <th>product</th>
      <th>big</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>apple</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ball</th>
      <td>2.0</td>
      <td>10.0</td>
      <td>20.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>cerill</th>
      <td>NaN</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>clock</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
    <tr>
      <th>nancy</th>
      <td>NaN</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Removing columns - pop
unneeded = df.pop('product')
unneeded
df
```




    apple      5.0
    ball      20.0
    cerill     NaN
    clock      NaN
    nancy      NaN
    Name: product, dtype: float64






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
      <th>one</th>
      <th>two</th>
      <th>big</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>apple</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ball</th>
      <td>2.0</td>
      <td>10.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>cerill</th>
      <td>NaN</td>
      <td>15.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>clock</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
    <tr>
      <th>nancy</th>
      <td>NaN</td>
      <td>20.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



### Removing columns - `del`


```python
del(df['two'])
df
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
      <th>one</th>
      <th>big</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>apple</th>
      <td>1.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>ball</th>
      <td>2.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>cerill</th>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>clock</th>
      <td>3.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>nancy</th>
      <td>NaN</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



### Inserting columnns


```python
df.insert(2, 'copy one', df['one'])
df
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
      <th>one</th>
      <th>big</th>
      <th>copy one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>apple</th>
      <td>1.0</td>
      <td>False</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>ball</th>
      <td>2.0</td>
      <td>False</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>cerill</th>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>clock</th>
      <td>3.0</td>
      <td>False</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>nancy</th>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Accessing a subslice


```python
a = df.iloc[3:4]
b = df['one'][:2] # values in column 'one', rows under 2
c = df[1:3] 

a
b
c
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
      <th>one</th>
      <th>big</th>
      <th>copy one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>clock</th>
      <td>3.0</td>
      <td>False</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>






    apple    1.0
    ball     2.0
    Name: one, dtype: float64






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
      <th>one</th>
      <th>big</th>
      <th>copy one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ball</th>
      <td>2.0</td>
      <td>False</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>cerill</th>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Dictionary -> Dataframe
* Automatically alphabetized
* All the keys become columns, each row in the new df represent the values of one of the dictionaries


```python
data = [{'alex': 1, 'joe': 2}, {'ema': 5, 'dora':10, 'alice': 20}] # a list
data = pd.DataFrame(data, index  = ['orange', 'red']) 
data

d = pd.DataFrame(data, columns = ['joe', 'dora', 'alice'] )
d
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
      <th>alex</th>
      <th>alice</th>
      <th>dora</th>
      <th>ema</th>
      <th>joe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>orange</th>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>red</th>
      <td>NaN</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>NaN</td>
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
      <th>joe</th>
      <th>dora</th>
      <th>alice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>orange</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>red</th>
      <td>NaN</td>
      <td>10.0</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(data.head)
print(data.columns)
```

    <bound method NDFrame.head of         alex  alice  dora  ema  joe
    orange   1.0    NaN   NaN  NaN  2.0
    red      NaN   20.0  10.0  5.0  NaN>
    Index(['alex', 'alice', 'dora', 'ema', 'joe'], dtype='object')



```python

```
