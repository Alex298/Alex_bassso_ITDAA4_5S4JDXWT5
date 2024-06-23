import streamlit as st
import numpy as np
import os
import joblib

# Check if the model file exists
model_path = 'best_model.joblib'
if not os.path.exists(model_path):
    st.error(f"Model file '{model_path}' not found. Please ensure the file is in the correct directory.")
    st.stop()

# Load the saved model
try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Failed to load model. Please ensure the file '{model_path}' is present and valid. Error: {e}")
    st.stop()

# Define a function to make predictions
def predict_heart_disease(input_data):
    try:
        prediction = model.predict([input_data])
        return prediction[0]
    except Exception as e:
        st.error(f"Failed to make prediction. Error: {e}")
        return None

# Streamlit application
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2e003e;
    }
    .stButton>button {
        background-color: #800080;
        color: white;
    }
    .stNumberInput>div>div>input {
        border: 2px solid #800080;
        color: white;
        background-color: #4b0082;
    }
    .stSelectbox>div>div>div>button {
        background-color: #800080;
        color: white;
    }
    .stSelectbox>div>div>div>button>div {
        color: white;
    }
    .stMarkdown {
        color: #800080;
    }
    .stSidebar .stButton>button {
        background-color: #800080;
        color: white;
    }
    .stSidebar .stMarkdown {
        color: #800080;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Heart Disease Prediction")

# Create input fields for all the features required by the model
age = st.number_input("Age", min_value=0, max_value=120, step=1)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=0, max_value=300, step=1)
chol = st.number_input("Serum Cholestoral", min_value=0, max_value=600, step=1)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=220, step=1)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

# Collect the input data into a list
input_data = [age, 1 if sex == "Male" else 0, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

# Predict heart disease based on user input
if st.button("Predict"):
    prediction = predict_heart_disease(input_data)
    if prediction is not None:
        if prediction == 1:
            st.success("The patient is likely to have heart disease. Further tests are recommended.")
        else:
            st.success("The patient is unlikely to have heart disease.")

# Add some documentation
st.sidebar.title("Documentation")
st.sidebar.info("""
This application predicts the likelihood of a patient having heart disease based on several medical parameters. 
Fill in the patient details in the form provided and click 'Predict' to see the result.
""")

# Add the footer
st.markdown(
    """
    <div style='text-align: center; padding: 20px; color: #800080;'>
        <strong>Alex Basson 5S4JDXWT5</strong>
    </div>
    """,
    unsafe_allow_html=True
)
