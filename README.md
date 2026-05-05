# Senior Student Classifier — CPCS-331 AI Seminar

A full-stack ML demo that predicts whether a student is a **Senior** based on course completion history. Built with **FastAPI** and **scikit-learn**, it exposes a simple REST endpoint that any frontend can call via HTTP.

![python](https://img.shields.io/badge/python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-brightgreen)
![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange)
![pandas](https://img.shields.io/badge/pandas-latest-blue)
![joblib](https://img.shields.io/badge/joblib-latest-lightgrey)
![jupyter](https://img.shields.io/badge/jupyter-notebook-orange)
![license](https://img.shields.io/badge/license-MIT-green)
![status](https://img.shields.io/badge/status-complete-brightgreen)

## How to Run

**1. Install dependencies**
```bash
pip install fastapi uvicorn scikit-learn pandas joblib matplotlib jupyter
```

**2. Start the backend**
```bash
uvicorn backend.main:app --reload --port 8000
```

**3. Open the frontend**

Double-click `frontend/index.html` in your browser.

## Project Structure

```
seminar/
  backend/main.py                  ← FastAPI server (POST /predict)
  frontend/index.html              ← KAU-styled form UI
  docs/architecture.md             ← Architecture & usage docs
  simple_tree.ipynb                ← Notebook that trains & saves the model
  students_senior_dataset.csv      ← Training dataset (300 students)
  senior_classifier_model.pkl      ← Trained DecisionTreeClassifier
  PlayNoPlay_DecisionTree.drawio   ← ID3 diagram (weather example)
  LoanApproval_DecisionTree.drawio ← ID3 diagram (loan approval example)
```

## Example Request & Response

**POST** `http://localhost:8000/predict`

```json
{
  "DS204": "Yes",
  "Algo223": "Yes",
  "OS361": "No",
  "AI331": "Yes",
  "Compiler302": "No",
  "Training323": "Yes"
}
```

```json
{ "prediction": "Senior" }
```
