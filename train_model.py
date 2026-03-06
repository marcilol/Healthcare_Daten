# src/model/train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from config import DATABASE_PATH, MODEL_PATH
import sqlite3
import joblib

def load_data_for_model():
    """Load relevant data for training the readmission prediction model."""
    conn = sqlite3.connect(DATABASE_PATH)
    query = '''
    SELECT e.patient_id, p.age, e.diagnosis, e.length_of_stay, e.readmission_within_30_days,
           COUNT(e.encounter_id) AS prior_visits, 
           MAX(l.test_result) AS max_lab_result
    FROM encounters e
    JOIN patients p ON e.patient_id = p.patient_id
    LEFT JOIN lab_results l ON e.patient_id = l.patient_id
    GROUP BY e.patient_id
    '''
    data = pd.read_sql(query, conn)
    conn.close()
    return data

def preprocess_data(data):
    """Preprocess data for model training."""
    data['diagnosis'] = data['diagnosis'].map({
        'Diabetes': 1, 'Hypertension': 2, 'Pneumonia': 3, 'Cancer': 4, 'Heart Disease': 5
    })
    X = data[['age', 'diagnosis', 'length_of_stay', 'prior_visits', 'max_lab_result']]
    y = data['readmission_within_30_days']
    return X, y

def train_and_save_model(X, y):
    """Train the model and save it to disk."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate the model
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Save the trained model
    joblib.dump(clf, MODEL_PATH)

def main():
    data = load_data_for_model()
    X, y = preprocess_data(data)
    train_and_save_model(X, y)

if __name__ == "__main__":
    main()
