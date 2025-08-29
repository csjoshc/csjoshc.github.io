
  🏠 Home
  🐍 Python

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

```
`[["Jesse", "Maybel"], ["Maggie", "Callie"]]`
```
Some thoughts: The algorithm always chooses the HEAVIEST cow first. This means that we sometimes get nonoptimal solutions, such as the fact with a weight limit of 10 you could'vce fit 3 cows in the first trip (5, 3, and 2 units) if you had avoided choosing weight 6 first. 

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
            weight = max(v for k, v in cowsleft.items() if v  limit:
                # break out of current set parition (for trip in item)
                # print("Is greater:", trip, tripweight, limit)
                #print("Breaking on trip:", trip, tripweight)
                fits = False

        #print(item, "break", fits)
        # if "fits" flag is True, that means all trips were tested and were not broken out of because of excessive weight
        # therefore we can use it to trigger a return for the current item

        if fits:

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