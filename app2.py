import streamlit as st
import pandas as pd
# import sqlite3
from sklearn.externals import joblib

# Load the pre-trained model
model = joblib.load('content/readmission_model.pkl')

# Set up database connection
conn = sqlite3.connect('healthcare_data.db')
data = pd.read_sql('SELECT * FROM encounters', conn)

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
# Example of chronic disease analysis
st.header('Chronic Disease Analysis')
diabetes = data[data['diagnosis'] == 'Diabetes']
st.write(f'Diabetes Patients: {diabetes.shape[0]}')

# More visualizations...
