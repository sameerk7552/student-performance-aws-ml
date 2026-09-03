import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1. Load training and testing data
train_data = pd.read_csv("data/train.csv")
test_data = pd.read_csv("data/test.csv")


# 2. Separate features and target
X_train = train_data.drop("final_score", axis=1)
y_train = train_data["final_score"]

X_test = test_data.drop("final_score", axis=1)
y_test = test_data["final_score"]


# 3. Create ML model
model = LinearRegression()


# 4. Train the model
model.fit(X_train, y_train)


# 5. Make predictions
y_pred = model.predict(X_test)


# 6. Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("===== MODEL EVALUATION =====")

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)


# 7. Save trained model
joblib.dump(model, "model/model.pkl")

print("\nModel saved successfully!")
print("Location: model/model.pkl")