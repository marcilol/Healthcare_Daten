# config.py
import os

# Database Configuration
DATABASE_PATH = os.path.join(os.getcwd(), 'healthcare_data.db')

# Model Configuration
MODEL_PATH = os.path.join(os.getcwd(), 'models', 'readmission_model.pkl')

# Data Generation Parameters
NUM_PATIENTS = 50000
NUM_ENCOUNTERS = 200000
NUM_LAB_RESULTS = 200000
NUM_MEDICATIONS = 200000
