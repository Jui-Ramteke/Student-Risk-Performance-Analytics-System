def detect_drift(train_df, new_df):
    train_mean = train_df.mean(numeric_only=True)
    new_mean = new_df.mean(numeric_only=True)
    drift = (train_mean - new_mean).abs()
    return drift