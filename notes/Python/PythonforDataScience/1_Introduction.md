
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>

  


Sources of data have massively grown, as well as advances in storage and computing at scale, increasing the demand for its processing to provide data driven predictions for a variety of industries. 

# Introduction

* Data science involves diverse skillsets in Math/Stats, Programming and so on, working in teams  
* Python is a clear leader in many data sciences, as it offers a diverse libraries for data management, processing and visualization, all parts of pipeline 
     * Jupyter Notebooks make the process repeatable  
     * NumPy 
     * Pandas 
     * Matplotlib 
     * Scikit-learn 
     * BeautifulSoup
 
# Steps for Data Analysis

* Data science big picture: statistics, big picture
* Justify using analytics - seek to obtain actionable insights

Work process
* Acquire raw data, prepare, analyze, report, act
* Data engineering & computational data science/analytics
* Formulate the right questions - define the problem 
* Assess situation - C/B analysis, contingencies, regulations, resources and requirements

## Acquisition
* Data can come from relational or noSQL databases, csv and Text files, live feeds or unstructured. 
* Databases provide APIs for data access, and so do some websites

## Preparation
* Preliminary Analysis - understand the nature of data
    * Correlations, general trends
    * Summary statistics - mean, mode, median, range, stdev
    * Histograms, boxplots, line graphs, heat maps, scatterplots

* Pre-process Data
    * Remove outliers, missing/null values, duplications, inconsistencies, invalid data and other unwanted entries
    * Generate estimates for data imputation
    * Dimensional reduction
        * Determine  a smaller subset of dimensions that capture most of the variability in the data
    * Feature selection - select attributes that have the greatest impact on target of predictions
        * Models are easier to train and interpret, and better generalize to new scenarios
        * Derive new features where necessary 
    * Transformation - reduce noise and variability, aggregate where necessary 
    * Scaling - normalize ranges
    * Data manipulation - sorting, grouping, computing summary statistics
    
## Analysis
* Iterative, repeatable process 
    * Select technique, build model, validate model
    * Split into training and test sets
    * Consider repeating or adding data
* Supervised & unsupervised learning
    * Classification - predict categories or a binary (0,1) and compare with a correct value
    * Regression - predict numerical value and compare with correct value
    * Clustering - organize similar items into groups
    * Association analysis - find rules that capture associations amongst observations - verify predictions
        * Market basket analysis
    * Graph analysis - data is a graphical representation with nodes and links
        * find connections between entities 
        * verify existence of predicted phenomena in the real world
* Scikit-learn 
* Sklearn-cluster -> kmeans clustering
     * Group observations into meaningful sets using those attributes
* Interpreting cluster results
     * Similarities within each cluster and differences between clusters
     * Each group is unique in difereing from each other in at least one attribute
     * Customized improvement strategies for each group

## Report results and then act
