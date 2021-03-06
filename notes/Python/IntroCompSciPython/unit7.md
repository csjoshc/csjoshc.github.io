
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>
<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
</head>

# Testing and Debugging 

* Write function specifications
* Modularize programs
  * Each part can be tested in turn
* Check input & output conditions w/ assertions
* Be aware of edge cases, and compare input output pairs

## Types of Testing

* Unit testing - validate each function by testing separately
* Regression testing - test for bugs that may be been introduced or reintroduced
* Integration testing - for the overall program

## Black box testing

Reason through the paths in the specification, separate from the code, focusing on edge cases. 

* If it is on lists, consider an empty list, a one element list, and so on. 
* If it is on numbers, consider 0, perfect squares, numbers less than 1, negative numbers, extremes, and so on. 

## Glass box 

Base test cases on paths through the code, aiming to be path complete by running though all potential paths. Make sure to hit every branch in a branching if tree, enter for and while loops and test exit conditions. 

## Bugs 

Overt - obvious case with crashing or doesn't stop
Covert - code runs but return not correct
Persistent - occurs predictably
Intermittent - occurs sometimes

Good defensive programming will ensure that bugs will be overt and persistent. Intermittent and Covert bugs are worse. 

Add in print statements liberally to isolate where things might be wrong. 