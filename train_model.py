import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load CSV
df = pd.read_csv('car_data.csv')

# Drop rows with missing values
df.dropna(inplace=True)

# Rename columns for easier handling
df.rename(columns={
    'Model': 'model',
    'Selling Price': 'price',
    'Kilometers Driven': 'kms_driven',
    'Year': 'year',
    'Fuel Type': 'fuel_type',
    'Transmission': 'transmission',
    'Owner': 'owner',
    'Insurance': 'insurance'
}, inplace=True)

# Feature engineering
df['car_age'] = 2025 - df['year']
df.drop('year', axis=1, inplace=True)

# Drop 'Car Condition' (not used)
df.drop('Car Condition', axis=1, inplace=True)

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=['model', 'fuel_type', 'transmission', 'owner', 'insurance'], drop_first=True)

# Split features and target
X = df.drop('price', axis=1)
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
pickle.dump(model, open('car_price_model.pkl', 'wb'))

print("✅ Model trained and saved as car_price_model.pkl")
