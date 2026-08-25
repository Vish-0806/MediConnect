# 🩺🏥 MediConnect

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/AI%20Engine-Groq%20(Llama--3.3--70B)-f55036.svg)](https://groq.com/)
[![spaCy](https://img.shields.io/badge/NLP-spaCy-09A3D5.svg?logo=spacy&logoColor=white)](https://spacy.io/)
[![Project Status](https://img.shields.io/badge/Status-In%20Active%20Development-orange.svg)](#-current-project-status--roadmap)

**MediConnect** is an AI-driven healthcare platform designed to bridge preliminary symptom assessment with professional clinical care. It allows patients to analyze their health concerns using state-of-the-art LLMs and NLP, understand potential conditions, receive safety guidance, and connect directly with verified doctors and hospitals for consultations and appointments.

---

> [!WARNING]
> **Medical Disclaimer:** MediConnect provides preliminary AI-assisted health analysis for informational purposes only. It is **not** a substitute for professional clinical diagnosis, emergency medical care, or qualified health advice.

---

## 🚀 Key Features

- **🧠 AI Symptom Assessment:** Integrates Groq Cloud (`llama-3.3-70b-versatile`) with robust JSON schema validation to provide structured insights:
  - Possible health conditions (3–5 non-definitive possibilities)
  - Practical recommended actions & self-care advice
  - Red-flag warning signs requiring urgent medical attention
  - Fallback local NLP parsing via **spaCy** tokenization and lemmatization (`backend/ai_engine/diagnosis_engine.py`)
- **🔐 User & Provider Authentication:** Role-based access control for Patients, Doctors, and Administrators *(Scaffolded)*
- **🏥 Doctor & Clinic Matching:** Directory and discovery system to match patients with medical specialists based on symptoms *(Scaffolded)*
- **📅 Appointment Scheduling:** Seamless booking flow between patients and healthcare providers *(Scaffolded)*
- **📁 Medical History & Records:** Tracking past diagnoses, consultation notes, and appointment history *(Scaffolded)*

---

## 🛠 Tech Stack

### ⚙️ Backend
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Validation & Serialization:** [Pydantic v2](https://docs.pydantic.dev/)
- **Server:** [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- **AI / LLM Inference:** [Groq Cloud API](https://console.groq.com/) (`llama-3.3-70b-versatile`)
- **NLP / Text Processing:** [spaCy](https://spacy.io/) (`en_core_web_sm` model)
- **Configuration & Secrets:** `python-dotenv`

### 🗄 Database (Planned)
- **Engine:** PostgreSQL
- **ORM / Migrations:** SQLAlchemy / Alembic

### 🌐 Frontend (Scaffolded)
- **Framework:** React.js
- **Styling:** Tailwind CSS

---

## 📁 Repository Structure

```text
MediConnect/
│
├── .gitignore
├── README.md
│
├── backend/                             # Core FastAPI backend service
│   ├── main.py                          # Application entrypoint & route registration
│   ├── test_api.py                      # Standalone test runner for Groq AI diagnosis
│   │
│   ├── ai_engine/                       # AI & NLP integration modules
│   │   ├── __init__.py
│   │   ├── diagnosis_engine.py          # Rule-based spaCy NLP symptom analyzer
│   │   ├── groq_client.py               # Groq API client (Llama 3.3 70B Versatile)
│   │   └── prompt_templates.py          # Structured prompt definitions
│   │
│   ├── config/                          # Application settings & environment configs
│   │   └── settings.py
│   │
│   ├── database/                        # Database connection & seed scripts
│   │   ├── database.py
│   │   └── seed_data.py
│   │
│   ├── models/                          # Database ORM models
│   │   ├── __init__.py
│   │   ├── appointment.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   └── user.py
│   │
│   ├── routes/                          # FastAPI route controllers
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── appointments.py
│   │   ├── auth.py
│   │   ├── diagnosis.py                 # POST /diagnosis implementation
│   │   ├── doctors.py
│   │   └── patients.py
│   │
│   ├── schemas/                         # Pydantic request/response schemas
│   │   ├── appointment_schema.py
│   │   ├── diagnosis_schema.py
│   │   ├── doctor_schema.py
│   │   └── patient_schema.py
│   │
│   ├── services/                        # Business logic & domain services
│   │   ├── appointment_service.py
│   │   ├── diagnosis_service.py
│   │   ├── doctor_service.py
│   │   └── patient_service.py
│   │
│   ├── tests/                           # Unit and integration test suites
│   │   ├── test_api.py
│   │   ├── test_database.py
│   │   └── test_diagnosis.py
│   │
│   └── utils/                           # Shared utility helpers & validators
│       ├── helpers.py
│       └── validators.py
│
├── frontend/                            # React.js web interface (scaffolded)
│   ├── public/
│   └── src/
│       ├── assets/
│       ├── components/
│       ├── hooks/
│       ├── pages/
│       └── services/
│
└── docs/                                # Project documentation and assets
```

---

## ⚡ Quickstart Guide

### 1. Prerequisites
- **Python 3.10+** installed
- A **[Groq Cloud API Key](https://console.groq.com/)** (Free tier available)

### 2. Clone the Repository
```bash
git clone https://github.com/Vish-0806/MediConnect.git
cd MediConnect
```

### 3. Set Up Virtual Environment & Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Windows (CMD):
.\venv\Scripts\activate.bat
# On Linux/macOS:
source venv/bin/activate

# Install required Python packages
pip install fastapi uvicorn requests python-dotenv spacy pydantic

# Download spaCy NLP model (for local rule-based analysis)
python -m spacy download en_core_web_sm
```

### 4. Configure Environment Variables
Create a `.env` file in the `backend/` directory or root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Backend Service

Run from the `backend/` folder:
```bash
cd backend
uvicorn main:app --reload --port 8000
```
Or run directly from the root workspace:
```bash
python -m uvicorn backend.main:app --reload --port 8000
```

- **API Base URL:** `http://localhost:8000`
- **Interactive Swagger Docs:** `http://localhost:8000/docs`
- **Alternative ReDoc Docs:** `http://localhost:8000/redoc`

---

## 🔌 API Reference

### Health Check
- **Endpoint:** `GET /`
- **Response:**
  ```json
  {
    "message": "MediConnect Backend Running 🚀"
  }
  ```

### AI Symptom Diagnosis
- **Endpoint:** `POST /diagnosis`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "symptoms": "High fever, persistent dry cough, and headache for 2 days"
  }
  ```
- **Response (200 OK):**
  ```json
  {
    "possible_conditions": [
      "Influenza (Flu)",
      "Viral Upper Respiratory Infection",
      "Acute Bronchitis"
    ],
    "recommended_actions": [
      "Rest and ensure adequate hydration",
      "Monitor body temperature regularly",
      "Consult a healthcare professional if symptoms worsen"
    ],
    "warning_signs": [
      "Shortness of breath or difficulty breathing",
      "Persistent chest pain or pressure",
      "Fever exceeding 103°F (39.4°C) or unresponsive to medication"
    ],
    "medical_disclaimer": "This analysis is for informational purposes and is not a professional medical diagnosis. Consult a qualified doctor for medical advice."
  }
  ```

---

## 📌 Current Project Status & Roadmap

- [x] **Backend Skeleton:** FastAPI application configured with modular router architecture.
- [x] **AI Engine:** Groq Cloud integration running `llama-3.3-70b-versatile` with response sanitization and strict schema parsing.
- [x] **NLP Fallback:** spaCy-based keyword and symptom token analysis engine (`backend/ai_engine/diagnosis_engine.py`).
- [ ] **Data Persistence:** Implement PostgreSQL models and Alembic migrations (`backend/models`, `backend/database`).
- [ ] **Authentication & Security:** JWT-based authentication for patients and healthcare providers (`backend/routes/auth.py`).
- [ ] **Doctor & Appointment Services:** Booking pipeline, calendar availability, and doctor directories.
- [ ] **Automated Test Suite:** Comprehensive pytest integration for route verification (`backend/tests/`).
- [ ] **Frontend Application:** React + Tailwind CSS client connecting user symptom submission to appointment scheduling.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the repository for details.
