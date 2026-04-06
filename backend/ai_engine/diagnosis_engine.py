import spacy


nlp = spacy.load("en_core_web_sm")


def diagnose_symptoms(symptoms: str) -> dict:
	doc = nlp(symptoms)
	meaningful_words = []

	for token in doc:
		if token.is_stop or token.is_punct or not token.is_alpha:
			continue
		if token.pos_ in {"NOUN", "PROPN", "ADJ", "VERB"}:
			meaningful_words.append(token.lemma_.lower())

	possible_diseases = []

	if "fever" in meaningful_words:
		possible_diseases.append("Flu")
	if "cough" in meaningful_words:
		possible_diseases.append("Common Cold")
	if "headache" in meaningful_words:
		possible_diseases.append("Migraine")

	if not possible_diseases:
		return {
			"possible_diseases": ["Unknown"],
			"confidence": "Low",
		}

	confidence = "High" if len(possible_diseases) >= 2 else "Medium"
	return {
		"possible_diseases": possible_diseases,
		"confidence": confidence,
	}
