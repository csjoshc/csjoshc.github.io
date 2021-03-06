
<p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>

Clustering with scikit-learn

<br><br></p>

In this notebook, we will learn how to perform k-means lustering using scikit-learn in Python. 

We will use cluster analysis to generate a big picture model of the weather at a local station using a minute-graunlarity data. In this dataset, we have in the order of millions records. How do we create 12 clusters our of them?

**NOTE:** The dataset we will use is in a large CSV file called *minute_weather.csv*. Please download it into the *weather* directory in your *Week-7-MachineLearning* folder. The download link is: https://drive.google.com/open?id=0B8iiZ7pSaSFZb3ItQ1l4LWRMTjg 

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Importing the Necessary Libraries<br></p>


```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import os
%matplotlib inline
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Creating a Pandas DataFrame from a CSV file<br><br></p>



```python
print(os.listdir('../../../../../data/w7ml'))
data = pd.read_csv('../../../../../data/w7ml/minute_weather.csv')
```

    ['minute_weather.csv']


<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold">Minute Weather Data Description</p>
<br>
The **minute weather dataset** comes from the same source as the daily weather dataset that we used in the decision tree based classifier notebook. The main difference between these two datasets is that the minute weather dataset contains raw sensor measurements captured at one-minute intervals. Daily weather dataset instead contained processed and well curated data. The data is in the file **minute_weather.csv**, which is a comma-separated file.

As with the daily weather data, this data comes from a weather station located in San Diego, California. The weather station is equipped with sensors that capture weather-related measurements such as air temperature, air pressure, and relative humidity. Data was collected for a period of three years, from September 2011 to September 2014, to ensure that sufficient data for different seasons and weather conditions is captured.

Each row in **minute_weather.csv** contains weather data captured for a one-minute interval. Each row, or sample, consists of the following variables:

* **rowID:** 	unique number for each row	(*Unit: NA*)
* **hpwren_timestamp:**	timestamp of measure	(*Unit: year-month-day hour:minute:second*)
* **air_pressure:** air pressure measured at the timestamp	(*Unit: hectopascals*)
* **air_temp:**	air temperature measure at the timestamp	(*Unit: degrees Fahrenheit*)
* **avg_wind_direction:**	wind direction averaged over the minute before the timestamp	(*Unit: degrees, with 0 means coming from the North, and increasing clockwise*)
* **avg_wind_speed:**	wind speed averaged over the minute before the timestamp	(*Unit: meters per second*)
* **max_wind_direction:**	highest wind direction in the minute before the timestamp	(*Unit: degrees, with 0 being North and increasing clockwise*)
* **max_wind_speed:**	highest wind speed in the minute before the timestamp	(*Unit: meters per second*)
* **min_wind_direction:**	smallest wind direction in the minute before the timestamp	(*Unit: degrees, with 0 being North and inceasing clockwise*)
* **min_wind_speed:**	smallest wind speed in the minute before the timestamp	(*Unit: meters per second*)
* **rain_accumulation:**	amount of accumulated rain measured at the timestamp	(*Unit: millimeters*)
* **rain_duration:**	length of time rain has fallen as measured at the timestamp	(*Unit: seconds*)
* **relative_humidity:**	relative humidity measured at the timestamp	(*Unit: percent*)


```python
data.shape
```




    (1587257, 13)




```python
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
      <th>rowID</th>
      <th>hpwren_timestamp</th>
      <th>air_pressure</th>
      <th>air_temp</th>
      <th>avg_wind_direction</th>
      <th>avg_wind_speed</th>
      <th>max_wind_direction</th>
      <th>max_wind_speed</th>
      <th>min_wind_direction</th>
      <th>min_wind_speed</th>
      <th>rain_accumulation</th>
      <th>rain_duration</th>
      <th>relative_humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2011-09-10 00:00:49</td>
      <td>912.3</td>
      <td>64.76</td>
      <td>97.0</td>
      <td>1.2</td>
      <td>106.0</td>
      <td>1.6</td>
      <td>85.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>60.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2011-09-10 00:01:49</td>
      <td>912.3</td>
      <td>63.86</td>
      <td>161.0</td>
      <td>0.8</td>
      <td>215.0</td>
      <td>1.5</td>
      <td>43.0</td>
      <td>0.2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>39.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2011-09-10 00:02:49</td>
      <td>912.3</td>
      <td>64.22</td>
      <td>77.0</td>
      <td>0.7</td>
      <td>143.0</td>
      <td>1.2</td>
      <td>324.0</td>
      <td>0.3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2011-09-10 00:03:49</td>
      <td>912.3</td>
      <td>64.40</td>
      <td>89.0</td>
      <td>1.2</td>
      <td>112.0</td>
      <td>1.6</td>
      <td>12.0</td>
      <td>0.7</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>49.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2011-09-10 00:04:49</td>
      <td>912.3</td>
      <td>64.40</td>
      <td>185.0</td>
      <td>0.4</td>
      <td>260.0</td>
      <td>1.0</td>
      <td>100.0</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>58.8</td>
    </tr>
  </tbody>
</table>
</div>



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Data Sampling<br></p>

Lots of rows, so let us sample down by taking every 10th row. <br>



```python
sampled_df = data[(data['rowID'] % 10) == 0]
sampled_df.shape
```




    (158726, 13)



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Statistics
<br><br></p>



```python
sampled_df.describe().transpose()
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rowID</th>
      <td>158726.0</td>
      <td>793625.000000</td>
      <td>458203.937510</td>
      <td>0.00</td>
      <td>396812.5</td>
      <td>793625.00</td>
      <td>1190437.50</td>
      <td>1587250.00</td>
    </tr>
    <tr>
      <th>air_pressure</th>
      <td>158726.0</td>
      <td>916.830161</td>
      <td>3.051717</td>
      <td>905.00</td>
      <td>914.8</td>
      <td>916.70</td>
      <td>918.70</td>
      <td>929.50</td>
    </tr>
    <tr>
      <th>air_temp</th>
      <td>158726.0</td>
      <td>61.851589</td>
      <td>11.833569</td>
      <td>31.64</td>
      <td>52.7</td>
      <td>62.24</td>
      <td>70.88</td>
      <td>99.50</td>
    </tr>
    <tr>
      <th>avg_wind_direction</th>
      <td>158680.0</td>
      <td>162.156100</td>
      <td>95.278201</td>
      <td>0.00</td>
      <td>62.0</td>
      <td>182.00</td>
      <td>217.00</td>
      <td>359.00</td>
    </tr>
    <tr>
      <th>avg_wind_speed</th>
      <td>158680.0</td>
      <td>2.775215</td>
      <td>2.057624</td>
      <td>0.00</td>
      <td>1.3</td>
      <td>2.20</td>
      <td>3.80</td>
      <td>31.90</td>
    </tr>
    <tr>
      <th>max_wind_direction</th>
      <td>158680.0</td>
      <td>163.462144</td>
      <td>92.452139</td>
      <td>0.00</td>
      <td>68.0</td>
      <td>187.00</td>
      <td>223.00</td>
      <td>359.00</td>
    </tr>
    <tr>
      <th>max_wind_speed</th>
      <td>158680.0</td>
      <td>3.400558</td>
      <td>2.418802</td>
      <td>0.10</td>
      <td>1.6</td>
      <td>2.70</td>
      <td>4.60</td>
      <td>36.00</td>
    </tr>
    <tr>
      <th>min_wind_direction</th>
      <td>158680.0</td>
      <td>166.774017</td>
      <td>97.441109</td>
      <td>0.00</td>
      <td>76.0</td>
      <td>180.00</td>
      <td>212.00</td>
      <td>359.00</td>
    </tr>
    <tr>
      <th>min_wind_speed</th>
      <td>158680.0</td>
      <td>2.134664</td>
      <td>1.742113</td>
      <td>0.00</td>
      <td>0.8</td>
      <td>1.60</td>
      <td>3.00</td>
      <td>31.60</td>
    </tr>
    <tr>
      <th>rain_accumulation</th>
      <td>158725.0</td>
      <td>0.000318</td>
      <td>0.011236</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>3.12</td>
    </tr>
    <tr>
      <th>rain_duration</th>
      <td>158725.0</td>
      <td>0.409627</td>
      <td>8.665523</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>2960.00</td>
    </tr>
    <tr>
      <th>relative_humidity</th>
      <td>158726.0</td>
      <td>47.609470</td>
      <td>26.214409</td>
      <td>0.90</td>
      <td>24.7</td>
      <td>44.70</td>
      <td>68.00</td>
      <td>93.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
sampled_df[sampled_df['rain_accumulation'] == 0].shape
```




    (157812, 13)




```python
sampled_df[sampled_df['rain_duration'] == 0].shape
```




    (157237, 13)



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Drop all the Rows with Empty rain_duration and rain_accumulation
<br><br></p>



```python
del sampled_df['rain_accumulation']
del sampled_df['rain_duration']
```


```python
rows_before = sampled_df.shape[0]
sampled_df = sampled_df.dropna()
rows_after = sampled_df.shape[0]
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

How many rows did we drop ?
<br><br></p>



```python
rows_before - rows_after
```




    46




```python
sampled_df.columns
```




    Index(['rowID', 'hpwren_timestamp', 'air_pressure', 'air_temp',
           'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction',
           'max_wind_speed', 'min_wind_direction', 'min_wind_speed',
           'relative_humidity'],
          dtype='object')



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Select Features of Interest for Clustering
<br><br></p>



```python
features = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction', 
        'max_wind_speed','relative_humidity']
```


```python
select_df = sampled_df[features]
```


```python
select_df.columns
```




    Index(['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed',
           'max_wind_direction', 'max_wind_speed', 'relative_humidity'],
          dtype='object')




```python
select_df
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
      <th>air_pressure</th>
      <th>air_temp</th>
      <th>avg_wind_direction</th>
      <th>avg_wind_speed</th>
      <th>max_wind_direction</th>
      <th>max_wind_speed</th>
      <th>relative_humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>912.3</td>
      <td>64.76</td>
      <td>97.0</td>
      <td>1.2</td>
      <td>106.0</td>
      <td>1.6</td>
      <td>60.5</td>
    </tr>
    <tr>
      <th>10</th>
      <td>912.3</td>
      <td>62.24</td>
      <td>144.0</td>
      <td>1.2</td>
      <td>167.0</td>
      <td>1.8</td>
      <td>38.5</td>
    </tr>
    <tr>
      <th>20</th>
      <td>912.2</td>
      <td>63.32</td>
      <td>100.0</td>
      <td>2.0</td>
      <td>122.0</td>
      <td>2.5</td>
      <td>58.3</td>
    </tr>
    <tr>
      <th>30</th>
      <td>912.2</td>
      <td>62.60</td>
      <td>91.0</td>
      <td>2.0</td>
      <td>103.0</td>
      <td>2.4</td>
      <td>57.9</td>
    </tr>
    <tr>
      <th>40</th>
      <td>912.2</td>
      <td>64.04</td>
      <td>81.0</td>
      <td>2.6</td>
      <td>88.0</td>
      <td>2.9</td>
      <td>57.4</td>
    </tr>
    <tr>
      <th>50</th>
      <td>912.1</td>
      <td>63.68</td>
      <td>102.0</td>
      <td>1.2</td>
      <td>119.0</td>
      <td>1.5</td>
      <td>51.4</td>
    </tr>
    <tr>
      <th>60</th>
      <td>912.0</td>
      <td>64.04</td>
      <td>83.0</td>
      <td>0.7</td>
      <td>101.0</td>
      <td>0.9</td>
      <td>51.4</td>
    </tr>
    <tr>
      <th>70</th>
      <td>911.9</td>
      <td>64.22</td>
      <td>82.0</td>
      <td>2.0</td>
      <td>97.0</td>
      <td>2.4</td>
      <td>62.2</td>
    </tr>
    <tr>
      <th>80</th>
      <td>911.9</td>
      <td>61.70</td>
      <td>67.0</td>
      <td>3.3</td>
      <td>70.0</td>
      <td>3.5</td>
      <td>71.5</td>
    </tr>
    <tr>
      <th>90</th>
      <td>911.9</td>
      <td>61.34</td>
      <td>67.0</td>
      <td>3.6</td>
      <td>75.0</td>
      <td>4.2</td>
      <td>72.5</td>
    </tr>
    <tr>
      <th>100</th>
      <td>911.8</td>
      <td>62.96</td>
      <td>95.0</td>
      <td>2.3</td>
      <td>106.0</td>
      <td>2.5</td>
      <td>63.9</td>
    </tr>
    <tr>
      <th>110</th>
      <td>911.8</td>
      <td>64.22</td>
      <td>83.0</td>
      <td>2.1</td>
      <td>88.0</td>
      <td>2.5</td>
      <td>59.1</td>
    </tr>
    <tr>
      <th>120</th>
      <td>911.8</td>
      <td>63.86</td>
      <td>68.0</td>
      <td>2.1</td>
      <td>76.0</td>
      <td>2.4</td>
      <td>63.5</td>
    </tr>
    <tr>
      <th>130</th>
      <td>911.6</td>
      <td>64.40</td>
      <td>156.0</td>
      <td>0.5</td>
      <td>203.0</td>
      <td>0.7</td>
      <td>50.4</td>
    </tr>
    <tr>
      <th>140</th>
      <td>911.5</td>
      <td>65.30</td>
      <td>85.0</td>
      <td>2.2</td>
      <td>92.0</td>
      <td>2.5</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>150</th>
      <td>911.4</td>
      <td>64.58</td>
      <td>154.0</td>
      <td>1.3</td>
      <td>176.0</td>
      <td>2.1</td>
      <td>50.2</td>
    </tr>
    <tr>
      <th>160</th>
      <td>911.4</td>
      <td>65.48</td>
      <td>154.0</td>
      <td>0.9</td>
      <td>208.0</td>
      <td>1.9</td>
      <td>46.2</td>
    </tr>
    <tr>
      <th>170</th>
      <td>911.5</td>
      <td>65.66</td>
      <td>95.0</td>
      <td>1.1</td>
      <td>109.0</td>
      <td>1.6</td>
      <td>45.2</td>
    </tr>
    <tr>
      <th>180</th>
      <td>911.4</td>
      <td>65.66</td>
      <td>155.0</td>
      <td>1.1</td>
      <td>167.0</td>
      <td>1.6</td>
      <td>42.8</td>
    </tr>
    <tr>
      <th>190</th>
      <td>911.4</td>
      <td>67.10</td>
      <td>157.0</td>
      <td>1.2</td>
      <td>172.0</td>
      <td>1.6</td>
      <td>36.8</td>
    </tr>
    <tr>
      <th>200</th>
      <td>911.4</td>
      <td>68.00</td>
      <td>53.0</td>
      <td>0.3</td>
      <td>69.0</td>
      <td>0.5</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>210</th>
      <td>911.3</td>
      <td>67.64</td>
      <td>167.0</td>
      <td>1.5</td>
      <td>196.0</td>
      <td>2.2</td>
      <td>34.4</td>
    </tr>
    <tr>
      <th>220</th>
      <td>911.4</td>
      <td>67.82</td>
      <td>4.0</td>
      <td>0.6</td>
      <td>25.0</td>
      <td>0.7</td>
      <td>34.2</td>
    </tr>
    <tr>
      <th>230</th>
      <td>911.4</td>
      <td>66.74</td>
      <td>172.0</td>
      <td>1.3</td>
      <td>192.0</td>
      <td>1.9</td>
      <td>37.8</td>
    </tr>
    <tr>
      <th>240</th>
      <td>911.4</td>
      <td>66.56</td>
      <td>39.0</td>
      <td>0.2</td>
      <td>145.0</td>
      <td>0.3</td>
      <td>41.6</td>
    </tr>
    <tr>
      <th>250</th>
      <td>911.4</td>
      <td>65.66</td>
      <td>56.0</td>
      <td>1.9</td>
      <td>67.0</td>
      <td>2.2</td>
      <td>51.8</td>
    </tr>
    <tr>
      <th>260</th>
      <td>911.5</td>
      <td>65.66</td>
      <td>74.0</td>
      <td>0.8</td>
      <td>101.0</td>
      <td>1.2</td>
      <td>41.1</td>
    </tr>
    <tr>
      <th>270</th>
      <td>911.4</td>
      <td>66.92</td>
      <td>147.0</td>
      <td>0.9</td>
      <td>174.0</td>
      <td>1.1</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>280</th>
      <td>911.3</td>
      <td>64.76</td>
      <td>73.0</td>
      <td>1.0</td>
      <td>82.0</td>
      <td>1.2</td>
      <td>43.3</td>
    </tr>
    <tr>
      <th>290</th>
      <td>911.3</td>
      <td>64.94</td>
      <td>164.0</td>
      <td>1.3</td>
      <td>176.0</td>
      <td>1.7</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1586960</th>
      <td>914.7</td>
      <td>76.46</td>
      <td>247.0</td>
      <td>0.6</td>
      <td>264.0</td>
      <td>0.7</td>
      <td>43.4</td>
    </tr>
    <tr>
      <th>1586970</th>
      <td>914.8</td>
      <td>76.28</td>
      <td>208.0</td>
      <td>0.7</td>
      <td>216.0</td>
      <td>0.9</td>
      <td>43.7</td>
    </tr>
    <tr>
      <th>1586980</th>
      <td>914.8</td>
      <td>76.10</td>
      <td>209.0</td>
      <td>0.7</td>
      <td>216.0</td>
      <td>0.9</td>
      <td>43.9</td>
    </tr>
    <tr>
      <th>1586990</th>
      <td>914.9</td>
      <td>76.28</td>
      <td>339.0</td>
      <td>0.5</td>
      <td>350.0</td>
      <td>0.7</td>
      <td>43.4</td>
    </tr>
    <tr>
      <th>1587000</th>
      <td>914.9</td>
      <td>75.92</td>
      <td>344.0</td>
      <td>0.4</td>
      <td>352.0</td>
      <td>0.6</td>
      <td>43.9</td>
    </tr>
    <tr>
      <th>1587010</th>
      <td>915.0</td>
      <td>75.56</td>
      <td>323.0</td>
      <td>0.3</td>
      <td>348.0</td>
      <td>0.5</td>
      <td>45.5</td>
    </tr>
    <tr>
      <th>1587020</th>
      <td>915.1</td>
      <td>75.56</td>
      <td>324.0</td>
      <td>1.1</td>
      <td>347.0</td>
      <td>1.5</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>1587030</th>
      <td>915.1</td>
      <td>75.74</td>
      <td>1.0</td>
      <td>1.3</td>
      <td>13.0</td>
      <td>1.7</td>
      <td>45.8</td>
    </tr>
    <tr>
      <th>1587040</th>
      <td>915.2</td>
      <td>75.38</td>
      <td>355.0</td>
      <td>0.9</td>
      <td>1.0</td>
      <td>1.1</td>
      <td>46.1</td>
    </tr>
    <tr>
      <th>1587050</th>
      <td>915.3</td>
      <td>75.38</td>
      <td>359.0</td>
      <td>1.4</td>
      <td>11.0</td>
      <td>1.5</td>
      <td>45.8</td>
    </tr>
    <tr>
      <th>1587060</th>
      <td>915.4</td>
      <td>75.38</td>
      <td>11.0</td>
      <td>1.1</td>
      <td>21.0</td>
      <td>1.3</td>
      <td>45.7</td>
    </tr>
    <tr>
      <th>1587070</th>
      <td>915.5</td>
      <td>75.38</td>
      <td>13.0</td>
      <td>1.4</td>
      <td>24.0</td>
      <td>1.6</td>
      <td>46.6</td>
    </tr>
    <tr>
      <th>1587080</th>
      <td>915.6</td>
      <td>75.20</td>
      <td>18.0</td>
      <td>1.0</td>
      <td>24.0</td>
      <td>1.2</td>
      <td>46.5</td>
    </tr>
    <tr>
      <th>1587090</th>
      <td>915.6</td>
      <td>75.20</td>
      <td>356.0</td>
      <td>1.7</td>
      <td>1.0</td>
      <td>1.9</td>
      <td>47.2</td>
    </tr>
    <tr>
      <th>1587100</th>
      <td>915.7</td>
      <td>75.38</td>
      <td>13.0</td>
      <td>1.5</td>
      <td>24.0</td>
      <td>1.7</td>
      <td>46.7</td>
    </tr>
    <tr>
      <th>1587110</th>
      <td>915.7</td>
      <td>75.02</td>
      <td>19.0</td>
      <td>1.2</td>
      <td>28.0</td>
      <td>1.4</td>
      <td>46.7</td>
    </tr>
    <tr>
      <th>1587120</th>
      <td>915.7</td>
      <td>74.84</td>
      <td>25.0</td>
      <td>1.4</td>
      <td>35.0</td>
      <td>1.6</td>
      <td>46.5</td>
    </tr>
    <tr>
      <th>1587130</th>
      <td>915.8</td>
      <td>74.84</td>
      <td>23.0</td>
      <td>1.3</td>
      <td>30.0</td>
      <td>1.5</td>
      <td>46.9</td>
    </tr>
    <tr>
      <th>1587140</th>
      <td>915.8</td>
      <td>74.84</td>
      <td>32.0</td>
      <td>1.4</td>
      <td>41.0</td>
      <td>1.7</td>
      <td>45.5</td>
    </tr>
    <tr>
      <th>1587150</th>
      <td>915.8</td>
      <td>75.20</td>
      <td>23.0</td>
      <td>1.1</td>
      <td>31.0</td>
      <td>1.4</td>
      <td>45.7</td>
    </tr>
    <tr>
      <th>1587160</th>
      <td>915.8</td>
      <td>75.38</td>
      <td>16.0</td>
      <td>1.2</td>
      <td>28.0</td>
      <td>1.5</td>
      <td>46.3</td>
    </tr>
    <tr>
      <th>1587170</th>
      <td>915.7</td>
      <td>75.38</td>
      <td>347.0</td>
      <td>1.2</td>
      <td>353.0</td>
      <td>1.4</td>
      <td>48.1</td>
    </tr>
    <tr>
      <th>1587180</th>
      <td>915.8</td>
      <td>75.74</td>
      <td>326.0</td>
      <td>1.2</td>
      <td>337.0</td>
      <td>1.6</td>
      <td>48.3</td>
    </tr>
    <tr>
      <th>1587190</th>
      <td>915.9</td>
      <td>75.92</td>
      <td>289.0</td>
      <td>0.7</td>
      <td>309.0</td>
      <td>0.9</td>
      <td>48.1</td>
    </tr>
    <tr>
      <th>1587200</th>
      <td>915.9</td>
      <td>75.74</td>
      <td>335.0</td>
      <td>0.9</td>
      <td>348.0</td>
      <td>1.1</td>
      <td>47.8</td>
    </tr>
    <tr>
      <th>1587210</th>
      <td>915.9</td>
      <td>75.56</td>
      <td>330.0</td>
      <td>1.0</td>
      <td>341.0</td>
      <td>1.3</td>
      <td>47.8</td>
    </tr>
    <tr>
      <th>1587220</th>
      <td>915.9</td>
      <td>75.56</td>
      <td>330.0</td>
      <td>1.1</td>
      <td>341.0</td>
      <td>1.4</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>1587230</th>
      <td>915.9</td>
      <td>75.56</td>
      <td>344.0</td>
      <td>1.4</td>
      <td>352.0</td>
      <td>1.7</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>1587240</th>
      <td>915.9</td>
      <td>75.20</td>
      <td>359.0</td>
      <td>1.3</td>
      <td>9.0</td>
      <td>1.6</td>
      <td>46.3</td>
    </tr>
    <tr>
      <th>1587250</th>
      <td>915.9</td>
      <td>74.84</td>
      <td>6.0</td>
      <td>1.5</td>
      <td>20.0</td>
      <td>1.9</td>
      <td>46.1</td>
    </tr>
  </tbody>
</table>
<p>158680 rows × 7 columns</p>
</div>



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Scale the Features using StandardScaler
<br><br></p>



```python
X = StandardScaler().fit_transform(select_df)
X
```




    14.154615859301948



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Use k-Means Clustering
<br><br></p>



```python
kmeans = KMeans(n_clusters=12)
model = kmeans.fit(X)
print("model\n", model)
```

    model
     KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
        n_clusters=12, n_init=10, n_jobs=None, precompute_distances='auto',
        random_state=None, tol=0.0001, verbose=0)


<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

What are the centers of 12 clusters we formed ?
<br><br></p>



```python
centers = model.cluster_centers_
centers
```




    array([[-0.69617887,  0.54330632,  0.17691394, -0.58403412,  0.34627312,
            -0.59739003, -0.11397498],
           [ 0.25351851, -0.99440789,  0.66010373, -0.54766866,  0.85136707,
            -0.53024374,  1.15770715],
           [ 0.72995971,  0.43639747,  0.28548467, -0.53484748,  0.47328985,
            -0.54109706, -0.77185388],
           [-0.2112256 ,  0.63143998,  0.40854271,  0.73491299,  0.51667841,
             0.67289003, -0.15002398],
           [ 1.18998385, -0.25541715, -1.15503601,  2.12557789, -1.05344849,
             2.24273108, -1.13420131],
           [ 1.36864611, -0.08213106, -1.2068389 , -0.04709512, -1.07582646,
            -0.02667577, -0.97766761],
           [-1.17907135, -0.87684488,  0.44663448,  1.97558807,  0.53860587,
             1.93685078,  0.91508678],
           [-0.84007473, -1.1983503 ,  0.37524244,  0.35343529,  0.47369357,
             0.34132145,  1.36278947],
           [ 0.06044811, -0.78794919, -1.19709094, -0.57079157, -1.04316035,
            -0.58531415,  0.87761989],
           [ 0.13082952,  0.84369388,  1.41103689, -0.63843851,  1.67507664,
            -0.58918289, -0.71428014],
           [ 0.23378992,  0.3194701 ,  1.88794624, -0.65194259, -1.55164204,
            -0.57678283, -0.28275652],
           [-0.16198023,  0.86303025, -1.31114806, -0.58983767, -1.1668154 ,
            -0.6051521 , -0.64229717]])



<p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>

Plots
<br><br></p>


Let us first create some utility functions which will help us in plotting graphs:


```python
# Function that creates a DataFrame with a column for Cluster Number

def pd_centers(featuresUsed, centers):
	colNames = list(featuresUsed)
	colNames.append('prediction')

	# Zip with a column called 'prediction' (index)
	Z = [np.append(A, index) for index, A in enumerate(centers)]

	# Convert to pandas data frame for plotting
	P = pd.DataFrame(Z, columns=colNames)
	P['prediction'] = P['prediction'].astype(int)
	return P
```


```python
# Function that creates Parallel Plots

def parallel_plot(data):
	my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(data)))
	plt.figure(figsize=(15,8)).gca().axes.set_ylim([-3,+3])
	parallel_coordinates(data, 'prediction', color = my_colors, marker='o')
```


```python
P = pd_centers(features, centers)
P
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
      <th>air_pressure</th>
      <th>air_temp</th>
      <th>avg_wind_direction</th>
      <th>avg_wind_speed</th>
      <th>max_wind_direction</th>
      <th>max_wind_speed</th>
      <th>relative_humidity</th>
      <th>prediction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.696179</td>
      <td>0.543306</td>
      <td>0.176914</td>
      <td>-0.584034</td>
      <td>0.346273</td>
      <td>-0.597390</td>
      <td>-0.113975</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.253519</td>
      <td>-0.994408</td>
      <td>0.660104</td>
      <td>-0.547669</td>
      <td>0.851367</td>
      <td>-0.530244</td>
      <td>1.157707</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.729960</td>
      <td>0.436397</td>
      <td>0.285485</td>
      <td>-0.534847</td>
      <td>0.473290</td>
      <td>-0.541097</td>
      <td>-0.771854</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.211226</td>
      <td>0.631440</td>
      <td>0.408543</td>
      <td>0.734913</td>
      <td>0.516678</td>
      <td>0.672890</td>
      <td>-0.150024</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.189984</td>
      <td>-0.255417</td>
      <td>-1.155036</td>
      <td>2.125578</td>
      <td>-1.053448</td>
      <td>2.242731</td>
      <td>-1.134201</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.368646</td>
      <td>-0.082131</td>
      <td>-1.206839</td>
      <td>-0.047095</td>
      <td>-1.075826</td>
      <td>-0.026676</td>
      <td>-0.977668</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-1.179071</td>
      <td>-0.876845</td>
      <td>0.446634</td>
      <td>1.975588</td>
      <td>0.538606</td>
      <td>1.936851</td>
      <td>0.915087</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.840075</td>
      <td>-1.198350</td>
      <td>0.375242</td>
      <td>0.353435</td>
      <td>0.473694</td>
      <td>0.341321</td>
      <td>1.362789</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.060448</td>
      <td>-0.787949</td>
      <td>-1.197091</td>
      <td>-0.570792</td>
      <td>-1.043160</td>
      <td>-0.585314</td>
      <td>0.877620</td>
      <td>8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.130830</td>
      <td>0.843694</td>
      <td>1.411037</td>
      <td>-0.638439</td>
      <td>1.675077</td>
      <td>-0.589183</td>
      <td>-0.714280</td>
      <td>9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.233790</td>
      <td>0.319470</td>
      <td>1.887946</td>
      <td>-0.651943</td>
      <td>-1.551642</td>
      <td>-0.576783</td>
      <td>-0.282757</td>
      <td>10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>-0.161980</td>
      <td>0.863030</td>
      <td>-1.311148</td>
      <td>-0.589838</td>
      <td>-1.166815</td>
      <td>-0.605152</td>
      <td>-0.642297</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



# Dry Days


```python
parallel_plot(P[P['relative_humidity'] < -0.5])
```


![png](Weather%20Data%20Clustering%20using%20k-Means_files/Weather%20Data%20Clustering%20using%20k-Means_38_0.png)


# Warm Days


```python
parallel_plot(P[P['air_temp'] > 0.5])
```


![png](Weather%20Data%20Clustering%20using%20k-Means_files/Weather%20Data%20Clustering%20using%20k-Means_40_0.png)


# Cool Days


```python
parallel_plot(P[(P['relative_humidity'] > 0.5) & (P['air_temp'] < 0.5)])
```


![png](Weather%20Data%20Clustering%20using%20k-Means_files/Weather%20Data%20Clustering%20using%20k-Means_42_0.png)

