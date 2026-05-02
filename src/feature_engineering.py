def create_features(df):
    df["engagement_score"] = df["lms_logins"]
    df["performance_score"] = df["quiz_avg"] + df["assign_avg"]
    df["discipline_score"] = df["on_time_submit_pct"]

    return df