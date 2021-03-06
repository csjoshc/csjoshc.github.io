
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
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import os, sys
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python



```python
os.chdir(sys.path[0]) # Change dir to the folder this .ipynb file is in
print(os.listdir('../../../../data/w4pd'))
movies = pd.read_csv('../../../../data/w4pd/movies.csv')
tags = pd.read_csv('../../../../data/w4pd/tags.csv')
ratings = pd.read_csv('../../../../data/w4pd/ratings.csv')
```

    ['genome-scores.csv', 'genome-tags.csv', 'Icon\r', 'links.csv', 'movies.csv', 'ratings.csv', 'README.txt', 'tags.csv']


# Manipulating Data


```python
ratings.head(5)
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



## `df[['col1', 'col2']].groupby('col1')` - Aggregating and Grouping 
It makes sense to calculate different aggregate stats for different groupings. `groupby` doesn't do any aggregate calculations by default - it just reorders the df so that the same values in the grouping column are all consecutive. You can also use .count() on a grouping. 


```python
user_ratings = ratings[['userId', 'rating']].groupby('userId').mean() 
user_ratings.head()
movie_ratings = ratings[['movieId', 'rating']].groupby('movieId').mean() 
movie_ratings.head()
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
      <th>rating</th>
    </tr>
    <tr>
      <th>userId</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>3.742857</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.122995</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.571429</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4.272727</td>
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
      <th>rating</th>
    </tr>
    <tr>
      <th>movieId</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>3.921240</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.211977</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.151040</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.861393</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3.064592</td>
    </tr>
  </tbody>
</table>
</div>



## Plotting aggregated data
Generate a histogram of movie ratings (so group by the ratings column). 


```python
ratings_hist = ratings[['movieId', 'rating']].groupby('rating').count()
print(ratings_hist)

# Now we plot

import matplotlib

ratings_hist.plot(kind = "bar", figsize = (5, 5)) 

plt.show() 
```

            movieId
    rating         
    0.5      239125
    1.0      680732
    1.5      279252
    2.0     1430997
    2.5      883398
    3.0     4291193
    3.5     2200156
    4.0     5561926
    4.5     1534824
    5.0     2898660





    <matplotlib.axes._subplots.AxesSubplot at 0x7f642ce23f98>




![png](4_Pandas4_files/4_Pandas4_8_2.png)


## Filtering
Encode a filter that saves the indices of a dataframe (for which a condition is true), and then apply the filter as a mask to extract the desired values. (This can also apply to 3D image matrices).

Below - find the most active raters (count of userId groupings of the ratings df). Looking at the mean and standard dev set the cutoff at 2000! movie ratings. 



```python
active_raters = ratings[['userId', 'rating']].groupby('userId').count()
print(active_raters.mean(), active_raters.std())
highly_active_raters = active_raters[active_raters['rating'] > 2000]
print(highly_active_raters.shape[0])
```

    rating    144.41353
    dtype: float64 rating    230.267257
    dtype: float64
    255


### Filtering based on string matching
Using the movies dataframe, filter for movies with Animation as a genre:


```python
movies.head()
is_anime = movies['genres'].str.contains('Ani*') 
the_anime = movies[is_anime]
the_anime.shape[0]
the_anime.head()
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






    1027






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
      <th>12</th>
      <td>13</td>
      <td>Balto (1995)</td>
      <td>Adventure|Animation|Children</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>Pocahontas (1995)</td>
      <td>Animation|Children|Drama|Musical|Romance</td>
    </tr>
    <tr>
      <th>236</th>
      <td>239</td>
      <td>Goofy Movie, A (1995)</td>
      <td>Animation|Children|Comedy|Romance</td>
    </tr>
    <tr>
      <th>241</th>
      <td>244</td>
      <td>Gumby: The Movie (1995)</td>
      <td>Animation|Children</td>
    </tr>
  </tbody>
</table>
</div>



# Joining Data
Combining data from multiple dataframes or sources. 

## `pd.concat([df1, df2])` - Stack dataframes
The stacking is not really ideal in this scenario - it would be better to stack df's that have matched columns and data types.


```python
stack_1 = pd.concat([tags.head(), movies.head()])
stack_1
```

    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
    of pandas will change to not sort by default.
    
    To accept the future behavior, pass 'sort=False'.
    
    To retain the current behavior and silence the warning, pass 'sort=True'.
    
      """Entry point for launching an IPython kernel.





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
      <th>genres</th>
      <th>movieId</th>
      <th>tag</th>
      <th>timestamp</th>
      <th>title</th>
      <th>userId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>4141</td>
      <td>Mark Waters</td>
      <td>1.240597e+09</td>
      <td>NaN</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>208</td>
      <td>dark hero</td>
      <td>1.368150e+09</td>
      <td>NaN</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>353</td>
      <td>dark hero</td>
      <td>1.368150e+09</td>
      <td>NaN</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>521</td>
      <td>noir thriller</td>
      <td>1.368150e+09</td>
      <td>NaN</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>592</td>
      <td>dark hero</td>
      <td>1.368150e+09</td>
      <td>NaN</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Toy Story (1995)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Adventure|Children|Fantasy</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Jumanji (1995)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Comedy|Romance</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Grumpier Old Men (1995)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Comedy|Drama|Romance</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Waiting to Exhale (1995)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Comedy</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## `df1.append(df2)` - Stack dataframes
This gives the same results as using stack. 


```python
append_1 = tags.head().append(movies.head())
append_1 
```

    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/pandas/core/frame.py:6692: FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
    of pandas will change to not sort by default.
    
    To accept the future behavior, pass 'sort=False'.
    
    To retain the current behavior and silence the warning, pass 'sort=True'.
    
      sort=sort)





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
      <th>genres</th>
      <th>movieId</th>
      <th>tag</th>
      <th>timestamp</th>
      <th>title</th>
      <th>userId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>4141</td>
      <td>Mark Waters</td>
      <td>1.240597e+09</td>
      <td>NaN</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>208</td>
      <td>dark hero</td>
      <td>1.368150e+09</td>
      <td>NaN</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>353</td>
      <td>dark hero</td>
      <td>1.368150e+09</td>
      <td>NaN</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>521</td>
      <td>noir thriller</td>
      <td>1.368150e+09</td>
      <td>NaN</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>592</td>
      <td>dark hero</td>
      <td>1.368150e+09</td>
      <td>NaN</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Toy Story (1995)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Adventure|Children|Fantasy</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Jumanji (1995)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Comedy|Romance</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Grumpier Old Men (1995)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Comedy|Drama|Romance</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Waiting to Exhale (1995)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Comedy</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## **Inner join** - using`*pd.concat` with `axis = 1, join = "inner"`
This is NOT the same as an INNER JOIN ON tb1.field1 = tbl2.field1 as it would be in SQL
As a result, this isn't particularly useful since you're not matching as you combine data. 


```python
joined = pd.concat([tags.head(), movies.head()], axis = 1, join = "inner")
joined 
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
      <th>userId</th>
      <th>movieId</th>
      <th>tag</th>
      <th>timestamp</th>
      <th>movieId</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>4141</td>
      <td>Mark Waters</td>
      <td>1240597180</td>
      <td>1</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>65</td>
      <td>208</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>2</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children|Fantasy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65</td>
      <td>353</td>
      <td>dark hero</td>
      <td>1368150079</td>
      <td>3</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>65</td>
      <td>521</td>
      <td>noir thriller</td>
      <td>1368149983</td>
      <td>4</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Comedy|Drama|Romance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>65</td>
      <td>592</td>
      <td>dark hero</td>
      <td>1368150078</td>
      <td>5</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
    </tr>
  </tbody>
</table>
</div>



## `df1.merge(df2, on = 'col1', how='inner')` - The actual inner join
The **actual** INNER JOIN

Below, inner jon the aggregated mean movie_ratings and a new movie_counts (the number of ratings per movie). Then inner join again to `movies` dataframe.


```python
movie_counts = ratings[['movieId', 'rating']].groupby('movieId').count() 
movie_ratings.head()
movie_counts.head()
merged_1 = movie_ratings.merge(movie_counts, on = 'movieId', how='inner')
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
      <th>rating</th>
    </tr>
    <tr>
      <th>movieId</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>3.921240</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.211977</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.151040</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.861393</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3.064592</td>
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
      <th>rating</th>
    </tr>
    <tr>
      <th>movieId</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>49695</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22243</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12735</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2756</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12161</td>
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
      <th>rating_x</th>
      <th>rating_y</th>
    </tr>
    <tr>
      <th>movieId</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>3.921240</td>
      <td>49695</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.211977</td>
      <td>22243</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.151040</td>
      <td>12735</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.861393</td>
      <td>2756</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3.064592</td>
      <td>12161</td>
    </tr>
  </tbody>
</table>
</div>



## Chaining together merges
Chained merging on a merged dataframe without a new object is possible, but becomes unreadable after a few in a row:


```python
merged_2 = merged_1.merge(movies, on = 'movieId', how='inner')
merged_3 = movie_ratings.merge(movie_counts, on = 'movieId', how='inner').merge(movies, on = 'movieId', how='inner')
merged_2.head() 
merged_3.head()
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
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3.921240</td>
      <td>49695</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3.211977</td>
      <td>22243</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children|Fantasy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3.151040</td>
      <td>12735</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2.861393</td>
      <td>2756</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Comedy|Drama|Romance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3.064592</td>
      <td>12161</td>
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
      <th>movieId</th>
      <th>rating_x</th>
      <th>rating_y</th>
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3.921240</td>
      <td>49695</td>
      <td>Toy Story (1995)</td>
      <td>Adventure|Animation|Children|Comedy|Fantasy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3.211977</td>
      <td>22243</td>
      <td>Jumanji (1995)</td>
      <td>Adventure|Children|Fantasy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3.151040</td>
      <td>12735</td>
      <td>Grumpier Old Men (1995)</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2.861393</td>
      <td>2756</td>
      <td>Waiting to Exhale (1995)</td>
      <td>Comedy|Drama|Romance</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3.064592</td>
      <td>12161</td>
      <td>Father of the Bride Part II (1995)</td>
      <td>Comedy</td>
    </tr>
  </tbody>
</table>
</div>



# Combining everything

After merging three dataframes with aggregated ratings and rating counts data, we can apply a filter - the `is_anime` which was a string filter, as well as a new filter for movies that were both highly rated (more than 4) and actively rated (more than 2000 ratings). 


```python
ani_summary = merged_3[is_anime & (merged_3['rating_x'] > 4) & (merged_3['rating_y'] > 2000)]
ani_summary
ani_summary.shape[0]
```

    /home/jcmint/anaconda3/envs/learningenv/lib/python3.7/site-packages/ipykernel_launcher.py:1: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
      """Entry point for launching an IPython kernel.





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
      <th>title</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>708</th>
      <td>720</td>
      <td>4.109473</td>
      <td>8171</td>
      <td>Wallace &amp; Gromit: The Best of Aardman Animatio...</td>
      <td>Adventure|Animation|Comedy</td>
    </tr>
    <tr>
      <th>732</th>
      <td>745</td>
      <td>4.167315</td>
      <td>12073</td>
      <td>Wallace &amp; Gromit: A Close Shave (1995)</td>
      <td>Animation|Children|Comedy</td>
    </tr>
    <tr>
      <th>1125</th>
      <td>1148</td>
      <td>4.181068</td>
      <td>15022</td>
      <td>Wallace &amp; Gromit: The Wrong Trousers (1993)</td>
      <td>Animation|Children|Comedy|Crime</td>
    </tr>
    <tr>
      <th>1197</th>
      <td>1223</td>
      <td>4.066765</td>
      <td>7781</td>
      <td>Grand Day Out with Wallace and Gromit, A (1989)</td>
      <td>Adventure|Animation|Children|Comedy|Sci-Fi</td>
    </tr>
    <tr>
      <th>2914</th>
      <td>3000</td>
      <td>4.096299</td>
      <td>9564</td>
      <td>Princess Mononoke (Mononoke-hime) (1997)</td>
      <td>Action|Adventure|Animation|Drama|Fantasy</td>
    </tr>
    <tr>
      <th>3340</th>
      <td>3429</td>
      <td>4.120696</td>
      <td>2585</td>
      <td>Creature Comforts (1989)</td>
      <td>Animation|Comedy</td>
    </tr>
    <tr>
      <th>5519</th>
      <td>5618</td>
      <td>4.203810</td>
      <td>13466</td>
      <td>Spirited Away (Sen to Chihiro no kamikakushi) ...</td>
      <td>Adventure|Animation|Fantasy</td>
    </tr>
    <tr>
      <th>5591</th>
      <td>5690</td>
      <td>4.089744</td>
      <td>3198</td>
      <td>Grave of the Fireflies (Hotaru no haka) (1988)</td>
      <td>Animation|Drama|War</td>
    </tr>
    <tr>
      <th>5872</th>
      <td>5971</td>
      <td>4.149481</td>
      <td>5489</td>
      <td>My Neighbor Totoro (Tonari no Totoro) (1988)</td>
      <td>Animation|Children|Drama|Fantasy</td>
    </tr>
    <tr>
      <th>6251</th>
      <td>6350</td>
      <td>4.061917</td>
      <td>3537</td>
      <td>Laputa: Castle in the Sky (Tenkû no shiro Rapy...</td>
      <td>Action|Adventure|Animation|Children|Fantasy|Sc...</td>
    </tr>
    <tr>
      <th>6987</th>
      <td>7099</td>
      <td>4.092082</td>
      <td>3334</td>
      <td>Nausicaä of the Valley of the Wind (Kaze no ta...</td>
      <td>Adventure|Animation|Drama|Fantasy|Sci-Fi</td>
    </tr>
  </tbody>
</table>
</div>






    11



In conclusion, it seems that the two big categories were Wallance & Gromit and Anime, which makes sense, although it misses some Pixar and Disney films which I would've expected to make the cut. 
