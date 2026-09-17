# Maternal Health Risk Prediction

A machine learning project that classifies maternal health risk into **Low Risk, Mid Risk, and High Risk** using key health indicators such as age, blood pressure, blood sugar, body temperature, and heart rate.

The project focuses on understanding the complete machine learning workflow, from data exploration and preprocessing to model training, evaluation, and prediction on new patient data.

> **Disclaimer:** This project is developed for educational and research purposes only. It is not a medical diagnostic system and should not be used to make clinical decisions.

---

## 📌 Project Overview

Maternal health can be influenced by several measurable health indicators, including blood pressure, blood sugar, body temperature, and heart rate.

This project uses these indicators to build a **multiclass classification model** capable of predicting one of three risk categories:

- **Low Risk**
- **Mid Risk**
- **High Risk**

Two machine learning algorithms were explored:

1. Logistic Regression — baseline model
2. Random Forest Classifier — primary model

The Random Forest model achieved **87.19% accuracy** on the held-out test set used in this project.

---

## 🎯 Objectives

The main objectives of this project are:

- Understand and analyze maternal health data
- Perform exploratory data analysis (EDA)
- Identify relationships between health indicators and risk levels
- Prepare the dataset for machine learning
- Build a multiclass classification model
- Compare different machine learning algorithms
- Evaluate model performance using multiple metrics
- Generate predictions for new input data
- Understand the practical limitations of machine learning in healthcare

---

## 📊 Dataset

The project uses the **Maternal Health Risk Data** dataset.

### Dataset Sources

- Kaggle: [Maternal Health Risk Data](https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data)
- UCI Machine Learning Repository: [Maternal Health Risk](https://archive.ics.uci.edu/dataset/863/maternal+health+risk)

The dataset used in this project contains **1,014 records**.

---

## 🧾 Features

The model uses six input features:

| Feature | Description |
|---|---|
| `Age` | Age of the mother |
| `SystolicBP` | Systolic blood pressure |
| `DiastolicBP` | Diastolic blood pressure |
| `BS` | Blood sugar level |
| `BodyTemp` | Body temperature |
| `HeartRate` | Heart rate |

### Target Variable

The target variable is:

```text
RiskLevel
