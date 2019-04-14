def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            print(i, j)
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

# Based on reading forum responses, you can represent each of the 2^n combinations
# as a binary number. Convert each decimal integer from 0 to 2^n - 1 into
# a binary number, by testing each decimal integer to see if has at least one multiple of the powers of 2, 
# from 2^0 to 2^n. For a power set with three possible elements, this would be 2^0, 2^1 and 2^2

# For example, the first iteration of the generator if called with
# powerSet((4, 5, 6)) will have i be 0, corresponding to a binary number of 000
# Since 0 >> {0, 1, 2} will all have a quotient of 0, there will also be no remainder, and no 
# items will be appended to the combo. Thus it returns an empty list []

# In the 6th iteration, i will be 5. 5 >> {0, 1, 2} will be (5, 2, 1) as quotient
# This yields True, False, True for them being odd numbers (using x % 2 == 1)
# Only the True are appended to combo, coresponding to [4, 6]. This makes sense since
# 5 can be represented as 101 in a binary digits - so we would expect to miss the 2nd value from the set.

# In the 8th and last iteration, i will be 7. 
# 7 >> {0, 1, 2} for a 3 bit binary number yields (7, 3, 1)
# then, (7, 3, 1) % 2 yields True for all - all are odd
# The binary representation (which is a mapping of the power set) is (1, 1, 1)
# This yields [4, 5, 6] as the yield of the generator's last iteration

# The actual function returns the list of actual numbers, instead of a 
# binary representation of the indices of the chosen numbers - this is done using items[j]

# represent it as a list of 0, 1 and 2 - neither, list1, and list2

def twoBag(items):
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            #print(i, j)
            if (i // (3**j)) % 2 == 1: # or == 0
                bag1.append(items[j])
            if (i // (3**j)) % 3 == 2: # or == 1
                bag2.append(items[j])
        yield (bag1, bag2)



test = twoBag((0, 2, 3))
while True:
        test.__next__()
