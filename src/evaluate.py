import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

model = joblib.load("models/model.pkl")

data = pd.read_csv("data/student_data.csv")

X = data.drop("final_score", axis=1)
y = data["final_score"]

preds = model.predict(X)

mse = mean_squared_error(y, preds)
rmse = np.sqrt(mse)
r2 = r2_score(y, preds)

print(f"RMSE: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")