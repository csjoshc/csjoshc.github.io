<a href="../../../index.html">Go back to index</a>
<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
</head>

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

## Arrays

Arrays are collections of like (similar) values. While arrays are smaller memory wise, they are difficult to mutate, whether inserting or deleting, since all the subsequent elements have to be shifted. The shifting of values would require additional space allocated to the array, which in turns requires initializing a new array and copying over all the values (and then the old array needs to have its memory freed). Lookup and sorting are much better, since the contiguous nature allows easily jumping to a specific location.

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