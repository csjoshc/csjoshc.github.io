<a href="../../../../index.html">Go back to index</a>

<a href="../../base.html">Go back to Python Portal</a>

<head>
  <link rel="stylesheet" href="../../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

# Optimization models & the Knapsack problem

* Objective function to maximize or minimize
* Constraints 
* Often just approximate a solution with a greedy algorithm

## Knapsack problem

In the knapsack problem, you have a capacity and have to decide how to fill it. Discrete contents are harder than continuous ones. 

* Each item is a pair of value and weight
* Knapsack has a total capacity, *w* 
* A set of available items
* A list indicating whether an item has already been taken
* For each item in available items, choose those to take and multiply it by its value.
* The sum of chosen items' weights is less than *w*

## Brute force algorithm

* Try every possible combination (every subset of subject set), remove those not under *w*, and choose the remaining with highest value. 
  * The algorithm is exponential, having 2^n complexity
  * Find approximate and optimal solutions

## Greedy algorithm

* while the knapsack is not full, put the best available item in. 
* nlog(n) complexity

What does 'best' mean? Based on the highest value, lowest weight, or the ratio? 

```python
def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)
```

Using the lambda function:
```python
f = lambda x, y: 'yes' if (x%y == 0) else 'no'
f(1, 2)
'no'
f(2, 2)
'yes'
```

The keyfunction will define how the greedy algorithm makes choices. Different answers will result since locally optimal choices won't necessarily yield globally optimal solutions. 
* especially seen in local optima
* performance will depend on constraints

# Decision trees and dynamic programming

* Select from the list of available items
* If an item fits, a node represents the decision to take (left) or not to take (right) that item. 
* Recursively apply to nonleaf children
* complexity is exponential, 2^n

```python
def maxVal(toConsider, avail):
"""Assumes toConsider a list of items, avail a weight
Returns a tuples of the total value of a solution to the 0/1 knapsack
problem and the items of that solution"""
if toConsider == [] or avail == 0:
    result = (0, ())
elif toConsider[0].getCost() > avail:
    # Explore right branch only
    result = maxVal(toConsider[1:], avail)
else:
    nextItem = toConsider[0]
    # Explore left branch
    withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
    withVal += nextItem.getValue()
    # Explore right branch
    withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
    # Explore better branch
    if withVal > withoutVal:
        result = (withVal, withToTake + (nextItem,))
    else:
        result = (withoutVal, withoutToTake)
return result
```

* Consider the first item - if it exceeds the available space, recursively call itself to consider the rest of thelist
* Else - consider the cases where the item is **taken** or **not taken**; in both cases the item is **removed** from the items to take (`toConsider[1:]`).
* If the item is **taken**, then call the function recursively with the avaiable space minus that of the taken item (`avail - nextItem.getUnits()`).
* If the item is **not taken**, call the function recursively with the same available space, `avail`. 
* Finally, evaluate both branches for the better outcome. 
* Return `result`, a tuple of the value in a set, and a list of the items in a set. This is the best solution thus far. 

## Recursive Fibonacci 

The below implementation is simple but impossible to run for moderately sized numbers due to how inefficient it is, since the number of function calls is basically related to the growth in fibonacci value itself. For example fib(120) is about 8.7E24.

```python
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

## Memoization - Dynamic Programming

When repeating function calls for identical inputs, lookup the output value in a previously recorded table instead of recalculating it. If it hasn't been calculated yet, calculate it and add it to the table. 

```python 
def fastFib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    # return the value at key in memo if n != 0,1
    try:
        return memo[n]
    # calculate new value and store in memo dict if unknown
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result
```

Dynamic programming criteria:

* **Optimal Substructure** - locally optimal solutions can be comebined for globally optimal solutions
* **Overlapping subproblems** - identical subproblems use identical solutions 

## Dynamic Programming

For a bag problem, subproblems can be made to be overlapping by generalizing the problem to be solved as a function of remaining weight and the weight of taken items, regardless of the specific items taken. For example, two subproblems would overlap if the occupied weight and available items to choose from were identical, even if the items chosen so far were different. 

In defining a specific subproblem, pass a dictionary of previously encountered subproblems and optimal solutions: The key is a tuple of items left to be considered (length of the item list since items are removed after being considered) and the remaining weight. 

Overall, dynamic programming runs on low order polynomial in a best case scenario, and can be much, much faster than a comparable exponential algorithm. 

* solve problems with exponential solution space
* find optimal solutions, not just approximate ones
* reduce sorting order below nlogn from merge sort
* Example: choosing step sizes (1, 2) for N steps to traverse is a problem with optimal substructure and overlapping subproblems. 

# Graph Problems

A graph is a set of nodes/vertices that may have properties associated with them (color in this example). The edges/arcs connecting pairs of nodes can be undirected or directed (with parent and child nodes), and unweighted or weighed. This example is of a graph with directed, weighted edges. 

![](screenshot2.png)

A tree is a special case of a graph. Networks in general can be represented by graphs. In these networks, note attributes can include the color, size and label of the node. 

 ## Roads and graph theory

 A good example of real world application is modeling travel distance between two locations, with those locations and other intermediate locations modeled as nodes, and the distance between modeled as edges. Each edge has a weight representing the source to destination travel time. Then, the ideal travel time would be the solution of a graph optimization problem. 

 For this class of problems more generally, graphs allow the abstraction away of irrelevant details. 

 ## Class Graph

 There are a few classes implemented, and I'll just summarize them each here
  
  * `Node` - only has a "Name" attribute
  * `Edge` - constructor has source, dest attributes assumed to be of class Node
  * `Digraph` - constructor takes no arguments, but has an edges attribute that is initialized empty, a dictionary mapping each of its Node attributes to one or more of its other Node attrributes. The primary helper functions include those adding Nodes, Edges and also a decorator to define the conversion to a string when printing the object. Other helper functions are for accessing and returning Node attributes. 
  * `Graph` - a subclass of Digraph with a `addEdge()` method that overrides the parent class method by adding an additional reversed edge to the edges dictionary attribute.

The edges attribute of Class Digraph is an adjacency list, associating each node with a list of child nodes. 

When representing graphs, phenomena such as loops can arise, which complicates the optimization search. 

## Exercise 3 - three students in a line

Combination of three students (ordered line) are represented by nodes. Two nodes are connected by an edge if the ordered lines are interchangeable by just switching one pair of adjacent students. 

The way the addEdge method is implemented for Graph class, the node must be in the edges attribute first before an edge can be added. 

## Finding the shortest path

The depth first search is similar to the left first search of a bag problem. The main difference is keeping track of previously traversed nodes, since there can be loops in the graph. Also:

* return to most recent node once a node with no children is reached
* discard paths not shorter than the current shortest path
* recursively find the DFS on child nodes not in the current path. 

The breadth first search is somewhat more complex because it is searching across all nodes simultaneously, and thus needs to keep track of the depth of its search as it goes. It generates paths in a branching fashion - all child nodes of the current path are simultaneously generated and appended to a pathqueue. The oldest item in the pathqueue is removed and its child nodes are appended to it, and then added back to the pathqueue. As soon as a path is found, the algorithm stops - this works because all the path lengths in pathqueue increment in length together - therefore the first found path **must** be the shortest. 

BFS isn't modifiable for use in a weighted path search. It is of O(n) complexity.

* may run slower or faster than DFS
* if it prioritizes the same nodes, will be as fast as DFS in 

Graph problems are in some sense already solved with many algorithms - what is complex is fitting real world situations into the framework of graphs. 

Last exercise - when defining a child class with its own constructor (not just its own methods), I needed to redefine all the attribute assignment, there should be a way to use the superclass constructor and just set the additional attributes

```python
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() + ' (' + str(self.getWeight()) + ')'

```