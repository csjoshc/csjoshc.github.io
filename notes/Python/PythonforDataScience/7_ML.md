
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>

<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
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

**Gini index** -  a measure of impurity measure that is minimized in order to determine the best splits

* Test variables and thresholds to split on

#### Stopping the node splitting process

* Splitting stops once there is no longer a significant increase in classification results with further splitting
* Or, when a threshold purity for a node is reached (for example, 90%)

#### Pros and Cons 

* rectilinear when splitting on single variable
* splitting on multiple variables simultanesously is computationally intensive 
* relatively simple to understand
* Greedy approach guarantees the best decision **at a node**, but not necessarily the best outcome for the dataset as a whole


## Clustering - organize similar items in data set into groups 

* Segment data into similar groups - similar to classification, but with no objective class labels, so Unsupervised
* Segmentation of existing observations, classifying new data, anomaly detection (observations that aren't outliers in any one variable, but their combination makes them fall outside of existing cluster)
* Intracluster differences are minimized, intercluster differences are maximized 

### Normalizing values

* Since distance is used to assess similarity and dissimilarity, normalization of input variables is necessary to prevent any one from dominating the calculations. 

### k-means clustering

1. Select *k* initial centroids
2. Assign each sample in the data set to the closest centroids
    * This is based on a distance calculation between the point and the centroid
3. Calculate cluster means, which become the new centroids
4. Repeat 2 & 3 until some stopping criteria is reached 


#### Choosing initial centroids

* Final clusters are sensitive to initial centroids. In order to solve this, repeat algorithm with randomized initial centroids to generate aggregate results.

#### Evaluating cluster results

* Within cluster sum of squares
    * Error is the distance between the sample and centroid - square this error 
    * Errors for all points in a cluster are summed
    * Clusters sums are summed 
    * Within-Cluster Sum of Squared Error - WSSE

* A cluster having a smaller WSSE is numerically better, but not more correct
* Increasing k will always decrease WSSE 

#### Choosing k

* Visualize for natural clusters, or depend on intended application/domain specific knowledge
* Data driven - generate metrics for a range of k values

One method is the elbow plot - see where the dropoff in WSSE as k increases begins to plateau, suggesting little benefit to adding further centroids

![](https://pythonprogramminglanguage.com/wp-content/uploads/2017/07/elbow-method.png)

#### Stopping criteria 

* No changes to centroids
* Cluster assignment changes per cycle fall below a threshold (such as 1%) 


## Naive Bayes

* Probability of one event given another event

## Regression: Predict a numeric value

* Used for forecasting, estimation, predictions future trends
* Input variables can be numeric or categorical
* Supervised, since the target label is a numeric value

### Linear regression

* Simple but powerful model for a linear relationship between input and output; multiple linear regression can handle multiple inputs
* Regression minimizes the error using the least squares method (square of the distance between the predicted and actual value, or the residual) 


## Association Analysis - identify associations between items or events (co-occurence)

Supervised vs Unsupervised learning

* Supervised requires labeled target data - classification and regression 
* Unsupervised - no target or labeled data - Clustering and association analysis

Scikit-learn

* end to end functionality for machine learning from data cleaning to modeling and analysis
* cross validation, dimensionality reduction, visualization

I'm curious how Skikit-learn functions match up against my experience working with R. Some of the best packages I've used in R include dplyr, tidyr, ggplot2
