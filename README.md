# 🏦 Credit Risk Intelligence Platform

### AI-Powered Loan Default Prediction using XGBoost & Streamlit

An end-to-end Machine Learning application that predicts the probability of customer loan default and generates business-oriented risk assessment reports to support lending decisions.

---

## 📌 Project Overview

Financial institutions face significant losses due to loan defaults. The objective of this project is to build an intelligent credit risk assessment system capable of identifying high-risk borrowers before loan approval.

This platform:

- Predicts customer default probability
- Classifies borrowers into risk categories
- Generates customer-specific risk reports
- Provides business recommendations
- Visualizes risk insights through an interactive dashboard

---

## 🚀 Live Demo

[Credit Risk Intelligence Platform](#)

---

## 📊 Problem Statement

Given a customer's personal, financial, and loan information, predict whether the customer is likely to default on a loan.

Target Variable:

```text
loan_status

1 → Defaulter
0 → Non-Defaulter
```

---

## 📂 Dataset

Dataset Used:

**Credit Risk Dataset**

The dataset contains borrower information such as:

- Age
- Annual Income
- Employment Length
- Home Ownership
- Loan Amount
- Loan Intent
- Loan Grade
- Loan Interest Rate
- Loan Percent Income
- Credit History Length
- Previous Default on File

The dataset is not included in this repository due to licensing and repository size considerations.

---

## ⚙️ Feature Engineering

Additional business-oriented features were created:

### LoanToIncomeAmount

```text
Loan Amount ÷ Annual Income
```

Measures the loan burden relative to the borrower's income.

### Categorical Encoding

```text
One-Hot Encoding applied to:
- Home Ownership
- Loan Intent
- Loan Grade
- Previous Default on File
```

Converts categorical borrower attributes into model-ready numerical features.

---

## 🤖 Models Evaluated

### Logistic Regression

Used as a baseline model.

### XGBoost Classifier

Selected as the final model due to:

- Better handling of non-linear relationships
- Higher predictive performance
- Stronger generalization capability

---

## 📈 Model Performance

| Metric | Value |
|----------|----------|
| ROC-AUC | 0.93 |
| Model | XGBoost |
| Decision Threshold | 0.20 |

### Threshold Optimization

Instead of using the default threshold of 0.50, the decision threshold was optimized to 0.20 to improve recall and identify a larger proportion of potential defaulters.

This approach aligns better with real-world lending scenarios where missing a defaulter is more costly than flagging a few additional customers for review.

---

## 🛠️ Tech Stack

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Machine Learning

- Scikit-Learn
- XGBoost

### Explainability

- SHAP

### Visualization

- Matplotlib
- Plotly

### Deployment

- Streamlit

### Version Control

- Git
- GitHub

---

## 🖥️ Application Features

### Risk Assessment Dashboard

- Customer Information Input
- Loan & Financial Details
- Real-Time Prediction
- Risk Probability Gauge

### Customer Risk Analysis Report

- Executive Summary
- Risk Classification
- Key Risk Drivers
- Business Recommendation

### Model Insights

- Feature Importance
- SHAP Explainability
- Model Performance Overview

---

## 📸 Application Screenshots

### Home Page

![Homepage](screenshots/Homepage.png)

---

### Risk Prediction

![Prediction](screenshots/Risk_Gauge.png)

---

## 📁 Project Structure

```text
Credit-Risk-Intelligence-Platform/

├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── models/
│   └── loan_default_xgb.pkl
│
├── notebooks/
│   └── model.ipynb
│
├── assets/
│   ├── feature_importance.png
│   └── shap_summary.png
│
├── data/
│   └── credit_risk_dataset.csv
│
└── screenshots/
```

---

## 🔮 Future Improvements

- PDF Risk Reports
- Dynamic Threshold Adjustment
- Database Integration
- User Authentication
- Portfolio Analytics Dashboard
- Cloud Deployment Enhancements

---

## 🎯 Key Learnings

Through this project I gained hands-on experience with:

- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Feature Engineering
- Classification Models
- ROC-AUC Evaluation
- Threshold Optimization
- Explainable AI (SHAP)
- Streamlit Application Development
- Git & GitHub Workflow
- End-to-End Machine Learning Deployment

---

## 👨‍💻 Author

yash viramgama

Interested in:

- Data Science
- Machine Learning
- Analytics
- AI-Powered Business Solutions

---
⭐ If you found this project interesting, feel free to star the repository.
