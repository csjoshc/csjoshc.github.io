
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>

<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>


```python
import sys
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('fivethirtyeight')
import os, sys
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Data Visualization
Simplifies data interpretation. 

**Conceptual or data-driven**
For example, a theoretical plot - supply & demand, stress & strain. 

**Declarative or Exploratory**
Presentation of real-world data to reach a final conclusion. 
Exploratory is just for quick analysis rather than polishing the visualization itself. 

**Principles of Good Design**

* Trustworthy 
 * Evidence for a figure should be in the data. E.g. zooming in on an axis to exaggerate a change in a value is not trustworthy. 
* Accessible
 * Make visuals appropriate for audience, and to fulfill its intended purpose
* Elegant

## Visualization libraries - Matplotlib
Matplotlib is the main go-to for day to day visualization; others have specialization for specific use cases.
Common components include a chart type, axes ranges and labels, figure labels, legend, aesthetics and annotations. 

* Using [the Indicators](https://www.kaggle.com/worldbank/world-development-indicators/version/2#Indicators.csv) data set. 


```python
indicators = pd.read_csv('../../../../data/w5vis/Indicators.csv')
# no need to run often, so separate into its own code cell. 
```


```python
# print head of dataframe
indicators.head()

# unique country names
countries = indicators['CountryName'].unique().tolist()
print("country num:", len(countries))

# number of country codes
cocodes = indicators['CountryCode'].unique().tolist()
print("country codes:", len(cocodes))

# how many indicators? 
inds = indicators['IndicatorName'].unique().tolist()
print("indicators:", len(inds))

# years and range of data
years = indicators['Year'].unique().tolist()
print(len(years), min(years), "to", max(years))
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
</div>



    country num: 247
    country codes: 247
    indicators: 1344
    56 1960 to 2015


This is actually a 4D dataset, with country, indicator, year and value. I would say its combination of the first three that match each value. 


```python
# pick a random indicator for a random country
hist_indicator = 'Population in the largest city'
hist_country = 'MEX'

# grab data 
data = indicators[indicators['IndicatorName'].str.contains(hist_indicator) & indicators['CountryCode'].str.contains(hist_country)]     
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>15382</th>
      <td>Mexico</td>
      <td>MEX</td>
      <td>Population in the largest city (% of urban pop...</td>
      <td>EN.URB.LCTY.UR.ZS</td>
      <td>1960</td>
      <td>28.280377</td>
    </tr>
    <tr>
      <th>40837</th>
      <td>Mexico</td>
      <td>MEX</td>
      <td>Population in the largest city (% of urban pop...</td>
      <td>EN.URB.LCTY.UR.ZS</td>
      <td>1961</td>
      <td>28.287121</td>
    </tr>
    <tr>
      <th>68643</th>
      <td>Mexico</td>
      <td>MEX</td>
      <td>Population in the largest city (% of urban pop...</td>
      <td>EN.URB.LCTY.UR.ZS</td>
      <td>1962</td>
      <td>28.305114</td>
    </tr>
    <tr>
      <th>97213</th>
      <td>Mexico</td>
      <td>MEX</td>
      <td>Population in the largest city (% of urban pop...</td>
      <td>EN.URB.LCTY.UR.ZS</td>
      <td>1963</td>
      <td>28.334391</td>
    </tr>
    <tr>
      <th>126125</th>
      <td>Mexico</td>
      <td>MEX</td>
      <td>Population in the largest city (% of urban pop...</td>
      <td>EN.URB.LCTY.UR.ZS</td>
      <td>1964</td>
      <td>28.378130</td>
    </tr>
  </tbody>
</table>
</div>



## Bar Plot


```python
fig, axis = plt.subplots()
fig.set_size_inches(10, 6)
plt.bar(data['Year'].values, data['Value'].values)
plt.show();
```


![png](5_Matplotlib_files/5_Matplotlib_9_0.png)


## Line Plot


```python
fig, axis = plt.subplots()
fig.set_size_inches(10, 6)
plt.plot(data['Year'].values, data['Value'].values)
plt.xlabel('Year')
plt.ylabel(data['IndicatorName'].iloc[0], fontsize=10)
plt.title('Largest City pop %')
plt.axis([1959, 2015,0,30])
plt.show();
```


![png](5_Matplotlib_files/5_Matplotlib_11_0.png)


## Histogram


```python
# Prep data for histogram
import re
cond_gdp_worker_ppp = indicators['IndicatorName'] == 'GDP per person employed (constant 1990 PPP $)'
cond_2014 = indicators['Year'] == 2014
data_2 = indicators[cond_gdp_worker_ppp & cond_2014]
display(data_2.head())

# add a semicolon to last plt in a cell to avoid printing extra info
fig, axis = plt.subplots()
fig.set_size_inches(10, 6)
plt.hist(data_2['Value'].values, 100, density=False, facecolor='green');
plt.xlabel(data_2['IndicatorName'].iloc[0]);
plt.ylabel('# of Countries');
plt.title('Histogram Example');
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>5534383</th>
      <td>Arab World</td>
      <td>ARB</td>
      <td>GDP per person employed (constant 1990 PPP $)</td>
      <td>SL.GDP.PCAP.EM.KD</td>
      <td>2014</td>
      <td>16767.221871</td>
    </tr>
    <tr>
      <th>5534893</th>
      <td>Central Europe and the Baltics</td>
      <td>CEB</td>
      <td>GDP per person employed (constant 1990 PPP $)</td>
      <td>SL.GDP.PCAP.EM.KD</td>
      <td>2014</td>
      <td>25167.333899</td>
    </tr>
    <tr>
      <th>5535240</th>
      <td>East Asia &amp; Pacific (all income levels)</td>
      <td>EAS</td>
      <td>GDP per person employed (constant 1990 PPP $)</td>
      <td>SL.GDP.PCAP.EM.KD</td>
      <td>2014</td>
      <td>18639.269885</td>
    </tr>
    <tr>
      <th>5535541</th>
      <td>East Asia &amp; Pacific (developing only)</td>
      <td>EAP</td>
      <td>GDP per person employed (constant 1990 PPP $)</td>
      <td>SL.GDP.PCAP.EM.KD</td>
      <td>2014</td>
      <td>15755.489075</td>
    </tr>
    <tr>
      <th>5536004</th>
      <td>Euro area</td>
      <td>EMU</td>
      <td>GDP per person employed (constant 1990 PPP $)</td>
      <td>SL.GDP.PCAP.EM.KD</td>
      <td>2014</td>
      <td>45073.794771</td>
    </tr>
  </tbody>
</table>
</div>



![png](5_Matplotlib_files/5_Matplotlib_13_1.png)


## Scatterplot

#### Data Prep for Scatterplot
Now, plot GDP per worker vs percent urbanization for all countries for all years of data 

* No need to aggregate - just use the 'World' CountryName 
* 2 Filters: 
     * GDP per worker, GDP per person employed (constant 1990 PPP $)
     * percent urbanization, Urban population (% of total)
* Only pull year and value - other columns aren't needed
* Inner join tables on Year. Merge seems to automatically drop missing years where the first dataframe had no values
* Plot urbanization on x, gdp per person on y


```python
cond_world = indicators['CountryName'] == 'World'
gdp_worker_ppp = indicators[cond_gdp_worker_ppp & cond_world][['Year', 'Value']]
cond_3 = indicators['IndicatorName'] == 'Urban population (% of total)'
urban_perc = indicators[cond_3 & cond_world][['Year', 'Value']]
data_3 = urban_perc.merge(gdp_worker_ppp, on = 'Year', how = 'inner')

display(gdp_worker_ppp.head(), urban_perc.head(), data_3.head())
len(gdp_worker_ppp), len(urban_perc), len(data_3)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012906</th>
      <td>1991</td>
      <td>12056.692883</td>
    </tr>
    <tr>
      <th>2129349</th>
      <td>1992</td>
      <td>12144.729023</td>
    </tr>
    <tr>
      <th>2251054</th>
      <td>1993</td>
      <td>12242.591709</td>
    </tr>
    <tr>
      <th>2374887</th>
      <td>1994</td>
      <td>12430.524713</td>
    </tr>
    <tr>
      <th>2501760</th>
      <td>1995</td>
      <td>12767.091788</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3491</th>
      <td>1960</td>
      <td>33.557608</td>
    </tr>
    <tr>
      <th>27221</th>
      <td>1961</td>
      <td>34.073235</td>
    </tr>
    <tr>
      <th>54067</th>
      <td>1962</td>
      <td>34.517820</td>
    </tr>
    <tr>
      <th>82472</th>
      <td>1963</td>
      <td>34.908136</td>
    </tr>
    <tr>
      <th>111146</th>
      <td>1964</td>
      <td>35.303686</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Value_x</th>
      <th>Value_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1991</td>
      <td>43.285793</td>
      <td>12056.692883</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1992</td>
      <td>43.624850</td>
      <td>12144.729023</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1993</td>
      <td>43.982123</td>
      <td>12242.591709</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1994</td>
      <td>44.334518</td>
      <td>12430.524713</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1995</td>
      <td>44.703049</td>
      <td>12767.091788</td>
    </tr>
  </tbody>
</table>
</div>





    (24, 55, 24)



#### Scatterplot generation


```python
fig, axis = plt.subplots()
# Grid lines, Xticks, Xlabel, Ylabel

axis.yaxis.grid(True)
axis.set_title('GDP per person employed vs Urban population',fontsize=16)
axis.set_xlabel('Urban population (% of total)',fontsize=10)
axis.set_ylabel('GDP per person employed (constant 1990 PPP $)',fontsize=10)
fig.set_size_inches(10, 6)

X = data_3['Value_x']
Y = data_3['Value_y']
axis.scatter(X, Y)
plt.show();
```


![png](5_Matplotlib_files/5_Matplotlib_17_0.png)


#### What is the correlation?


```python
np.corrcoef(X, Y)
```




    array([[1.        , 0.99437166],
           [0.99437166, 1.        ]])



The correlation is extremely strong. 

## Boxplot
Compare distributions of life expectancy in 1960 vs 2013


```python
cond_2013, cond_1960 = indicators['Year'] == 2013, indicators['Year'] == 1960
cond_life_exp = indicators['IndicatorName'] == 'Life expectancy at birth, total (years)'
life_exp_1960 = indicators[cond_1960 & cond_life_exp]['Value']
life_exp_2013 = indicators[cond_2013 & cond_life_exp]['Value']
life_exp_data = [life_exp_1960, life_exp_2013]

fig, axes = plt.subplots()

axis.yaxis.grid(True)
bplot = axes.boxplot(life_exp_data,
                    vert=True)     # vertical aligmnent
plt.xticks([1, 2], ['1960', '2013'])
axes.set_title('Life expectancy at birth vs Year',fontsize=16)
axes.set_xlabel('Year',fontsize=14)
axes.set_ylabel('Life expectancy at birth, total (years)',fontsize=14)
plt.show();
```


![png](5_Matplotlib_files/5_Matplotlib_21_0.png)


The distribution has tightened somewhat. 
