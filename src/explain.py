import shap

def get_explainer(model, X_sample):
    try:
        explainer = shap.TreeExplainer(model)
    except:
        explainer = shap.Explainer(model, X_sample)
    return explainer

def get_shap_values(explainer, X):
    return explainer(X)

def get_class_shap(shap_values):
    """
    Fix for classification models (prevents waterfall error)
    """
    if len(shap_values.values.shape) == 3:
        return shap_values[:,:,1]  # class 1
    return shap_values