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