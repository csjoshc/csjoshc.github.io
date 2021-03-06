
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

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('fivethirtyeight')
```

    /home/jcmint/anaconda3/envs/learningenv/bin/python


# Decision Tree 

Needed to install scikit-learn package with conda. 


```python
# Import libraries for decision tree
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from random import randint
# Import Data
data = pd.read_csv('Week-7-MachineLearning/weather/daily_weather.csv')
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
      <td>0.0</td>
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
      <td>0.0</td>
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
      <td>0.0</td>
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
      <td>0.0</td>
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
      <td>8.9</td>
      <td>14730.0</td>
      <td>92.410000</td>
      <td>76.740000</td>
    </tr>
  </tbody>
</table>
</div>



## Cleaning Data

The tutorial wants to do a few things with the data

* drop 'number' column
* drop NA rows


```python
clean_data = data.copy()
clean_data[clean_data.isnull().any(axis = 1)].head()
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
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
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
      <td>0.0</td>
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
      <td>0.0</td>
      <td>0.0</td>
      <td>52.580000</td>
      <td>54.030000</td>
    </tr>
  </tbody>
</table>
</div>



I will drop these rows for now. However, that isn't the only thing you can do with them (you could use linear interpolation since they are numeric and this is time series data with evenly spaces intervals)


```python
del clean_data['number']
clean_data = clean_data.dropna()
```

## Prep data for analysis

* Bin humidity values into low (0) and high (1) to make it a binary classification problem and store in `high_humidity_label`
* store bin labels as `y`
* Store training variables names into `morning_features`, then store training data into `x` 
* split `x` and `y` into training and testing subsets, `x_train`, `x_test`, `y_train`, `y_test`


```python
clean_data['high_humidity_label'] = (clean_data['relative_humidity_3pm'] >= 25)*1
clean_data[['high_humidity_label','relative_humidity_3pm']].head(8)
y=clean_data[['high_humidity_label']].copy()
morning_features = ['air_pressure_9am','air_temp_9am','avg_wind_direction_9am','avg_wind_speed_9am',
        'max_wind_direction_9am','max_wind_speed_9am','rain_accumulation_9am',
        'rain_duration_9am']
x = clean_data[morning_features].copy()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=324).copy()
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
      <th>relative_humidity_3pm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>36.160000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>19.426597</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>14.460000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>12.742547</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>76.740000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>33.930000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>21.385657</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>74.920000</td>
    </tr>
  </tbody>
</table>
</div>



## Fit decision tree classifier and generate predictions

* Create decision tree object (object attributes passed)
* run decision tree method with training data
* run decision tree method with testing intput data
* look at results, calculate average accuracy


```python
humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0);
humidity_classifier.fit(x_train, y_train);
y_test.loc[:,'predictions'] = humidity_classifier.predict(x_test)
y_test.head(10)
(y_test.iloc[:,0] == y_test.iloc[:,1]).mean()
```




    DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
                max_features=None, max_leaf_nodes=10,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, presort=False, random_state=0,
                splitter='best')






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
      <th>predictions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>456</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>845</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>693</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>259</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>723</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>224</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>300</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>442</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>585</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1057</th>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>






    0.8153409090909091



## Extending the example

* I want to see how the 'threshold' for binning affects the classification accuracy (e.g. if the cutoff is closer to the mean then it should be less accurate)
* Instead of dropping the null values, linear impute and create a new variable to as a shadow variable (1 in this column means that another column was imputed)
* Iterate through random states for splitting into test and train sets (10 tries) - return vector of accuracy values
* refactor decision tree to a method to return vectors of classification accuracy and recall (true positive rate for the high humidity label) for  a specific threshold



```python
clean_data = data.copy()
clean_data.loc[clean_data.isnull().any(axis = 1),'Missing'] = 1
clean_data['Missing'] = clean_data['Missing'].fillna(0)
print("Number of interpolated values:", sum(clean_data['Missing']))
clean_data = clean_data.interpolate()
morning_features.append('Missing')
x = clean_data[morning_features].copy()
def tree_acc_recall(threshold):
    clean_data['high_humidity_label'] = (clean_data['relative_humidity_3pm'] >= threshold)*1
    y=clean_data[['high_humidity_label']]
    # x stays the same
    my_val = pd.DataFrame(columns = ['Accuracy', 'True Positives', 'False Positives'], index = range(0,20))
    for i in range(0,20): # 20 trials for each threshold
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=randint(99,100000000))
        humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0);
        humidity_classifier.fit(x_train, y_train);
        y_test['predictions'] = humidity_classifier.predict(x_test)
        
        
        nums = confusion_matrix(y_test['high_humidity_label'], y_test['predictions']).ravel()
        if (len(nums) == 1):
            tn, fp, fn, tp = 1, 1, 1, 1
        else:
            tn, fp, fn, tp = nums
            my_val.iloc[[i],0] = (tp + tn)/(tn + fp + fn + tp)
            my_val.iloc[[i],1] = tp/(tp + fn)
            my_val.iloc[[i],2] = fp/(fp + tn)
        # Too many chained operations, too confusing
        #my_val.iloc[[i],0]  = (y_test.iloc[:,0] == y_test.iloc[:,1]).mean() # accuracy
        #my_val.iloc[[i],1] = ((y_test.iloc[:,1] == 1)&(y_test.iloc[:,0] == y_test.iloc[:,1])).sum()/(y_test.iloc[:,0].sum()) # true positive 
        #my_val.iloc[[i],2] = ((y_test.iloc[:,1] == 1)&(y_test.iloc[:,0] != y_test.iloc[:,1])).sum()/(y_test.iloc[:,0].sum()) # false positive

    return(my_val)
```

    Number of interpolated values: 31.0



```python
list(x)
```




    ['air_pressure_9am',
     'air_temp_9am',
     'avg_wind_direction_9am',
     'avg_wind_speed_9am',
     'max_wind_direction_9am',
     'max_wind_speed_9am',
     'rain_accumulation_9am',
     'rain_duration_9am',
     'Missing']




```python
%%capture
my_out = pd.DataFrame(columns = ['Humidity Threshold', 'Average Accuracy', 'Average True Positives', 'Average False Positives'], index = range(0,101))
k = 0
for i in range(0,101, 1):
    temp = tree_acc_recall(i)
    my_out.iloc[[k],0] = i
    my_out.iloc[[k],1] = temp['Accuracy'].mean()
    my_out.iloc[[k],2] = temp['True Positives'].mean()
    my_out.iloc[[k],3] = temp['False Positives'].mean()
    k+=1
```


```python
my_out.head(10)
my_out.tail(10)
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
      <th>Humidity Threshold</th>
      <th>Average Accuracy</th>
      <th>Average True Positives</th>
      <th>Average False Positives</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>0.994911</td>
      <td>0.996361</td>
      <td>0.909091</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>0.99294</td>
      <td>0.996611</td>
      <td>0.75</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>0.985221</td>
      <td>0.992595</td>
      <td>0.637024</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>0.977901</td>
      <td>0.990382</td>
      <td>0.576939</td>
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
      <th>Humidity Threshold</th>
      <th>Average Accuracy</th>
      <th>Average True Positives</th>
      <th>Average False Positives</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>91</th>
      <td>91</td>
      <td>0.979282</td>
      <td>0.194167</td>
      <td>0.0124086</td>
    </tr>
    <tr>
      <th>92</th>
      <td>92</td>
      <td>0.989677</td>
      <td>0.125</td>
      <td>0.00670898</td>
    </tr>
    <tr>
      <th>93</th>
      <td>93</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>94</th>
      <td>94</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>95</th>
      <td>95</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>96</th>
      <td>96</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>97</th>
      <td>97</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>98</th>
      <td>98</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>99</th>
      <td>99</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>100</th>
      <td>100</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## ROC Curve 

* `my_out` has NaN when it is dividing by 0, when the threshold is so high that there are no true or false positives 


```python
fig, axis = plt.subplots()
axis.yaxis.grid(True)
axis.set_title('ROC Curve',fontsize=16)
axis.set_xlabel('False positive rate',fontsize=10)
axis.set_ylabel('True Positive Rate',fontsize=10)

axis.plot(my_out.iloc[:,3], my_out.iloc[:,2])
plt.show();
```


![png](7_ML_DT_files/7_ML_DT_18_0.png)


## Classification accuracy vs Threshold for classifying as high humidity


```python
fig, axis = plt.subplots()
axis.yaxis.grid(True)
axis.set_title('Accuracy vs Threshold',fontsize=16)
axis.set_xlabel('High humidiy threshold',fontsize=10)
axis.set_ylabel('Overall classification accuracy',fontsize=10)

axis.plot(my_out.iloc[:,0], my_out.iloc[:,1])
plt.show();
```


![png](7_ML_DT_files/7_ML_DT_20_0.png)

