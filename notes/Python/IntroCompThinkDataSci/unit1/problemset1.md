<a href="../../../../index.html">Go back to index</a>

<a href="../../base.html">Go back to Python Portal</a>
<head>
  <link rel="stylesheet" href="../../../../cssthemes/github.css">
</head>

# Planning for problem set 1

## Overview

A problem of selecting items to fit in a bag based on the 'space' available

Each possible entry has a name and a space consumption associated with it:

```
Maggie,3
Herman,7
Betsy,9
Oreo,6
Moo Moo,3
Milkshake,2
Millie,5
Lola,2
Florence,2
Henrietta,9
```

## Problem 1 - Greedy Cow Transport 

* pick the heaviest cow first
* don't mutate the dictionary that is passed in - make a `.copy()` of that dictionary? 
* Order doesn't matter, break same weight ties arbitrarily, unique names

Example: Running the function with two parameters: a list of cows to transport, and the weight limit per trip
```
`{"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}, 10`
```
The correct answer would be 
```
`[["Jesse", "Maybel"], ["Maggie", "Callie"]]`
```

Some thoughts: The algorithm always chooses the HEAVIEST cow first. This means that we sometimes get nonoptimal solutions, such as the fact with a weight limit of 10 you could'vce fit 3 cows in the first trip (5, 3, and 2 units) if you had avoided choosing weight 6 first. 

The logic would be 

1. While there are cows left to transport:
2. While there is space in the current trip
3. Choose the heaviest cow and add it
4. If there is no space, begin a new trip

I think I'll try implementing this as nested loops before trying recursion

### Solution for problem 1

Spoilers below.

My way of dealing with dictionaries and finding the correct key to append to the trip list was a little crude, but it works overall. 

```python
def greedy_cow_transport(cows,limit=10):
    cowsleft = cows.copy()
    triplist = []
    index = 0
    while len(cowsleft) != 0:
        space = limit
        triplist.append([])
        while len(cowsleft) != 0 and space >= cowsleft[min(cowsleft, key=cowsleft.get)]:
        # filling a trip can empty the remaining cow list - need to prevent ValueError when trying to find min of empty dict
            # While there is space for the smallest cow, try putting in all the cows
            keys = []
            weight = max(v for k, v in cowsleft.items() if v <= space)
            for key, val in cowsleft.items():
                if val == weight:
                    keys.append(key)
            triplist[index].append(keys[0])
            cowsleft.pop(keys[0], None)
            space = space - weight
            # still filling up the same trip here
        # exiting to the first while loop means the trip became full.  
        # therefore we need to increase trip index by one
        index +=1
        # now we can loop again to begin loading for the next trip
    return triplist
```