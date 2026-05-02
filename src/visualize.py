import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs", exist_ok=True)

data = pd.read_csv("data/student_data.csv")

plt.figure()
sns.scatterplot(x="study_hours", y="final_score", data=data)
plt.title("Study Hours vs Final Score")
plt.savefig("outputs/study_vs_score.png")

print("📊 Graph saved in outputs/")