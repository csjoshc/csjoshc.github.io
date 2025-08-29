
  🏠 Home
  🐍 Python

```python

print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0

import matplotlib.pyplot as plt
import os, sys
os.chdir(sys.path[0]) # Change dir to the folder this .ipynb file is in
tags = pd.read_csv('../../../../data/w4pd/tags.csv')
```
    /home/jcmint/anaconda3/envs/learningenv/bin/python
# Dataframe data types - strings & timestamps
## String functions
Str functions don't seem to mutate the original dataframe
### Splitting columns of dataframe
**Code:** `df['col1'].str.split(' ')`
```python
tags['tag'].str.split(' ').head()
```
    0      [Mark, Waters]
    1        [dark, hero]
    2        [dark, hero]
    3    [noir, thriller]
    4        [dark, hero]
    Name: tag, dtype: object
### Testing for string contents
**Code:** `df['col'].str.contains(' ')`
```python
tags['isdark'] = tags['tag'].str.contains('dark')
tags.head()
```

|  | userId | movieId | tag | timestamp | isdark |
| --- | --- | --- | --- | --- | --- |
| 0 | 18 | 4141 | Mark Waters | 1240597180 | False |
| 1 | 65 | 208 | dark hero | 1368150078 | True |
| 2 | 65 | 353 | dark hero | 1368150079 | True |
| 3 | 65 | 521 | noir thriller | 1368149983 | False |
| 4 | 65 | 592 | dark hero | 1368150078 | True |

### Replace strings with other strings
**Code:** `df['col1].str.replace('from', 'to')`
```python
tags['light tag'] = tags['tag'].str.replace('dark', 'light').head()
tags.head()
```

|  | userId | movieId | tag | timestamp | isdark | light tag |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 18 | 4141 | Mark Waters | 1240597180 | False | Mark Waters |
| 1 | 65 | 208 | dark hero | 1368150078 | True | light hero |
| 2 | 65 | 353 | dark hero | 1368150079 | True | light hero |
| 3 | 65 | 521 | noir thriller | 1368149983 | False | noir thriller |
| 4 | 65 | 592 | dark hero | 1368150078 | True | light hero |

### Match regex
**Code:** `df['col1'].str.extract('*')`

```python
tags['first tag'] = tags['tag'].str.extract('([a-zA-Z][A-Za-z])')
tags.head()
```

|  | userId | movieId | tag | timestamp | isdark | light tag | first tag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 18 | 4141 | Mark Waters | 1240597180 | False | Mark Waters | Ma |
| 1 | 65 | 208 | dark hero | 1368150078 | True | light hero | da |
| 2 | 65 | 353 | dark hero | 1368150079 | True | light hero | da |
| 3 | 65 | 521 | noir thriller | 1368149983 | False | noir thriller | no |
| 4 | 65 | 592 | dark hero | 1368150078 | True | light hero | da |

### Split str column
**Code:** `df['col1'].str.split(' ', expand = True)`
```python
output = tags['light tag'].str.split(' ', expand =True)
output.head()
```

|  | 0 | 1 |
| --- | --- | --- |
| 0 | Mark | Waters |
| 1 | light | hero |
| 2 | light | hero |
| 3 | noir | thriller |
| 4 | light | hero |

### Cleanup
```python
tags.drop(tags.columns[4:7], axis = 1, inplace=True)
tags.head()
```

|  | userId | movieId | tag | timestamp |
| --- | --- | --- | --- | --- |
| 0 | 18 | 4141 | Mark Waters | 1240597180 |
| 1 | 65 | 208 | dark hero | 1368150078 |
| 2 | 65 | 353 | dark hero | 1368150079 |
| 3 | 65 | 521 | noir thriller | 1368149983 |
| 4 | 65 | 592 | dark hero | 1368150078 |

## Dealing with timestamps
Need to convert UNIX POSIX timestamp to Python format before using it.
### Convert timestamp
**Code:** `pd.to_datetime(df['col1'], unit = 's')`
```python
tags['parsed time'] = pd.to_datetime(tags['timestamp'], unit='s')
tags.head()
```

|  | userId | movieId | tag | timestamp | parsed time |
| --- | --- | --- | --- | --- | --- |
| 0 | 18 | 4141 | Mark Waters | 1240597180 | 2009-04-24 18:19:40 |
| 1 | 65 | 208 | dark hero | 1368150078 | 2013-05-10 01:41:18 |
| 2 | 65 | 353 | dark hero | 1368150079 | 2013-05-10 01:41:19 |
| 3 | 65 | 521 | noir thriller | 1368149983 | 2013-05-10 01:39:43 |
| 4 | 65 | 592 | dark hero | 1368150078 | 2013-05-10 01:41:18 |

### Using timestamp to filter
```python
tags['After Dec 31 2013'] = tags['parsed time'] > '2013-12-31'
tags.head()
```

|  | userId | movieId | tag | timestamp | parsed time | After Dec 31 2013 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 18 | 4141 | Mark Waters | 1240597180 | 2009-04-24 18:19:40 | False |
| 1 | 65 | 208 | dark hero | 1368150078 | 2013-05-10 01:41:18 | False |
| 2 | 65 | 353 | dark hero | 1368150079 | 2013-05-10 01:41:19 | False |
| 3 | 65 | 521 | noir thriller | 1368149983 | 2013-05-10 01:39:43 | False |
| 4 | 65 | 592 | dark hero | 1368150078 | 2013-05-10 01:41:18 | False |

### Sort based on time
**Code:** `df.sort_values(by ='col1', ascending = False)`
```python
tags = tags.sort_values(by = 'parsed time', ascending =False)
tags.head()
```

|  | userId | movieId | tag | timestamp | parsed time | After Dec 31 2013 |
| --- | --- | --- | --- | --- | --- | --- |
| 339178 | 102853 | 115149 | russian mafia | 1427771352 | 2015-03-31 03:09:12 | True |
| 158780 | 46072 | 6058 | premonition | 1427760764 | 2015-03-31 00:12:44 | True |
| 158763 | 46072 | 3409 | premonition | 1427760726 | 2015-03-31 00:12:06 | True |
| 288375 | 87797 | 215 | Vienna | 1427755801 | 2015-03-30 22:50:01 | True |
| 290535 | 88044 | 106782 | profanity | 1427754096 | 2015-03-30 22:21:36 | True |
