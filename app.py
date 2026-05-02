import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import shap

from src.feature_engineering import create_features
from src.risk import risk_category
from src.drift import detect_drift
from src.recommend import recommend
from src.data_loader import load_and_validate
from src.evaluate_model import evaluate_model
from src.explain import get_explainer, get_shap_values, get_class_shap
from src.utils import get_model_features

from sklearn.model_selection import train_test_split

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- UI ----------------
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg,#05060A,#0A0F1C); color:#E5E7EB; }
.block-container { padding-top:1rem; padding-left:2rem; padding-right:2rem; }

section[data-testid="stSidebar"] {
    background:#0B0F1A;
    border-right:1px solid #1E293B;
}

.card {
    background:#0B0F1A;
    padding:20px;
    border-radius:12px;
    border:1px solid rgba(255,255,255,0.08);
    margin-bottom:16px;
}

.kpi {
    background:#111827;
    padding:16px;
    border-radius:10px;
    text-align:center;
}

.stButton button {
    background:linear-gradient(90deg,#6366F1,#22D3EE);
    color:white;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## ⚙ Control Panel")

model_name = st.sidebar.selectbox("Model", ["logreg", "rf"])
mode = st.sidebar.radio("Mode", ["Single", "Batch"])

model = joblib.load(f"models/{model_name}.pkl")

# ---------------- LAYOUT ----------------
col_center, col_right = st.columns([3,1])

df_global = None
prediction_result = None

# ================= RIGHT PANEL =================
with col_right:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔮 Prediction")

    attendance = st.slider("Attendance",0,100,70)
    quiz = st.slider("Quiz Avg",0,100,60)
    study = st.slider("Study Hours",0,10,5)
    lms = st.slider("LMS Logins",0,50,10)
    assign = st.slider("Assignment Avg",0,100,65)
    submit = st.slider("On-time Submit %",0,100,80)

    if st.button("Predict"):
        df_single = pd.DataFrame([{
            "attendance":attendance,
            "quiz_avg":quiz,
            "study_hours":study,
            "lms_logins":lms,
            "assign_avg":assign,
            "on_time_submit_pct":submit
        }])

        df_single = create_features(df_single)

        prob = model.predict_proba(df_single)[0][1]
        category = risk_category(prob)

        prediction_result = (prob,category,df_single)

    st.markdown('</div>', unsafe_allow_html=True)

    # RESULT
    if prediction_result:
        prob,category,df_single = prediction_result

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📊 Result")

        st.write(f"Risk: {category}")
        st.write(f"Probability: {prob:.2f}")

        # SHAP FIXED
        explainer = get_explainer(model, df_single)
        shap_values = get_shap_values(explainer, df_single)
        shap_values = get_class_shap(shap_values)

        fig = plt.figure()
        shap.plots.waterfall(shap_values[0], show=False)
        st.pyplot(fig)

        st.write("### 💡 Recommendation")
        st.write(recommend(df_single.iloc[0]))

        st.markdown('</div>', unsafe_allow_html=True)

    # Upload
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📂 Upload CSV")

    file = st.file_uploader("Upload Student Data")

    if file:
        df = load_and_validate(file)
        df = create_features(df)

        probs = model.predict_proba(df)[:,1]
        df["risk_prob"] = probs
        df["risk_category"] = df["risk_prob"].apply(risk_category)
        df["recommendation"] = df.apply(recommend, axis=1)

        df_global = df

    st.markdown('</div>', unsafe_allow_html=True)

# ================= CENTER =================
with col_center:

    st.markdown("## ⚡ Student Risk & Performance Analytics System")

    if df_global is not None:
        total = len(df_global)
        at_risk = len(df_global[df_global["risk_category"]=="HIGH RISK"])
        risk_pct = (at_risk/total)*100
        avg_score = df_global["quiz_avg"].mean()
    else:
        total = at_risk = risk_pct = avg_score = 0

    k1,k2,k3,k4 = st.columns(4)
    k1.markdown(f"<div class='kpi'><h4>Total</h4><h2>{total}</h2></div>",unsafe_allow_html=True)
    k2.markdown(f"<div class='kpi'><h4>At Risk</h4><h2>{at_risk}</h2></div>",unsafe_allow_html=True)
    k3.markdown(f"<div class='kpi'><h4>Risk %</h4><h2>{risk_pct:.1f}%</h2></div>",unsafe_allow_html=True)
    k4.markdown(f"<div class='kpi'><h4>Avg Score</h4><h2>{avg_score:.1f}</h2></div>",unsafe_allow_html=True)

    tab1,tab2,tab3,tab4 = st.tabs(["Trends","Segments","Performance","Explain"])

    if df_global is not None:

        with tab1:
            df_global["week"]=range(len(df_global))
            st.line_chart(df_global.groupby("week")["risk_prob"].mean())

        with tab3:
            y=(df_global["risk_category"]=="HIGH RISK").astype(int)
            X=get_model_features(df_global)

            X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

            metrics=evaluate_model(model,X_test,y_test)

            st.metric("ROC-AUC",f"{metrics['roc_auc']:.2f}")
            st.metric("F1",f"{metrics['f1']:.2f}")
            st.metric("Brier",f"{metrics['brier']:.2f}")

        with tab4:
            X=get_model_features(df_global)
            X_sample=X.sample(min(50,len(X)))

            explainer=get_explainer(model,X_sample)
            shap_values=get_shap_values(explainer,X_sample)
            shap_values=get_class_shap(shap_values)

            fig=plt.figure()
            shap.plots.bar(shap_values,show=False)
            st.pyplot(fig)

        st.dataframe(df_global)

    else:
        st.info("Upload CSV to start")