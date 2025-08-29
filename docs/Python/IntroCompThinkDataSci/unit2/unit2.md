
  🏠 Home
  🐍 Python

# Stochastic Thinking
Predictive nondeterminism - The core premise here is that while causal outcomes are theoretically predictable, in real world situations the lack of knowledge doesn't allow making deterministic predictions, so in certain situations things may as well be treated as inherently unpredictable. 
A stochastic process - the next state depends on prior state and a random element. This can be challenging for making results reproducible. 
```python

def genEven():
    return random.choice(range(0, 100, 2))
```
# Probabilities
Setting a random seed using random.seed(x) is not truly random which is useful for repeatability. For rare events, many trials are necessary to converge on a sample probability that approximates a derived actual probability (which can be calculated for certain but not all events)
# Random Walk 
Simulations are descriptive, unlike optimization algorithms that are prescriptive. They can help model mathematically undefined systems and can be improved incrementally. The random walk is an example of a simulation. 

 In simulating random walks, there are a few aspects to model - each random walk has some number of steps, the walks are repeated some number of times, and an average distance from the origin of the walks is aggregated. The field is unbounded and defined as a dictionary mapping each wandering entity to a location. The entities can have balanced or biased wandering characteristics. 
Then, after running a simulation of n steps, there is an offset to the biased wanderer location cluster corresponding to the net average bias per step multiplied by the number of steps. For example, if an 'up' step of 0.9 and down step of '1.1' results in an average net bias per 4 steps of 0.2 downwards, then per step there is an average net bias of 0.05 downwards, and the cluster of biased wanderer final locations after 10000 steps would be 0.05 * 10000 or 500 units downwards of the origin.