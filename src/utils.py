def get_model_features(df):
    """
    Keep only features used during training
    """
    return df.drop(
        ["risk_prob", "risk_category", "recommendation", "week"],
        axis=1,
        errors="ignore"
    )