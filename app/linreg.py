import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the training and testing data
training_data_path = 'Training Data (2012-2022).xlsx'
testing_data_path = 'Testing Data (2023).xlsx'

training_data = pd.read_excel(training_data_path)
testing_data = pd.read_excel(testing_data_path)

# Drop rows with missing values (if any)
training_data.dropna(inplace=True)
testing_data.dropna(inplace=True)

# Separate features and target variable for training data
X_train = training_data.drop(columns=['Date', 'HomeTeam', 'AwayTeam', 'HomeTeamRuns', 'AwayTeamRuns', 'HomeTeamWon'])
y_train = training_data['HomeTeamWon']

# Separate features and target variable for testing data
X_test = testing_data.drop(columns=['Date', 'HomeTeam', 'AwayTeam', 'HomeTeamRuns', 'AwayTeamRuns', 'HomeTeamWon'])
y_test = testing_data['HomeTeamWon']

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train_scaled, y_train)

# Predict on the test data
y_pred = model.predict(X_test_scaled)
y_pred_binary = [1 if pred >= 0.5 else 0 for pred in y_pred]

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred_binary)

print('Accuracy: ', accuracy)

# Save the trained model
joblib.dump(model, 'linear_regression_model.pkl')
joblib.dump(scaler, 'scaler.pkl')


# Plot the regression line (for a single feature example)
plt.figure(figsize=(12, 8))
plt.scatter(X_test_scaled[:, 0], y_test, color='blue', label='Actual', alpha=0.6, edgecolors='w', s=100)
plt.scatter(X_test_scaled[:, 0], y_pred, color='red', label='Predicted', alpha=0.6, edgecolors='w', s=100)
plt.plot(np.sort(X_test_scaled[:, 0]), np.sort(y_pred), color='green', linewidth=2)
plt.xlabel('Feature 1 (scaled)', fontsize=14)
plt.ylabel('Home Team Won', fontsize=14)
plt.title('Linear Regression - Actual vs Predicted', fontsize=16)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Feature importance
importance = model.coef_
features = X_train.columns

plt.figure(figsize=(12, 8))
sns.barplot(x=importance, y=features)
plt.xlabel('Coefficient Value', fontsize=14)
plt.ylabel('Features', fontsize=14)
plt.title('Feature Importance', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()