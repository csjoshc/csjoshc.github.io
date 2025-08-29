
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
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Numpy 
Numpy contains multidimensional arrays that have built-in functions based on compiled c code
* Arrays in Numpy are fixed in size, unlike Python lists which have changeable sizes
* Elements must all be the same type
* Well optimized and useful matrix operations
* Pandas are built on top of numpy
* Matrices - Rank 2 ndarrays are a key feature

When creating an array using `=` instead of np.array, the new reference points to the same object in memory. Therefore, if either the original or copy is mutated, the other will be updated as well


```python
import numpy as np
a1 = np.array([[0, 5, 10], [2, 4, 6]])  

# Note that the col_slice is returned as a row. These are both 1D/Rank one arrays
row_slice = a1[0,:]
col_slice = a1[:,0]
print(a1, row_slice, col_slice)
```

    [[ 0  5 10]
     [ 2  4  6]] [ 0  5 10] [0 2]


Row and column slices will mutate along with the original array 


```python
a1[0,0] = 1
print(a1, row_slice, col_slice)
```

    [[ 1  5 10]
     [ 2  4  6]] [ 1  5 10] [1 2]


Since the slices are 1D you can extract with just one index value


```python
print(row_slice[1], col_slice[1])
```

    5 2


## Creating column array 


```python
# Instead of: 
long = np.array([[1], [2], [3], [4]]) 

# you can use `.T` (transposon) to easily create column array
long2 = np.array([[1,2,3,4]]).T 
long2
```




    array([[1],
           [2],
           [3],
           [4]])



## Boolean indexing
* Use conditional indexing to access and permute arrays


```python
a1 = np.array([[0, 5, 10], [2, 4, 6]])  

# Creating a boolean array using `=` operator - but the boolean isn't mutated when the original is.
small_num = a1 > 5
small_num
```




    array([[False, False,  True],
           [False, False,  True]])



The boolean array doesn't get mutated along with the original one


```python
a1[1,:] = [6, 7, 8]
print(a1, "\n", small_num)
```

    [[ 0  5 10]
     [ 6  7  8]] 
     [[False False  True]
     [False False  True]]


Get a list of values in the arrays for which conditional is TRUE


```python
a1[a1 > 5]
```




    array([10,  6,  7,  8])



### Multiple conditionals and assigning values where **True**


```python
print(a1)
# Get a list of values in the arrays for which multiple conditionals are TRUE
a1[(a1 > 2) & (a1 < 8)]
```

    [[ 0  5 10]
     [ 6  7  8]]





    array([5, 6, 7])



### Assigning new values using logical filter 


```python
a1[a1 % 2 == 0] += 100 
a1
```




    array([[100,   5, 110],
           [106,   7, 108]])



## `np.array` data types 
* Array types are explicit - you can't add in values of a different type from initialization time
* you can force int and float array to have each other's data type 


```python
ex1 = np.array([1,2])
ex2 = np.array([1.1, 2.2])
ex3 = np.array(ex1, dtype = np.float64)
ex4 = np.array(ex2, dtype=np.int64)

# Coerced int array to float, float to int (rounding DOWN to nearest int)
print(ex1.dtype, ex2.dtype, ex3.dtype, ex4.dtype, ex4)
```

    int64 float64 float64 int64 [1 2]


In general, its preferable to have arrays in floating point, so Python won't give errors when assigning values and you avoid losing precision.
* Arrays will be upcast to higher precision types when performing operations
* Array operations are NOT matrix operations:


```python
ex5 = np.array([[2, 2], [3, 3]]) 
ex6 = np.array([[4, 4], [5, 5]]) 
ex5 * ex6
```




    array([[ 8,  8],
           [15, 15]])



## `np.array` operations - `array.dot(), np.arange(), array.T, array.where()`
* For matrix math, use the `np.array.*` functions instead of generic operations (*)


```python
print(ex5, "\n", ex6)

# Dot product (matrix product)
# As expected, the result 18 = 2 * 4 + 2 * 5 
ex5.dot(ex6)
```

    [[2 2]
     [3 3]] 
     [[4 4]
     [5 5]]





    array([[18, 18],
           [27, 27]])



### Get a sequence within a range by a certain step


```python
np.arange(1, 10, 2)
```




    array([1, 3, 5, 7, 9])



### Filter values from one of two matrices 
If true, grab from the first matrix, else grab from second


```python
filter = np.array([[True, False], [False, True]])
np.where(filter, ex5, ex6)
```




    array([[2, 4],
           [5, 3]])



## np statistics and set operations - array. `min(), max() ,mean(), sum(), median()`
For these functions, you can specify axis = 0 or 1 to get values by column or row


```python
a1, a1.max(axis = 0), a1.max(axis = 1)
```




    (array([[100,   5, 110],
            [106,   7, 108]]), array([106,   7, 110]), array([110, 108]))



## Sorting Arrays and finding uniques - **array.sort(), np.unique(array)**


```python
# If needed, create a new array to avoid modifying the original array
# Sort by both rows and columns 
sorted = np.array(a1)
sorted.sort(axis = 0)
print(sorted)
sorted.sort(axis = 1)
print(sorted)
print(np.unique(a1))

```

    [[100   5 108]
     [106   7 110]]
    [[  5 100 108]
     [  7 106 110]]





    array([  5,   7, 100, 106, 108, 110])



## Set operations on arrays - `.intersect1d(), .setdiff1d(), .in1d()`


```python
s1 = np.array(['a', 'b', 'c']) 
s2 = np.array(['b', 'c', 'd']) 
```

### `intersect1d`
Values that are in both


```python
np.intersect1d(s1, s2)
```




    array(['b', 'c'], dtype='<U1')



### `setdiff1d*`
`['a']`, elements IN s1 but NOT in s2


```python
np.setdiff1d(s1, s2)
```




    array(['a'], dtype='<U1')



`['d']`, elements IN s2 but NOT in s1 


```python
np.setdiff1d(s1, s2)
```




    array(['a'], dtype='<U1')



### `in1d`
`[False  True  True] `- which elements of s1 are in s2? boolean 


```python
np.in1d(s1, s2)
```




    array([False,  True,  True])



## Broadcasting
Perform operations on differently sized arrays. Preset the values to be added, then spread them over another array. You can broadcast either a 1d array with appropriate dimensions in one dimension, or a scalar value. 


```python
start = np.zeros((4,3)) # zeros array 4 rows 3 columns 
add_rows = np.array([1, 0, 2]) 
y = start + add_rows 
y
```




    array([[1., 0., 2.],
           [1., 0., 2.],
           [1., 0., 2.],
           [1., 0., 2.]])


