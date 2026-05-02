import joblib
import numpy as np

model = joblib.load("models/model.pkl")

# Example student
sample = np.array([[6, 85, 7, 8]])

prediction = model.predict(sample)

print(f"🎯 Predicted Score: {prediction[0]:.2f}")