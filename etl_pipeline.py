# src/etl/etl_pipeline.py
import pandas as pd
import sqlite3
from config import DATABASE_PATH

def create_tables(conn):
    """Creates tables for storing patient, encounter, lab results, and medication data."""
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY,
        age INTEGER,
        sex TEXT,
        race TEXT,
        zip_code TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS encounters (
        encounter_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        hospital_id INTEGER,
        admission_date TEXT,
        discharge_date TEXT,
        diagnosis TEXT,
        length_of_stay INTEGER,
        visit_type TEXT,
        readmission_within_30_days INTEGER,
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS lab_results (
        lab_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        test_name TEXT,
        test_result REAL,
        test_date TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medications (
        medication_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        medication_name TEXT,
        dose INTEGER,
        frequency TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
    )
    ''')

    conn.commit()

def load_data_into_db():
    """Load generated data into SQLite database."""
    patients = pd.read_csv('data/raw/synthetic_data_patients.csv')
    encounters = pd.read_csv('data/raw/synthetic_data_encounters.csv')
    lab_results = pd.read_csv('data/raw/synthetic_data_lab_results.csv')
    medications = pd.read_csv('data/raw/synthetic_data_medications.csv')

    conn = sqlite3.connect(DATABASE_PATH)
    create_tables(conn)

    patients.to_sql('patients', conn, if_exists='replace', index=False)
    encounters.to_sql('encounters', conn, if_exists='replace', index=False)
    lab_results.to_sql('lab_results', conn, if_exists='replace', index=False)
    medications.to_sql('medications', conn, if_exists='replace', index=False)

    conn.close()
    print("Data loaded into database.")
