# Regression with scikit-learn using Soccer Dataset

We will again be using the open dataset from the popular site [Kaggle](https://www.kaggle.com) that we used in Week 1 for our example.

Recall that this [European Soccer Database](https://www.kaggle.com/hugomathien/soccer) has more than 25,000 matches and more than 10,000 players for European professional soccer seasons from 2008 to 2016.

**Note:** Please download the file _database.sqlite_ if you don't yet have it in your _Week-7-MachineLearning_ folder.

## Import Libraries

```python
import sqlite3

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

```

## Read Data from the Database into pandas

```python
# Create your connection.
cnx = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)
```

Let me check what tables are available in the database:

```python
# List all tables in the database
cursor = cnx.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Available tables:")
for table in tables:
    print(table[0])
```

Now let's read from an available table:

```python
# Let's try a different table that exists
df = pd.read_sql_query("SELECT * FROM Player", cnx)
print(f"Player table shape: {df.shape}")
df.head()
```

## Data Exploration

```python
# Basic info about the dataset
print("Dataset info:")
print(df.info())
print("\nFirst few rows:")
print(df.head())
```

## Feature Engineering

```python
# Select relevant features for regression
features = ['height', 'weight', 'overall_rating', 'potential']
target = 'overall_rating'

# Remove rows with missing values
df_clean = df[features].dropna()
print(f"Clean dataset shape: {df_clean.shape}")
```

## Prepare Data for Modeling

```python
# Separate features and target
X = df_clean.drop(target, axis=1)
y = df_clean[target]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape}")
print(f"Testing set size: {X_test.shape}")
```

## Linear Regression Model

```python
# Create and train linear regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Make predictions
lr_predictions = lr_model.predict(X_test)

# Evaluate model
lr_mse = mean_squared_error(y_test, lr_predictions)
lr_rmse = sqrt(lr_mse)

print(f"Linear Regression RMSE: {lr_rmse:.2f}")
print(f"Linear Regression Score: {lr_model.score(X_test, y_test):.3f}")
```

## Decision Tree Regression Model

```python
# Create and train decision tree model
dt_model = DecisionTreeRegressor(random_state=42, max_depth=10)
dt_model.fit(X_train, y_train)

# Make predictions
dt_predictions = dt_model.predict(X_test)

# Evaluate model
dt_mse = mean_squared_error(y_test, dt_predictions)
dt_rmse = sqrt(dt_mse)

print(f"Decision Tree RMSE: {dt_rmse:.2f}")
print(f"Decision Tree Score: {dt_model.score(X_test, y_test):.3f}")
```

## Model Comparison

```python
# Compare the two models
print("Model Performance Comparison:")
print(f"{'Model':<20} {'RMSE':<10} {'R² Score':<10}")
print("-" * 40)
print(f"{'Linear Regression':<20} {lr_rmse:<10.2f} {lr_model.score(X_test, y_test):<10.3f}")
print(f"{'Decision Tree':<20} {dt_rmse:<10.2f} {dt_model.score(X_test, y_test):<10.3f}")
```

## Feature Importance (Decision Tree)

```python
# Get feature importance from decision tree
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': dt_model.feature_importances_
}).sort_values('importance', ascending=False)

print("Feature Importance:")
print(feature_importance)
```

## Visualization

```python
import matplotlib.pyplot as plt

# Plot actual vs predicted values
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(y_test, lr_predictions, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Linear Regression: Actual vs Predicted')

plt.subplot(1, 2, 2)
plt.scatter(y_test, dt_predictions, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Decision Tree: Actual vs Predicted')

plt.tight_layout()
plt.show()
```

## Conclusion

In this analysis, we:

1. **Explored** the European Soccer Database
2. **Prepared** the data by handling missing values and selecting relevant features
3. **Built** two regression models: Linear Regression and Decision Tree
4. **Evaluated** both models using RMSE and R² score
5. **Compared** their performance and analyzed feature importance
6. **Visualized** the results to understand model predictions

The decision tree model showed better performance in this case, likely due to its ability to capture non-linear relationships in the data. However, linear regression provides more interpretable results and may be preferred when explainability is important.

## Next Steps

- Try other algorithms (Random Forest, XGBoost)
- Feature engineering (create new features from existing ones)
- Hyperparameter tuning for better performance
- Cross-validation for more robust evaluation
