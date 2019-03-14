
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
print(tabulate(df, headers=df.columns, tablefmt='psql'))
```

    +--------+-------+-------+
    |        |   one |   two |
    |--------+-------+-------|
    | apple  |     1 |     5 |
    | ball   |     2 |    10 |
    | cerill |   nan |    15 |
    | clock  |     3 |   nan |
    | nancy  |   nan |    20 |
    +--------+-------+-------+


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
print(tabulate(df, headers=df.columns, tablefmt='psql'))
```

    +--------+-------+-------+-----------+-------+
    |        |   one |   two |   product | big   |
    |--------+-------+-------+-----------+-------|
    | apple  |     1 |     5 |         5 | False |
    | ball   |     2 |    10 |        20 | False |
    | cerill |   nan |    15 |       nan | True  |
    | clock  |     3 |   nan |       nan | False |
    | nancy  |   nan |    20 |       nan | True  |
    +--------+-------+-------+-----------+-------+



```python
# Removing columns - pop
unneeded = df.pop('product')
unneeded
print(tabulate(df, headers=df.columns, tablefmt='psql'))
```




    apple      5.0
    ball      20.0
    cerill     NaN
    clock      NaN
    nancy      NaN
    Name: product, dtype: float64



    +--------+-------+-------+-------+
    |        |   one |   two | big   |
    |--------+-------+-------+-------|
    | apple  |     1 |     5 | False |
    | ball   |     2 |    10 | False |
    | cerill |   nan |    15 | True  |
    | clock  |     3 |   nan | False |
    | nancy  |   nan |    20 | True  |
    +--------+-------+-------+-------+


### Removing columns - `del`


```python
del(df['two'])
print(tabulate(df, headers=df.columns, tablefmt='psql'))
```

    +--------+-------+-------+
    |        |   one | big   |
    |--------+-------+-------|
    | apple  |     1 | False |
    | ball   |     2 | False |
    | cerill |   nan | True  |
    | clock  |     3 | False |
    | nancy  |   nan | True  |
    +--------+-------+-------+


### Inserting columnns


```python
df.insert(2, 'copy one', df['one'])
print(tabulate(df, headers=df.columns, tablefmt='psql'))
```

    +--------+-------+-------+------------+
    |        |   one | big   |   copy one |
    |--------+-------+-------+------------|
    | apple  |     1 | False |          1 |
    | ball   |     2 | False |          2 |
    | cerill |   nan | True  |        nan |
    | clock  |     3 | False |          3 |
    | nancy  |   nan | True  |        nan |
    +--------+-------+-------+------------+


### Accessing a subslice


```python
a = df.iloc[3:4]
b = df['one'][:2] # values in column 'one', rows under 2
c = df[1:3] 

print(tabulate(a, headers=a.columns, tablefmt='psql'))
print(b)
print(tabulate(c, headers=c.columns, tablefmt='psql'))
```

    +-------+-------+-------+------------+
    |       |   one | big   |   copy one |
    |-------+-------+-------+------------|
    | clock |     3 | False |          3 |
    +-------+-------+-------+------------+
    apple    1.0
    ball     2.0
    Name: one, dtype: float64
    +--------+-------+-------+------------+
    |        |   one | big   |   copy one |
    |--------+-------+-------+------------|
    | ball   |     2 | False |          2 |
    | cerill |   nan | True  |        nan |
    +--------+-------+-------+------------+


## Dictionary -> Dataframe
* Automatically alphabetized
* All the keys become columns, each row in the new df represent the values of one of the dictionaries


```python
data = [{'alex': 1, 'joe': 2}, {'ema': 5, 'dora':10, 'alice': 20}] # a list
data = pd.DataFrame(data, index  = ['orange', 'red']) 
print(tabulate(data, headers=data.columns, tablefmt='psql'))

d = pd.DataFrame(data, columns = ['joe', 'dora', 'alice'] )
print(tabulate(d, headers=d.columns, tablefmt='psql'))
```

    +--------+--------+---------+--------+-------+-------+
    |        |   alex |   alice |   dora |   ema |   joe |
    |--------+--------+---------+--------+-------+-------|
    | orange |      1 |     nan |    nan |   nan |     2 |
    | red    |    nan |      20 |     10 |     5 |   nan |
    +--------+--------+---------+--------+-------+-------+
    +--------+-------+--------+---------+
    |        |   joe |   dora |   alice |
    |--------+-------+--------+---------|
    | orange |     2 |    nan |     nan |
    | red    |   nan |     10 |      20 |
    +--------+-------+--------+---------+



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
