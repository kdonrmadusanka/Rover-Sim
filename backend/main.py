from fastapi import FastAPI

app = FastAPI(title="Lunar Rover Simulator")

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}