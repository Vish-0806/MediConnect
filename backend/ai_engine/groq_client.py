import os

import requests
from dotenv import load_dotenv


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def get_ai_diagnosis(symptoms: str) -> str:
	url = "https://api.groq.com/openai/v1/chat/completions"

	headers = {
		"Authorization": f"Bearer {GROQ_API_KEY}",
		"Content-Type": "application/json",
	}

	payload = {
		"model": "llama-3.3-70b-versatile",
		"messages": [
			{
				"role": "system",
				"content": (
					"You are a helpful medical assistant. Based on the user's symptoms, "
					"suggest likely possibilities without giving a definitive diagnosis or "
					"claiming certainty. Return the response in exactly this structure, using "
					"plain text and short bullet points under each heading. Do not write a "
					"single paragraph and do not add any extra sections.\n\n"
					"Possible Conditions:\n"
					"- Condition 1\n"
					"- Condition 2\n"
					"- Condition 3\n\n"
					"Recommended Actions:\n"
					"- Action 1\n"
					"- Action 2\n"
					"- Action 3\n\n"
					"Warning Signs:\n"
					"- Warning 1\n"
					"- Warning 2\n\n"
					"Medical Disclaimer:\n"
					"- Always mention that this is not a professional medical diagnosis."
				),
			},
			{"role": "user", "content": symptoms},
		],
    }

	response = requests.post(url, headers=headers, json=payload)
	response_json = response.json()
	print(response.status_code)
	print(response.text)
	ai_response = response_json["choices"][0]["message"]["content"]

	return ai_response
