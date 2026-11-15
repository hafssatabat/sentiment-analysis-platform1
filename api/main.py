from fastapi import FastAPI

app = FastAPI(title="Sentiment Analysis API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: dict):
    return {"label": "neutral", "score": 0.0}   # factice, SAP-39 l'implémentera

@app.post("/predict/batch")
def predict_batch(payload: dict):
    return {"results": []}

@app.get("/history")
def history():
    return {"items": []}