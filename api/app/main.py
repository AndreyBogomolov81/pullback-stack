from fastapi import FastAPI

app = FastAPI(title="Pullback Stack API")

@app.get("/health")
def health():
    return {"status": "ok"}