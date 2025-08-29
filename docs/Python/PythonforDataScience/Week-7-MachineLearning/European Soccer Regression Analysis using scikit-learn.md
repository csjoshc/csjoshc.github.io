
  🏠 Home
  🐍 Python

Regresssion with scikit-learn using Soccer Dataset

We will again be using the open dataset from the popular site Kaggle that we used in Week 1 for our example. 
Recall that this European Soccer Database has more than 25,000 matches and more than 10,000 players for European professional soccer seasons from 2008 to 2016. 
**Note:** Please download the file *database.sqlite* if you don't yet have it in your *Week-7-MachineLearning* folder.

```python
import sqlite3

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

```

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

```python
target = ['overall_rating']
```

```python
df = df.dropna()
```

Extract Features and Target ('overall_rating') Values into Separate Dataframes

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

```

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)
```

(1) Linear Regression: Fit a model to the training set

```python
regressor = LinearRegression()
regressor.fit(X_train, y_train)
```

```python
y_prediction = regressor.predict(X_test)
y_prediction
```

What is the mean of the expected target value in test set ?

```python
y_test.describe()
```

```python
RMSE = sqrt(mean_squared_error(y_true = y_test, y_pred = y_prediction))
```
```python
print(RMSE)
```

(2) Decision Tree Regressor: Fit a new regression model to the training set

```python
regressor = DecisionTreeRegressor(max_depth=20)
regressor.fit(X_train, y_train)
```

```python
y_prediction = regressor.predict(X_test)
y_prediction
```

For comparision: What is the mean of the expected target value in test set ?

```python
y_test.describe()
```

```python
RMSE = sqrt(mean_squared_error(y_true = y_test, y_pred = y_prediction))
```
```python
print(RMSE)
```
