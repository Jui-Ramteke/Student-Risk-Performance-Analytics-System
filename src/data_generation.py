import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

np.random.seed(42)
n = 500

data = pd.DataFrame({
    "attendance": np.random.uniform(40, 100, n),
    "quiz_avg": np.random.uniform(30, 100, n),
    "study_hours": np.random.uniform(1, 10, n),
    "lms_logins": np.random.randint(0, 50, n),
    "assign_avg": np.random.uniform(30, 100, n),
    "on_time_submit_pct": np.random.uniform(40, 100, n)
})

# Create final score
data["final_score"] = (
    data["attendance"] * 0.2 +
    data["quiz_avg"] * 0.3 +
    data["study_hours"] * 2 +
    data["assign_avg"] * 0.3 +
    np.random.normal(0, 5, n)
)

data.to_csv("data/student_data.csv", index=False)

print("✅ New dataset created with correct schema")