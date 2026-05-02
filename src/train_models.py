import pandas as pd
import joblib
import os

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from src.feature_engineering import create_features

os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/student_data.csv")

# Feature engineering
df = create_features(df)

# Create target (binary classification)
df["risk"] = (df["final_score"] < 60).astype(int)

X = df.drop(["final_score", "risk"], axis=1)
y = df["risk"]

# Train models
logreg = LogisticRegression(max_iter=1000)
rf = RandomForestClassifier()

logreg.fit(X, y)
rf.fit(X, y)

# Save models
joblib.dump(logreg, "models/logreg.pkl")
joblib.dump(rf, "models/rf.pkl")

print("✅ Models saved in /models folder")