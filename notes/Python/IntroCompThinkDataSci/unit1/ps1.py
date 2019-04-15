###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================
import os, time
#print(os.getcwd())
os.chdir('notes/Python/IntroCompThinkDataSci/unit1')


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
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
        # exiting to the first while loop means the trip became full. therefore we need to increase trip index by one
        
        index +=1
        # now we can loop again to begin loading for the next trip
    return triplist
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

# Problem 2
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
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
#print(cows)



# trial = greedy_cow_transport({'Muscles': 65, 'Miss Bella': 15, 'Horns': 50, 'Louis': 45, 'Patches': 60, 'MooMoo': 85, 'Clover': 5, 'Lotus': 10, 'Polaris': 20, 'Milkshake': 75}, 100)
# print(trial)
# trial2 = greedy_cow_transport({'Lilly': 24, 'Dottie': 85, 'Betsy': 65, 'Patches': 12, 'Daisy': 50, 'Buttercup': 72, 'Willow': 35, 'Abby': 38, 'Coco': 10, 'Rose': 50}, 100)
# print(trial2)
# trial3 = greedy_cow_transport({'Coco': 59, 'Betsy': 39, 'Starlight': 54, 'Buttercup': 11, 'Willow': 59, 'Rose': 42, 'Abby': 28, 'Luna': 41}, 120)
# print(trial3)
# greedy_cow_transport({"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}, 10)
# print(greedy_cow_transport(cows, 10))
#greedy_cow_transport(cows, 15)
#greedy_cow_transport(cows, 20)


start = time.time()
print(greedy_cow_transport(cows, 10))
end = time.time()
print(end - start)

start1 = time.time()
print(brute_force_cow_transport(cows, 10))
end1 = time.time()
print(end1 - start1)
# test = brute_force_cow_transport(cows, 21)
# cows1 = {'Boo': 20, 'Horns': 25, 'Miss Bella': 25, 'Lotus': 40, 'Milkshake': 40, 'MooMoo': 50}

# test1 = brute_force_cow_transport(cows1, 100)
#print(test1)
#print("----------------------------")
#for item in get_partitions(cows1):
    #print(len(item))
#    pass
