import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/model.pkl")

# New student data
new_student = pd.DataFrame({
    "study_hours": [7],
    "attendance": [90],
    "previous_score": [80],
    "assignments_completed": [9]
})

# Make prediction
prediction = model.predict(new_student)

print("Predicted Final Score:", round(prediction[0], 2))