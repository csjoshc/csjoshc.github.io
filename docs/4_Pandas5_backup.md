
```python

print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0

import matplotlib.pyplot as plte 
import os, sys

tags = pd.read_csv('tags.csv')
```

    /Users/joshchiu/repos/csjoshc.github.io/.venv/bin/python

    ---------------------------------------------------------------------------

    Cell In[2], line 13
          9 import matplotlib.pyplot as plte 
         10 import os, sys
    ---> 13 tags = pd.read_csv('tags.csv')

    File ~/repos/csjoshc.github.io/.venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py:1026, in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)
       1013 kwds_defaults = _refine_defaults_read(
       1014     dialect,
       1015     delimiter,
       (...)   1022     dtype_backend=dtype_backend,
       1023 )
       1024 kwds.update(kwds_defaults)
    -> 1026 return _read(filepath_or_buffer, kwds)

    File ~/repos/csjoshc.github.io/.venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py:620, in _read(filepath_or_buffer, kwds)
        617 _validate_names(kwds.get("names", None))
        619 # Create the parser.
    --> 620 parser = TextFileReader(filepath_or_buffer, **kwds)
        622 if chunksize or iterator:
        623     return parser

    File ~/repos/csjoshc.github.io/.venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py:1620, in TextFileReader.__init__(self, f, engine, **kwds)
       1617     self.options["has_index_names"] = kwds["has_index_names"]
       1619 self.handles: IOHandles | None = None
    -> 1620 self._engine = self._make_engine(f, self.engine)

    File ~/repos/csjoshc.github.io/.venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py:1880, in TextFileReader._make_engine(self, f, engine)
       1878     if "b" not in mode:
       1879         mode += "b"
    -> 1880 self.handles = get_handle(
       1881     f,
       1882     mode,
       1883     encoding=self.options.get("encoding", None),
       1884     compression=self.options.get("compression", None),
       1885     memory_map=self.options.get("memory_map", False),
       1886     is_text=is_text,
       1887     errors=self.options.get("encoding_errors", "strict"),
       1888     storage_options=self.options.get("storage_options", None),
       1889 )
       1890 assert self.handles is not None
       1891 f = self.handles.handle

    File ~/repos/csjoshc.github.io/.venv/lib/python3.11/site-packages/pandas/io/common.py:873, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
        868 elif isinstance(handle, str):
        869     # Check whether the filename is to be opened in binary mode.
        870     # Binary mode does not support 'encoding' and 'newline'.
        871     if ioargs.encoding and "b" not in ioargs.mode:
        872         # Encoding
    --> 873         handle = open(
        874             handle,
        875             ioargs.mode,
        876             encoding=ioargs.encoding,
        877             errors=errors,
        878             newline="",
        879         )
        880     else:
        881         # Binary mode
        882         handle = open(handle, ioargs.mode)

    FileNotFoundError: [Errno 2] No such file or directory: 'tags.csv'

# Dataframe data types - strings & timestamps

## String functions
Str functions don't seem to mutate the original dataframe

# Change dir to the folder this .ipynb file is in
tags = pd.read_csv('tags.csv')
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python

# Dataframe data types - strings & timestamps

## String functions

Str functions don't seem to mutate the original dataframe

### Splitting columns of dataframe

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
`df.sort_values(by ='col1', ascending = False)`

```python
tags = tags.sort_values(by = 'parsed time', ascending =False) 
tags.head()
```

    ---------------------------------------------------------------------------

    Cell In[2], line 1
    ----> 1 tags = tags.sort_values(by = 'parsed time', ascending =False) 
          2 tags.head()

    NameError: name 'tags' is not defined
