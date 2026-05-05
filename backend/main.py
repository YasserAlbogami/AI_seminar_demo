import os
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Load the trained model from the project root (one level above this file)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "..", "senior_classifier_model.pkl"))

app = FastAPI(title="Senior Student Classifier")

# Allow all origins so the HTML file can be opened directly from the filesystem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

# The six course completion features the model was trained on
FEATURES = ["DS204", "Algo223", "OS361", "AI331", "Compiler302", "Training323"]


class StudentInput(BaseModel):
    DS204: str
    Algo223: str
    OS361: str
    AI331: str
    Compiler302: str
    Training323: str


@app.post("/predict")
def predict(student: StudentInput):
    # Convert Yes/No strings to 1/0
    encode = {"Yes": 1, "No": 0}
    values = [encode[getattr(student, feature)] for feature in FEATURES]

    # Build a DataFrame so sklearn sees the correct feature names
    df = pd.DataFrame([values], columns=FEATURES)

    result = model.predict(df)[0]
    label = "Senior" if result == 1 else "Not Senior"

    print(f"Received input: {student}")
    print(f"Prediction: {label}")

    return {"prediction": label}
