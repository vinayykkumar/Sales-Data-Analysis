import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load model and scaler
try:
    model = joblib.load("churn_model.pkl")
    scaler = joblib.load("scaler.pkl")
    st.success("Model loaded successfully!")
except FileNotFoundError:
    st.error("Model file not found. Run 'train_model.py' first.")
    model = None

# Streamlit UI
st.set_page_config(page_title="Telecom Churn Prediction", layout="wide")

st.title("📞 Telecom Churn Prediction App")
st.markdown("Enter customer details to predict whether they will churn.")

# Sidebar Info
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3059/3059518.png", width=100)
st.sidebar.markdown("**How to use:**\n1. Enter customer details\n2. Click 'Predict Churn'\n3. View results")

# User Inputs
col1, col2, col3 = st.columns(3)

with col1:
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 65.5)
    total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 2280.0)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.radio("Senior Citizen", ["No", "Yes"])
    partner = st.radio("Has Partner", ["No", "Yes"])
    dependents = st.radio("Has Dependents", ["No", "Yes"])

with col3:
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.radio("Paperless Billing", ["No", "Yes"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ])

# Encoding function (same encoding used in model training)
def encode_inputs():
    mapping = {
        "Male": 1, "Female": 0,
        "Yes": 1, "No": 0,
        "Month-to-month": 0, "One year": 1, "Two year": 2,
        "Electronic check": 0, "Mailed check": 1, "Bank transfer (automatic)": 2, "Credit card (automatic)": 3,
    }
    return np.array([
        tenure, monthly_charges, total_charges,
        mapping[gender], mapping[senior_citizen], mapping[partner], mapping[dependents],
        mapping[contract], mapping[paperless_billing], mapping[payment_method]
    ]).reshape(1, -1)

# Prediction
if st.button("Predict Churn", type="primary"):
    if model:
        input_data = encode_inputs()
        input_data = scaler.transform(input_data)  # Scale inputs
        prediction = model.predict(input_data)
        
        st.subheader("Prediction Result:")
        if prediction[0] == 1:
            st.error("🚨 The customer is **likely to churn**!")
        else:
            st.success("✅ The customer is **not likely to churn**.")
    else:
        st.error("Model is not loaded. Please train it first.")
