# Healthcare_Daten
Healthcare Datensatz und Auswertung
# Healthcare Analytics Project

This project simulates a healthcare environment, predicts patient readmission risk, and provides an interactive dashboard to explore hospital data.

## Setup

1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Generate synthetic data with `python src/data_generation/generate_data.py`.
4. Process and load data into the database with `python src/etl/etl_pipeline.py`.
5. Train the model with `python src/model/train_model.py`.
6. Run the Streamlit dashboard with `streamlit run dashboard/app.py`.

## Features
- Generate synthetic patient and hospital data
- Process data using an ETL pipeline
- Train and predict 30-day readmission risk using a RandomForest model
- Interactive dashboard for insights on healthcare data

## License
This project is licensed under the MIT License.
