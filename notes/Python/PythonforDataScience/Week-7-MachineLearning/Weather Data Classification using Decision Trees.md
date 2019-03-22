
<p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold">

Classification of Weather Data <br><br>
using scikit-learn
<br><br>
</p>

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>
Daily Weather Data Analysis</p>

In this notebook, we will use scikit-learn to perform a decision tree based classification of weather data.

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Importing the Necessary Libraries<br></p>


```python
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Creating a Pandas DataFrame from a CSV file<br></p>



```python
data = pd.read_csv('./weather/daily_weather.csv')
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold">Daily Weather Data Description</p>
<br>
The file **daily_weather.csv** is a comma-separated file that contains weather data.  This data comes from a weather station located in San Diego, California.  The weather station is equipped with sensors that capture weather-related measurements such as air temperature, air pressure, and relative humidity.  Data was collected for a period of three years, from September 2011 to September 2014, to ensure that sufficient data for different seasons and weather conditions is captured.<br><br>
Let's now check all the columns in the data.


```python
data.columns
```




    Index(['number', 'air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
           'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
           'rain_accumulation_9am', 'rain_duration_9am', 'relative_humidity_9am',
           'relative_humidity_3pm'],
          dtype='object')



<br>Each row in daily_weather.csv captures weather data for a separate day.  <br><br>
Sensor measurements from the weather station were captured at one-minute intervals.  These measurements were then processed to generate values to describe daily weather. Since this dataset was created to classify low-humidity days vs. non-low-humidity days (that is, days with normal or high humidity), the variables included are weather measurements in the morning, with one measurement, namely relatively humidity, in the afternoon.  The idea is to use the morning weather values to predict whether the day will be low-humidity or not based on the afternoon measurement of relative humidity.

Each row, or sample, consists of the following variables:

* **number:** unique number for each row
* **air_pressure_9am:** air pressure averaged over a period from 8:55am to 9:04am (*Unit: hectopascals*)
* **air_temp_9am:** air temperature averaged over a period from 8:55am to 9:04am (*Unit: degrees Fahrenheit*)
* **air_wind_direction_9am:** wind direction averaged over a period from 8:55am to 9:04am (*Unit: degrees, with 0 means coming from the North, and increasing clockwise*)
* **air_wind_speed_9am:** wind speed averaged over a period from 8:55am to 9:04am (*Unit: miles per hour*)
* ** max_wind_direction_9am:** wind gust direction averaged over a period from 8:55am to 9:10am (*Unit: degrees, with 0 being North and increasing clockwise*)
* **max_wind_speed_9am:** wind gust speed averaged over a period from 8:55am to 9:04am (*Unit: miles per hour*)
* **rain_accumulation_9am:** amount of rain accumulated in the 24 hours prior to 9am (*Unit: millimeters*)
* **rain_duration_9am:** amount of time rain was recorded in the 24 hours prior to 9am (*Unit: seconds*)
* **relative_humidity_9am:** relative humidity averaged over a period from 8:55am to 9:04am (*Unit: percent*)
* **relative_humidity_3pm:** relative humidity averaged over a period from 2:55pm to 3:04pm (*Unit: percent *)



```python
data
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
      <th>number</th>
      <th>air_pressure_9am</th>
      <th>air_temp_9am</th>
      <th>avg_wind_direction_9am</th>
      <th>avg_wind_speed_9am</th>
      <th>max_wind_direction_9am</th>
      <th>max_wind_speed_9am</th>
      <th>rain_accumulation_9am</th>
      <th>rain_duration_9am</th>
      <th>relative_humidity_9am</th>
      <th>relative_humidity_3pm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>918.060000</td>
      <td>74.822000</td>
      <td>271.100000</td>
      <td>2.080354</td>
      <td>295.400000</td>
      <td>2.863283</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>42.420000</td>
      <td>36.160000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>917.347688</td>
      <td>71.403843</td>
      <td>101.935179</td>
      <td>2.443009</td>
      <td>140.471548</td>
      <td>3.533324</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>24.328697</td>
      <td>19.426597</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>923.040000</td>
      <td>60.638000</td>
      <td>51.000000</td>
      <td>17.067852</td>
      <td>63.700000</td>
      <td>22.100967</td>
      <td>0.00</td>
      <td>20.0</td>
      <td>8.900000</td>
      <td>14.460000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>920.502751</td>
      <td>70.138895</td>
      <td>198.832133</td>
      <td>4.337363</td>
      <td>211.203341</td>
      <td>5.190045</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>12.189102</td>
      <td>12.742547</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>921.160000</td>
      <td>44.294000</td>
      <td>277.800000</td>
      <td>1.856660</td>
      <td>136.500000</td>
      <td>2.863283</td>
      <td>8.90</td>
      <td>14730.0</td>
      <td>92.410000</td>
      <td>76.740000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>915.300000</td>
      <td>78.404000</td>
      <td>182.800000</td>
      <td>9.932014</td>
      <td>189.000000</td>
      <td>10.983375</td>
      <td>0.02</td>
      <td>170.0</td>
      <td>35.130000</td>
      <td>33.930000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>915.598868</td>
      <td>70.043304</td>
      <td>177.875407</td>
      <td>3.745587</td>
      <td>186.606696</td>
      <td>4.589632</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>10.657422</td>
      <td>21.385657</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>918.070000</td>
      <td>51.710000</td>
      <td>242.400000</td>
      <td>2.527742</td>
      <td>271.600000</td>
      <td>3.646212</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>80.470000</td>
      <td>74.920000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>920.080000</td>
      <td>80.582000</td>
      <td>40.700000</td>
      <td>4.518619</td>
      <td>63.000000</td>
      <td>5.883152</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>29.580000</td>
      <td>24.030000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>915.010000</td>
      <td>47.498000</td>
      <td>163.100000</td>
      <td>4.943637</td>
      <td>195.900000</td>
      <td>6.576604</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>88.600000</td>
      <td>68.050000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>919.650000</td>
      <td>77.036000</td>
      <td>70.600000</td>
      <td>3.825167</td>
      <td>85.500000</td>
      <td>4.764682</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>22.070000</td>
      <td>32.130000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>915.640000</td>
      <td>45.716000</td>
      <td>241.600000</td>
      <td>5.860783</td>
      <td>265.800000</td>
      <td>8.030615</td>
      <td>0.55</td>
      <td>1770.0</td>
      <td>90.560000</td>
      <td>79.090000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>917.390000</td>
      <td>49.784000</td>
      <td>204.100000</td>
      <td>1.275056</td>
      <td>211.800000</td>
      <td>2.013246</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>73.150000</td>
      <td>58.430000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>920.820000</td>
      <td>62.438000</td>
      <td>213.600000</td>
      <td>2.617220</td>
      <td>165.700000</td>
      <td>3.310671</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>43.640000</td>
      <td>27.990000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>911.000000</td>
      <td>86.432000</td>
      <td>202.900000</td>
      <td>1.207948</td>
      <td>162.900000</td>
      <td>1.677705</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>15.190000</td>
      <td>24.370000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>922.383131</td>
      <td>70.865263</td>
      <td>36.174175</td>
      <td>1.847278</td>
      <td>58.428632</td>
      <td>2.529142</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>12.110889</td>
      <td>14.801706</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>917.890000</td>
      <td>NaN</td>
      <td>169.200000</td>
      <td>2.192201</td>
      <td>196.800000</td>
      <td>2.930391</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>48.990000</td>
      <td>51.190000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>916.915255</td>
      <td>77.018961</td>
      <td>234.539345</td>
      <td>2.274725</td>
      <td>229.474199</td>
      <td>2.906513</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>21.031462</td>
      <td>20.755683</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>918.800000</td>
      <td>67.082000</td>
      <td>176.100000</td>
      <td>4.876529</td>
      <td>183.400000</td>
      <td>5.569981</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>18.900000</td>
      <td>45.870000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>922.040000</td>
      <td>68.576000</td>
      <td>58.300000</td>
      <td>9.551734</td>
      <td>81.900000</td>
      <td>12.571603</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>7.540000</td>
      <td>7.740000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>20</td>
      <td>919.992262</td>
      <td>62.964383</td>
      <td>54.799094</td>
      <td>12.680436</td>
      <td>74.254223</td>
      <td>15.452306</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>18.809518</td>
      <td>14.649909</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>917.230000</td>
      <td>67.676000</td>
      <td>177.800000</td>
      <td>2.460634</td>
      <td>93.200000</td>
      <td>3.288302</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>40.640000</td>
      <td>41.340000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>22</td>
      <td>921.125626</td>
      <td>68.818772</td>
      <td>71.799092</td>
      <td>2.576538</td>
      <td>95.472334</td>
      <td>3.487444</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>11.742201</td>
      <td>17.281161</td>
    </tr>
    <tr>
      <th>23</th>
      <td>23</td>
      <td>920.350000</td>
      <td>47.570000</td>
      <td>192.100000</td>
      <td>6.263432</td>
      <td>205.700000</td>
      <td>7.605596</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>54.550000</td>
      <td>66.000000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>24</td>
      <td>921.788229</td>
      <td>71.659572</td>
      <td>217.405520</td>
      <td>1.946447</td>
      <td>253.758003</td>
      <td>2.719712</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>11.194250</td>
      <td>16.331716</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25</td>
      <td>918.030000</td>
      <td>50.666000</td>
      <td>128.900000</td>
      <td>2.527742</td>
      <td>117.400000</td>
      <td>4.004123</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>76.880000</td>
      <td>47.030000</td>
    </tr>
    <tr>
      <th>26</th>
      <td>26</td>
      <td>914.490000</td>
      <td>49.892000</td>
      <td>163.000000</td>
      <td>4.854160</td>
      <td>189.600000</td>
      <td>6.733189</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>92.100000</td>
      <td>90.990000</td>
    </tr>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>914.900000</td>
      <td>78.620000</td>
      <td>203.300000</td>
      <td>1.811921</td>
      <td>240.000000</td>
      <td>2.751436</td>
      <td>0.00</td>
      <td>220.0</td>
      <td>47.890000</td>
      <td>43.900000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>28</td>
      <td>915.840000</td>
      <td>40.118000</td>
      <td>171.900000</td>
      <td>10.535987</td>
      <td>188.000000</td>
      <td>12.929513</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>86.430000</td>
      <td>84.390000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>29</td>
      <td>916.310000</td>
      <td>45.428000</td>
      <td>183.100000</td>
      <td>8.343786</td>
      <td>194.600000</td>
      <td>10.088599</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>86.150000</td>
      <td>90.580000</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1065</th>
      <td>1065</td>
      <td>915.600000</td>
      <td>69.584000</td>
      <td>185.500000</td>
      <td>4.630466</td>
      <td>198.200000</td>
      <td>5.480503</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>28.970000</td>
      <td>39.370000</td>
    </tr>
    <tr>
      <th>1066</th>
      <td>1066</td>
      <td>919.564869</td>
      <td>73.726732</td>
      <td>68.704694</td>
      <td>3.551777</td>
      <td>102.571616</td>
      <td>4.861315</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>11.657314</td>
      <td>17.331823</td>
    </tr>
    <tr>
      <th>1067</th>
      <td>1067</td>
      <td>917.690000</td>
      <td>64.994000</td>
      <td>178.300000</td>
      <td>2.975130</td>
      <td>193.900000</td>
      <td>3.735690</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>54.880000</td>
      <td>52.070000</td>
    </tr>
    <tr>
      <th>1068</th>
      <td>1068</td>
      <td>920.330000</td>
      <td>68.864000</td>
      <td>122.400000</td>
      <td>2.035615</td>
      <td>182.000000</td>
      <td>3.086977</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>52.380000</td>
      <td>62.620000</td>
    </tr>
    <tr>
      <th>1069</th>
      <td>1069</td>
      <td>918.260000</td>
      <td>82.220000</td>
      <td>186.600000</td>
      <td>1.096101</td>
      <td>221.500000</td>
      <td>1.722444</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>32.460000</td>
      <td>56.930000</td>
    </tr>
    <tr>
      <th>1070</th>
      <td>1070</td>
      <td>911.600000</td>
      <td>46.346000</td>
      <td>110.200000</td>
      <td>2.304048</td>
      <td>96.100000</td>
      <td>3.154085</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>90.510000</td>
      <td>62.490000</td>
    </tr>
    <tr>
      <th>1071</th>
      <td>1071</td>
      <td>919.200000</td>
      <td>70.250000</td>
      <td>156.700000</td>
      <td>2.013246</td>
      <td>172.300000</td>
      <td>2.617220</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>42.060000</td>
      <td>41.850000</td>
    </tr>
    <tr>
      <th>1072</th>
      <td>1072</td>
      <td>923.100000</td>
      <td>75.596000</td>
      <td>178.300000</td>
      <td>1.409272</td>
      <td>205.200000</td>
      <td>1.856660</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>11.880000</td>
      <td>19.810000</td>
    </tr>
    <tr>
      <th>1073</th>
      <td>1073</td>
      <td>917.920000</td>
      <td>84.650000</td>
      <td>30.000000</td>
      <td>4.831790</td>
      <td>40.100000</td>
      <td>5.838413</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>16.220000</td>
      <td>27.450000</td>
    </tr>
    <tr>
      <th>1074</th>
      <td>1074</td>
      <td>913.870000</td>
      <td>66.938000</td>
      <td>171.900000</td>
      <td>6.509495</td>
      <td>182.300000</td>
      <td>7.471380</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>57.430000</td>
      <td>53.380000</td>
    </tr>
    <tr>
      <th>1075</th>
      <td>1075</td>
      <td>922.858110</td>
      <td>64.989361</td>
      <td>63.483047</td>
      <td>10.261187</td>
      <td>73.170504</td>
      <td>11.949206</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>14.525109</td>
      <td>15.511157</td>
    </tr>
    <tr>
      <th>1076</th>
      <td>1076</td>
      <td>925.550000</td>
      <td>50.918000</td>
      <td>32.600000</td>
      <td>5.413395</td>
      <td>57.500000</td>
      <td>8.120092</td>
      <td>0.00</td>
      <td>10.0</td>
      <td>29.090000</td>
      <td>23.720000</td>
    </tr>
    <tr>
      <th>1077</th>
      <td>1077</td>
      <td>920.130000</td>
      <td>73.292000</td>
      <td>193.600000</td>
      <td>4.115970</td>
      <td>211.300000</td>
      <td>4.966007</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>33.520000</td>
      <td>38.120000</td>
    </tr>
    <tr>
      <th>1078</th>
      <td>1078</td>
      <td>924.017856</td>
      <td>68.370307</td>
      <td>56.304083</td>
      <td>15.162800</td>
      <td>76.585117</td>
      <td>19.803578</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>11.599240</td>
      <td>9.373013</td>
    </tr>
    <tr>
      <th>1079</th>
      <td>1079</td>
      <td>917.200000</td>
      <td>65.264000</td>
      <td>137.600000</td>
      <td>1.767183</td>
      <td>176.700000</td>
      <td>2.550112</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>58.370000</td>
      <td>65.590000</td>
    </tr>
    <tr>
      <th>1080</th>
      <td>1080</td>
      <td>916.260000</td>
      <td>79.772000</td>
      <td>185.700000</td>
      <td>3.511996</td>
      <td>201.500000</td>
      <td>4.160708</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>27.680000</td>
      <td>20.400000</td>
    </tr>
    <tr>
      <th>1081</th>
      <td>1081</td>
      <td>920.856913</td>
      <td>69.884338</td>
      <td>47.335966</td>
      <td>12.238670</td>
      <td>66.729162</td>
      <td>16.067860</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>11.956852</td>
      <td>12.696233</td>
    </tr>
    <tr>
      <th>1082</th>
      <td>1082</td>
      <td>916.130000</td>
      <td>50.108000</td>
      <td>211.400000</td>
      <td>2.550112</td>
      <td>231.800000</td>
      <td>3.534365</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>89.800000</td>
      <td>53.860000</td>
    </tr>
    <tr>
      <th>1083</th>
      <td>1083</td>
      <td>916.320000</td>
      <td>48.308000</td>
      <td>46.900000</td>
      <td>4.854160</td>
      <td>61.700000</td>
      <td>5.860783</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>91.030000</td>
      <td>62.400000</td>
    </tr>
    <tr>
      <th>1084</th>
      <td>1084</td>
      <td>917.130000</td>
      <td>80.240000</td>
      <td>183.300000</td>
      <td>1.632966</td>
      <td>38.500000</td>
      <td>2.259309</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>28.260000</td>
      <td>34.690000</td>
    </tr>
    <tr>
      <th>1085</th>
      <td>1085</td>
      <td>914.840000</td>
      <td>47.354000</td>
      <td>190.900000</td>
      <td>3.713320</td>
      <td>204.400000</td>
      <td>4.652835</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>92.300000</td>
      <td>88.160000</td>
    </tr>
    <tr>
      <th>1086</th>
      <td>1086</td>
      <td>921.260000</td>
      <td>52.646000</td>
      <td>261.900000</td>
      <td>2.035615</td>
      <td>260.500000</td>
      <td>3.042238</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>91.110000</td>
      <td>81.890000</td>
    </tr>
    <tr>
      <th>1087</th>
      <td>1087</td>
      <td>914.000000</td>
      <td>66.650000</td>
      <td>173.800000</td>
      <td>8.366156</td>
      <td>181.000000</td>
      <td>9.439887</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>30.920000</td>
      <td>47.340000</td>
    </tr>
    <tr>
      <th>1088</th>
      <td>1088</td>
      <td>912.900000</td>
      <td>71.870000</td>
      <td>129.200000</td>
      <td>1.431642</td>
      <td>160.000000</td>
      <td>2.057985</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>51.840000</td>
      <td>55.490000</td>
    </tr>
    <tr>
      <th>1089</th>
      <td>1089</td>
      <td>915.000000</td>
      <td>55.040000</td>
      <td>191.800000</td>
      <td>5.368656</td>
      <td>220.900000</td>
      <td>7.068730</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>73.550000</td>
      <td>69.670000</td>
    </tr>
    <tr>
      <th>1090</th>
      <td>1090</td>
      <td>918.900000</td>
      <td>63.104000</td>
      <td>192.900000</td>
      <td>3.869906</td>
      <td>207.300000</td>
      <td>5.212070</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>26.020000</td>
      <td>38.180000</td>
    </tr>
    <tr>
      <th>1091</th>
      <td>1091</td>
      <td>918.710000</td>
      <td>49.568000</td>
      <td>241.600000</td>
      <td>1.811921</td>
      <td>227.400000</td>
      <td>2.371156</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>90.350000</td>
      <td>73.340000</td>
    </tr>
    <tr>
      <th>1092</th>
      <td>1092</td>
      <td>916.600000</td>
      <td>71.096000</td>
      <td>189.300000</td>
      <td>3.064608</td>
      <td>200.800000</td>
      <td>3.892276</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>45.590000</td>
      <td>52.310000</td>
    </tr>
    <tr>
      <th>1093</th>
      <td>1093</td>
      <td>912.600000</td>
      <td>58.406000</td>
      <td>172.700000</td>
      <td>3.825167</td>
      <td>189.100000</td>
      <td>4.764682</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>64.840000</td>
      <td>58.280000</td>
    </tr>
    <tr>
      <th>1094</th>
      <td>1094</td>
      <td>921.530000</td>
      <td>77.702000</td>
      <td>97.100000</td>
      <td>3.265932</td>
      <td>125.900000</td>
      <td>4.451511</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>14.560000</td>
      <td>15.100000</td>
    </tr>
  </tbody>
</table>
<p>1095 rows × 11 columns</p>
</div>




```python
data[data.isnull().any(axis=1)]
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
      <th>number</th>
      <th>air_pressure_9am</th>
      <th>air_temp_9am</th>
      <th>avg_wind_direction_9am</th>
      <th>avg_wind_speed_9am</th>
      <th>max_wind_direction_9am</th>
      <th>max_wind_speed_9am</th>
      <th>rain_accumulation_9am</th>
      <th>rain_duration_9am</th>
      <th>relative_humidity_9am</th>
      <th>relative_humidity_3pm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>917.890000</td>
      <td>NaN</td>
      <td>169.200000</td>
      <td>2.192201</td>
      <td>196.800000</td>
      <td>2.930391</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>48.990000</td>
      <td>51.190000</td>
    </tr>
    <tr>
      <th>111</th>
      <td>111</td>
      <td>915.290000</td>
      <td>58.820000</td>
      <td>182.600000</td>
      <td>15.613841</td>
      <td>189.000000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>21.500000</td>
      <td>29.690000</td>
    </tr>
    <tr>
      <th>177</th>
      <td>177</td>
      <td>915.900000</td>
      <td>NaN</td>
      <td>183.300000</td>
      <td>4.719943</td>
      <td>189.900000</td>
      <td>5.346287</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>29.260000</td>
      <td>46.500000</td>
    </tr>
    <tr>
      <th>262</th>
      <td>262</td>
      <td>923.596607</td>
      <td>58.380598</td>
      <td>47.737753</td>
      <td>10.636273</td>
      <td>67.145843</td>
      <td>13.671423</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>17.990876</td>
      <td>16.461685</td>
    </tr>
    <tr>
      <th>277</th>
      <td>277</td>
      <td>920.480000</td>
      <td>62.600000</td>
      <td>194.400000</td>
      <td>2.751436</td>
      <td>NaN</td>
      <td>3.869906</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>52.580000</td>
      <td>54.030000</td>
    </tr>
    <tr>
      <th>334</th>
      <td>334</td>
      <td>916.230000</td>
      <td>75.740000</td>
      <td>149.100000</td>
      <td>2.751436</td>
      <td>187.500000</td>
      <td>4.183078</td>
      <td>NaN</td>
      <td>1480.000000</td>
      <td>31.880000</td>
      <td>32.900000</td>
    </tr>
    <tr>
      <th>358</th>
      <td>358</td>
      <td>917.440000</td>
      <td>58.514000</td>
      <td>55.100000</td>
      <td>10.021491</td>
      <td>NaN</td>
      <td>12.705819</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>13.880000</td>
      <td>25.930000</td>
    </tr>
    <tr>
      <th>361</th>
      <td>361</td>
      <td>920.444946</td>
      <td>65.801845</td>
      <td>49.823346</td>
      <td>21.520177</td>
      <td>61.886944</td>
      <td>25.549112</td>
      <td>NaN</td>
      <td>40.364018</td>
      <td>12.278715</td>
      <td>7.618649</td>
    </tr>
    <tr>
      <th>381</th>
      <td>381</td>
      <td>918.480000</td>
      <td>66.542000</td>
      <td>90.900000</td>
      <td>3.467257</td>
      <td>89.400000</td>
      <td>4.406772</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>20.640000</td>
      <td>14.350000</td>
    </tr>
    <tr>
      <th>409</th>
      <td>409</td>
      <td>NaN</td>
      <td>67.853833</td>
      <td>65.880616</td>
      <td>4.328594</td>
      <td>78.570923</td>
      <td>5.216734</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>18.487385</td>
      <td>20.356594</td>
    </tr>
    <tr>
      <th>517</th>
      <td>517</td>
      <td>920.570000</td>
      <td>53.600000</td>
      <td>100.100000</td>
      <td>4.697574</td>
      <td>NaN</td>
      <td>6.285801</td>
      <td>4.712</td>
      <td>14842.000000</td>
      <td>79.880000</td>
      <td>84.530000</td>
    </tr>
    <tr>
      <th>519</th>
      <td>519</td>
      <td>916.250000</td>
      <td>55.670000</td>
      <td>176.400000</td>
      <td>6.666081</td>
      <td>188.200000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>72.550000</td>
      <td>74.390000</td>
    </tr>
    <tr>
      <th>546</th>
      <td>546</td>
      <td>NaN</td>
      <td>42.746000</td>
      <td>251.100000</td>
      <td>12.929513</td>
      <td>274.400000</td>
      <td>17.604718</td>
      <td>14.627</td>
      <td>7825.000000</td>
      <td>87.870000</td>
      <td>70.770000</td>
    </tr>
    <tr>
      <th>620</th>
      <td>620</td>
      <td>921.200000</td>
      <td>56.786000</td>
      <td>192.300000</td>
      <td>9.551734</td>
      <td>201.400000</td>
      <td>11.005745</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>59.790000</td>
      <td>77.750000</td>
    </tr>
    <tr>
      <th>625</th>
      <td>625</td>
      <td>912.400000</td>
      <td>50.774000</td>
      <td>171.600000</td>
      <td>NaN</td>
      <td>181.400000</td>
      <td>4.831790</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>86.840000</td>
      <td>64.740000</td>
    </tr>
    <tr>
      <th>656</th>
      <td>656</td>
      <td>920.830000</td>
      <td>66.344000</td>
      <td>NaN</td>
      <td>15.457255</td>
      <td>189.400000</td>
      <td>16.486248</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>23.770000</td>
      <td>51.630000</td>
    </tr>
    <tr>
      <th>670</th>
      <td>670</td>
      <td>910.920000</td>
      <td>48.362000</td>
      <td>156.500000</td>
      <td>NaN</td>
      <td>177.500000</td>
      <td>16.128337</td>
      <td>4.970</td>
      <td>10560.000000</td>
      <td>80.560000</td>
      <td>88.220000</td>
    </tr>
    <tr>
      <th>672</th>
      <td>672</td>
      <td>922.448945</td>
      <td>72.863773</td>
      <td>NaN</td>
      <td>3.682370</td>
      <td>214.196160</td>
      <td>4.849450</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>16.753670</td>
      <td>17.804720</td>
    </tr>
    <tr>
      <th>705</th>
      <td>705</td>
      <td>911.900000</td>
      <td>59.072000</td>
      <td>199.800000</td>
      <td>1.275056</td>
      <td>239.500000</td>
      <td>1.834291</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>77.630000</td>
      <td>59.130000</td>
    </tr>
    <tr>
      <th>731</th>
      <td>731</td>
      <td>922.970166</td>
      <td>51.391847</td>
      <td>33.810942</td>
      <td>NaN</td>
      <td>59.290089</td>
      <td>11.111555</td>
      <td>0.000</td>
      <td>4.735034</td>
      <td>34.807753</td>
      <td>18.418179</td>
    </tr>
    <tr>
      <th>737</th>
      <td>737</td>
      <td>917.895130</td>
      <td>76.804690</td>
      <td>104.771020</td>
      <td>1.632705</td>
      <td>97.178763</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>13.771311</td>
      <td>16.792455</td>
    </tr>
    <tr>
      <th>788</th>
      <td>788</td>
      <td>917.923442</td>
      <td>73.249717</td>
      <td>42.101739</td>
      <td>4.132698</td>
      <td>64.284969</td>
      <td>5.345258</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>6.939692</td>
      <td>18.793825</td>
    </tr>
    <tr>
      <th>840</th>
      <td>840</td>
      <td>918.043767</td>
      <td>NaN</td>
      <td>181.774042</td>
      <td>0.964376</td>
      <td>185.618601</td>
      <td>1.570007</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>11.911222</td>
      <td>18.154358</td>
    </tr>
    <tr>
      <th>848</th>
      <td>848</td>
      <td>915.250000</td>
      <td>37.562000</td>
      <td>246.500000</td>
      <td>11.587349</td>
      <td>258.700000</td>
      <td>NaN</td>
      <td>3.171</td>
      <td>2891.000000</td>
      <td>91.000000</td>
      <td>90.780000</td>
    </tr>
    <tr>
      <th>861</th>
      <td>861</td>
      <td>919.065408</td>
      <td>NaN</td>
      <td>172.303728</td>
      <td>2.639600</td>
      <td>193.058141</td>
      <td>3.326949</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>12.497839</td>
      <td>13.438518</td>
    </tr>
    <tr>
      <th>869</th>
      <td>869</td>
      <td>NaN</td>
      <td>45.104000</td>
      <td>259.000000</td>
      <td>3.265932</td>
      <td>275.000000</td>
      <td>4.026492</td>
      <td>0.000</td>
      <td>80.000000</td>
      <td>85.270000</td>
      <td>90.260000</td>
    </tr>
    <tr>
      <th>998</th>
      <td>998</td>
      <td>914.140000</td>
      <td>71.240000</td>
      <td>NaN</td>
      <td>1.722444</td>
      <td>232.900000</td>
      <td>2.326418</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>24.200000</td>
      <td>41.380000</td>
    </tr>
    <tr>
      <th>1031</th>
      <td>1031</td>
      <td>922.669195</td>
      <td>NaN</td>
      <td>47.946284</td>
      <td>7.969686</td>
      <td>65.770066</td>
      <td>10.262337</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>18.920805</td>
      <td>19.641841</td>
    </tr>
    <tr>
      <th>1035</th>
      <td>1035</td>
      <td>919.670000</td>
      <td>77.576000</td>
      <td>171.800000</td>
      <td>6.554234</td>
      <td>191.000000</td>
      <td>8.164831</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>56.860000</td>
      <td>50.650000</td>
    </tr>
    <tr>
      <th>1063</th>
      <td>1063</td>
      <td>917.300185</td>
      <td>65.790001</td>
      <td>NaN</td>
      <td>1.879553</td>
      <td>222.498226</td>
      <td>2.692862</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>14.972668</td>
      <td>20.966267</td>
    </tr>
    <tr>
      <th>1066</th>
      <td>1066</td>
      <td>919.564869</td>
      <td>73.726732</td>
      <td>68.704694</td>
      <td>3.551777</td>
      <td>102.571616</td>
      <td>4.861315</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>11.657314</td>
      <td>17.331823</td>
    </tr>
  </tbody>
</table>
</div>



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Data Cleaning Steps<br><br></p>

We will not need to number for each row so we can clean it.


```python
del data['number']
```

Now let's drop null values using the *pandas dropna* function.


```python
before_rows = data.shape[0]
print(before_rows)
```

    1095



```python
data = data.dropna()
```


```python
after_rows = data.shape[0]
print(after_rows)
```

    1064


<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

How many rows dropped due to cleaning?<br><br></p>



```python
before_rows - after_rows
```




    31



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold">
Convert to a Classification Task <br><br></p>
Binarize the relative_humidity_3pm to 0 or 1.<br>



```python
clean_data = data.copy()
clean_data['high_humidity_label'] = (clean_data['relative_humidity_3pm'] > 24.99)*1
print(clean_data['high_humidity_label'])
```

    0       1
    1       0
    2       0
    3       0
    4       1
    5       1
    6       0
    7       1
    8       0
    9       1
    10      1
    11      1
    12      1
    13      1
    14      0
    15      0
    16      1
    17      0
    18      1
    19      0
    20      0
    21      1
    22      0
    23      1
    24      0
    25      1
    26      1
    27      1
    28      1
    29      1
           ..
    1065    1
    1066    0
    1067    1
    1068    1
    1069    1
    1070    1
    1071    1
    1072    0
    1073    1
    1074    1
    1075    0
    1076    0
    1077    1
    1078    0
    1079    1
    1080    0
    1081    0
    1082    1
    1083    1
    1084    1
    1085    1
    1086    1
    1087    1
    1088    1
    1089    1
    1090    1
    1091    1
    1092    1
    1093    1
    1094    0
    Name: high_humidity_label, Length: 1095, dtype: int64


<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Target is stored in 'y'.
<br><br></p>



```python
y=clean_data[['high_humidity_label']].copy()
#y
```


```python
clean_data['relative_humidity_3pm'].head()
```




    0    36.160000
    1    19.426597
    2    14.460000
    3    12.742547
    4    76.740000
    Name: relative_humidity_3pm, dtype: float64




```python
y.head()
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
      <th>high_humidity_label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Use 9am Sensor Signals as Features to Predict Humidity at 3pm
<br><br></p>



```python
morning_features = ['air_pressure_9am','air_temp_9am','avg_wind_direction_9am','avg_wind_speed_9am',
        'max_wind_direction_9am','max_wind_speed_9am','rain_accumulation_9am',
        'rain_duration_9am']
```


```python
X = clean_data[morning_features].copy()
```


```python
X.columns
```




    Index(['air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
           'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
           'rain_accumulation_9am', 'rain_duration_9am'],
          dtype='object')




```python
y.columns
```




    Index(['high_humidity_label'], dtype='object')



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Perform Test and Train split

<br><br></p>



## REMINDER: Training Phase

In the **training phase**, the learning algorithm uses the training data to adjust the model’s parameters to minimize errors.  At the end of the training phase, you get the trained model.

<img src="TrainingVSTesting.jpg" align="middle" style="width:550px;height:360px;"/>

<BR>
In the **testing phase**, the trained model is applied to test data.  Test data is separate from the training data, and is previously unseen by the model.  The model is then evaluated on how it performs on the test data.  The goal in building a classifier model is to have the model perform well on training as well as test data.



```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)
```


```python
#type(X_train)
#type(X_test)
#type(y_train)
#type(y_test)
#X_train.head()
#y_train.describe()
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Fit on Train Set
<br><br></p>



```python
humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
humidity_classifier.fit(X_train, y_train)
```




    DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
                max_features=None, max_leaf_nodes=10,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, presort=False, random_state=0,
                splitter='best')




```python
type(humidity_classifier)
```




    sklearn.tree.tree.DecisionTreeClassifier



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Predict on Test Set 

<br><br></p>



```python
predictions = humidity_classifier.predict(X_test)
```


```python
predictions[:10]
```




    array([0, 0, 1, 1, 1, 1, 0, 0, 0, 1])




```python
y_test['high_humidity_label'][:10]
```




    456     0
    845     0
    693     1
    259     1
    723     1
    224     1
    300     1
    442     0
    585     1
    1057    1
    Name: high_humidity_label, dtype: int64



<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Measure Accuracy of the Classifier
<br><br></p>



```python
accuracy_score(y_true = y_test, y_pred = predictions)
```




    0.8153409090909091




```python

```
