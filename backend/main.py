from fastapi import FastAPI
from routes.diagnosis import router as diagnosis_router

app = FastAPI()
app.include_router(diagnosis_router)

@app.get("/")
def home():
    return {"message": "MediConnect Backend Running 🚀"}