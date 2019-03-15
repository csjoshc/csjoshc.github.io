
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>
<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
</head>


```python
import sys
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import HTML
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import os, sys
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Data Visualization
Simplifies data interpretation. 

## Conceptual or data-driven 
For example, a theoretical plot - supply & demand, stress & strain. 

## Declarative or Exploratory 
Presentation of real-world data to reach a final conclusion. 
Exploratory is just for quick analysis rather than polishing the visualization itself. 

## Principles of Good Design
* Trustworthy 
 * Evidence for a figure should be in the data. E.g. zooming in on an axis to exaggerate a change in a value is not trustworthy. 
* Accessible
 * Make visuals appropriate for audience, and to fulfill its intended purpose
* Elegant

## Visualization libraries
Matplotlib is the main go-to for day to day visualization; others have specialization for specific use cases.
* Using [the Indicators](https://www.kaggle.com/worldbank/world-development-indicators/version/2#Indicators.csv) data set. 

Below

* head of dataframe
* number of unique country names
* 


```python
indicators = pd.read_csv('../../../../data/w5vis/Indicators.csv')
# no need to run often, so separate into its own code cell. 
```


```python
# print head of dataframe!

display(HTML(indicators.head().to_html()))
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CountryName</th>
      <th>CountryCode</th>
      <th>IndicatorName</th>
      <th>IndicatorCode</th>
      <th>Year</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Adolescent fertility rate (births per 1,000 wo...</td>
      <td>SP.ADO.TFRT</td>
      <td>1960</td>
      <td>1.335609e+02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Age dependency ratio (% of working-age populat...</td>
      <td>SP.POP.DPND</td>
      <td>1960</td>
      <td>8.779760e+01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Age dependency ratio, old (% of working-age po...</td>
      <td>SP.POP.DPND.OL</td>
      <td>1960</td>
      <td>6.634579e+00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Age dependency ratio, young (% of working-age ...</td>
      <td>SP.POP.DPND.YG</td>
      <td>1960</td>
      <td>8.102333e+01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>Arms exports (SIPRI trend indicator values)</td>
      <td>MS.MIL.XPRT.KD</td>
      <td>1960</td>
      <td>3.000000e+06</td>
    </tr>
  </tbody>
</table>


This is actually a 4D dataset, with country, indicator, year and value. I would say its combination of the first three that match each value. 


