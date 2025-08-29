# Pandas - Introduction

- Merge and join data sets
- Better visualizations
- Exploratory data analysis
- Time series data
- Data pivoting, sorting, cleaning

# Series

- One dimensional labeled array
- Similar to fixed size dictionary

```bash

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
