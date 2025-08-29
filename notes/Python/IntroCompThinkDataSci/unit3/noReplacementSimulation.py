import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    
    prop = []
    for trial in range(numTrials + 1):
        # Represent different colors as 0 or 1. Then, if the sum of the drawn numbers is
        # either 0 or 3, the trial produced the same color 3 times
        bucket = [0, 0, 0, 1, 1, 1]
        results = []
        for draw in range(3):
            color = random.choice(bucket)
            results.append(color)
            bucket.remove(color)
        if (sum(results) == 0 or sum(results) == 3):
            prop.append(1)
        else:
            prop.append(0)
    return (sum(prop)/len(prop))

print(noReplacementSimulation(100))
