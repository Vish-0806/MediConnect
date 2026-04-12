import json
import re

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ai_engine.groq_client import get_ai_diagnosis


router = APIRouter(prefix="/diagnosis")


class DiagnosisRequest(BaseModel):
	symptoms: str


def _parse_ai_diagnosis(ai_response: str) -> dict:
	content = ai_response.strip()
	content = re.sub(r"^```(?:json)?\s*", "", content)
	content = re.sub(r"\s*```$", "", content)

	try:
		parsed_response = json.loads(content)
	except json.JSONDecodeError:
		json_match = re.search(r"\{.*\}", content, re.DOTALL)
		if not json_match:
			raise HTTPException(
				status_code=502,
				detail="AI response could not be parsed into structured diagnosis JSON.",
			)

		try:
			parsed_response = json.loads(json_match.group(0))
		except json.JSONDecodeError as exc:
			raise HTTPException(
				status_code=502,
				detail="AI response returned invalid JSON.",
			) from exc

	if not isinstance(parsed_response, dict):
		raise HTTPException(
			status_code=502,
			detail="AI response did not return a JSON object.",
		)

	required_fields = {
		"possible_conditions": list,
		"recommended_actions": list,
		"warning_signs": list,
		"medical_disclaimer": str,
	}

	structured_response = {}
	for field_name, expected_type in required_fields.items():
		if field_name not in parsed_response:
			raise HTTPException(
				status_code=502,
				detail=f"AI response is missing the '{field_name}' field.",
			)

		field_value = parsed_response[field_name]
		if not isinstance(field_value, expected_type):
			raise HTTPException(
				status_code=502,
				detail=f"AI response field '{field_name}' has an invalid type.",
			)

		if expected_type is list:
			structured_response[field_name] = [str(item) for item in field_value]
		else:
			structured_response[field_name] = str(field_value)

	return structured_response


@router.post("")
def diagnose(request: DiagnosisRequest):
	formatted_symptoms = (
		f"Symptoms: {request.symptoms}\n\n"
		"Respond in under 150 words using this structure:\n"
		"Possible conditions (3-5)\n"
		"Basic advice"
	)
	ai_response = get_ai_diagnosis(formatted_symptoms)
	return _parse_ai_diagnosis(ai_response)
