import streamlit as st
import pandas as pd
import sqlite3

# Load data from SQLite
conn = sqlite3.connect('healthcare_data.db')
data = pd.read_sql('SELECT * FROM encounters', conn)

# Page 1: Executive Overview
st.title('Healthcare Analytics Dashboard')

# Total Patients and Visits
total_patients = data['patient_id'].nunique()
total_visits = data.shape[0]
readmission_rate = data['readmission_within_
