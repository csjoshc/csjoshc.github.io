
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>
<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
</head>

# Machine Learning

## Classification : 
find a label for the target variable

* Binary or multi-variable (with more than two possible values)
* A function that maps input to output based on parameters
* The model adjusts the parameters to more accurately map input to output
* For classification, the observations exist on a feature space and are split up by **decision boundaries** into different regions, corresponding to different classifications
* Training phase - the algorithm uses the data to adjust the model to minimize error
* Testing phase - the model is evaluated on unseen data

### kNN - k nearest neighbors 

* samples with similar features likely belong to the same class
    
### Decision Tree

* Use decision paths to segment observations 
* In a 2D feature space, a decision tree can be represented by a series of splits along either axis, that successively divide the data increasingly pure subsets
* Attempt to subset the data so that the subsets are as pure as possible, containing samples of a single class
* Repeat this process until you reach a plateau of homogeneity in the nodes
* Start at the root node, and end up at leaf nodes at the bottom, each of which has a class label associated with it
* At the branches in between, the answers to test conditions decide which branch to traverse along. 
* Each decision is made at the node point, in a **greedy algorithm** 

Gini index -  a measure of impurity measure that is minimized in order to determine the best splits

* Test variables to split on

Stopping the node splitting process

* Splitting stops once there is no longer a significant increase in classification results with further splitting
* Or, when a threshold purity for a node is reached (for example, 90%)

#### Pros and Cons 

* rectilinear when splitting on single variable
* splitting on multiple variables simultanesously is computationally intensive 
* relatively simple to understand
* Greedy approach guarantees the best decision **at a node**, but not necessarily the best outcome for the dataset as a whole
    
### Naive Bayes

* Probability of one event given another event


## Regression: Predict a numeric value

## Clustering - organize similar items in data set into groups 

## Association Analysis - identify associations between items or events (co-occurence)

Supervised vs Unsupervised learning

* Supervised requires labeled target data - classification and regression 
* Unsupervised - no target or labeled data - Clustering and association analysis

Scikit-learn

* end to end functionality for machine learning from data cleaning to modeling and analysis
* cross validation, dimensionality reduction, visualization

I'm curious how Skikit-learn functions match up against my experience working with R. Some of the best packages I've used in R include dplyr, tidyr, ggplot2
