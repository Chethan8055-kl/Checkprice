import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('car_price_model.pkl', 'rb'))

st.set_page_config(page_title="Used Car Price Predictor")
st.title("🚗 Used Car Price Predictor")
st.markdown("Enter the details below to estimate your car's selling price.")

# User Inputs
model_name = st.text_input("Car Model (e.g., Maruti Swift VDI)")
kms_driven = st.number_input("Kilometers Driven", min_value=0)
car_age = st.slider("Car Age (in years)", 0, 30, 5)
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
transmission = st.selectbox("Transmission Type", ['Manual', 'Automatic'])
owner = st.selectbox("Owner Type", ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'])
insurance = st.selectbox("Insurance Status", ['Yes', 'No'])

# Get the columns from the trained model
cols = model.feature_names_in_

# Build the input data
input_data = pd.DataFrame([[0]*len(cols)], columns=cols)

# Fill basic fields
input_data['kms_driven'] = kms_driven
input_data['car_age'] = car_age

# Dynamically set one-hot encoded fields
col_keys = {
    f'model_{model_name}': 1,
    f'fuel_type_{fuel_type}': 1,
    f'transmission_{transmission}': 1,
    f'owner_{owner}': 1,
    f'insurance_{insurance}': 1
}

for key, value in col_keys.items():
    if key in input_data.columns:
        input_data[key] = value

# Prediction
if st.button("Predict Price"):
    predicted_price = model.predict(input_data)[0]
    st.success(f"💰 Estimated Selling Price: ₹ {int(predicted_price):,}")
