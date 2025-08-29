
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>



# Probability Theory

* A way to compute the probability of complex events
* assume the probability of basic events. 
Example: flipping coin 1000 times
Σ of k trials is such that it is less than 4k√
![](https://i.imgur.com/FlPlfL2.webp)

* Concentrated around 0, and limited to a range prdiceted by probability theory - as k grows, so does the boundary
![](https://i.imgur.com/FSMA8n2.webp)
With increasing flips, the results converge closer towards 0 relative to the total coin flips. 

# Statistics

Take data to infer the the underlying process. For example, if 1000 flips yields 570 heads, is it biased or not? 
**Statistical Inference**
* Suppose the coin is fair
* Calculate the probability of such a coin Σ = 140 
* However, it is very unlikely that |S1000| > 4* root(1000) ~ 126  
* Therefore, it is *very* unlikely that the coin is unbiased

In polling, extrapolate general conclusions from sample. 

# Three Card Puzzle example

* Three cards in a hat: (R/R), (R/B), (B/B) (differently colored sides)
* A card that is blue on one side could be blue or red on the other sides
* Run a simulation that randomly picks a card with a certain side facing up
* Matching sides = -$1, not matching = +$1 
* Since a "match" happens much less than a "not match", average is -$.33 per iteration (since it is 2:1 odds to get a match)

