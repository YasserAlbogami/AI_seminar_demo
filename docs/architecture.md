# Architecture — Senior Student Classifier

## Overview

```
   Browser (frontend/index.html)
           |
    [User fills form & clicks submit]
           |
           v
  fetch POST http://localhost:8000/predict
  Body: { "DS204": "Yes", "Algo223": "No", ... }
           |
           v
   FastAPI (backend/main.py)
   ┌──────────────────────────────┐
   │  1. Parse JSON body          │
   │  2. Yes → 1 / No → 0        │
   │  3. model.predict([...])     │
   │  4. 1 → "Senior"            │
   │     0 → "Not Senior"        │
   └──────────────────────────────┘
           |
           v
  { "prediction": "Senior" }
           |
           v
   Browser displays result banner
```

---

## File Structure

```
seminar/
  senior_classifier_model.pkl   ← trained DecisionTreeClassifier (read by backend)
  students_senior_dataset.csv   ← original training data
  backend/
    main.py                     ← FastAPI server (one endpoint: POST /predict)
  frontend/
    index.html                  ← self-contained UI (HTML + CSS + JS, no frameworks)
  docs/
    architecture.md             ← this file
  simple_tree.ipynb             ← notebook that trained and saved the model
```

---

## How to Run Locally

**Step 1 — Start the backend**

Open a terminal, navigate to the `seminar` folder, then run:

```bash
uvicorn backend.main:app --reload --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**Step 2 — Open the frontend**

Double-click `frontend/index.html` to open it in your browser, or drag it into a browser window.  
No local web server is needed — the file works directly from `file://`.

**Step 3 — Use the app**

1. Select Yes or No for each of the 6 courses.
2. Click **Check Senior Status**.
3. The result appears as a banner below the form.

---

## Example Request & Response

**POST** `http://localhost:8000/predict`

Request body:
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

Response:
```json
{
  "prediction": "Senior"
}
```

---

## Interactive API Docs

FastAPI auto-generates a Swagger UI. While the server is running, open:

```
http://localhost:8000/docs
```

You can test the `/predict` endpoint directly from the browser there.

---

## Dependencies

```
fastapi
uvicorn
joblib
scikit-learn
pandas
```

Install on a fresh machine:
```bash
pip install fastapi uvicorn joblib scikit-learn pandas
```
