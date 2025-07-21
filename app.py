import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("bangalore_home_prices_model.pickle", "rb") as f:
    model = pickle.load(f)

st.title("🏠 Bangalore House Price Predictor")

# Inputs
area = st.number_input("Enter area in square feet:", min_value=300)
bath = st.number_input("Number of bathrooms:", min_value=1, max_value=10)
bhk = st.number_input("Number of BHK (bedrooms):", min_value=1, max_value=10)

# Predict
if st.button("Predict Price"):
    input_df = pd.DataFrame([[area, bath, bhk]], columns=['total_sqft_int', 'bath', 'bhk'])
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: ₹ {round(prediction, 2)} Lakhs")

