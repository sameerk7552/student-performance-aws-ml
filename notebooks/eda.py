import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/student_performance.csv")

# Basic information
print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# -----------------------------
# 1. Study Hours vs Final Score
# -----------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="study_hours",
    y="final_score",
    data=df
)

plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")

plt.show()


# -----------------------------
# 2. Attendance vs Final Score
# -----------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="attendance",
    y="final_score",
    data=df
)

plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")

plt.show()


# -----------------------------
# 3. Previous Score vs Final Score
# -----------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="previous_score",
    y="final_score",
    data=df
)

plt.title("Previous Score vs Final Score")
plt.xlabel("Previous Score")
plt.ylabel("Final Score")

plt.show()


# -----------------------------
# 4. Correlation Heatmap
# -----------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation")

plt.show()