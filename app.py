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
age = st.number_input("Age (years)", min_value=0, max_value=120, step=1)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["0: Typical Angina", "1: Atypical Angina", "2: Non-Anginal Pain", "3: Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, step=1)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, step=1)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["0: No", "1: Yes"])
restecg = st.selectbox("Resting Electrocardiographic Results", ["0: Normal", "1: Having ST-T wave abnormality", "2: Showing probable or definite left ventricular hypertrophy by Estes' criteria"])
thalach = st.number_input("Maximum Heart Rate Achieved (bpm)", min_value=0, max_value=220, step=1)
exang = st.selectbox("Exercise Induced Angina", ["0: No", "1: Yes"])
oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["0: Upsloping", "1: Flat", "2: Downsloping"])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", ["0: Normal", "1: Fixed Defect", "2: Reversible Defect"])

# Collect the input data into a list
input_data = [age, 1 if sex == "Male" else 0, int(cp.split(":")[0]), trestbps, chol, int(fbs.split(":")[0]), int(restecg.split(":")[0]), thalach, int(exang.split(":")[0]), oldpeak, int(slope.split(":")[0]), ca, int(thal.split(":")[0])]

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
