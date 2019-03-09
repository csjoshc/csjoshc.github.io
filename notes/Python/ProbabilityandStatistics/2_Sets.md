
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>
<head>
  <link rel="stylesheet" href="../../../css_themes/github.css">
</head>

```python
import sys
print(sys.executable)
```
    /home/jcmint/anaconda3/envs/learningenv/bin/python
    
- [Sets](#sets)
  - [Convention - CAPITAL for sets, lowercase for its elements](#convention---capital-for-sets-lowercase-for-its-elements)
  - [Sets in Python](#sets-in-python)
- [Set visualization](#set-visualization)
  - [Visualizing sets in Python - venn diagrams with numeric elements](#visualizing-sets-in-python---venn-diagrams-with-numeric-elements)
- [Set Relations](#set-relations)
  - [Equality, `==`](#equality)
  - [Disjoint: `isdisjoint()`, `!=`](#disjoint-isdisjoint)
  - [Subset: `issubset()`, `<=`; strict: `<`](#subset-issubset--strict)
- [Set Operations](#set-operations)
  - [Complement](#complement)
  - [Intersection: `intersection()`, `&`](#intersection-intersection)
  - [Union: `union`, `|`](#union-union)
  - [Set difference: `.difference`, `-`](#set-difference-difference)
  - [Symmetric Difference (OR): `symmetric_difference()`, `^`](#symmetric-difference-or-symmetricdifference)
- [Cartesian Products](#cartesian-products)
  - [Generating Cartesian products in Python](#generating-cartesian-products-in-python)
- [Russell's Paradox](#russells-paradox)

# Sets

Sets are defined as a collection of elements, and can be defined explicitly {heads, tails}, or implicitly {1:9}, {A:Z}. 

![](https://i.imgur.com/zsEZlXr.png?1)

## Convention - CAPITAL for sets, lowercase for its elements 

* An element can belong to (∈) or not belong to(∉) a  set 
* A set can contain (∋) or lack a member (∌) 
* Repetition may or may not matter 
Different set types:

![](https://i.imgur.com/jNsXSFF.png?1)

## Sets in Python 


```python
myset = set([1,2,30])
print(myset)

# Create an empty set: set()  or set({})
empty = set()
print(empty) 
```

    {1, 2, 30}
    set()



```python
# Test emptiness
print(not myset) # does myset contain no elements?
print(len(myset))
```

    False
    3


# Set visualization 

Venn diagrams can represent set members - elements appear in or out of a set.

![](https://i.imgur.com/NkaVztK.png?1)

## Visualizing sets in Python - venn diagrams with numeric elements 

* Necessary to install matplotlib and matplotlib-venn
```
conda activate learningenv
conda install matplotlib
Proceed ([y]/n)? y
conda install -c conda-forge matplotlib-venn 
```


```python
import matplotlib.pyplot as plt 
import matplotlib_venn as venn 

S = {1, 2, 3} 
T = {0, 22, 1, 3} 
venn.venn2([S, T], set_labels = {'S', 'T'}) 
plt.show()
```


![output_6_0.png](https://raw.githubusercontent.com/csjoshc/csjoshc.github.io/master/notes/Python/ProbabilityandStatistics/output_6_0.png)



```python
s1 = {0, 1} 
s2 = {1, 0} 
s3 = {1, 0 , 1} 
s4  = {0, 2} 
s5 = {3, 4}
```

# Set Relations
Return a logical value that describes the relations between sets. 

## Equality, `==`
Two sets are equal if they have exactly the same elements:


```python
print(s1 == s2, s1 == s3, s1 == s5)
```

    True True False


Since all elements need to be in both sets for the sets to be equal, Equality is difficult to achieve. 

## Disjoint: `isdisjoint()`, `!=`
Two sets are disjoint if they share NO values - overlap region is EMPTY. Empty set is disjoint with all sets except all other empty sets. 

![](https://i.imgur.com/3NsZnOc.png)


```python
print(s1 != s2, s1.isdisjoint(s4))
```

    False False True


## Subset: `issubset()`, `<=`; strict: `<`
If every element in a set is in another set, then it is a subset of that set. {0} is a subset of every set. 
If two sets are subsets of each other, then they are equal (A <- B & B <- A means A == B)

![](https://i.imgur.com/mXWCR5S.png)

A strict subset - a subset that is NOT equal to its superset. 

![](https://i.imgur.com/09KLgkv.png?1)


```python
print(s1 <= s2 , s1.issubset(s4))
# Check for STRICT subset: using `<`
print(s1 < s2, s1 < {0, 1, 2})
```

    True False
    False True


# Set Operations
Obtain a set that is the result of an operation between sets.

## Complement 
* Complement is a set of every element NOT in a set. 
* Not definable in python without defining the 'Universe' first. 
* De Morgan's Law: The Complement of the Intersection of two sets.

![](https://i.imgur.com/4AVqEgU.png)

## Intersection: `intersection()`, `&`
* Intersection is a set of the common elements between sets. 
* The infinte set intersects every set.

![](https://i.imgur.com/YAwSLOJ.png)
![](https://i.imgur.com/2ZKgVnx.png?1)


```python
print(s1.intersection(s1), s1.intersection(s4), s1.intersection(s5))
```

    {0, 1} {0} set()


## Union: `union`, `|`
Union is a non repetitive collection of elements in multiple sets. 
![](https://i.imgur.com/WYjQZea.png?1)


```python
print(s1 | s2, s1.union(s5))
```

    {0, 1} {0, 1, 3, 4}


## Set difference: `.difference`, `-`
A - B is the set of elements in A but not B: 

![](https://i.imgur.com/HSVLpwH.png)


```python
print(s1 - s2, s1 - s4, s4 - s1)
```

    set() {1} {2}


## Symmetric Difference (OR): `symmetric_difference()`, `^`
The set of elements that are in one but NOT BOTH sets:

![](https://i.imgur.com/iO57Gkh.png)


```python
print(s1 ^ s2, s1 ^ s4, s5.symmetric_difference(s4))
```

    set() {1, 2} {0, 2, 3, 4}


# Cartesian Products
Basically, the Cartesian Product of two sets is the set of all combinations of the elements in both sets. You essentially generate `a * b` combinations where `a` and `b` are the number of elements in set `A` and `B`. For `n` sets, you generate a **cartesian coordinate**, an `n` element tuple ordered pair.

* for A and B, it is the set A x B of (a, b) ordered pairs where a ∈ A and b ∈ B 
* The first element must come from set A, and likewise the second from B 
* The cartesian product of the real numbers, R2 = {(x, y): x, y ∈ R} is the cartesian plane, the 2D plane containing all read numbers 
* Likewise, if A and B are sets with real numbers, then A x B will produce a rectangle in the cartesian plane. 
* Tables are essentially cartesian products, as are 3D cubes (A x B x C)

![](https://i.imgur.com/mjwKPan.png)

![](https://i.imgur.com/lKz0EBu.png?1) 
## Generating Cartesian products in Python


```python
from itertools import product 
faces = set({'J', 'Q', 'K'}) # Jack, queen, King 
suits = set({'Dia', 'Spa'}) #diamond, spade 
for i in product(faces, suits): 
    print(i) 
```

    ('K', 'Dia')
    ('K', 'Spa')
    ('J', 'Dia')
    ('J', 'Spa')
    ('Q', 'Dia')
    ('Q', 'Spa')

# Russell's Paradox 

* Sets can be elements and subsets of sets 
* However, it is unclear whether a set can be an element of itself 
* The empty set cannot belong to itself, because the empty set by definition has no elements  
* However, the complement of a set can belong to itself 
 * A set that is "Everything except 0" will contain itself as an element, since this "Not 0 set" is not zero.  
 

Russell's Paradox is that you can define a set that cannot exist: 

* R = {sets that don't belong to themselves} 
* The contradiction is that R is both in, and not in, R itself.  
* Definable but cannot exist 
* Basically, avoid sets that are self-referential or recursively defined 