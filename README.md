# ⚡ Student Risk & Performance Analytics System

An AI-powered system that predicts student performance, identifies at-risk students, and provides actionable insights using machine learning and analytics.

---

## 📌 Overview

This project is an **end-to-end Machine Learning + Analytics platform** designed to:

- Predict student performance
- Identify at-risk students early
- Provide explainable insights (SHAP)
- Enable data-driven decision-making

It simulates real-world **EdTech analytics systems** used in the industry.

---

## ❗ Problem Statement

Educational institutions often struggle to:

- Identify weak students early
- Understand performance drivers
- Take timely intervention actions
- Analyze large-scale student data

This system solves these issues using **predictive analytics and AI insights**.

---

## 🌍 Industry Relevance

This architecture and approach are actively used in:

- **EdTech platforms** (Coursera, Byju’s, Udemy)
- **Schools & Universities**
- **Learning Management Systems (LMS)**

### Use Cases:
- Dropout prediction
- Personalized learning paths
- Student engagement analysis
- Overall performance optimization

---

## 🧰 Tech Stack

* **Programming:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib
* **Explainable AI:** SHAP
* **Frontend UI:** Streamlit
* **Model Serialization:** Joblib
* **Version Control:** Git & GitHub

---

## 🏗️ Architecture

`Data` → `Validation` → `Feature Engineering` → `Model` → `Prediction` → `Explainability` → `Dashboard`

---

## 📂 Folder Structure
```text
Student-Risk-Performance-Analytics-System/
│
├── data/
├── models/
├── src/
│   ├── feature_engineering.py
│   ├── evaluate_model.py
│   ├── explain.py
│   ├── drift.py
│   ├── recommend.py
│   ├── utils.py
│
├── images/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

⚙️ Installation & How to Run

Follow these steps to run the project locally:

Clone the repository:

git clone [https://github.com/Jui-Ramteke/Student-Risk-Performance-Analytics-System.git](https://github.com/Jui-Ramteke/Student-Risk-Performance-Analytics-System.git)

cd Student-Risk-Performance-Analytics-System

Create and activate a virtual environment:

python -m venv venv

# Windows

venv\Scripts\activate  

# Linux/Mac

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

## 📈 Results

* **High-Accuracy Risk Prediction:** The Logistic Regression model achieved exceptional performance on the test cohort, successfully identifying at-risk students with a perfect **ROC-AUC of 1.00** and an **F1 Score of 1.00**.
* **Calibrated Probabilities:** Achieved a **Brier Score of 0.00**, indicating that the predicted probabilities of student risk are highly reliable and well-calibrated.
* **Actionable Intelligence:** Successfully isolated the most critical factors influencing student success (Study Hours, Attendance, and Previous Performance) to help educators focus on high-impact interventions.
* **Real-time Analytics Delivery:** Transformed a static machine learning model into a dynamic, real-time tool capable of processing both single inquiries and bulk student data instantly.

---

## 🎯 Key Features

* **Interactive Analytics Dashboard:** A clean, user-friendly UI built with Streamlit that visualizes complex data trends, risk segments, and key performance indicators.
* **Dual-Mode Prediction Engine:** 
  * *Single Mode:* Interactive sliders to adjust individual student metrics (attendance, study hours, etc.) and instantly see the predicted risk probability.
  * *Batch Mode:* Drag-and-drop CSV upload functionality to process and predict outcomes for entire classrooms or cohorts at once.
* **Explainable AI (XAI) Integration:** Uses SHAP (SHapley Additive exPlanations) to break down exactly *why* a model made a specific prediction, ensuring the AI's decisions are transparent to educators.
* **Automated Advisor Recommendations:** Generates specific, context-aware intervention strategies based on the individual student's risk profile to assist academic counselors.
* **Robust Feature Engineering:** A custom data pipeline that handles missing values, scales numerical features, and engineers new metrics (like engagement scores) to improve model accuracy.

---

## 📚 Learning Outcomes

By building this project, I demonstrated and strengthened the following skills:

* **End-to-End ML Engineering:** Managed the entire lifecycle of a machine learning project, from synthetic data generation and preprocessing to model training, evaluation, and deployment.
* **Explainable AI (XAI) Implementation:** Learned how to move beyond "black box" models by implementing SHAP values to build trust and interpretability into AI systems.
* **Full-Stack Data Science:** Bridged the gap between backend machine learning logic (Scikit-Learn, Pandas) and frontend user interfaces (Streamlit).
* **Translating Data into Business Value:** Focused not just on model accuracy, but on how the model's outputs can be used to solve a real-world business problem (improving student retention and academic success).


## 📊 Dashboard Screenshots

### 🔹 1. Main Dashboard & Interactive Prediction
<p align="center">
  <img src="./images/1.png" width="90%">
</p>
**Overview:** The primary interface featuring top-level KPIs (Total Students, At-Risk count, Risk Percentage, and Average Score). The central area displays risk trends and a detailed data table of student metrics. The right sidebar includes interactive sliders for running single-student predictions and a drag-and-drop CSV uploader for batch processing.

---

### 🔹 2. Prediction Results & Risk Assessment
<p align="center">
  <img src="./images/2.png" width="90%">
</p>
**Actionable Insights:** Showcases the result of a single student prediction. In this example, the model flags a "MEDIUM RISK" with a probability score of 0.55. It provides a visual breakdown of the contributing factors and a dedicated section for automated recommendations to assist academic advisors.

---

### 🔹 3. Model Performance Metrics
<p align="center">
  <img src="./images/3.png" width="90%">
</p>
**Validation:** The "Performance" tab highlights the rigorous evaluation of the active Logistic Regression model. It displays critical machine learning metrics, including a perfect ROC-AUC (1.00), F1 Score (1.00), and a Brier Score (0.00) on the test cohort, proving the model's reliability.

---

### 🔹 4. Explainable AI (SHAP Values)
<p align="center">
  <img src="./images/4.png" width="90%">
</p>
**Transparency:** The "Explain" tab utilizes SHAP (SHapley Additive exPlanations) to demystify the machine learning "black box." The bar chart clearly ranks feature importance, revealing that `performance_score`, `study_hours`, and `attendance` are the strongest predictors influencing the model's risk assessments.

---

### 🔹 5. Feature Correlation Insights
<p align="center">
  <img src="./images/5.png" width="90%">
</p>
**Data Exploration:** A scatter plot visualizing the relationship between "Study Hours" and "Final Score." This clearly demonstrates the strong positive correlation between increased study time and higher academic achievement, validating the fundamental assumptions of the predictive model.


👨‍💻 Author

Jui Ramteke

Email: juiramteke20@gmail.com

GitHub: https://github.com/Jui-Ramteke

LinkedIn: https://www.linkedin.com/in/jui-ramteke/