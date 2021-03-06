
<p style="font-family: Arial; font-size:2.75em;color:purple; font-style:bold"><br>

Regresssion with scikit-learn<br><br> using Soccer Dataset

<br><br></p>


We will again be using the open dataset from the popular site <a href="https://www.kaggle.com">Kaggle</a> that we used in Week 1 for our example. 

Recall that this <a href="https://www.kaggle.com/hugomathien/soccer">European Soccer Database</a> has more than 25,000 matches and more than 10,000 players for European professional soccer seasons from 2008 to 2016. 

**Note:** Please download the file *database.sqlite* if you don't yet have it in your *Week-7-MachineLearning* folder.

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Import Libraries<br><br></p>



```python
import sqlite3
import pandas as pd 
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Read Data from the Database into pandas
<br><br></p>



```python
# Create your connection.
cnx = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)
```


```python
df.head()
```


```python
df.shape
```


```python
df.columns
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Declare the Columns You Want to Use as Features
<br><br></p>



```python
features = [
       'potential', 'crossing', 'finishing', 'heading_accuracy',
       'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
       'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
       'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
       'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
       'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
       'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
       'gk_reflexes']
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Specify the Prediction Target
<br><br></p>



```python
target = ['overall_rating']
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Clean the Data<br><br></p>



```python
df = df.dropna()
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Extract Features and Target ('overall_rating') Values into Separate Dataframes
<br><br></p>



```python
X = df[features]
```


```python
y = df[target]
```

Let us look at a typical row from our features: 


```python
X.iloc[2]
```

Let us also display our target values: 


```python
y
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Split the Dataset into Training and Test Datasets
<br><br></p>



```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

(1) Linear Regression: Fit a model to the training set
<br><br></p>



```python
regressor = LinearRegression()
regressor.fit(X_train, y_train)
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Perform Prediction using Linear Regression Model
<br><br></p>



```python
y_prediction = regressor.predict(X_test)
y_prediction
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

What is the mean of the expected target value in test set ?
<br><br></p>



```python
y_test.describe()
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Evaluate Linear Regression Accuracy using Root Mean Square Error

<br><br></p>



```python
RMSE = sqrt(mean_squared_error(y_true = y_test, y_pred = y_prediction))
```


```python
print(RMSE)
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

(2) Decision Tree Regressor: Fit a new regression model to the training set
<br><br></p>



```python
regressor = DecisionTreeRegressor(max_depth=20)
regressor.fit(X_train, y_train)
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Perform Prediction using Decision Tree Regressor
<br><br></p>



```python
y_prediction = regressor.predict(X_test)
y_prediction
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

For comparision: What is the mean of the expected target value in test set ?
<br><br></p>



```python
y_test.describe()
```

<p style="font-family: Arial; font-size:1.75em;color:purple; font-style:bold"><br>

Evaluate Decision Tree Regression Accuracy using Root Mean Square Error

<br><br></p>



```python
RMSE = sqrt(mean_squared_error(y_true = y_test, y_pred = y_prediction))
```


```python
print(RMSE)
```
