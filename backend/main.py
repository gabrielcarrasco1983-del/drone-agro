from fastapi import FastAPI

app = FastAPI(title="Drone Agro API")

@app.get("/")
def root():
    return {"status": "ok", "app": "Drone Agro"}
