import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Predictoin")
st.write("Enter the details to predict Churn")

# Input Data
tenure = st.number_input("Tenure", 0, 100)
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Credit card"])

# Convert inputs into dataframe (IMPORTANT)
input_data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges],
    "Contract": [contract],
    "InternetService": [internet],
    "PaymentMethod": [payment]
})

# Predict button
if st.button("Predict Churn"):
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error("⚠ Customer WILL churn")
    else:
        st.success("✅ Customer will NOT churn")

    st.write("Probability:", prob)