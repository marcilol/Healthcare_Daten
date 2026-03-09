import streamlit as st
import pandas as pd
import sqlite3
import joblib
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Hospital Analytics Dashboard",
    layout="wide"
)

st.title("🏥 Healthcare Analytics Dashboard")

# -------------------------
# Load Data
# -------------------------

conn = sqlite3.connect("healthcare_data.db")

data = pd.read_sql("""
SELECT 
    e.*,
    p.age
FROM encounters e
JOIN patients p
ON e.patient_id = p.patient_id
""", conn)

model = joblib.load("readmission_model.pkl")

# -------------------------
# Sidebar Filters
# -------------------------

st.sidebar.header("Filters")

hospital_filter = st.sidebar.multiselect(
    "Select Hospital",
    options=sorted(data["hospital_id"].unique()),
    default=sorted(data["hospital_id"].unique())
)

diagnosis_filter = st.sidebar.multiselect(
    "Diagnosis",
    options=sorted(data["diagnosis"].unique()),
    default=sorted(data["diagnosis"].unique())
)

filtered_data = data[
    (data["hospital_id"].isin(hospital_filter)) &
    (data["diagnosis"].isin(diagnosis_filter))
]

# -------------------------
# KPI Metrics
# -------------------------

total_patients = filtered_data["patient_id"].nunique()
total_visits = filtered_data.shape[0]
readmission_rate = filtered_data["readmission_within_30_days"].mean()*100
avg_los = filtered_data["length_of_stay"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", f"{total_patients:,}")
col2.metric("Total Visits", f"{total_visits:,}")
col3.metric("Readmission Rate", f"{readmission_rate:.2f}%")
col4.metric("Avg Length of Stay", f"{avg_los:.2f} days")

st.divider()

# -------------------------
# Tabs
# -------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "Executive Overview",
    "Chronic Disease Analysis",
    "Hospital Utilization",
    "Readmission Risk Prediction"
])

# -------------------------
# Executive Overview
# -------------------------

with tab1:

    st.subheader("Visits by Diagnosis")

    diagnosis_counts = filtered_data["diagnosis"].value_counts()

    fig, ax = plt.subplots()
    ax.bar(diagnosis_counts.index, diagnosis_counts.values)
    ax.set_ylabel("Visits")
    ax.set_xlabel("Diagnosis")
    plt.xticks(rotation=45)

    st.pyplot(fig)

# -------------------------
# Chronic Disease Analysis
# -------------------------

with tab2:

    st.subheader("Chronic Disease Distribution")

    disease_counts = filtered_data["diagnosis"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        disease_counts,
        labels=disease_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

# -------------------------
# Hospital Utilization
# -------------------------

with tab3:

    st.subheader("Hospital Utilization")

    hospital_visits = filtered_data["hospital_id"].value_counts()

    fig, ax = plt.subplots()

    ax.bar(hospital_visits.index, hospital_visits.values)

    ax.set_xlabel("Hospital ID")
    ax.set_ylabel("Visits")

    st.pyplot(fig)

# -------------------------
# Readmission Prediction
# -------------------------

with tab4:

    st.subheader("Predict 30-Day Readmission Risk")

    patient_id_input = st.selectbox(
        "Select Patient ID",
        sorted(filtered_data["patient_id"].unique())
    )

    patient_rows = filtered_data[
        filtered_data["patient_id"] == patient_id_input
    ]

    if patient_rows.empty:
        st.warning("No encounter data available.")
    else:

        patient_data = patient_rows.iloc[0]

        features = pd.DataFrame([{
            "age": patient_data["age"],
            "diagnosis": 1,
            "length_of_stay": patient_data["length_of_stay"],
            "prior_visits": patient_rows.shape[0],
            "max_lab_result": 100
        }])

        prediction = model.predict_proba(features)[0][1]

        st.metric(
            "Predicted Readmission Risk",
            f"{prediction:.2%}"
        )

        if prediction > 0.5:
            st.error("High Risk Patient")
        else:
            st.success("Low Risk Patient")
