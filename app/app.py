from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib


app = FastAPI()


# Allow frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load ML model
model = joblib.load("model/model.pkl")


class StudentData(BaseModel):

    study_hours: float

    attendance: float

    previous_score: float

    assignments_completed: int


@app.get("/")
def home():

    return {
        "message": "Student Performance Prediction API is running"
    }


@app.post("/predict")
def predict(data: StudentData):

    student = pd.DataFrame({

        "study_hours": [data.study_hours],

        "attendance": [data.attendance],

        "previous_score": [data.previous_score],

        "assignments_completed": [
            data.assignments_completed
        ]

    })


    prediction = model.predict(student)[0]


    # Keep score between 0 and 100
    prediction = max(0, min(100, prediction))


    return {

        "predicted_final_score":
            round(prediction, 2)

    }