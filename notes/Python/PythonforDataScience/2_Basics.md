
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
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Python Basics 
* Dynamic heap assignment, automatic garbage collection for objects with no pointers

## Mutating lists and dictionaries
List functions `list.append`, `list[index] = value`, `list.pop(index)`, `list.remove(value)`, `list.extend(value)`, `del(index)` all mutate the list. A list that was assigned as `newlist = list` before these functions are executed will point to the same mutated list.

Dictionary funcitons `dict[('key')] = value`, `del(dict[('key')])` also mutate the dictionary similar as above. 

## String & list functions


```python
# String functions
word = 'Hello'
word[1:3], 'He' in word, word.find('ll') # The lowest index start point
```




    ('el', True, 2)



### Adding to lists - `append`


```python
list = [1,2,3]
newlist = list
list.append(4)
list[0] = 0
list, newlist
```




    ([0, 2, 3, 4], [0, 2, 3, 4])



### Removing elements - `pop`
* Notice that list.pop(2) returns the element at position 2 in `list`
* The int 3 is removed from list, and assigned to list2


```python
list2 = list.pop(2)
list2, list, type(list2)
```




    (3, [0, 2, 4], int)



### Removing elements - `remove`
list.remove(2) does not return a value - it just removes the value '1' (not the value at index = 1)


```python
list3 = list.remove(2)
list3, list, newlist
```




    (None, [0, 4], [0, 4])



### Adding to list - `extend`
`newlist` continues to be mutated along with `list`


```python
list4 = [5, 6]
list.extend(list4)
list, newlist
```




    ([0, 4, 5, 6], [0, 4, 5, 6])



### Removing elements - `del`
`del` deletes the value at an INDEX, and returns nothing.


```python
newlist = list
del(list[2]) 
list, newlist
```




    ([0, 4, 6], [0, 4, 6])



## Dictionaries
* unordered Key-value pairs
* anything can be a value in a dictionary
* a Key can be a tuple since it is immutable

### Adding dictionary pair


```python
dict = {('String', 2000): 2} 
dict[('string2', 2001)] = 3 
dict[('mykey')] = 2
dict[(2)] = 'myvalue'
dict
```




    {('String', 2000): 2, ('string2', 2001): 3, 'mykey': 2, 2: 'myvalue'}




```python
# Returning the value at specific key (tuple, int, string)
x = dict.get(('string3', 2002))
y = dict.get(2)
x, x == None, y, y == None, 'myid' in dict
```




    (None, True, 'myvalue', False, False)



### Removing Dictionary pair - `pop`
`3` is the value, the rest is `dict`


```python
dict.pop(('string2', 2001)), dict
```




    (3, {('String', 2000): 2, 'mykey': 2, 2: 'myvalue'})



### Removing dictionary pair - `del`
newdict similar to newlist is mutated along with the original object


```python
newdict = dict
del(dict[('mykey')])
dict, newdict
```




    ({('String', 2000): 2, 2: 'myvalue'}, {('String', 2000): 2, 2: 'myvalue'})



## Iterating through dictionaries by key value pairs
* don't mutate data structures through which you are iterating
* instead, iterate through dictionary while appending to a to-do list
* Then, iterate through the to-do list while mutating the dictionary
* Therefore you never iterate and mutate the same data structure simultaneously 


```python
for key, value in dict.items(): 
    print(key, value)
```

    ('String', 2000) 2
    2 myvalue

