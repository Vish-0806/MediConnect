from fastapi import APIRouter
from pydantic import BaseModel
from ai_engine.diagnosis_engine import diagnose_symptoms


router = APIRouter(prefix="/diagnosis")


class DiagnosisRequest(BaseModel):
	symptoms: str


@router.post("")
def diagnose(request: DiagnosisRequest):
	return diagnose_symptoms(request.symptoms)
