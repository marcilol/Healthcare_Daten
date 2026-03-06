# src/data_generation/generate_data.py
import pandas as pd
import numpy as np
from random import randint, choice
from datetime import datetime, timedelta
from config import NUM_PATIENTS, NUM_ENCOUNTERS, NUM_LAB_RESULTS, NUM_MEDICATIONS

def generate_patients():
    """Generates synthetic patient data."""
    patients = []
    for i in range(NUM_PATIENTS):
        patients.append({
            'patient_id': i,
            'age': randint(18, 90),
            'sex': choice(['M', 'F']),
            'race': choice(['White', 'Black', 'Asian', 'Hispanic', 'Other']),
            'zip_code': f'{randint(10000, 99999)}',
        })
    return pd.DataFrame(patients)

def generate_encounters():
    """Generates synthetic hospital encounter data."""
    encounters = []
    for i in range(NUM_ENCOUNTERS):
        encounters.append({
            'encounter_id': i,
            'patient_id': randint(0, NUM_PATIENTS - 1),
            'hospital_id': randint(0, 10),
            'admission_date': datetime.now() - timedelta(days=randint(1, 365)),
            'discharge_date': datetime.now() - timedelta(days=randint(1, 5)),
            'diagnosis': choice(['Diabetes', 'Hypertension', 'Pneumonia', 'Cancer', 'Heart Disease']),
            'length_of_stay': randint(1, 10),
            'visit_type': choice(['Emergency', 'Elective', 'Urgent', 'Routine']),
            'readmission_within_30_days': choice([0, 1])
        })
    return pd.DataFrame(encounters)

def generate_lab_results():
    """Generates synthetic lab result data."""
    lab_results = []
    for i in range(NUM_LAB_RESULTS):
        lab_results.append({
            'lab_id': i,
            'patient_id': randint(0, NUM_PATIENTS - 1),
            'test_name': choice(['Blood Pressure', 'Cholesterol', 'Glucose', 'Kidney Function']),
            'test_result': np.random.uniform(5, 200),
            'test_date': datetime.now() - timedelta(days=randint(1, 365))
        })
    return pd.DataFrame(lab_results)

def generate_medications():
    """Generates synthetic medication data."""
    medications = []
    for i in range(NUM_MEDICATIONS):
        medications.append({
            'medication_id': i,
            'patient_id': randint(0, NUM_PATIENTS - 1),
            'medication_name': choice(['Metformin', 'Amlodipine', 'Lisinopril', 'Aspirin', 'Atorvastatin']),
            'dose': randint(1, 5),
            'frequency': choice(['Daily', 'Twice a day', 'As needed']),
        })
    return pd.DataFrame(medications)

def generate_and_save_data():
    """Generate and save synthetic data to CSV files."""
    patients = generate_patients()
    encounters = generate_encounters()
    lab_results = generate_lab_results()
    medications = generate_medications()

    patients.to_csv('data/raw/synthetic_data_patients.csv', index=False)
    encounters.to_csv('data/raw/synthetic_data_encounters.csv', index=False)
    lab_results.to_csv('data/raw/synthetic_data_lab_results.csv', index=False)
    medications.to_csv('data/raw/synthetic_data_medications.csv', index=False)

    print("Data generation complete.")
