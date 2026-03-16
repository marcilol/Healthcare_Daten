# 🏥 Healthcare Analytics Dashboard

https://healthcaredaten.streamlit.app/


Ein kleines **End-to-End Data Science und Data Engineering Projekt**, das ein
Krankenhausnetzwerk simuliert und Analysen zu Patienten,
Krankenhausaufenthalten und Wiederaufnahmerisiken bereitstellt.

Das Projekt umfasst:

-   Generierung synthetischer Gesundheitsdaten
-   Aufbau einer Datenpipeline
-   Training eines Machine-Learning-Modells
-   Entwicklung eines interaktiven Analytics Dashboards
-   Deployment als Web-App

Das Ziel hiermit ist, typische **Healthcare Analytics Workflows** zu
demonstrieren, wie sie in Krankenhäusern, Versicherungen oder
Health-Tech-Unternehmen verwendet werden könnten.

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
-   Matplotlib

**Versionierung & Deployment**

-   Git
-   GitHub
-   Streamlit Cloud

------------------------------------------------------------------------

# ⚙️ Features

## 1️⃣ Synthetischer Healthcare Datensatz

In diesem Projekt habe ich folgende realistisch strukturierte Gesundheitsdaten generiert:

-   5.000 Patienten
-   20.000 Krankenhausaufenthalte
-   Laborergebnisse
-   Medikationsdaten
-   Diagnosen
-   Krankenhausstandorte

------------------------------------------------------------------------

## 2️⃣ Datenpipeline (ETL)

Eine Python-basierte ETL-Pipeline verarbeitet die Daten:

**Schritte**

1.  Generierung synthetischer Rohdaten
2.  Datenbereinigung
3.  Transformation in ein Analyseformat
4.  Speicherung in einer SQLite-Datenbank
5.  Erstellung eines Analytics-Datensatzes für Machine Learning


------------------------------------------------------------------------

## 3️⃣ Machine Learning Modell

Trainiert wurde ein Modell zur Vorhersage von **30-Tage
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
Die Genauigkeit und Aussagekraft dieses einfachen Modells ist natürlich begrenzt und dient nur der Veranschaulichung.

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

Simuliert ein typisches **Clinical Decision Support System**.

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

