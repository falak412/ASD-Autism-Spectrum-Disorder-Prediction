import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('models/asd_model.pkl')

st.set_page_config(page_title="ASD Predictor", layout="centered")
st.title("🧠 Autism Spectrum Disorder (ASD) Prediction")
st.markdown("This tool helps screen individuals for ASD using basic questions.")

st.header("📋 Input Information")

# Collect inputs
age = st.slider("Age", 1, 100, 25)
gender = st.radio("Gender", ["Male", "Female"])
jaundice = st.selectbox("Was there jaundice at birth?", ["Yes", "No"])
family_history = st.selectbox("Family member diagnosed with ASD?", ["Yes", "No"])

st.subheader("🧠 Screening Questions (Yes / No)")

q1 = st.radio("1. Does the person make eye contact?", ["Yes", "No"])
q2 = st.radio("2. Does the person smile back when smiled at?", ["Yes", "No"])
q3 = st.radio("3. Does the person respond to their name?", ["Yes", "No"])
q4 = st.radio("4. Does the person enjoy social interactions?", ["Yes", "No"])
q5 = st.radio("5. Does the person get upset by schedule changes?", ["Yes", "No"])

# Helper: Yes/No → Binary
def yn(value):
    return 1 if value == "Yes" else 0

gender_map = {"Male": 1, "Female": 0}

# Build input feature array (order must match selected_cols in preprocess.py)
features = np.array([
    age,
    gender_map[gender],
    yn(jaundice),
    yn(family_history),  # This is 'austim' in your CSV and training
    yn(q1),  # A1_Score
    yn(q2),  # A2_Score
    yn(q3),  # A3_Score
    yn(q4),  # A4_Score
    yn(q5),  # A5_Score
]).reshape(1, -1)

# Predict
if st.button("🚀 Predict ASD"):
    prediction = model.predict(features)[0]
    result = "🟢 Negative for ASD" if prediction == 0 else "🔴 Positive for ASD"
    st.success(f"Prediction: **{result}**")
