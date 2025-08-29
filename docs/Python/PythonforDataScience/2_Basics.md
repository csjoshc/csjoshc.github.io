
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

# Python Basics

- Dynamic heap assignment, automatic garbage collection for objects with no pointers

## Mutating lists and dictionaries

List functions `list.append`, `list[index] = value`, `list.pop(index)`, `list.remove(value)`, `list.extend(value)`, `del(index)` all mutate the list. A list that was assigned as `newlist = list` before these functions are executed will point to the same mutated list.
Dictionary funcitons `dict[('key')] = value`, `del(dict[('key')])` also mutate the dictionary similar as above.

## String & list functions

```python
# String functions
word = 'Hello'
word[1 to 3], 'He' in word, word.find('ll') # The lowest index start point
```

    ('el', True, 2)

### Adding to lists

**C