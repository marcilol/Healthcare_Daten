# 🏥 Healthcare Analytics Dashboard

https://healthcaredaten.streamlit.app/


Ein **End-to-End Data Science und Data Engineering Projekt**, das ein
Krankenhausnetzwerk simuliert und Analysen zu Patienten,
Krankenhausaufenthalten und Wiederaufnahmerisiken bereitstellt.

Das Projekt umfasst:

-   Generierung synthetischer Gesundheitsdaten
-   Aufbau einer Datenpipeline
-   Training eines Machine-Learning-Modells
-   Entwicklung eines interaktiven Analytics Dashboards
-   Deployment als Web-App

Das Ziel ist es, typische **Healthcare Analytics Workflows** zu
demonstrieren, wie sie in Krankenhäusern, Versicherungen oder
Health-Tech-Unternehmen verwendet werden.

------------------------------------------------------------------------

# 🎯 Projektübersicht

Das System simuliert ein Netzwerk aus Krankenhäusern mit tausenden
Patienten und Aufenthalten.\
Auf Basis dieser Daten werden Analysen durchgeführt und ein Modell
trainiert, das das **30-Tage-Wiederaufnahmerisiko (Hospital Readmission
Risk)** vorhersagt.

Das interaktive Dashboard ermöglicht es, wichtige Kennzahlen zu
visualisieren und Patientendaten zu analysieren.

------------------------------------------------------------------------

# 🧰 Verwendeter Tech-Stack

**Programmiersprache**

-   Python

**Datenverarbeitung**

-   Pandas
-   NumPy

**Machine Learning**

-   Scikit-learn
-   RandomForestClassifier

**Datenbank**

-   SQLite

**Dashboard**

-   Streamlit

**Versionierung & Deployment**

-   Git
-   GitHub
-   Streamlit Cloud

------------------------------------------------------------------------

# 📊 Datenmodell

Das Projekt simuliert mehrere miteinander verbundene Datentabellen:

  Tabelle       Beschreibung
  ------------- ------------------------
  patients      Patientendemografie
  encounters    Krankenhausaufenthalte
  lab_results   Laborwerte
  medications   Medikationen
  hospitals     Krankenhausstandorte

------------------------------------------------------------------------

# ⚙️ Features

## 1️⃣ Synthetischer Healthcare Datensatz

Das Projekt generiert realistisch strukturierte Gesundheitsdaten:

-   50.000 Patienten
-   200.000 Krankenhausaufenthalte
-   Laborergebnisse
-   Medikationsdaten
-   Diagnosen
-   Krankenhausstandorte

Die Daten werden vollständig synthetisch generiert, um
Datenschutzprobleme zu vermeiden, behalten jedoch eine realistische
Struktur.

------------------------------------------------------------------------

## 2️⃣ Datenpipeline (ETL)

Eine Python-basierte ETL-Pipeline verarbeitet die Daten:

**Schritte**

1.  Generierung synthetischer Rohdaten
2.  Datenbereinigung
3.  Transformation in ein Analyseformat
4.  Speicherung in einer SQLite-Datenbank
5.  Erstellung eines Analytics-Datensatzes für Machine Learning

Dies simuliert typische **Data Engineering Workflows in Healthcare
Analytics**.

------------------------------------------------------------------------

## 3️⃣ Machine Learning Modell

Das Projekt trainiert ein Modell zur Vorhersage von **30-Tage
Krankenhaus-Wiederaufnahmen**.

Verwendeter Algorithmus:

-   Random Forest Classifier

Das Modell nutzt folgende Features:

-   Alter des Patienten
-   Diagnosekategorie
-   Anzahl vorheriger Krankenhausbesuche
-   Länge des Krankenhausaufenthalts
-   Laborwerte

Das Modell berechnet einen **Readmission Risk Score**, der im Dashboard
visualisiert wird.

------------------------------------------------------------------------

## 4️⃣ Interaktives Analytics Dashboard

Das Dashboard wurde mit **Streamlit** entwickelt und stellt mehrere
Analysebereiche bereit.

### Executive Overview

Zeigt zentrale KPIs:

-   Gesamtanzahl Patienten
-   Gesamtanzahl Krankenhausbesuche
-   Durchschnittliche Aufenthaltsdauer
-   Wiederaufnahmerate

------------------------------------------------------------------------

### Chronische Erkrankungen Analyse

Analysiert die Verteilung häufiger chronischer Krankheiten wie:

-   Diabetes
-   Hypertonie
-   Herzkrankheiten

Visualisierungen zeigen die Verteilung und Häufigkeit der Diagnosen.

------------------------------------------------------------------------

### Krankenhausauslastung

Analysiert die Nutzung verschiedener Krankenhäuser.

Beispielanalysen:

-   Aufenthalte pro Krankenhaus
-   Besuchstypen
-   Diagnoseverteilung

------------------------------------------------------------------------

### Wiederaufnahmerisiko Vorhersage

Ein integriertes Machine-Learning-Modul ermöglicht:

-   Auswahl eines Patienten
-   Berechnung des individuellen Wiederaufnahmerisikos
-   Visualisierung als Risikoscore

Dies simuliert typische **Clinical Decision Support Systeme**.

------------------------------------------------------------------------

## 5️⃣ Interaktive Filter

Das Dashboard enthält interaktive Filter zur Datenexploration:

-   Krankenhausfilter
-   Diagnosefilter
-   Patientenauswahl

Dies ermöglicht flexible Analyse verschiedener Patientengruppen.

------------------------------------------------------------------------

# 📈 Beispielvisualisierungen

Das Dashboard enthält mehrere Visualisierungen:

-   KPI-Metriken
-   Balkendiagramme
-   Verteilungsdiagramme
-   Diagnosenanalyse
-   Krankenhausauslastung

------------------------------------------------------------------------

# 🚀 Deployment

Die Anwendung kann lokal oder in der Cloud gestartet werden.

## Lokal starten

``` bash
streamlit run app.py
```

Das Dashboard ist anschließend unter folgendem Link erreichbar:

    http://localhost:8501

------------------------------------------------------------------------

## Deployment mit Streamlit Cloud

1.  Repository auf GitHub hochladen
2.  Bei Streamlit Cloud anmelden
3.  Repository auswählen
4.  `app.py` als Startdatei wählen
5.  Deployment starten

Nach dem Deployment ist das Dashboard über eine öffentliche URL
erreichbar.

------------------------------------------------------------------------

# 📁 Projektstruktur

    healthcare-analytics/
    │
    ├── data/
    │   ├── raw/
    │   └── processed/
    │
    ├── src/
    │   ├── data_generation/
    │   ├── etl/
    │   ├── model/
    │   └── utils/
    │
    ├── dashboard/
    │   └── app.py
    │
    ├── models/
    │   └── readmission_model.pkl
    │
    ├── healthcare_data.db
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# 🎓 Ziel des Projekts

Dieses Projekt demonstriert Fähigkeiten in:

-   Data Engineering
-   Machine Learning
-   Datenvisualisierung
-   Datenbankintegration
-   End-to-End Data Science Workflows
-   Deployment von Datenanwendungen

------------------------------------------------------------------------

# 📄 Lizenz

Dieses Projekt dient zu Demonstrations- und Lernzwecken.
