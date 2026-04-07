from fastapi import APIRouter
from pydantic import BaseModel
from ai_engine.groq_client import get_ai_diagnosis


router = APIRouter(prefix="/diagnosis")


class DiagnosisRequest(BaseModel):
	symptoms: str


@router.post("")
def diagnose(request: DiagnosisRequest):
	formatted_symptoms = (
		f"Symptoms: {request.symptoms}\n\n"
		"Respond in under 150 words using this structure:\n"
		"Possible conditions (3-5)\n"
		"Basic advice"
	)
	ai_response = get_ai_diagnosis(formatted_symptoms)
	return {"diagnosis": ai_response}
