from fastapi import FastAPI

from app.request_models.payload import Payload
from app.models.baseline.model import NaiveMap


app = FastAPI()


@app.get("/ping")
async def root():
    return {"message": "Available!"}

V1_MODEL = NaiveMap()
@app.post("/invoke/v1")
async def invoke_baseline(payload: Payload):
    preds = V1_MODEL.annotate(payload.case_num, payload.patient_history)
    return {"request": payload, "annotations": preds}