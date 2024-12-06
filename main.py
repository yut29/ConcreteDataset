import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load("random_forest_model.pkl")

# Streamlit user input
st.title("Concrete Strength Prediction")
st.write("Enter the parameters of the concrete mix to predict the strength.")

# Create sliders for concrete parameters with actual data ranges
cement = st.slider("Cement Content (kg)", 
    min_value=102.0, max_value=550.0, value=300.0, step=10.0,
    help="Cement content range: 102-550 kg")

slag = st.slider("Slag Content (kg)", 
    min_value=0.0, max_value=360.0, value=100.0, step=10.0,
    help="Slag content range: 0-360 kg")

flyash = st.slider("Fly Ash Content (kg)", 
    min_value=0.0, max_value=200.0, value=50.0, step=10.0,
    help="Fly ash content range: 0-200 kg")

water = st.slider("Water Content (kg)", 
    min_value=120.0, max_value=250.0, value=185.0, step=5.0,
    help="Water content range: 120-250 kg")

superplasticizer = st.slider("Superplasticizer Content (kg)", 
    min_value=0.0, max_value=33.0, value=6.0, step=0.5,
    help="Superplasticizer content range: 0-33 kg")

coarseaggregate = st.slider("Coarse Aggregate Content (kg)", 
    min_value=800.0, max_value=1145.0, value=960.0, step=20.0,
    help="Coarse aggregate content range: 800-1145 kg")

fineaggregate = st.slider("Fine Aggregate Content (kg)", 
    min_value=594.0, max_value=993.0, value=750.0, step=20.0,
    help="Fine aggregate content range: 594-993 kg")

age = st.slider("Age of Concrete (days)", 
    min_value=1, max_value=365, value=28, step=1,
    help="Concrete age range: 1-365 days")

# Create a button for prediction
if st.button("Predict"):
    input_data = np.array([[cement, slag, flyash, water, superplasticizer, coarseaggregate, fineaggregate, age]])
    prediction = model.predict(input_data)
    st.write(f"Predicted Concrete Strength: {prediction[0]:.2f} MPa")
