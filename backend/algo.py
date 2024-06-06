import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the datasets
training_data_path = 'Training Data (2022-2012).xlsx'
testing_data_path = 'Testing Data (2023).xlsx'

training_data = pd.read_excel(training_data_path)
testing_data = pd.read_excel(testing_data_path)

# Encode categorical features
label_encoder = LabelEncoder()
training_data['HomeTeam'] = label_encoder.fit_transform(training_data['HomeTeam'])
training_data['VisitingTeam'] = label_encoder.fit_transform(training_data['VisitingTeam'])
testing_data['HomeTeam'] = label_encoder.transform(testing_data['HomeTeam'])
testing_data['VisitingTeam'] = label_encoder.transform(testing_data['VisitingTeam'])

# Encode target variable
training_data['HomeTeamWin'] = training_data['HomeTeamWin'].apply(lambda x: 1 if x == 'win' else 0)
testing_data['HomeTeamWin'] = testing_data['HomeTeamWin'].apply(lambda x: 1 if x == 'win' else 0)

# Features and target
features = ['HomeTeam', 'VisitingTeam', 'VisitorERA', 'VisitorWHIP', 'HomeSLG', 'HomeOBP', 'HomePythagoreanWP', 'HomeLog5WinProbability']
target = 'HomeTeamWin'

X_train = training_data[features]
y_train = training_data[target]
X_test = testing_data[features]
y_test = testing_data[target]

# Create and train the XGBoost model with optimized settings
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', n_estimators=100, max_depth=3)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Display results
print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(pd.DataFrame(conf_matrix, columns=["Predicted Loss", "Predicted Win"], index=["Actual Loss", "Actual Win"]))