<a href="../../../../index.html">Go back to index</a>

<a href="../../base.html">Go back to Python Portal</a>

<head>
  <link rel="stylesheet" href="../../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>

# Inferential Statistics 

For a sample drawn out of a population, the larger the variance in the feature, the more samples that are required to approximate the distribution in the population. Simulations can each have a number of trials, and the simulation itself can be run multiple times to yield a distribution of results. 

Bernoulli: when repeating a test with a probability p, the actual aggregate probability taken as a proportion of trials will converge to this theoretical probability (and the difference converges to 0) as the number of trials increases to infinity. 

Gambler's Fallacy - a prior deviation from expected behavior has no bearing on likely future behavior. This is because each event is taken to be independent from prior events, even if they are extreme events. On the other hand, in regression to the mean, an extreme event is likely to be followed by a non extreme event (however, the extreme event is *not* causing subsequent events to not be extreme).

# Confidence intervals and standard deviation

The number of samples needed to estimate the probability of an event close to accurately depends on the sample variance or standard deviation, in context of the mean. The standard deviation can be used to construct a confidence interval, which is the probability that a range contains a true unknown probability of an event, such as "The return on betting is -5% with a +/- 1% with a 95% level of confidence."

* +/- 1 s.d. for 68% confidence
* +/- 2 s.d. for 95% confidence
* +/- 3 s.d. for 99.7% confidence

As the sample size grows (whether number of trials, or iterations of simulations), the confidence interval shrinks. 

## Calculating standard deviation

Standard deviation is calculated as follows:

![](std.png)

Implement a function that returns the standard deviation of a list of strings, or float('NaN') if empty. Here I implement it the classic list way as well as the simple one liner from numpy (which is similar to lapply from R, to vectorize a function to a list or array..)

```python
def stdDevOfLengths(L):
    from math import sqrt
    if len(L) == 0:
        return float('NaN')
    else:
        lengths = []
        for string in L:
            lengths.append(len(string))
        # mean is mu
        mean = sum(lengths) / len(lengths)
        # diff_sq is t - mu squared
        diff_sq = []
        for item in lengths:
            diff_sq.append((item - mean)**2)
        return sqrt(sum(diff_sq)/len(lengths))
        
def stdDevNumpyWay(L):
    import numpy as np
    if len(L) == 0:
        return float('NaN')
    else:
        return np.vectorize(len)(L).std()
```

# Inferential statistics and probability

The estimation of confidence intervals using an empirical rule is only valid for a zero mean estimation error, and a normal distribution. A probability distribution can either be discrete or continuous, with the latter being trickier to work with. A **probability density function** shows the probability of the value falling within a certain range, with the area under the curve being the probability. 

A normal distribution is defined by its mean and standard deviation. It peaks at the mean, and asymptotically approaches 0 at either end. It's easy to generate normal distributions in python:

```python
import pylab
import random

dist = []
for i in range(10000):
    dist.append(random.gauss(0, 10))
pylab.hist(dist, 10)
```
![](Figure_1.png)

While a normal distribution can be integrated (when defined as a gaussian function) using the SciPy.integrate library, many random events are individually not normally distributed - for example, the value of random card from a deck or a spin of a roulette wheel is **equally** distributed across all the possible values (assuming it is fair!) These random events will only begin to approximate a normal distribution once many trials are conducted and the probabilities are aggregated. 

Central Limit theorem: Given a large enough sample, the means of a set of samples will be approximately normally distributed, have a mean close to the original distribution's mean, and have a variance close to the original distribution's variance divided by sample size. 

Example of sampling without replacement. There are a lot more elegant solutions - the silver lining is that the code being broken down into lots of small steps makes debugging with breakpoints easier. 

```python
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
```

# Data Sampling 

It is also possible to generate a confidence interval without repeated sampling or simulations, such as in polling. In stratified sampling, subgroups are individually sampled so representative results can be found for each subgroup. The goal is to have the sample mean and standard deviation converge on the population mean and standard deviation. 

When repeating samples of a population to get a normal distribution of sample statistics, increasing the sample size will affect the standard deviation (tighten the confidence interval) more than increasing the number of samples. However, at a certain point the aggregate number of observations across all the samples may be too much if the number of samples and sample size are inflated excessively. In this case, it may be useful to look at what we can conclude from a single, reasonably small sample. 

## Standard Error

One a sample reaches a reasonable size, the sample std dev approximates the population std dev. When testing this outcome for uniform, gaussian and exponential distributions, the greatest difference in sample vs population std dev occurs for the exponential distributions. While all three have the difference in sample vs population std dev fall off with increasing sample size, the exponential distribution will have a larger difference compared to the other distributions, at any one sample size. 

On the other hand, sample size does **not matter** - even sampling a few hundred data points from millions will yield a std dev that can be used to generate an estimated standard error, which can be used to generate confidence intervals around the sample mean. This relies on choosing independent, random samples from the population - this isn't always possible to achieve. 


