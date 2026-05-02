import numpy as np
from sklearn.metrics import (
    confusion_matrix,
    roc_auc_score,
    f1_score,
    brier_score_loss,
    roc_curve
)

def evaluate_model(model, X, y):
    probs = model.predict_proba(X)[:, 1]
    preds = (probs > 0.5).astype(int)

    cm = confusion_matrix(y, preds)
    auc = roc_auc_score(y, probs)
    f1 = f1_score(y, preds)
    brier = brier_score_loss(y, probs)

    fpr, tpr, _ = roc_curve(y, probs)

    return {
        "conf_matrix": cm,
        "roc_auc": auc,
        "f1": f1,
        "brier": brier,
        "fpr": fpr,
        "tpr": tpr
    }