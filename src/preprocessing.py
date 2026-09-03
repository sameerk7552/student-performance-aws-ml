import pandas as pd
from sklearn.model_selection import train_test_split


# 1. Load dataset
df = pd.read_csv("data/student_performance.csv")

print("Original Dataset:")
print(df.head())


# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())


# 3. Separate features and target
X = df.drop("final_score", axis=1)
y = df["final_score"]


# 4. Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. Display shapes
print("\nTraining Data:")
print(X_train.shape)

print("\nTesting Data:")
print(X_test.shape)


# 6. Save processed datasets
train_data = X_train.copy()
train_data["final_score"] = y_train

test_data = X_test.copy()
test_data["final_score"] = y_test


train_data.to_csv("data/train.csv", index=False)
test_data.to_csv("data/test.csv", index=False)


print("\nPreprocessing completed successfully!")
print("train.csv and test.csv created.")