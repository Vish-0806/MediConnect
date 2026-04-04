def diagnose_symptoms(symptoms: str) -> str:
	if "fever" in symptoms.lower():
		return "Flu"

	return "Unknown"
