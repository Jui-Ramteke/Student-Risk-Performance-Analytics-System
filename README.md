# ⚡ Student Risk & Performance Analytics System

An AI-powered system designed to predict student performance, identify at-risk students, and provide actionable insights using machine learning and data analytics.

---

## 📌 Overview

This project is a complete **end-to-end Machine Learning + Analytics platform** that helps educational institutions:

- Predict student performance
- Identify at-risk students early
- Provide explainable insights
- Enable data-driven decision making

It combines **ML models, explainable AI (SHAP), and interactive dashboards** to simulate real-world EdTech systems.

---

## ❗ Problem Statement

Educational institutions often struggle to:

- Identify weak students early
- Understand factors affecting performance
- Take timely intervention actions
- Analyze large-scale student data effectively

This system solves these challenges using **predictive analytics and AI-driven insights**.

---

## 🌍 Industry Relevance

This project reflects real-world applications used by:

- EdTech platforms (Coursera, Byju’s, Udemy)
- Schools & universities
- Learning management systems (LMS)
- Academic analytics tools

Use cases:

- Dropout prediction
- Personalized learning
- Student engagement analysis
- Performance optimization

---

## 🧰 Tech Stack

**Programming**
- Python

**Libraries**
- Pandas, NumPy
- Scikit-learn
- SHAP (Explainable AI)
- Matplotlib

**Frontend**
- Streamlit (Dashboard UI)

**Other**
- Joblib (model saving)
- Git & GitHub

---

## 🏗️ Architecture

**Flow:**
1. Data ingestion (CSV)
2. Schema validation
3. Feature engineering
4. Model prediction (LogReg / RF)
5. Risk scoring
6. SHAP explainability
7. Visualization in dashboard

---

## 📂 Folder Structure
Student-Risk-Performance-Analytics-System/
│
├── data/
├── models/
├── src/
│ ├── feature_engineering.py
│ ├── evaluate_model.py
│ ├── explain.py
│ ├── drift.py
│ ├── recommend.py
│ ├── utils.py
│
├── images/
│ ├── 1.png
│ ├── 2.png
│ ├── 3.png
│ ├── 4.png
│ ├── 5.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Installation

```bash
git clone https://github.com/Jui-Ramteke/Student-Risk-Performance-Analytics-System.git

cd Student-Risk-Performance-Analytics-System

python -m venv venv

venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

▶️ How to Run

streamlit run app.py

Then open in browser:

http://localhost:8501

## 📊 Dashboard Screenshots

### 🔹 1. Main Dashboard Overview
![Dashboard](images/1.png)

This is the main interface of the system showing key KPIs:
- Total students
- Number of at-risk students
- Risk percentage
- Average performance score  
It provides a quick high-level summary for decision-making.

---

### 🔹 2. Risk Trend Analysis
![Trends](images/2.png)

Displays how student risk changes over time.  
Helps in identifying patterns such as increasing risk trends or unstable performance behavior.

---

### 🔹 3. Model Performance Metrics
![Performance](images/3.png)

Shows evaluation metrics of the model:
- ROC-AUC
- F1 Score
- Brier Score  

These metrics validate the reliability and effectiveness of the prediction system.

---

### 🔹 4. Explainability (SHAP Analysis)
![Explainability](images/4.png)

Visualizes feature importance using SHAP:
- Highlights which factors influence predictions
- Helps understand why a student is classified as at-risk  

This is critical for building trust in ML systems.

---

### 🔹 5. Feature Relationship Analysis
![Insights](images/5.png)

Scatter plot showing relationship between study hours and performance.  
Reveals strong correlation patterns and supports data-driven insights.

---

📈 Results

* Accurate prediction of student risk levels

* Identification of key performance drivers

* Real-time analytics dashboard

* Explainable AI insights using SHAP

*Evaluation metrics:

  * ROC-AUC
  * F1 Score
  * Brier Score

🎯 Key Features

✅ Student risk prediction

✅ Multi-model system (LogReg, RF)

✅ Feature engineering pipeline

✅ Batch + single prediction

✅ SHAP explainability

✅ Drift detection

✅ Advisor panel (high-risk students)

✅ Search & filtering

✅ Interactive dashboard


📚 Learning Outcomes

Through this project, I learned:

* End-to-end ML pipeline design

* Feature engineering techniques

* Model evaluation & validation

* Explainable AI using SHAP

* Dashboard development using Streamlit

* Handling real-world ML issues (feature mismatch, drift)

* Building industry-oriented projects

👨‍💻 Author Jui Ramteke

Email: juiramteke20@gmail.com

GitHub: https://github.com/Jui-Ramteke

LinkedIn: https://www.linkedin.com/in/jui-ramteke/

Instagram: https://www.instagram.com/jui_ramteke_/