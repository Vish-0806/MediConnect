#  🩺🏥 MediConnect

MediConnect is an AI-powered healthcare platform that allows users to perform preliminary diagnosis based on symptoms and connect with doctors for further consultation.

---

## 🚀 Features

- 🔐 User Authentication (Login/Signup)
- 🧠 Symptom-based Diagnosis (AI/NLP)
- 📊 Health Result Dashboard
- 🏥 Doctor & Hospital Selection
- 📅 Appointment Booking
- 📁 Patient History Tracking

---

## 🎯 Objective

To provide users with quick health insights and guide them toward appropriate medical care.

---

## ⚠️ Disclaimer

This platform provides only preliminary health analysis and is not a substitute for professional medical advice.

---

## 🛠 Tech Stack

### 🌐 Frontend
- HTML
- React.js
- Tailwind CSS

### ⚙️ Backend
- FastAPI (Python)

### 🧠 AI / NLP
- spaCy

### 🗄 Database
- PostgreSQL

---


## 📁 Project Structure

```
MediConnect/
│
├── backend/
│   ├── main.py
│   ├── test_api.py
│   └── ai_engine/
│       ├── __init__.py
│       ├── diagnosis_engine.py
│       ├── groq_client.py
│       └── prompt_templates.py
├── config/
│   └── settings.py
├── database/
│   ├── database.py
│   └── seed_data.py
├── models/
│   ├── __init__.py
│   ├── appointment.py
│   ├── doctor.py
│   ├── patient.py
│   └── user.py
├── routes/
│   ├── __init__.py
│   ├── admin.py
│   ├── appointments.py
│   ├── auth.py
│   ├── diagnosis.py
│   ├── doctors.py
│   └── patients.py
├── schemas/
│   ├── appointment_schema.py
│   ├── diagnosis_schema.py
│   ├── doctor_schema.py
│   └── patient_schema.py
├── services/
│   ├── appointment_service.py
│   ├── diagnosis_service.py
│   ├── doctor_service.py
│   └── patient_service.py
├── tests/
│   ├── test_api.py
│   ├── test_database.py
│   └── test_diagnosis.py
├── utils/
│   ├── helpers.py
│   └── validators.py
├── docs/
└── frontend/
	├── public/
	└── src/
		├── assets/
		├── components/
		├── hooks/
		├── pages/
		└── services/

```


## 📌 Current Stage

- **Backend:** FastAPI app scaffolded (`backend/main.py`) with diagnosis routes and working home endpoint.
- **AI / NLP:** `backend/ai_engine` contains diagnosis logic (`diagnosis_engine.py`, `groq_client.py`, `prompt_templates.py`).
- **Database:** DB helpers and seed data present in `backend/database`.
- **Models & Services:** Domain models, services, and route modules implemented under `backend/models`, `backend/services`, and `backend/routes`.
- **Tests:** Basic scripts exist (`backend/test_api.py`, `backend/tests/*`) for quick checks.
- **Frontend:** Project scaffold exists under `frontend/` (`public/` and `src/`) but app work is in progress.

Next steps: add CI/tests, complete frontend pages, and wire frontend to backend APIs.

🚧 Project setup completed — development starting. On Progress
