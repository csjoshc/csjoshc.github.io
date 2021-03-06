
<a href="../../../index.html">Go back to index</a>

<a href="../base.html">Go back to Python Portal</a>

<head>
  <link rel="stylesheet" href="../../../cssthemes/github.css">
  <meta name="viewport" content="initial-scale=1, width=device-width">
</head>


```python
import datetime
time_start = datetime.datetime.now()

import sys
print(sys.executable)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
InteractiveShell.colors = "Linux"
InteractiveShell.separate_in = 0
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Clustering - kmeans

The clustering tutorial was based on weather data and classifying them into hot or cold days based on 7-8 features. However, I wanted to try something on my own using the movies rating data. I wanted to 2-D graph movies by the number of raters and the average score, and plot. Then, I would use a third variable (the decade it was released) to color the points, to see if movies released in certain decades were more actively reviewed or had higher. A fourth variable, the average review timestamp, would be used as intensity for a heatmap for the color variable. 

After assessing the data, I would then run the data through a cluster algoritm, including generating an elbow curve. 

Installed seaborn from conda for leanringenv


```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from itertools import cycle, islice
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
sns.set(style="ticks", context="talk")
```


```python
movies = pd.read_csv('../../../../data/w4pd/movies.csv')
ratings = pd.read_csv('../../../../data/w4pd/ratings.csv')
```


```python
movies.shape, ratings.shape
movies.head()
ratings.head()
```




    ((27278, 3), (20000263, 4))






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
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children|Fantasy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Comedy|Drama|Romance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
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
      <th>userId</th>
      <th>movieId</th>
      <th>rating</th>
      <th>timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3.5</td>
      <td>1112486027</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>29</td>
      <td>3.5</td>
      <td>1112484676</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>32</td>
      <td>3.5</td>
      <td>1112484819</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>47</td>
      <td>3.5</td>
      <td>1112484727</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>50</td>
      <td>3.5</td>
      <td>1112484580</td>
    </tr>
  </tbody>
</table>
</div>



# Data Prep

## Joining data

Here, I join together two tables and calculate aggregate values, so that I condense the information from million of rows into a few tens of thousands. 


```python
movie_ratings = ratings[['movieId', 'rating']].groupby('movieId').mean() 
movie_counts = ratings[['movieId', 'rating']].groupby('movieId').count() 
movie_timestamps = pd.to_datetime(ratings[['movieId', 'timestamp']].groupby('movieId').mean()['timestamp'], unit = 's').dt.date
```


```python
print("Timestamp range is ", movie_timestamps.min(), " to ", movie_timestamps.max())
```

    Timestamp range is  1997-03-02  to  2015-03-30


Join all three on Movie ID


```python
merged_1 = movie_ratings.merge(movie_counts, on = 'movieId', how='inner').merge(movie_timestamps, on = 'movieId', how='inner')
merged_1 = merged_1.merge(movies[['movieId', 'title']], on = 'movieId', how='inner')
merged_1.head()
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
      <th>movieId</th>
      <th>rating_x</th>
      <th>rating_y</th>
      <th>timestamp</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3.921240</td>
      <td>49695</td>
      <td>2003-05-11</td>
      <td>Toy Story (1995)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3.211977</td>
      <td>22243</td>
      <td>2002-11-18</td>
      <td>Jumanji (1995)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3.151040</td>
      <td>12735</td>
      <td>2000-05-30</td>
      <td>Grumpier Old Men (1995)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2.861393</td>
      <td>2756</td>
      <td>1999-04-15</td>
      <td>Waiting to Exhale (1995)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3.064592</td>
      <td>12161</td>
      <td>2000-06-26</td>
      <td>Father of the Bride Part II (1995)</td>
    </tr>
  </tbody>
</table>
</div>



## Splitting columns - title and year

Next, extract the year from the title and bin into a decade 


```python
Title = merged_1['title'].str.extract('(.+?) \(')
Year  = merged_1['title'].str.extract('(\d\d\d\d)')
Title = Title.rename(columns = {Title.columns[0]: "Name"})
Year = Year.rename(columns = {Year.columns[0]: "Year"})

merged_1 = pd.concat([merged_1, Title, Year], axis = 1, join = "inner")
merged_1.head()

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
      <th>movieId</th>
      <th>rating_x</th>
      <th>rating_y</th>
      <th>timestamp</th>
      <th>title</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3.921240</td>
      <td>49695</td>
      <td>2003-05-11</td>
      <td>Toy Story (1995)</td>
      <td>Toy Story</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3.211977</td>
      <td>22243</td>
      <td>2002-11-18</td>
      <td>Jumanji (1995)</td>
      <td>Jumanji</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3.151040</td>
      <td>12735</td>
      <td>2000-05-30</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Grumpier Old Men</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2.861393</td>
      <td>2756</td>
      <td>1999-04-15</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Waiting to Exhale</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3.064592</td>
      <td>12161</td>
      <td>2000-06-26</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Father of the Bride Part II</td>
      <td>1995</td>
    </tr>
  </tbody>
</table>
</div>



Finally, drop the title column since it's been split


```python
del merged_1['title']
merged_1 = merged_1.rename(columns={merged_1.columns[1]: "Score", merged_1.columns[2] : "Ratings", merged_1.columns[3]:"Date"})
merged_1.head()
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
      <th>movieId</th>
      <th>Score</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3.921240</td>
      <td>49695</td>
      <td>2003-05-11</td>
      <td>Toy Story</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3.211977</td>
      <td>22243</td>
      <td>2002-11-18</td>
      <td>Jumanji</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3.151040</td>
      <td>12735</td>
      <td>2000-05-30</td>
      <td>Grumpier Old Men</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2.861393</td>
      <td>2756</td>
      <td>1999-04-15</td>
      <td>Waiting to Exhale</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3.064592</td>
      <td>12161</td>
      <td>2000-06-26</td>
      <td>Father of the Bride Part II</td>
      <td>1995</td>
    </tr>
  </tbody>
</table>
</div>



I need to actually hold onto the POSIX average rating timestamps so that I can convert them to numbers for analysis. 


```python
scaled_1 = merged_1.copy()
del scaled_1['Name']
del scaled_1['Date']
scaled_1 = scaled_1.merge(ratings[['movieId', 'timestamp']].groupby('movieId').mean().astype(int), on = 'movieId', how='inner') 
del scaled_1['movieId']
scaled_1 = scaled_1.rename(columns={scaled_1.columns[3]: "Date"})
scaled_1.head()
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
      <th>Score</th>
      <th>Ratings</th>
      <th>Year</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.921240</td>
      <td>49695</td>
      <td>1995</td>
      <td>1052654098</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.211977</td>
      <td>22243</td>
      <td>1995</td>
      <td>1037616295</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.151040</td>
      <td>12735</td>
      <td>1995</td>
      <td>959648019</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.861393</td>
      <td>2756</td>
      <td>1995</td>
      <td>924214411</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.064592</td>
      <td>12161</td>
      <td>1995</td>
      <td>962016085</td>
    </tr>
  </tbody>
</table>
</div>




```python
%%capture
scaled_1['Year'] = pd.to_numeric(scaled_1['Year'])
var_corr = scaled_1.corr()
normalized = StandardScaler().fit_transform(scaled_1)
```

# Visualization 

## Exploring Correlation

Finally, we can graph our data, starting with a heatmap for correlation between numerical variables (this is why I needed to hold onto the rating timestamp in POSIX format, since I wasn't able top pass a human readable format directly into the method. 


```python
sns.heatmap(var_corr)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f09d13d7f28>




![png](7_ML_Clust_files/7_ML_Clust_19_1.png)



```python
fig, axis = plt.subplots()
fig.set_size_inches(11.7, 4)
axis.set_title('Ratings vs Rating Date',fontsize=26)
axis.set_xlabel('Average Date of Ratings',fontsize=18)
axis.set_ylabel('Number of Ratings',fontsize=18)
plt.plot_date(x='Date', y = 'Ratings', data = merged_1)
plt.show();

fig, axis = plt.subplots()
fig.set_size_inches(6, 10)
axis.set_title('Score vs Ratings',fontsize=26)
axis.set_xlabel('Number of Ratings',fontsize=18)
axis.set_ylabel('Average Score',fontsize=18)
plt.scatter(x='Ratings', y = 'Score', marker = '.', s=4, data = merged_1)
plt.show();
```


![png](7_ML_Clust_files/7_ML_Clust_20_0.png)



![png](7_ML_Clust_files/7_ML_Clust_20_1.png)


## What's next?

* Bin 'Year' column into decades so I can color by the different buckets. Use this to compare to the clusters generated by kmeans clustering (color by either classification and compare side by side)
* Since I'm already familiar with ggplot, I would want to try to use [python ggplot](https://github.com/has2k1/plotnine) to color and facet by categorical variable and see if I can do something with it

Try using plotnine
`conda install -c conda-forge plotnine`



```python
merged_1['Year'] = pd.to_numeric(merged_1['Year'])
```


```python
from plotnine import ggplot, geom_point, aes, stat_smooth, geom_histogram
ggplot() + geom_histogram(aes('Year'), data = merged_1)
```

    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/plotnine/stats/stat_bin.py:93: UserWarning: 'stat_bin()' using 'bins = 3865'. Pick better value with 'binwidth'.
      warn(msg.format(params['bins']))
    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/plotnine/layer.py:360: UserWarning: stat_bin : Removed 19 rows containing non-finite values.
      data = self.stat.compute_layer(data, params, layout)



![png](7_ML_Clust_files/7_ML_Clust_23_1.png)





    <ggplot: (8729985344730)>



What is going on with the Year column of merged_1? Very odd, so I look at min and max. 

# Further Data Cleaning


```python
merged_1['Year'].min(), merged_1['Year'].max()
movies[movies['title'].str.contains('1000')]
movies[movies['title'].str.contains('9012')]
merged_1[merged_1['Year']==1000]
merged_1[merged_1['Year']==9012]
```




    (1000.0, 9012.0)






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
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6191</th>
      <td>6290</td>
      <td>House of 1000 Corpses (2003)</td>
      <td>Horror</td>
    </tr>
    <tr>
      <th>7695</th>
      <td>8198</td>
      <td>1000 Eyes of Dr. Mabuse, The (Die 1000 Augen d...</td>
      <td>Crime|Horror|Mystery|Thriller</td>
    </tr>
    <tr>
      <th>22287</th>
      <td>107155</td>
      <td>Captive Women (1000 Years from Now) (3000 A.D....</td>
      <td>Sci-Fi</td>
    </tr>
    <tr>
      <th>26429</th>
      <td>126999</td>
      <td>1000 Journals (2007)</td>
      <td>(no genres listed)</td>
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
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18578</th>
      <td>92477</td>
      <td>Yes: 9012 Live (1985)</td>
      <td>Documentary|Musical</td>
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
      <th>movieId</th>
      <th>Score</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6191</th>
      <td>6290</td>
      <td>2.855172</td>
      <td>870</td>
      <td>2007-08-23</td>
      <td>House of 1000 Corpses</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>7695</th>
      <td>8198</td>
      <td>3.398438</td>
      <td>64</td>
      <td>2008-06-21</td>
      <td>1000 Eyes of Dr. Mabuse, The</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>22185</th>
      <td>107155</td>
      <td>0.500000</td>
      <td>1</td>
      <td>2014-04-13</td>
      <td>Captive Women</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>25962</th>
      <td>126999</td>
      <td>2.000000</td>
      <td>1</td>
      <td>2015-01-30</td>
      <td>1000 Journals</td>
      <td>1000.0</td>
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
      <th>movieId</th>
      <th>Score</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18533</th>
      <td>92477</td>
      <td>1.5</td>
      <td>1</td>
      <td>2012-01-22</td>
      <td>Yes: 9012 Live</td>
      <td>9012.0</td>
    </tr>
  </tbody>
</table>
</div>



I guess I could fiddle with the regex more but I'd rather just manually assign these and move on. I need to find the release years for the movie titles that were cut off first, and then find the correct index by the movieId in the merged dataframe. It seems like movie with Id 6290 wasn't actually misassigned since its year doesn't equal 1000 in the merged table. 


```python
print("Movie row number 7695, movieId 8198:", movies.iloc[7695, 1])
print("Movie row number 22287, movieId 107155:", movies.iloc[22287, 1])

# fixing the year = 1000 entry
merged_1[merged_1['movieId'] == 8198]
merged_1.iloc[7695, 5] = 1960

merged_1[merged_1['movieId'] == 107155]
merged_1.iloc[22185, 5] = 1960

merged_1[merged_1['movieId'] == 126999]
merged_1.iloc[25962, 5] = 2007

# Fixing the year = 9012 entry
merged_1[merged_1['movieId'] == 92477]
merged_1.iloc[18533, 5] = 1985
```

    Movie row number 7695, movieId 8198: 1000 Eyes of Dr. Mabuse, The (Die 1000 Augen des Dr. Mabuse) (1960)
    Movie row number 22287, movieId 107155: Captive Women (1000 Years from Now) (3000 A.D.) (1952)





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
      <th>movieId</th>
      <th>Score</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7695</th>
      <td>8198</td>
      <td>3.398438</td>
      <td>64</td>
      <td>2008-06-21</td>
      <td>1000 Eyes of Dr. Mabuse, The</td>
      <td>1000.0</td>
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
      <th>movieId</th>
      <th>Score</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22185</th>
      <td>107155</td>
      <td>0.5</td>
      <td>1</td>
      <td>2014-04-13</td>
      <td>Captive Women</td>
      <td>1000.0</td>
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
      <th>movieId</th>
      <th>Score</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25962</th>
      <td>126999</td>
      <td>2.0</td>
      <td>1</td>
      <td>2015-01-30</td>
      <td>1000 Journals</td>
      <td>1000.0</td>
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
      <th>movieId</th>
      <th>Score</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18533</th>
      <td>92477</td>
      <td>1.5</td>
      <td>1</td>
      <td>2012-01-22</td>
      <td>Yes: 9012 Live</td>
      <td>9012.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_1['Year'].min(), merged_1['Year'].max()
```




    (1000.0, 9000.0)



So at this point, I want to just find all the values from before 1900 and after 2018. Based on this the regex matching needs a bit of work to accurately grab values. Since I did want to focus more on machine learning rather than string manipulation for now I'll just drop these rows, since they only represent a tiny, tiny subset of data (I have 27 thousand rows)


```python
cond_1 = merged_1['Year'] > 2016
cond_2 = merged_1['Year'] < 1900
merged_1[cond_1 | cond_2]

len(merged_1[cond_1 | cond_2])
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
      <th>movieId</th>
      <th>Score</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>662</th>
      <td>671</td>
      <td>3.676938</td>
      <td>6361</td>
      <td>2002-04-07</td>
      <td>Mystery Science Theater 3000: The Movie</td>
      <td>3000.0</td>
    </tr>
    <tr>
      <th>1388</th>
      <td>1422</td>
      <td>3.058688</td>
      <td>2820</td>
      <td>2001-09-22</td>
      <td>Murder at 1600</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>2223</th>
      <td>2308</td>
      <td>2.800000</td>
      <td>35</td>
      <td>2004-01-05</td>
      <td>Detroit 9000</td>
      <td>9000.0</td>
    </tr>
    <tr>
      <th>4065</th>
      <td>4159</td>
      <td>2.741048</td>
      <td>1508</td>
      <td>2005-07-06</td>
      <td>3000 Miles to Graceland</td>
      <td>3000.0</td>
    </tr>
    <tr>
      <th>4216</th>
      <td>4311</td>
      <td>1.968750</td>
      <td>16</td>
      <td>2005-11-21</td>
      <td>Bloody Angels</td>
      <td>1732.0</td>
    </tr>
    <tr>
      <th>5213</th>
      <td>5310</td>
      <td>2.311798</td>
      <td>356</td>
      <td>2004-05-23</td>
      <td>Transylvania 6-5000</td>
      <td>5000.0</td>
    </tr>
    <tr>
      <th>5375</th>
      <td>5472</td>
      <td>3.452809</td>
      <td>445</td>
      <td>2006-01-24</td>
      <td>1776</td>
      <td>1776.0</td>
    </tr>
    <tr>
      <th>6191</th>
      <td>6290</td>
      <td>2.855172</td>
      <td>870</td>
      <td>2007-08-23</td>
      <td>House of 1000 Corpses</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>6535</th>
      <td>6645</td>
      <td>3.454427</td>
      <td>1152</td>
      <td>2007-08-05</td>
      <td>THX 1138</td>
      <td>1138.0</td>
    </tr>
    <tr>
      <th>8181</th>
      <td>8864</td>
      <td>2.640323</td>
      <td>310</td>
      <td>2007-03-22</td>
      <td>Mr. 3000</td>
      <td>3000.0</td>
    </tr>
    <tr>
      <th>8222</th>
      <td>8905</td>
      <td>3.084810</td>
      <td>395</td>
      <td>2008-03-19</td>
      <td>1492: Conquest of Paradise</td>
      <td>1492.0</td>
    </tr>
    <tr>
      <th>9252</th>
      <td>27266</td>
      <td>3.673495</td>
      <td>1196</td>
      <td>2008-11-09</td>
      <td>2046</td>
      <td>2046.0</td>
    </tr>
    <tr>
      <th>9490</th>
      <td>27800</td>
      <td>3.762500</td>
      <td>280</td>
      <td>2011-02-05</td>
      <td>Interstella 5555: The 5tory of the 5ecret 5tar...</td>
      <td>5555.0</td>
    </tr>
    <tr>
      <th>11954</th>
      <td>53953</td>
      <td>3.290909</td>
      <td>2365</td>
      <td>2010-04-05</td>
      <td>1408</td>
      <td>1408.0</td>
    </tr>
    <tr>
      <th>13737</th>
      <td>68874</td>
      <td>3.542857</td>
      <td>35</td>
      <td>2011-07-11</td>
      <td>Jeanne Dielman, 23 Quai du Commerce, 1080 Brux...</td>
      <td>1080.0</td>
    </tr>
    <tr>
      <th>14749</th>
      <td>73862</td>
      <td>3.722222</td>
      <td>9</td>
      <td>2011-08-20</td>
      <td>Note by Note: The Making of Steinway L1037</td>
      <td>1037.0</td>
    </tr>
    <tr>
      <th>14859</th>
      <td>74491</td>
      <td>3.461538</td>
      <td>13</td>
      <td>2011-08-30</td>
      <td>1066</td>
      <td>1066.0</td>
    </tr>
    <tr>
      <th>14903</th>
      <td>74706</td>
      <td>3.571429</td>
      <td>7</td>
      <td>2012-02-23</td>
      <td>Commune, La</td>
      <td>1871.0</td>
    </tr>
    <tr>
      <th>16077</th>
      <td>81453</td>
      <td>3.000000</td>
      <td>2</td>
      <td>2010-10-31</td>
      <td>Dial 1119</td>
      <td>1119.0</td>
    </tr>
    <tr>
      <th>16289</th>
      <td>82337</td>
      <td>3.750000</td>
      <td>10</td>
      <td>2013-04-06</td>
      <td>Four Heads Are Better Than One</td>
      <td>1898.0</td>
    </tr>
    <tr>
      <th>16294</th>
      <td>82362</td>
      <td>3.625000</td>
      <td>4</td>
      <td>2011-07-24</td>
      <td>Pyramid of Triboulet, The</td>
      <td>1899.0</td>
    </tr>
    <tr>
      <th>16697</th>
      <td>84551</td>
      <td>3.125000</td>
      <td>4</td>
      <td>2011-07-17</td>
      <td>44500 Max</td>
      <td>4450.0</td>
    </tr>
    <tr>
      <th>17086</th>
      <td>86637</td>
      <td>2.250000</td>
      <td>2</td>
      <td>2011-12-24</td>
      <td>1612: Khroniki smutnogo vremeni</td>
      <td>1612.0</td>
    </tr>
    <tr>
      <th>17597</th>
      <td>88674</td>
      <td>2.714286</td>
      <td>7</td>
      <td>2011-10-13</td>
      <td>Edison Kinetoscopic Record of a Sneeze</td>
      <td>1894.0</td>
    </tr>
    <tr>
      <th>18004</th>
      <td>90460</td>
      <td>2.750000</td>
      <td>8</td>
      <td>2012-11-21</td>
      <td>2019: After the Fall of New York</td>
      <td>2019.0</td>
    </tr>
    <tr>
      <th>18242</th>
      <td>91421</td>
      <td>2.333333</td>
      <td>3</td>
      <td>2012-07-21</td>
      <td>Red Line 7000</td>
      <td>7000.0</td>
    </tr>
    <tr>
      <th>18934</th>
      <td>94431</td>
      <td>5.000000</td>
      <td>1</td>
      <td>2012-05-09</td>
      <td>Ella Lola, a la Trilby</td>
      <td>1898.0</td>
    </tr>
    <tr>
      <th>18964</th>
      <td>94657</td>
      <td>5.000000</td>
      <td>1</td>
      <td>2012-05-21</td>
      <td>Turkish Dance, Ella Lola</td>
      <td>1898.0</td>
    </tr>
    <tr>
      <th>19032</th>
      <td>94951</td>
      <td>3.428571</td>
      <td>7</td>
      <td>2013-02-24</td>
      <td>Dickson Experimental Sound Film</td>
      <td>1894.0</td>
    </tr>
    <tr>
      <th>19160</th>
      <td>95541</td>
      <td>3.375000</td>
      <td>4</td>
      <td>2013-03-02</td>
      <td>Blacksmith Scene</td>
      <td>1893.0</td>
    </tr>
    <tr>
      <th>19265</th>
      <td>96009</td>
      <td>2.928571</td>
      <td>7</td>
      <td>2013-01-14</td>
      <td>Kiss, The</td>
      <td>1896.0</td>
    </tr>
    <tr>
      <th>19601</th>
      <td>97242</td>
      <td>3.166667</td>
      <td>6</td>
      <td>2013-09-27</td>
      <td>Daleks' Invasion Earth: 2150 A.D.</td>
      <td>2150.0</td>
    </tr>
    <tr>
      <th>19785</th>
      <td>98019</td>
      <td>3.205882</td>
      <td>17</td>
      <td>2014-01-03</td>
      <td>Vexille</td>
      <td>2077.0</td>
    </tr>
    <tr>
      <th>20023</th>
      <td>98981</td>
      <td>3.437500</td>
      <td>16</td>
      <td>2013-10-05</td>
      <td>Arrival of a Train, The</td>
      <td>1896.0</td>
    </tr>
    <tr>
      <th>20971</th>
      <td>102762</td>
      <td>3.500000</td>
      <td>3</td>
      <td>2013-07-12</td>
      <td>My Wrongs 8245-8249 and 117</td>
      <td>8245.0</td>
    </tr>
    <tr>
      <th>20996</th>
      <td>102856</td>
      <td>3.333333</td>
      <td>6</td>
      <td>2014-06-04</td>
      <td>3096 Days</td>
      <td>3096.0</td>
    </tr>
    <tr>
      <th>21082</th>
      <td>103130</td>
      <td>4.000000</td>
      <td>2</td>
      <td>2014-03-10</td>
      <td>AM1200</td>
      <td>1200.0</td>
    </tr>
    <tr>
      <th>21430</th>
      <td>104370</td>
      <td>3.000000</td>
      <td>1</td>
      <td>2013-10-25</td>
      <td>Wartorn: 1861-2010</td>
      <td>1861.0</td>
    </tr>
    <tr>
      <th>21543</th>
      <td>104798</td>
      <td>3.500000</td>
      <td>2</td>
      <td>2013-12-13</td>
      <td>6954 Kilometriä Kotiin</td>
      <td>6954.0</td>
    </tr>
    <tr>
      <th>22630</th>
      <td>108862</td>
      <td>2.000000</td>
      <td>1</td>
      <td>2014-02-05</td>
      <td>New Gladiators</td>
      <td>2072.0</td>
    </tr>
    <tr>
      <th>22741</th>
      <td>109277</td>
      <td>3.375000</td>
      <td>4</td>
      <td>2014-11-20</td>
      <td>Love Story 2050</td>
      <td>2050.0</td>
    </tr>
    <tr>
      <th>22804</th>
      <td>109514</td>
      <td>3.000000</td>
      <td>2</td>
      <td>2014-03-03</td>
      <td>Apartment 1303</td>
      <td>1303.0</td>
    </tr>
    <tr>
      <th>22805</th>
      <td>109516</td>
      <td>1.333333</td>
      <td>3</td>
      <td>2014-11-11</td>
      <td>Apartment 1303 3D</td>
      <td>1303.0</td>
    </tr>
    <tr>
      <th>23160</th>
      <td>110867</td>
      <td>3.500000</td>
      <td>2</td>
      <td>2014-11-09</td>
      <td>Conquest 1453</td>
      <td>1453.0</td>
    </tr>
    <tr>
      <th>23358</th>
      <td>111856</td>
      <td>2.833333</td>
      <td>3</td>
      <td>2014-10-25</td>
      <td>7500</td>
      <td>7500.0</td>
    </tr>
    <tr>
      <th>23633</th>
      <td>113048</td>
      <td>2.250000</td>
      <td>2</td>
      <td>2014-10-18</td>
      <td>Tables Turned on the Gardener</td>
      <td>1895.0</td>
    </tr>
    <tr>
      <th>23653</th>
      <td>113143</td>
      <td>1.000000</td>
      <td>1</td>
      <td>2014-12-23</td>
      <td>America 3000</td>
      <td>3000.0</td>
    </tr>
    <tr>
      <th>23847</th>
      <td>113968</td>
      <td>3.666667</td>
      <td>3</td>
      <td>2014-11-16</td>
      <td>2081</td>
      <td>2081.0</td>
    </tr>
    <tr>
      <th>24024</th>
      <td>114721</td>
      <td>2.944444</td>
      <td>9</td>
      <td>2014-11-23</td>
      <td>Bugs Bunny's 3rd Movie: 1001 Rabbit Tales</td>
      <td>1001.0</td>
    </tr>
    <tr>
      <th>24330</th>
      <td>116157</td>
      <td>3.750000</td>
      <td>2</td>
      <td>2014-11-12</td>
      <td>Electronic Labyrinth THX 1138 4EB</td>
      <td>1138.0</td>
    </tr>
    <tr>
      <th>25193</th>
      <td>120869</td>
      <td>4.000000</td>
      <td>1</td>
      <td>2015-01-05</td>
      <td>Employees Leaving the Lumière Factory</td>
      <td>1895.0</td>
    </tr>
    <tr>
      <th>25724</th>
      <td>125978</td>
      <td>2.500000</td>
      <td>1</td>
      <td>2015-01-22</td>
      <td>Santa Claus</td>
      <td>1898.0</td>
    </tr>
    <tr>
      <th>25812</th>
      <td>126164</td>
      <td>2.000000</td>
      <td>1</td>
      <td>2015-01-22</td>
      <td>1001 Nights</td>
      <td>1001.0</td>
    </tr>
    <tr>
      <th>26481</th>
      <td>129849</td>
      <td>3.000000</td>
      <td>1</td>
      <td>2015-03-12</td>
      <td>Old Man Drinking a Glass of Beer</td>
      <td>1898.0</td>
    </tr>
    <tr>
      <th>26482</th>
      <td>129851</td>
      <td>3.000000</td>
      <td>1</td>
      <td>2015-03-12</td>
      <td>Dickson Greeting</td>
      <td>1891.0</td>
    </tr>
  </tbody>
</table>
</div>






    55




```python
# drop buggy rows
merged_1 = merged_1[~(cond_1 | cond_2)]
cond_1 = merged_1['Year'] > 2016
cond_2 = merged_1['Year'] < 1900

merged_1[cond_1 | cond_2]
ggplot() + geom_histogram(aes('Year'), data = merged_1)
sns.heatmap(var_corr)
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
      <th>movieId</th>
      <th>Score</th>
      <th>Ratings</th>
      <th>Date</th>
      <th>Name</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/plotnine/stats/stat_bin.py:93: UserWarning: 'stat_bin()' using 'bins = 56'. Pick better value with 'binwidth'.
      warn(msg.format(params['bins']))
    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/plotnine/layer.py:360: UserWarning: stat_bin : Removed 19 rows containing non-finite values.
      data = self.stat.compute_layer(data, params, layout)



![png](7_ML_Clust_files/7_ML_Clust_31_2.png)





    <ggplot: (-9223363306851432774)>






    <matplotlib.axes._subplots.AxesSubplot at 0x7f09cc69b518>




![png](7_ML_Clust_files/7_ML_Clust_31_5.png)


# Returning to visualization

Compare the heatmaps before and after removing the outlier years, and get a new scaled version 


```python
scaled_1 = merged_1.copy()
del scaled_1['Name']
del scaled_1['Date']
scaled_1 = scaled_1.merge(ratings[['movieId', 'timestamp']].groupby('movieId').mean().astype(int), on = 'movieId', how='inner') 
del scaled_1['movieId']
scaled_1 = scaled_1.rename(columns={scaled_1.columns[3]: "Date"})
scaled_1['Year'] = pd.to_numeric(scaled_1['Year'])
var_corr = scaled_1.corr()
normalized = StandardScaler().fit_transform(scaled_1)
sns.heatmap(var_corr)
```

    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/sklearn/preprocessing/data.py:645: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.
      return self.partial_fit(X, y)
    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/sklearn/base.py:464: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.
      return self.fit(X, **fit_params).transform(X)





    <matplotlib.axes._subplots.AxesSubplot at 0x7f09c037e630>




![png](7_ML_Clust_files/7_ML_Clust_33_2.png)


So it seems like the outliers and misidentified values had some influence on the Year correlation with other variables. 

# Data Manipulations - Binning

Here, I want to bin the release year into decade buckets so that I can use that as a factor level to color the plots. 


```python
bins =  ["{0}s".format(decades) for decades in range(1900, 2020, 10)]
num_bins = len(bins)
scaled_1['decade'] = pd.cut(x=scaled_1['Year'], bins=num_bins, labels=bins)
scaled_1.head()
scaled_1.tail()
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
      <th>Score</th>
      <th>Ratings</th>
      <th>Year</th>
      <th>Date</th>
      <th>decade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.921240</td>
      <td>49695</td>
      <td>1995.0</td>
      <td>1052654098</td>
      <td>1990s</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.211977</td>
      <td>22243</td>
      <td>1995.0</td>
      <td>1037616295</td>
      <td>1990s</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.151040</td>
      <td>12735</td>
      <td>1995.0</td>
      <td>959648019</td>
      <td>1990s</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.861393</td>
      <td>2756</td>
      <td>1995.0</td>
      <td>924214411</td>
      <td>1990s</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.064592</td>
      <td>12161</td>
      <td>1995.0</td>
      <td>962016085</td>
      <td>1990s</td>
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
      <th>Score</th>
      <th>Ratings</th>
      <th>Year</th>
      <th>Date</th>
      <th>decade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26684</th>
      <td>4.0</td>
      <td>1</td>
      <td>2007.0</td>
      <td>1427743979</td>
      <td>2010s</td>
    </tr>
    <tr>
      <th>26685</th>
      <td>4.0</td>
      <td>1</td>
      <td>2002.0</td>
      <td>1427744888</td>
      <td>2000s</td>
    </tr>
    <tr>
      <th>26686</th>
      <td>2.5</td>
      <td>1</td>
      <td>2014.0</td>
      <td>1427745392</td>
      <td>2010s</td>
    </tr>
    <tr>
      <th>26687</th>
      <td>3.0</td>
      <td>1</td>
      <td>2001.0</td>
      <td>1427745466</td>
      <td>2000s</td>
    </tr>
    <tr>
      <th>26688</th>
      <td>4.0</td>
      <td>1</td>
      <td>2014.0</td>
      <td>1427747966</td>
      <td>2010s</td>
    </tr>
  </tbody>
</table>
</div>



## Binning results 

Plot all the data, divided by decade of release. 


```python
# Drop na year values
scaled_1.dropna(inplace = True)
scaled_1['log_Ratings'] = np.log(scaled_1['Ratings'])
from plotnine import options as ops
from plotnine import facet_wrap
ops.figure_size = (10.4, 6.8)
ggplot(scaled_1, aes('log_Ratings', 'Score', color = 'Year')) + geom_point() + stat_smooth() + facet_wrap('~decade')
```

    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/numpy/core/fromnumeric.py:2389: FutureWarning: Method .ptp is deprecated and will be removed in a future version. Use numpy.ptp instead.
      return ptp(axis=axis, out=out, **kwargs)



![png](7_ML_Clust_files/7_ML_Clust_37_1.png)





    <ggplot: (8729992780783)>



# Modeling

## Exploratory elbow plot 

I generate an elbow plot to see how many clusters might be a good value. 


```python
%%capture
X = StandardScaler().fit_transform(scaled_1[['Score', 'Ratings', 'Date']])
error = []

for k in range(2, 20):
    kmeans_model = KMeans(n_clusters = k);
    kmeans_model.fit(X);
    error.append(kmeans_model.inertia_);
```


```python
error = pd.Series(error)
elbow = pd.DataFrame({'Clusters': list(range(2,20)), 'Error' : error} ) 
elbow
from plotnine import geom_line 
from plotnine import scale_x_continuous
ggplot(elbow, aes(x = 'Clusters', y = 'Error')) + geom_line() + scale_x_continuous(breaks = list(range(2,20)))
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
      <th>Clusters</th>
      <th>Error</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>56811.269952</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>40924.920341</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>27773.559122</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>23374.464711</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>19266.801939</td>
    </tr>
    <tr>
      <th>5</th>
      <td>7</td>
      <td>16360.115736</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8</td>
      <td>14559.723656</td>
    </tr>
    <tr>
      <th>7</th>
      <td>9</td>
      <td>13013.149628</td>
    </tr>
    <tr>
      <th>8</th>
      <td>10</td>
      <td>11561.152691</td>
    </tr>
    <tr>
      <th>9</th>
      <td>11</td>
      <td>10591.417401</td>
    </tr>
    <tr>
      <th>10</th>
      <td>12</td>
      <td>9788.753401</td>
    </tr>
    <tr>
      <th>11</th>
      <td>13</td>
      <td>8926.882872</td>
    </tr>
    <tr>
      <th>12</th>
      <td>14</td>
      <td>8267.855712</td>
    </tr>
    <tr>
      <th>13</th>
      <td>15</td>
      <td>7703.456423</td>
    </tr>
    <tr>
      <th>14</th>
      <td>16</td>
      <td>7303.171993</td>
    </tr>
    <tr>
      <th>15</th>
      <td>17</td>
      <td>6815.445542</td>
    </tr>
    <tr>
      <th>16</th>
      <td>18</td>
      <td>6496.663156</td>
    </tr>
    <tr>
      <th>17</th>
      <td>19</td>
      <td>6190.330783</td>
    </tr>
  </tbody>
</table>
</div>




![png](7_ML_Clust_files/7_ML_Clust_40_1.png)





    <ggplot: (-9223363306868393342)>



## Elbow plot - defining the bend mathematically 

In most cases you would just eyeball the curve to see where the dropoff starts to plateau. But since we are using code and there are builtin functions we can easily grab the max of the second derivative as the point where the elbow plot is plateauing most quickly 


```python
np.diff(elbow['Error'])
np.diff(np.diff(elbow['Error']))
np.diff(np.diff(elbow['Error'])).max()
```




    array([-15886.34961051, -13151.36121902,  -4399.09441152,  -4107.66277137,
            -2906.68620346,  -1800.3920797 ,  -1546.5740278 ,  -1451.99693761,
             -969.73528993,   -802.66399959,   -861.87052968,   -659.02715945,
             -564.39928912,   -400.28443027,   -487.72645071,   -318.78238598,
             -306.33237349])






    array([2734.98839149, 8752.2668075 ,  291.43164015, 1200.97656791,
           1106.29412376,  253.8180519 ,   94.57709019,  482.26164768,
            167.07129033,  -59.20653009,  202.84337023,   94.62787033,
            164.11485886,  -87.44202044,  168.94406473,   12.45001249])






    8752.266807496679



For added confirmation we can plot the first (blue line) and second (red line) derivatives. Indeed, the max of the 2nd derivative is at k = 5. 


```python
diff_1 = [0]
elbow['First Derivative'] = np.append(np.array([0]), np.diff(elbow['Error']))
elbow['Second Derivative'] = np.append(np.array([0, 0]), np.diff(np.diff(elbow['Error'])))
elbow_d = ggplot(elbow, aes(x = 'Clusters', y = 'Error')) + geom_line() + scale_x_continuous(breaks = list(range(2,20))) 
elbow_d + geom_line(aes(x = 'Clusters', y = 'First Derivative'), color = 'blue') + geom_line(aes(x = 'Clusters', y = 'Second Derivative'), color = 'red')
```


![png](7_ML_Clust_files/7_ML_Clust_44_0.png)





    <ggplot: (8729990934669)>



# Final cluster and visualization

From this plot we can see that the bend of the elbow plot is mathematically at k = 5 clusters. We can finally move on to the last part, return to using the KMeans model to generate label assignments, and color our data by the different clusters. 


```python
kmeans_model = KMeans(n_clusters = 5);
kmeans_model.fit(X);
scaled_1['Cluster'] = kmeans_model.fit_predict(X)
ops.figure_size = (10.4, 6.8)
ggplot(scaled_1, aes('log_Ratings', 'Score', color = 'Cluster')) + geom_point() + facet_wrap('~decade')

ggplot(scaled_1, aes('log_Ratings', 'Year',  color = 'Cluster')) + geom_point() + facet_wrap('~decade')
```




    KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
        n_clusters=5, n_init=10, n_jobs=None, precompute_distances='auto',
        random_state=None, tol=0.0001, verbose=0)




![png](7_ML_Clust_files/7_ML_Clust_46_1.png)





    <ggplot: (-9223363306863402254)>




![png](7_ML_Clust_files/7_ML_Clust_46_3.png)





    <ggplot: (8729991373488)>



Since I've faceted the graphs by decade of the movie release year, these plots are slices of a 3d plot. If we imagine that the Ratings and Score are the x and y dimensions when looking straight down, then the Year is the vertical dimensions. Here, I also I give a side view of the decade slices on the Ratings side. Finally, how long did this entire file take to run?


```python
time_stop = datetime.datetime.now()

time_stop - time_start
```




    datetime.timedelta(seconds=46, microseconds=211675)


