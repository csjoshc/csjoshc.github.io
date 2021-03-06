<a href="../../../../index.html">Go back to index</a>

<a href="../../base.html">Go back to Python Portal</a>

<head>
  <link rel="stylesheet" href="../../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

# Planning for problem set 1

## Overview

A problem of selecting items (Cows) to fit in a bag based on the 'space' available

Each possible cow has a name and a space consumption associated with it:

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

# Problem 2 - Brute Force Transport

The brute force algorithm finds the **minimum number** of trips to transport all the cows. Therefore, it starts from the least number of **set partitions** and increases it as lower numbers are ruled out. 

* the `get_partitions(list)` function returns a generator object for all the set partitions of the given list. The output needs to be sorted. 
* save the returned item and call `item.__next__()`

The logic would be
1. for the set partitions in the generator object
2. For each trip in the set parition
3. Test capacity (under the limit) for **that trip**
4. Loop through all trips. 
   1. If any is over the limit, immediately break out of the weight counting loop and go onto the next set partition
   2. Else no breaks then return the set partition


The roadblock for this problem was understanding that the generator, the way it was implemented, did not yield set partitions in increasing set number (smallest number of sets first). Basically the generator was a black box for this problem set since I didn't really want to dig into how it made the sets. Once you apply sorting to a list of all the generator's yields, then you can use the above logic to get the optimal solution. 

### Solution for Problem 2

Spoilers below. 

```python
def brute_force_cow_transport(cows,limit=10):
    cowgen = get_partitions(cows)
    mypartitions = []
    for item in cowgen:
        mypartitions.append(item)
    mypartitions.sort(key=len)

    for item in mypartitions:
        
        for trip in item:
            tripweight = 0
            fits = True
            # the 'trip fits' flag is True by default and is changed w/ break
            
            for cow in trip:
                tripweight += cows[cow]
            # compare summed weight to limit
            #print(tripweight)
            
            if tripweight > limit:
                # break out of current set parition (for trip in item)
                # print("Is greater:", trip, tripweight, limit)
                #print("Breaking on trip:", trip, tripweight)
                fits = False
                break
            
        #print(item, "break", fits)
        # if "fits" flag is True, that means all trips were tested and were not broken out of because of excessive weight
        # therefore we can use it to trigger a return for the current item
        
        if fits:
            return item
```

# Problem 3 - Compare the algorithms 

The brute force algorithm takes 6800 times as long the way I implemented it. It is guaranteed to give the optimal solution, while the greedy one *may* or *may not* arrive at the optimal solution. 

### Solution for Problem 3

Spoilers below. This was a quick and dirty snippet to answer the multiple choice questions since they didn't actually need ask for code for the grader for problem 3. 

```python
start = time.time()
print(greedy_cow_transport(cows, 10))
end = time.time()
print(end - start)

start1 = time.time()
print(brute_force_cow_transport(cows, 10))
end1 = time.time()
print(end1 - start1)

[['Betsy'], ['Henrietta'], ['Herman', 'Maggie'], ['Oreo', 'Moo Moo'], ['Millie', 'Milkshake', 'Lola'], ['Florence']]
0.00010728836059570312
[['Henrietta'], ['Betsy'], ['Florence', 'Millie', 'Maggie'], ['Moo Moo', 'Herman'], ['Milkshake', 'Oreo', 'Lola']]
0.7299518585205078
```

