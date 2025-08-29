
  🏠 Home
  🐍 Python

```python

print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0

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

```

```
```python

ser = pd.Series([1, 2, 3, "letter", "word"],['a', 'b', 'c', 'd', 'e'])

```
    a         1
    b         2
    c         3

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

```

|  | one | two |
| --- | --- | --- |
| apple | 1.0 | 5.0 |
| ball | 2.0 | 10.0 |
| cerill | NaN | 15.0 |
| clock | 3.0 | NaN |
| nancy | NaN | 20.0 |

## Access & Operations
### Accessing Columns
```python
df['one']
```
    apple     1.0
    ball      2.0

    clock     3.0

    Name: one, dtype: float64
### Creating new columns
```python
df['product'] = df['one'] * df['two'] 
df['big'] = df['two'] > 10 

```

|  | one | two | product | big |
| --- | --- | --- | --- | --- |
| apple | 1.0 | 5.0 | 5.0 | False |
| ball | 2.0 | 10.0 | 20.0 | False |
| cerill | NaN | 15.0 | NaN | True |
| clock | 3.0 | NaN | NaN | False |
| nancy | NaN | 20.0 | NaN | True |

```python
# Removing columns - pop
unneeded = df.pop('product')

```
    apple      5.0
    ball      20.0

    Name: product, dtype: float64

|  | one | two | big |
| --- | --- | --- | --- |
| apple | 1.0 | 5.0 | False |
| ball | 2.0 | 10.0 | False |
| cerill | NaN | 15.0 | True |
| clock | 3.0 | NaN | False |
| nancy | NaN | 20.0 | True |

### Removing columns - `del`
```python
del(df['two'])

```

|  | one | big |
| --- | --- | --- |
| apple | 1.0 | False |
| ball | 2.0 | False |
| cerill | NaN | True |
| clock | 3.0 | False |
| nancy | NaN | True |

### Inserting columnns
```python
df.insert(2, 'copy one', df['one'])

```

|  | one | big | copy one |
| --- | --- | --- | --- |
| apple | 1.0 | False | 1.0 |
| ball | 2.0 | False | 2.0 |
| cerill | NaN | True | NaN |
| clock | 3.0 | False | 3.0 |
| nancy | NaN | True | NaN |

### Accessing a subslice
```python
a = df.iloc[3:4]
b = df['one'][:2] # values in column 'one', rows under 2
c = df[1:3] 

```

|  | one | big | copy one |
| --- | --- | --- | --- |
| clock | 3.0 | False | 3.0 |

    apple    1.0
    ball     2.0
    Name: one, dtype: float64

|  | one | big | copy one |
| --- | --- | --- | --- |
| ball | 2.0 | False | 2.0 |
| cerill | NaN | True | NaN |

## Dictionary -> Dataframe
* Automatically alphabetized
* All the keys become columns, each row in the new df represent the values of one of the dictionaries
```python
data = [{'alex': 1, 'joe': 2}, {'ema': 5, 'dora':10, 'alice': 20}] # a list
data = pd.DataFrame(data, index  = ['orange', 'red']) 

d = pd.DataFrame(data, columns = ['joe', 'dora', 'alice'] )

```

|  | alex | alice | dora | ema | joe |
| --- | --- | --- | --- | --- | --- |
| orange | 1.0 | NaN | NaN | NaN | 2.0 |
| red | NaN | 20.0 | 10.0 | 5.0 | NaN |

|  | joe | dora | alice |
| --- | --- | --- | --- |
| orange | 2.0 | NaN | NaN |
| red | NaN | 10.0 | 20.0 |

```python
print(data.head)
print(data.columns)
```

    Index(['alex', 'alice', 'dora', 'ema', 'joe'], dtype='object')
```python
```