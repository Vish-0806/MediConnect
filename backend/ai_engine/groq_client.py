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
					"You are a helpful medical assistant. Suggest possible "
					"conditions based on symptoms. Do not give definitive diagnosis."
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
