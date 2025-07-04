import streamlit as st
import numpy as np
import joblib

# Load the trained model and column names
model = joblib.load("pollution_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# Page title
st.title("Water Pollutant (CL) Predictor")
st.markdown("This app predicts the **Chloride (CL)** level based on water quality parameters.")

# Create input fields for all required features
user_input = []
for col in model_columns:
    value = st.number_input(f"{col}:", min_value=0.0, format="%.3f")
    user_input.append(value)

# Predict button
if st.button("Predict CL Level"):
    input_array = np.array(user_input).reshape(1, -1)
    predicted_cl = model.predict(input_array)[0]

    # Display result
    st.success(f"✅ Predicted Chloride (CL) level: **{predicted_cl:.2f} mg/L**")
