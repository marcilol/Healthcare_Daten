import streamlit as st
import pandas as pd
import sqlite3
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load the pre-trained model (make sure it's stored in the correct path)
model = joblib.load('readmission_model.pkl')

# Set up database connection (make sure the SQLite file is in the correct path)
conn = sqlite3.connect('healthcare_data.db')


data = pd.read_sql("""
SELECT 
    e.*,
    p.age,
    l.test_result
FROM encounters e
JOIN patients p ON e.patient_id = p.patient_id
LEFT JOIN lab_results l ON e.patient_id = l.patient_id
""", conn)

# Page 1: Executive Overview
st.title('Healthcare Analytics Dashboard')

# Total Patients and Visits
total_patients = data['patient_id'].nunique()
total_visits = data.shape[0]
readmission_rate = data['readmission_within_30_days'].mean() * 100
average_length_of_stay = data['length_of_stay'].mean()

st.header('Executive Overview')
st.subheader(f'Total Patients: {total_patients}')
st.subheader(f'Total Visits: {total_visits}')
st.subheader(f'Readmission Rate: {readmission_rate:.2f}%')
st.subheader(f'Average Length of Stay: {average_length_of_stay:.2f} days')

# Page 2: Chronic Disease Analysis
st.header('Chronic Disease Analysis')

# Diabetes patients
diabetes = data[data['diagnosis'] == 'Diabetes']
hypertension = data[data['diagnosis'] == 'Hypertension']
heart_disease = data[data['diagnosis'] == 'Heart Disease']

# Display chronic disease statistics
st.write(f"Total Diabetes Patients: {diabetes.shape[0]}")
st.write(f"Total Hypertension Patients: {hypertension.shape[0]}")
st.write(f"Total Heart Disease Patients: {heart_disease.shape[0]}")

# Chronic Disease Distribution Pie Chart
st.subheader('Chronic Disease Distribution')
disease_counts = data['diagnosis'].value_counts()
st.write(disease_counts)

# Display Pie Chart
fig, ax = plt.subplots()
ax.pie(disease_counts, labels=disease_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Page 3: Hospital Utilization

st.header('Hospital Utilization')

# Visits by Hospital
hospital_visits = data['hospital_id'].value_counts()
st.write('Hospital Visits Breakdown:')
st.write(hospital_visits)

# Bar chart for hospital visits
fig, ax = plt.subplots()
ax.bar(hospital_visits.index, hospital_visits.values)
ax.set_xlabel('Hospital ID')
ax.set_ylabel('Number of Visits')
ax.set_title('Hospital Visits Breakdown')
st.pyplot(fig)

# Page 4: Predicting 30-day Readmission Risk

st.header('Readmission Risk Prediction')

# User input to predict readmission risk
patient_id_input = st.number_input('Enter Patient ID:', min_value=0, max_value=total_patients-1, step=1)

if patient_id_input is not None:
    # Get data for the selected patient
    patient_data = data[data['patient_id'] == patient_id_input].iloc[0]
    
    # Prepare features for the prediction model (adjust based on your model's input features)
    patient_features = {
        'age': patient_data['age'],
        'diagnosis': patient_data['diagnosis'],
        'length_of_stay': patient_data['length_of_stay'],
        'prior_visits': data[data['patient_id'] == patient_id_input].shape[0],
        'max_lab_result': data[data['patient_id'] == patient_id_input]['test_result'].max()
    }
    
    # Convert categorical 'diagnosis' feature into numerical encoding
    diagnosis_mapping = {'Diabetes': 1, 'Hypertension': 2, 'Heart Disease': 3, 'Pneumonia': 4, 'Cancer': 5}
    patient_features['diagnosis'] = diagnosis_mapping.get(patient_features['diagnosis'], 0)

    # Convert features into a DataFrame for prediction
    patient_df = pd.DataFrame([patient_features])

    # Predict readmission risk
    prediction = model.predict_proba(patient_df)[:, 1]  # Probability of readmission
    st.write(f"Predicted Readmission Risk: {prediction[0]:.2f}")

    # Display result (threshold to classify high/low risk)
    if prediction[0] > 0.5:
        st.warning("This patient is at **high risk** for readmission.")
    else:
        st.success("This patient is at **low risk** for readmission.")
