<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to General topics portal</a>

  

# C++ skimming

A few tidbits picked up from the intro on C. I'm not going to include too much on cpp since I don't have a compiler (no Visual Studio) and don't feel its **too** relevant to my situation.

* The curly braces encapsulate nested code similar to identation in Python.
* get_string is a user-defined function that is a wrapper around stdin
* `int main(void)` - no real counterpart to this in Python. `if __name__ == "__main__":` in Python is a related concept but not analogous either.
* floats and doubles can't represent numbers perfectly. For example, 2/10 which should be 0.2, has inaccuracies after 7 or 15 decimal points in the float and double data types, respectively. 
  
```cpp
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("What is your name?\n");
    printf("hello, %s\n", name);
}
```

For loops

```cpp
for (int i = 0; i < 50; i++)
{
  printf("Number %s", i)
}
```

function definitions - do a dummy reference to function so the main definition can go elsewhere.

```cpp

void do_thing(int n);

int main(void)
{
  int num = 2 + 2;
  do_thing(num);
}

void do_thing(int n)
{
  printf("Num is %s", n);
}
```

do-while loop

```cpp
int n = 0;
do
{
  n ++;
}
while (n < 10)
```

## About strings...

Apparently, strings are not directly implemented in c, but are instead stored as memory pointers to char *s arrays - specifically, the first bit of a memory block corresponding to the first character of the stored string, and which is terminated by a null character. This is much more abstract than anything I encountered in Python or R, so for now it's probably good enough to just be aware of the quirks of such a data type, such as null characters, copying strings, memory allocation, etc. For example, testing equality is more involved than just using a boolean comparison with string pointers since that test for the equality of the memory pointer (a hexadecimal location), not the bits making up the actual char *s array. 

## Pointers

Pointers can be created by appending a `*`. The code below assigns the memory location of int k to the pointer pk, which has the value of a memory address, and a type describing the data stored at that memory address. These pointers can be passed between functions, allowing the data at the pointers to be accessed and modified directly. 

In C++ objects are created by allocating a memory location and then filling it. This is different from Python, where variables are created as references to objects containing the assigned value. 

```cpp
int k; 
k = 3; 
int* pk;
pk = &k;
```

The `malloc()` function returns a pointer for a block of dynamically allocated memory. This memory block must be freed after the function that uses it is finished executing. 

## Arrays

Arrays are collections of like (similar) values that are stored in contiguous memory locations. The variable assigned to an array is just a pointer to the first element of the memory block storing elements of the array. While arrays are smaller memory wise, they are difficult to mutate, whether inserting or deleting, since all the subsequent elements have to be shifted. The shifting of values would require additional space allocated to the array, which in turns requires initializing a new array and copying over all the values (and then the old array needs to have its memory freed). Lookup and sorting are much better, since the contiguous nature allows easily jumping to a specific location.

# Algoritms

## Selection sort

In selection sort, you a two step process until all elements are sorted. First, search the unsorted portion to find the smallest value. Then, swap that value with the first unsorted element. This build a sorted array from left to right (smallest first).

The algorithmic complexity is O(n^2) in the worst and best cases. 

## Bubble sort

In bubble sort, you start the algorithm with a nonzero counter value before the first iteration, but set it to 0 at the beginning of each iteration. Then, until the swap counter is 0, swap any two adjacent incorrectly ordered elements,adding 1 to the swap counter each time. This results in moving the largest element to the rightmost index, building a sorted array from right to left (largest first). 

Worst case is O(n^2), but best case is O(n) if it is already sorted. 

## Insertion sort

In insertion sort, declare the first element sorted. Then, look at each unsorted element one at a time, and insert it into the preceding sorted block. Shift a subset of the previously sorted block rightwards as needed. 

Worst case is O(n^2), best case again is O(n) if already sorted. 

## Merge sort

Merge sort uses recursion and subsetting the sorting problems, to sort each half on its own. Subsets are recursively subsetted themselves assuming the size of a subset is greater than one element. Each one element subset is considered sorted on its own. 

The last step, Merging arrays, is where the real work occurs. When merging arrays (of arbitrary size), compare the first elements of the two arrays being merged; the smaller element becomes the next element of the merged array. Continue this process until all the elements of both arrays are assigned into the new array. Once one array has been completely merged, the other array can be dropped in immediately, since there are no more values to compare against and they must necessarily be in order as-is. 

Worst and best case scenarios is O(n*log(n)).

## Linear search

One caveat of a linear search is that you won't know something **isn't** in the array until every element has been examined. Worst case scenario is O(n), while the best case is O(1). 

## Binary search

When an array is sorted, you can jump to the middle of the array, and discard the half of the array that cannot contain the target element. The worst case is log(n), while the best case is O(1). 

# Data Structures

## Singly linked lists

Singly linked lists consist of nodes containing a value (int) and a memory pointer to the next node. The most important node is the first - it can grant access to subsequent nodes. A downside is that you can't go back from a node to a prior node, but the upside is that you don't need to copy all the elements as you would for an array with fixed size, and also don't need to worry about overallocation. Size-wise, doubly linked lists and singly linked lists are slightly larger than arrays, but not significantly so. 

* For sorted order, algorithmic complexity of inserting elements is O(n) since you need to traverse along the list until the correct point is reached. This is the same as the complexity of lookup (since you have to lookup as you insert in order).
* For unsorted order, inserting is O(1), since you can just point the first node at the newly inserted node, and point the newly inserted node at the node that was previously the second (but is now the third)
* Deletion is also a breeze, since all you need to do is change where the *next pointer is pointing. 

## Hash Tables

Hash tables are a way of binning values into "belonging" into a category, so that they will be inserted into the appropriate linked list. The list of categories functions similar to an array in allowing **jumping** to the correct category during a lookup. For example, Alphabetical hash table will on average allow half of letters to be skipped (that would otherwise have to be traversed in singly linked lists) - of course, in the real world words are not normally distributed amongst all the letters. 

* The array of a hash table contains pointers to linked lists, which in turn contain the actual stored values. This array is immutable - (for example, the set of letters is immutable).
* Theoretically, hash tables are still O(n) asymptotically, but in the real world the hash table would always be defined so that the loaded data would be meaningfully subsetted into linked lists (or else what would the point of the has table be?).

## Tries/Tree structure

The Trie data structure can be implemented as a linked list with **two** or more *next pointers, to a left and right child. The node positions encode mathematical logic (between child and parent nodes). This forms branches that mathematically subset the data in log complexity - e.g. the height of a tree structure will be the log of number of branching decisions that need to be made (for example, the length of a word).

Building a Trie has large overhead at the beginning, but insertion is easy once the framework is set up, and repeatedly used nodes have already been initialized. Deletion is good, and lookups/sorting is 2nd to that of arrays. The downside is that each node contains pointers to all the possible child nodes, so size grows rapidly with these pointers. 
