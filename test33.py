import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pickle

# Sample Data
data = pd.DataFrame({
    'Age': [25, 32, 47, 51, 62],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 80000, 72000, 90000],
    'Purchased': [0, 1, 1, 0, 1]
})

# Step 1: One-hot encode categorical variables
data_encoded = pd.get_dummies(data, columns=['Gender'])

# Step 2: Feature Scaling
X = data_encoded.drop('Purchased', axis=1)
y = data_encoded['Purchased']

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 4: Model Training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 5: Save Model, Scaler, and Columns
#with open('model.pkl', 'wb') as f:
#    pickle.dump(model, f)
pickle.dump(model,open("model.pkl",'wb'))

#with open('scaler.pkl', 'wb') as f:
#    pickle.dump(scaler, f)
pickle.dump(scaler,open("scalar.pkl",'wb'))
#with open('columns.pkl', 'wb') as f:
#    pickle.dump(X.columns.tolist(), f)
pickle.dump(X.columns.tolist(),open("columns.pkl",'wb'))
print("Model, Scaler, and Columns saved successfully.")
