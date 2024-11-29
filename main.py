import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load("random_forest_model.pkl")

# Streamlit user input
st.title("Concrete Strength Prediction")
st.write("Enter the parameters of the concrete mix to predict the strength.")

# Create input fields for concrete parameters
cement = st.number_input("Cement Content (kg)", min_value=0.0, step=1.0)
slag = st.number_input("Slag Content (kg)", min_value=0.0, step=1.0)
flyash = st.number_input("Fly Ash Content (kg)", min_value=0.0, step=1.0)
water = st.number_input("Water Content (kg)", min_value=0.0, step=0.1)
superplasticizer = st.number_input("Superplasticizer Content (kg)", min_value=0.0, step=0.1)
coarseaggregate = st.number_input("Coarse Aggregate Content (kg)", min_value=0.0, step=1.0)
fineaggregate = st.number_input("Fine Aggregate Content (kg)", min_value=0.0, step=1.0)
age = st.number_input("Age of Concrete (days)", min_value=0.0, step=1.0)

# Create a button for prediction
if st.button("Predict"):
    input_data = np.array([[cement, slag, flyash, water, superplasticizer, coarseaggregate, fineaggregate, age]])
    prediction = model.predict(input_data)
    st.write(f"Predicted Concrete Strength: {prediction[0]:.2f} MPa")
