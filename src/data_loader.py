import pandas as pd

REQUIRED_COLUMNS = [
    "attendance",
    "quiz_avg",
    "study_hours",
    "lms_logins",
    "assign_avg",
    "on_time_submit_pct"
]

def load_and_validate(file_path):
    df = pd.read_csv(file_path)

    # Schema validation
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")

    # Missing value handling
    df.fillna(df.mean(numeric_only=True), inplace=True)

    return df