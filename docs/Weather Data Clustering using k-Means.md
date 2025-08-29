
Clustering with scikit-learn

In this notebook, we will learn how to perform k-means lustering using scikit-learn in Python.
We will use cluster analysis to generate a big picture model of the weather at a local station using a minute-graunlarity data. In this dataset, we have in the order of millions records. How do we create 12 clusters our of them?
**NOTE:** The dataset we will use is in a large CSV file called *minute_weather.csv*. Please download it into the *weather* directory in your *Week-7-MachineLearning* folder. The download link is: https://drive.google.com/open?id=0B8iiZ7pSaSFZb3ItQ1l4LWRMTjg

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

%matplotlib inline
```

```python
print(os.listdir('../../../../../data/w7ml'))
data = pd.read_csv('../../../../../data/w7ml/minute_weather.csv')
```

    ['minute_weather.csv']

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

|  | rowID | hpwren_timestamp | air_pressure | air_temp | avg_wind_direction | avg_wind_speed | max_wind_direction | max_wind_speed | min_wind_direction | min_wind_speed | rain_accumulation | rain_duration | relative_humidity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 2011-09-10 00:00:49 | 912.3 | 64.76 | 97.0 | 1.2 | 106.0 | 1.6 | 85.0 | 1.0 | NaN | NaN | 60.5 |
| 1 | 1 | 2011-09-10 00:01:49 | 912.3 | 63.86 | 161.0 | 0.8 | 215.0 | 1.5 | 43.0 | 0.2 | 0.0 | 0.0 | 39.9 |
| 2 | 2 | 2011-09-10 00:02:49 | 912.3 | 64.22 | 77.0 | 0.7 | 143.0 | 1.2 | 324.0 | 0.3 | 0.0 | 0.0 | 43.0 |
| 3 | 3 | 2011-09-10 00:03:49 | 912.3 | 64.40 | 89.0 | 1.2 | 112.0 | 1.6 | 12.0 | 0.7 | 0.0 | 0.0 | 49.5 |
| 4 | 4 | 2011-09-10 00:04:49 | 912.3 | 64.40 | 185.0 | 0.4 | 260.0 | 1.0 | 100.0 | 0.1 | 0.0 | 0.0 | 58.8 |

Lots of rows, so let us sample down by taking every 10th row. 

```python
sampled_df = data[(data['rowID'] % 10) == 0]
sampled_df.shape
```

    (158726, 13)

```python
sampled_df.describe().transpose()
```

|  | count | mean | std | min | 25% | 50% | 75% | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rowID | 158726.0 | 793625.000000 | 458203.937510 | 0.00 | 396812.5 | 793625.00 | 1190437.50 | 1587250.00 |
| air_pressure | 158726.0 | 916.830161 | 3.051717 | 905.00 | 914.8 | 916.70 | 918.70 | 929.50 |
| air_temp | 158726.0 | 61.851589 | 11.833569 | 31.64 | 52.7 | 62.24 | 70.88 | 99.50 |
| avg_wind_direction | 158680.0 | 162.156100 | 95.278201 | 0.00 | 62.0 | 182.00 | 217.00 | 359.00 |
| avg_wind_speed | 158680.0 | 2.775215 | 2.057624 | 0.00 | 1.3 | 2.20 | 3.80 | 31.90 |
| max_wind_direction | 158680.0 | 163.462144 | 92.452139 | 0.00 | 68.0 | 187.00 | 223.00 | 359.00 |
| max_wind_speed | 158680.0 | 3.400558 | 2.418802 | 0.10 | 1.6 | 2.70 | 4.60 | 36.00 |
| min_wind_direction | 158680.0 | 166.774017 | 97.441109 | 0.00 | 76.0 | 180.00 | 212.00 | 359.00 |
| min_wind_speed | 158680.0 | 2.134664 | 1.742113 | 0.00 | 0.8 | 1.60 | 3.00 | 31.60 |
| rain_accumulation | 158725.0 | 0.000318 | 0.011236 | 0.00 | 0.0 | 0.00 | 0.00 | 3.12 |
| rain_duration | 158725.0 | 0.409627 | 8.665523 | 0.00 | 0.0 | 0.00 | 0.00 | 2960.00 |
| relative_humidity | 158726.0 | 47.609470 | 26.214409 | 0.90 | 24.7 | 44.70 | 68.00 | 93.00 |

```python
sampled_df[sampled_df['rain_accumulation'] == 0].shape
```

    (157812, 13)

```python
sampled_df[sampled_df['rain_duration'] == 0].shape
```

    (157237, 13)

Drop all the Rows with Empty rain_duration and rain_accumulation

```python
del sampled_df['rain_accumulation']
del sampled_df['rain_duration']
```

```python
rows_before = sampled_df.shape[0]
sampled_df = sampled_df.dropna()
rows_after = sampled_df.shape[0]
```

How many rows did we drop ?

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

|  | air_pressure | air_temp | avg_wind_direction | avg_wind_speed | max_wind_direction | max_wind_speed | relative_humidity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 912.3 | 64.76 | 97.0 | 1.2 | 106.0 | 1.6 | 60.5 |
| 10 | 912.3 | 62.24 | 144.0 | 1.2 | 167.0 | 1.8 | 38.5 |
| 20 | 912.2 | 63.32 | 100.0 | 2.0 | 122.0 | 2.5 | 58.3 |
| 30 | 912.2 | 62.60 | 91.0 | 2.0 | 103.0 | 2.4 | 57.9 |
| 40 | 912.2 | 64.04 | 81.0 | 2.6 | 88.0 | 2.9 | 57.4 |
| 50 | 912.1 | 63.68 | 102.0 | 1.2 | 119.0 | 1.5 | 51.4 |
| 60 | 912.0 | 64.04 | 83.0 | 0.7 | 101.0 | 0.9 | 51.4 |
| 70 | 911.9 | 64.22 | 82.0 | 2.0 | 97.0 | 2.4 | 62.2 |
| 80 | 911.9 | 61.70 | 67.0 | 3.3 | 70.0 | 3.5 | 71.5 |
| 90 | 911.9 | 61.34 | 67.0 | 3.6 | 75.0 | 4.2 | 72.5 |
| 100 | 911.8 | 62.96 | 95.0 | 2.3 | 106.0 | 2.5 | 63.9 |
| 110 | 911.8 | 64.22 | 83.0 | 2.1 | 88.0 | 2.5 | 59.1 |
| 120 | 911.8 | 63.86 | 68.0 | 2.1 | 76.0 | 2.4 | 63.5 |
| 130 | 911.6 | 64.40 | 156.0 | 0.5 | 203.0 | 0.7 | 50.4 |
| 140 | 911.5 | 65.30 | 85.0 | 2.2 | 92.0 | 2.5 | 58.0 |
| 150 | 911.4 | 64.58 | 154.0 | 1.3 | 176.0 | 2.1 | 50.2 |
| 160 | 911.4 | 65.48 | 154.0 | 0.9 | 208.0 | 1.9 | 46.2 |
| 170 | 911.5 | 65.66 | 95.0 | 1.1 | 109.0 | 1.6 | 45.2 |
| 180 | 911.4 | 65.66 | 155.0 | 1.1 | 167.0 | 1.6 | 42.8 |
| 190 | 911.4 | 67.10 | 157.0 | 1.2 | 172.0 | 1.6 | 36.8 |
| 200 | 911.4 | 68.00 | 53.0 | 0.3 | 69.0 | 0.5 | 33.4 |
| 210 | 911.3 | 67.64 | 167.0 | 1.5 | 196.0 | 2.2 | 34.4 |
| 220 | 911.4 | 67.82 | 4.0 | 0.6 | 25.0 | 0.7 | 34.2 |
| 230 | 911.4 | 66.74 | 172.0 | 1.3 | 192.0 | 1.9 | 37.8 |
| 240 | 911.4 | 66.56 | 39.0 | 0.2 | 145.0 | 0.3 | 41.6 |
| 250 | 911.4 | 65.66 | 56.0 | 1.9 | 67.0 | 2.2 | 51.8 |
| 260 | 911.5 | 65.66 | 74.0 | 0.8 | 101.0 | 1.2 | 41.1 |
| 270 | 911.4 | 66.92 | 147.0 | 0.9 | 174.0 | 1.1 | 36.0 |
| 280 | 911.3 | 64.76 | 73.0 | 1.0 | 82.0 | 1.2 | 43.3 |
| 290 | 911.3 | 64.94 | 164.0 | 1.3 | 176.0 | 1.7 | 43.0 |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 1586960 | 914.7 | 76.46 | 247.0 | 0.6 | 264.0 | 0.7 | 43.4 |
| 1586970 | 914.8 | 76.28 | 208.0 | 0.7 | 216.0 | 0.9 | 43.7 |
| 1586980 | 914.8 | 76.10 | 209.0 | 0.7 | 216.0 | 0.9 | 43.9 |
| 1586990 | 914.9 | 76.28 | 339.0 | 0.5 | 350.0 | 0.7 | 43.4 |
| 1587000 | 914.9 | 75.92 | 344.0 | 0.4 | 352.0 | 0.6 | 43.9 |
| 1587010 | 915.0 | 75.56 | 323.0 | 0.3 | 348.0 | 0.5 | 45.5 |
| 1587020 | 915.1 | 75.56 | 324.0 | 1.1 | 347.0 | 1.5 | 46.0 |
| 1587030 | 915.1 | 75.74 | 1.0 | 1.3 | 13.0 | 1.7 | 45.8 |
| 1587040 | 915.2 | 75.38 | 355.0 | 0.9 | 1.0 | 1.1 | 46.1 |
| 1587050 | 915.3 | 75.38 | 359.0 | 1.4 | 11.0 | 1.5 | 45.8 |
| 1587060 | 915.4 | 75.38 | 11.0 | 1.1 | 21.0 | 1.3 | 45.7 |
| 1587070 | 915.5 | 75.38 | 13.0 | 1.4 | 24.0 | 1.6 | 46.6 |
| 1587080 | 915.6 | 75.20 | 18.0 | 1.0 | 24.0 | 1.2 | 46.5 |
| 1587090 | 915.6 | 75.20 | 356.0 | 1.7 | 1.0 | 1.9 | 47.2 |
| 1587100 | 915.7 | 75.38 | 13.0 | 1.5 | 24.0 | 1.7 | 46.7 |
| 1587110 | 915.7 | 75.02 | 19.0 | 1.2 | 28.0 | 1.4 | 46.7 |
| 1587120 | 915.7 | 74.84 | 25.0 | 1.4 | 35.0 | 1.6 | 46.5 |
| 1587130 | 915.8 | 74.84 | 23.0 | 1.3 | 30.0 | 1.5 | 46.9 |
| 1587140 | 915.8 | 74.84 | 32.0 | 1.4 | 41.0 | 1.7 | 45.5 |
| 1587150 | 915.8 | 75.20 | 23.0 | 1.1 | 31.0 | 1.4 | 45.7 |
| 1587160 | 915.8 | 75.38 | 16.0 | 1.2 | 28.0 | 1.5 | 46.3 |
| 1587170 | 915.7 | 75.38 | 347.0 | 1.2 | 353.0 | 1.4 | 48.1 |
| 1587180 | 915.8 | 75.74 | 326.0 | 1.2 | 337.0 | 1.6 | 48.3 |
| 1587190 | 915.9 | 75.92 | 289.0 | 0.7 | 309.0 | 0.9 | 48.1 |
| 1587200 | 915.9 | 75.74 | 335.0 | 0.9 | 348.0 | 1.1 | 47.8 |
| 1587210 | 915.9 | 75.56 | 330.0 | 1.0 | 341.0 | 1.3 | 47.8 |
| 1587220 | 915.9 | 75.56 | 330.0 | 1.1 | 341.0 | 1.4 | 48.0 |
| 1587230 | 915.9 | 75.56 | 344.0 | 1.4 | 352.0 | 1.7 | 48.0 |
| 1587240 | 915.9 | 75.20 | 359.0 | 1.3 | 9.0 | 1.6 | 46.3 |
| 1587250 | 915.9 | 74.84 | 6.0 | 1.5 | 20.0 | 1.9 | 46.1 |
158680 rows × 7 columns

```python
X = StandardScaler().fit_transform(select_df)

```

    14.154615859301948

Use k-Means Clustering

```python
kmeans = KMeans(n_clusters=12)
model = kmeans.fit(X)
print("model\n", model)
```

     KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
        n_clusters=12, n_init=10, n_jobs=None, precompute_distances='auto',
        random_state=None, tol=0.0001, verbose=0)

What are the centers of 12 clusters we formed ?

```python
centers = model.cluster_centers_

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

```

|  | air_pressure | air_temp | avg_wind_direction | avg_wind_speed | max_wind_direction | max_wind_speed | relative_humidity | prediction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | -0.696179 | 0.543306 | 0.176914 | -0.584034 | 0.346273 | -0.597390 | -0.113975 | 0 |
| 1 | 0.253519 | -0.994408 | 0.660104 | -0.547669 | 0.851367 | -0.530244 | 1.157707 | 1 |
| 2 | 0.729960 | 0.436397 | 0.285485 | -0.534847 | 0.473290 | -0.541097 | -0.771854 | 2 |
| 3 | -0.211226 | 0.631440 | 0.408543 | 0.734913 | 0.516678 | 0.672890 | -0.150024 | 3 |
| 4 | 1.189984 | -0.255417 | -1.155036 | 2.125578 | -1.053448 | 2.242731 | -1.134201 | 4 |
| 5 | 1.368646 | -0.082131 | -1.206839 | -0.047095 | -1.075826 | -0.026676 | -0.977668 | 5 |
| 6 | -1.179071 | -0.876845 | 0.446634 | 1.975588 | 0.538606 | 1.936851 | 0.915087 | 6 |
| 7 | -0.840075 | -1.198350 | 0.375242 | 0.353435 | 0.473694 | 0.341321 | 1.362789 | 7 |
| 8 | 0.060448 | -0.787949 | -1.197091 | -0.570792 | -1.043160 | -0.585314 | 0.877620 | 8 |
| 9 | 0.130830 | 0.843694 | 1.411037 | -0.638439 | 1.675077 | -0.589183 | -0.714280 | 9 |
| 10 | 0.233790 | 0.319470 | 1.887946 | -0.651943 | -1.551642 | -0.576783 | -0.282757 | 10 |
| 11 | -0.161980 | 0.863030 | -1.311148 | -0.589838 | -1.166815 | -0.605152 | -0.642297 | 11 |

# Dry Days

```python
parallel_plot(P[P['relative_humidity']  0.5])
```

*[Image: png - file not found]*

# Cool Days

```python
parallel_plot(P[(P['relative_humidity'] > 0.5) & (P['air_temp'] < 0.5)])
```

*[Image: png - file not found]*
