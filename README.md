<div align="center">

# 🩺 MediConnect

### *Next-Generation AI Healthcare Triage & Clinical Consultation Platform*

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Groq LPU](https://img.shields.io/badge/AI%20Engine-Groq%20Llama%203.3--70B-f55036?style=for-the-badge)](https://groq.com/)
[![spaCy](https://img.shields.io/badge/NLP-spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Tailwind CSS](https://img.shields.io/badge/Styling-Tailwind%20CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=for-the-badge)](https://github.com/Vish-0806/MediConnect/pulls)

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-interactive-triage-preview">Live Preview</a> •
  <a href="#-system-architecture">Architecture</a> •
  <a href="#-clinical-workflow">Clinical Flow</a> •
  <a href="#-database-schema">Data Model</a> •
  <a href="#-key-features">Features</a> •
  <a href="#-ai-engine--safety-guardrails">AI Engine & Safety</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-repository-structure">Structure</a> •
  <a href="#-quickstart-guide">Quickstart</a> •
  <a href="#-docker--containerization">Docker</a> •
  <a href="#-api-documentation">API Reference</a> •
  <a href="#-project-roadmap">Roadmap</a> •
  <a href="#-faq">FAQ</a>
</p>

</div>

---

> [!WARNING]
> ### ⚠️ Clinical Disclaimer 
> **MediConnect provides preliminary, automated symptom analysis strictly for educational and informational purposes.** It is **NOT** a diagnostic medical device, medical opinion, or substitute for consultation with a licensed healthcare practitioner. In the event of an acute medical emergency, immediately contact your local emergency services (e.g., 911, 112) or visit the nearest emergency medical facility.

---

## 📖 Overview

Navigating primary healthcare often involves friction: patients struggle to interpret physical symptoms, experience anxiety from unstructured internet searches, and face delays in securing appointments with the appropriate medical specialists 

**MediConnect** bridges this gap by unifying **intelligent natural language symptom triage** with **clinical booking pathways**:
1. **Conversational Symptom Intake:** Patients describe their symptoms in plain, natural language.
2. **High-Speed Dual AI Engine:** Queries the ultra-fast **Groq Cloud API** running `llama-3.3-70b-versatile` with strict JSON schema parsing, reinforced by a local **spaCy** token and rule-based fallback analyzer.
3. **Structured Clinical Guidance:** Delivers 3–5 differential possibilities, non-invasive self-care suggestions, and immediate "red-flag" warning signs requiring urgent clinical care.
4. **Specialist Pathway:** Seamlessly matches patients with verified doctors, clinic directories, and real-time consultation scheduling.

---

## 📱 Interactive Triage Preview

Here is how MediConnect transforms a natural symptom description into structured clinical insights:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│  👤 PATIENT INPUT: "Fever of 101°F, persistent dry cough, and chest tightness for 3 days"      │
└────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                │
                                                ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│  🩺 MEDICONNECT STRUCTURED CLINICAL CARD                                                       │
├────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                │
│  🔍 POSSIBLE CONDITIONS                                                                        │
│  • Influenza (Flu)                                                                             │
│  • Viral Upper Respiratory Tract Infection                                                     │
│  • Early Acute Bronchitis                                                                      │
│                                                                                                │
│  💡 RECOMMENDED ACTIONS                                                                        │
│  • Rest thoroughly and maintain fluid intake (> 2.5L water or warm broths)                     │
│  • Monitor body temperature every 4 hours                                                      │
│  • Schedule an appointment with a General Physician or Pulmonologist                           │
│                                                                                                │
│  🚨 WARNING SIGNS (Seek Emergency Care Immediately If You Experience):                        │
│  • Severe difficulty breathing or gasping for air                                              │
│  • Persistent pain or pressure in the chest                                                    │
│  • Bluish discoloration of the lips or face                                                    │
│  • Temperature exceeding 103°F (39.4°C) unresponsive to fever reducers                         │
│                                                                                                │
│  👨‍⚕️ RECOMMENDED SPECIALTY: Pulmonology / Internal Medicine                                    │
│  [📅 Find Specialists & Book Consultation]                                                     │
│                                                                                                │
│  ⚖️ Disclaimer: Not a formal diagnosis. Consult a licensed physician for medical advice.      │
└────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏛 System Architecture

The following diagram illustrates MediConnect's layered architecture spanning client interaction, API gateways, intelligence engines, and data storage:

```mermaid
flowchart TD
    subgraph Client ["Client Presentation Layer"]
        A[Web Browser / React Frontend]
        Mobile[Mobile Web / Responsive PWA]
    end

    subgraph Gateway ["FastAPI API Gateway (backend/main.py)"]
        B["ASGI Server / Uvicorn Router"]
        R1["Health Endpoint (GET /)"]
        R2["Diagnosis Router (POST /diagnosis)"]
        R3["Auth Router (POST /auth/login)"]
        R4["Doctors Router (GET /doctors)"]
        R5["Appointments Router (POST /appointments)"]
        B --> R1
        B --> R2
        B --> R3
        B --> R4
        B --> R5
    end

    subgraph Intelligence ["AI & NLP Intelligence Layer (backend/ai_engine)"]
        D1["Groq API Client (Llama 3.3 70B Versatile)"]
        D2["spaCy Tokenizer & Lemmatizer (en_core_web_sm)"]
        P["Strict JSON Regex & Schema Validator"]
        R2 -->|Primary Inference| D1
        R2 -.->|Offline / Fallback| D2
        D1 --> P
    end

    subgraph Domain ["Application Business Logic (backend/services)"]
        S1["Authentication & RBAC Service"]
        S2["Doctor Directory & Matching Service"]
        S3["Appointment Booking Engine"]
        S4["Patient Medical Records Service"]
    end

    subgraph Persistence ["Persistence Layer (backend/database)"]
        DB[(PostgreSQL Database)]
        Models["SQLAlchemy ORM Entities"]
        DB --- Models
        S1 --> DB
        S2 --> DB
        S3 --> DB
        S4 --> DB
    end

    Client -->|"HTTP / REST API"| Gateway
    P -->|"Sanitized JSON Response"| Client
    Gateway --> Domain
```

---

## 🔄 Clinical Workflow

The sequence below illustrates the end-to-end lifecycle of a patient session:

```mermaid
sequenceDiagram
    autonumber
    actor Patient as 👤 Patient
    participant Frontend as 🌐 React App
    participant API as ⚙️ FastAPI Gateway
    participant Groq as ⚡ Groq Cloud (Llama 3.3)
    participant Validator as 🛡️ Schema Validator
    participant DB as 🗄️ PostgreSQL
    actor Doctor as 👨‍⚕️ Doctor

    Patient->>Frontend: Enter symptoms ("fever and shortness of breath")
    Frontend->>API: POST /diagnosis { symptoms: "..." }
    API->>Groq: Prompt Llama 3.3 70B (Enforced JSON Schema)
    Groq-->>API: Raw AI Completion
    API->>Validator: Strip code fences & regex match JSON
    Validator-->>API: Validated Dict (Conditions, Advice, Warnings)
    API-->>Frontend: 200 OK Structured Diagnosis Card
    Frontend-->>Patient: Render differential conditions & warnings

    opt Book Clinical Consultation
        Patient->>Frontend: Select Recommended Specialist
        Frontend->>API: POST /appointments/book
        API->>DB: Save Appointment & Link Diagnosis Dossier
        DB-->>API: Booking Confirmed (Ref ID: #APT-482)
        API-->>Doctor: Push Notification / Dashboard Alert
        API-->>Frontend: Confirmation & Calendar Invite
    end
```

---

## 🗄 Database Schema

The relational data model connects users, patients, doctors, diagnosis history, and appointments:

```mermaid
erDiagram
    USER ||--o| PATIENT : "has"
    USER ||--o| DOCTOR : "has"
    PATIENT ||--o{ APPOINTMENT : "books"
    DOCTOR ||--o{ APPOINTMENT : "attends"
    PATIENT ||--o{ DIAGNOSIS_RECORD : "receives"

    USER {
        uuid id PK
        string email UK
        string hashed_password
        string role "patient | doctor | admin"
        timestamp created_at
    }

    PATIENT {
        uuid id PK
        uuid user_id FK
        string full_name
        date date_of_birth
        string blood_group
        text emergency_contact
    }

    DOCTOR {
        uuid id PK
        uuid user_id FK
        string full_name
        string specialization
        string license_number UK
        string hospital_affiliation
        decimal consultation_fee
        float rating
    }

    APPOINTMENT {
        uuid id PK
        uuid patient_id FK
        uuid doctor_id FK
        timestamp appointment_time
        string status "pending | confirmed | completed | cancelled"
        text notes
    }

    DIAGNOSIS_RECORD {
        uuid id PK
        uuid patient_id FK
        text reported_symptoms
        jsonb possible_conditions
        jsonb recommended_actions
        jsonb warning_signs
        timestamp created_at
    }
```

---

## 🧠 AI Engine & Safety Guardrails

### Why Groq LPU™ for Healthcare Triage?
When patients describe acute symptoms, response time directly impacts anxiety and usability. Traditional cloud LLM APIs can exhibit 10–20 second latency. MediConnect integrates **Groq LPU™ (Language Processing Unit)** hardware running **Meta Llama 3.3 70B Versatile**:
- ⚡ **Inference Speed:** ~250–300 tokens/second
- ⏱️ **End-to-End Latency:** Sub-second (< 800ms) turnaround for full clinical triage
- 🎯 **Accuracy:** 70B parameter frontier model capabilities for nuanced medical terminology

### Guardrail Pipeline

```
Raw Patient Symptoms ➔ System Prompt Guardrails ➔ Groq Inference ➔ Code Fence Stripper ➔ Regex Pattern Extractor ➔ Pydantic Type Check ➔ 502 Shield
```

1. **Liability Boundary Enforcement:** System prompt forbids definitive clinical claims or certainty declarations.
2. **Defensive Normalization:** The parsing engine (`backend/routes/diagnosis.py: _parse_ai_diagnosis`) strips backticks, extracts matching JSON objects via regex, and verifies all required schema fields (`possible_conditions`, `recommended_actions`, `warning_signs`, `medical_disclaimer`).
3. **Local NLP Fallback:** If the external API is unreachable or rate-limited, MediConnect automatically falls back to `backend/ai_engine/diagnosis_engine.py`, leveraging spaCy's POS tagging and lemma analysis.

---

## 🚀 Key Features Matrix

| Domain | Feature | Description | Status |
| :--- | :--- | :--- | :---: |
| **AI Triage** | **LLM Symptom Reasoning** | Ultra-low-latency clinical evaluation via Groq Llama 3.3 70B. | ✅ **Active** |
| **NLP** | **spaCy Linguistic Fallback** | Tokenization, POS filtering, and lemma matching (`en_core_web_sm`). | ✅ **Active** |
| **Security** | **Schema Sanitization** | Regex extraction and Pydantic validation intercepting malformed outputs. | ✅ **Active** |
| **Auth** | **JWT & Role-Based Access** | Role separation for Patients, Doctors, and Hospital Admins. | ⏳ *Scaffolded* |
| **Directory** | **Doctor & Clinic Discovery** | Specialist directory searchable by department, ratings, and hospital. | ⏳ *Scaffolded* |
| **Scheduling** | **Appointment Engine** | Multi-slot scheduling, double-booking prevention, and calendar sync. | ⏳ *Scaffolded* |
| **Records** | **Patient Health Dossier** | Comprehensive history tracking symptom evaluations and clinical notes. | ⏳ *Scaffolded* |
| **Frontend** | **React Web Dashboard** | Modern, responsive web interface built with React.js & Tailwind CSS. | ⏳ *Scaffolded* |

---

## 🛠 Tech Stack

### ⚙️ Backend & API Gateway
- **Language:** Python 3.10+
- **API Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Data Validation:** [Pydantic v2](https://docs.pydantic.dev/)
- **ASGI Server:** [Uvicorn](https://www.uvicorn.org/)
- **HTTP Client:** [Requests](https://requests.readthedocs.io/)
- **Environment Management:** [python-dotenv](https://github.com/theskumar/python-dotenv)

### 🧠 AI, NLP & Machine Learning
- **Primary Inference:** [Groq Cloud](https://console.groq.com/) — Meta Llama 3.3 70B Versatile
- **Natural Language Processing:** [spaCy](https://spacy.io/) with `en_core_web_sm` model

### 🗄 Database & Persistence (Planned)
- **Database:** [PostgreSQL](https://www.postgresql.org/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Migrations:** [Alembic](https://alembic.sqlalchemy.org/)

### 🌐 Frontend (Scaffolded)
- **Framework:** [React.js](https://react.dev/)
- **Styling:** [Tailwind CSS](https://tailwindcss.com/)
- **Icons:** Lucide React / Heroicons

---

## 📁 Repository Structure

```text
MediConnect/
│
├── .gitignore                           # Excludes venv, .env, pycache, build artifacts
├── README.md                            # Comprehensive project guide
│
├── backend/                             # Core FastAPI Backend Application
│   ├── main.py                          # App initialization & router mounting
│   ├── test_api.py                      # Standalone CLI diagnosis runner
│   │
│   ├── ai_engine/                       # AI & NLP Intelligence Engine
│   │   ├── __init__.py
│   │   ├── diagnosis_engine.py          # Local spaCy tokenization & rule-based engine
│   │   ├── groq_client.py               # Groq Cloud API caller (Llama 3.3 70B)
│   │   └── prompt_templates.py          # Clinical assistant prompt definitions
│   │
│   ├── config/                          # Configuration & Settings
│   │   └── settings.py                  # Pydantic BaseSettings & env loader
│   │
│   ├── database/                        # PostgreSQL Connection & Seeds
│   │   ├── database.py                  # Engine & sessionmaker setup
│   │   └── seed_data.py                 # Mock doctors & clinic data
│   │
│   ├── models/                          # SQLAlchemy ORM Entities
│   │   ├── __init__.py
│   │   ├── appointment.py               # Appointment ORM model
│   │   ├── doctor.py                    # Doctor profile ORM model
│   │   ├── patient.py                   # Patient dossier ORM model
│   │   └── user.py                      # User credentials ORM model
│   │
│   ├── routes/                          # FastAPI Controller Routers
│   │   ├── __init__.py
│   │   ├── admin.py                     # Administrative actions
│   │   ├── appointments.py              # Booking & scheduling endpoints
│   │   ├── auth.py                      # Authentication & token endpoints
│   │   ├── diagnosis.py                 # POST /diagnosis implementation
│   │   ├── doctors.py                   # Doctor search & directory
│   │   └── patients.py                  # Patient profiles & history
│   │
│   ├── schemas/                         # Pydantic Schemas (DTOs)
│   │   ├── appointment_schema.py
│   │   ├── diagnosis_schema.py
│   │   ├── doctor_schema.py
│   │   └── patient_schema.py
│   │
│   ├── services/                        # Business Logic Layer
│   │   ├── appointment_service.py
│   │   ├── diagnosis_service.py
│   │   ├── doctor_service.py
│   │   └── patient_service.py
│   │
│   ├── tests/                           # Test Suites
│   │   ├── test_api.py
│   │   ├── test_database.py
│   │   └── test_diagnosis.py
│   │
│   └── utils/                           # Helpers & Validators
│       ├── helpers.py
│       └── validators.py
│
├── frontend/                            # React Client (Scaffolded)
│   ├── public/                          # Static assets
│   └── src/                             # Source code
│       ├── assets/                      # Brand graphics, icons
│       ├── components/                  # Diagnosis cards, Navigation, Forms
│       ├── hooks/                       # useAuth, useDiagnosis hooks
│       ├── pages/                       # Home, Triage, Doctors, Appointments
│       └── services/                    # Axios API client
│
└── docs/                                # Documentation assets & architecture guides
```

---

## ⚡ Quickstart Guide

### 1. Prerequisites
- **Python 3.10+**
- **Git**
- A free **Groq Cloud API Key** from [console.groq.com](https://console.groq.com/)

### 2. Clone the Repository
```bash
git clone https://github.com/Vish-0806/MediConnect.git
cd MediConnect
```

### 3. Create & Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install fastapi uvicorn requests python-dotenv spacy pydantic
```

Download the spaCy NLP linguistic pipeline:
```bash
python -m spacy download en_core_web_sm
```

### 5. Configure Environment Variables
Create a `.env` file in the `backend/` directory or root workspace:

```env
# Required: Groq Cloud API Key for AI Diagnosis
GROQ_API_KEY=gsk_your_groq_api_key_here

# Optional Application Settings
PORT=8000
ENVIRONMENT=development
DATABASE_URL=postgresql://postgres:password@localhost:5432/mediconnect_db
JWT_SECRET=your_jwt_secret_key_here
```

### 6. Run the Backend Service

Run Uvicorn from the `backend/` directory:
```bash
cd backend
uvicorn main:app --reload --port 8000
```
*(Or from root: `python -m uvicorn backend.main:app --reload --port 8000`)*

Access the interactive API explorer:
- 🌐 **Root Health:** [http://localhost:8000](http://localhost:8000)
- 📚 **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- 📖 **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🐳 Docker & Containerization

To run MediConnect in a containerized environment with Docker:

### 1. Create `Dockerfile` in `backend/`
```dockerfile
FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2. Build & Run
```bash
docker build -t mediconnect-backend ./backend
docker run -p 8000:8000 --env-file backend/.env mediconnect-backend
```

---

## 🔌 API Documentation

### 1. Root Service Check
Verifies server health and gateway availability.

- **Method:** `GET`
- **Path:** `/`
- **Response (`200 OK`):**
  ```json
  {
    "message": "MediConnect Backend Running 🚀"
  }
  ```

---

### 2. AI Symptom Diagnosis
Evaluates conversational patient symptoms and returns structured clinical differential guidance.

- **Method:** `POST`
- **Path:** `/diagnosis`
- **Headers:** `Content-Type: application/json`

#### Request Payload
```json
{
  "symptoms": "High fever, persistent dry cough, sore throat, and mild headache for 2 days"
}
```

#### Success Response (`200 OK`)
```json
{
  "possible_conditions": [
    "Influenza (Flu)",
    "Viral Upper Respiratory Tract Infection",
    "Early Stage Acute Bronchitis"
  ],
  "recommended_actions": [
    "Rest thoroughly and ensure adequate hydration (> 2.5 liters daily)",
    "Track body temperature at regular 4-hour intervals",
    "Consult a physician if symptoms do not improve within 48-72 hours"
  ],
  "warning_signs": [
    "Shortness of breath or difficulty breathing",
    "Persistent chest pain or pressure",
    "Fever exceeding 103°F (39.4°C) or unresponsive to antipyretics",
    "Bluish coloration of lips or fingers"
  ],
  "medical_disclaimer": "This analysis is generated by an AI assistant for informational purposes and is not a professional medical diagnosis. Consult a qualified doctor for medical advice."
}
```

#### Response Fields Specification
| Field | Type | Description |
| :--- | :--- | :--- |
| `possible_conditions` | `Array<string>` | 3 to 5 potential non-definitive conditions matching reported symptoms. |
| `recommended_actions` | `Array<string>` | Practical, non-invasive self-care and monitoring recommendations. |
| `warning_signs` | `Array<string>` | Critical red-flag emergency symptoms requiring urgent medical attention. |
| `medical_disclaimer` | `string` | Mandatory safety statement reiterating the non-definitive nature of the AI analysis. |

---

### 3. Client Integration Examples

#### cURL
```bash
curl -X POST "http://localhost:8000/diagnosis" \
     -H "Content-Type: application/json" \
     -d '{"symptoms": "fever of 101F, dry cough, and fatigue for 3 days"}'
```

#### Python (`requests`)
```python
import requests

response = requests.post(
    "http://localhost:8000/diagnosis",
    json={"symptoms": "sudden sharp headache and sensitivity to bright light"}
)

print(response.status_code)
print(response.json())
```

#### JavaScript (`fetch` / TypeScript)
```typescript
interface DiagnosisResponse {
  possible_conditions: string[];
  recommended_actions: string[];
  warning_signs: string[];
  medical_disclaimer: string;
}

const res = await fetch("http://localhost:8000/diagnosis", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ symptoms: "mild sore throat and runny nose" }),
});

const data: DiagnosisResponse = await res.json();
console.log(data.possible_conditions);
```

---

## ⚠️ Error Handling Matrix

| HTTP Status | Error Detail / Cause | Resolution |
| :--- | :--- | :--- |
| `422 Unprocessable Entity` | Missing or invalid `symptoms` string in request body. | Ensure body is JSON with a non-empty `{"symptoms": "..."}` string. |
| `502 Bad Gateway` | AI response could not be parsed into valid JSON. | Check Groq API availability or review LLM response formatting. |
| `502 Bad Gateway` | Missing required schema field in AI response. | Guardrails catch truncated responses; retry the request. |
| `500 Internal Server Error` | Unhandled server exception or missing `GROQ_API_KEY`. | Verify `.env` configuration contains a valid `GROQ_API_KEY`. |

---

## 🧪 Testing & Verification

### Smoke Test
Verify that your Groq API connection and prompt pipelines work without starting the FastAPI web server:
```bash
python backend/test_api.py
```

### Running Unit & Integration Tests (pytest)
```bash
pytest backend/tests/ -v --tb=short
```

---

## 🔒 Security & Medical Safety

- **Anonymized Processing:** No Personal Health Information (PHI) or personally identifiable metadata is submitted to external LLM APIs.
- **Defensive Parsing:** Responses are scrubbed of code fences and verified against strict Pydantic types before being dispatched to clients.
- **Liability Boundaries:** Prompt engineering explicitly instructs the model to prioritize red-flag warnings and abstain from definitive diagnostic declarations.
- **Secret Isolation:** Environment secrets (`GROQ_API_KEY`, database credentials) are never checked into version control.

---

## 🗺️ Project Roadmap

- [x] **Phase 1: AI Diagnostics Foundation**
  - [x] FastAPI skeleton & modular router structure
  - [x] Groq Cloud API integration running `llama-3.3-70b-versatile`
  - [x] Strict JSON regex validation & 502 bad gateway shields
  - [x] Local spaCy rule-based NLP fallback engine
- [ ] **Phase 2: Database & Data Persistence**
  - [ ] PostgreSQL connection pool configuration (`backend/database/database.py`)
  - [ ] SQLAlchemy ORM models for Users, Doctors, Patients, Appointments, and Diagnoses
  - [ ] Alembic migration framework
- [ ] **Phase 3: Authentication & Security**
  - [ ] JWT authentication with bcrypt password hashing (`backend/routes/auth.py`)
  - [ ] Role-based access control (Patient, Doctor, Admin)
- [ ] **Phase 4: Doctor Discovery & Appointment Scheduling**
  - [ ] Doctor directory search by specialty, hospital, and rating
  - [ ] Time-slot conflict resolution and calendar booking
- [ ] **Phase 5: React Web Application**
  - [ ] Symptom intake UI with real-time feedback
  - [ ] Responsive diagnosis card with red-flag badges
  - [ ] Doctor selection and appointment booking flow

---

## ❓ FAQ

<details>
<summary><b>1. Is Groq Cloud free to use?</b></summary>
Yes. Groq provides a generous free tier for developers with high token limits, making it ideal for testing and development with <code>llama-3.3-70b-versatile</code> at zero cost.
</details>

<details>
<summary><b>2. Can MediConnect operate entirely offline?</b></summary>
Yes. While Groq provides frontier LLM reasoning, MediConnect includes a built-in local fallback engine (<code>backend/ai_engine/diagnosis_engine.py</code>) that utilizes spaCy's offline English model to extract key symptoms and provide rule-based matching.
</details>

<details>
<summary><b>3. How do I contribute to the frontend?</b></summary>
The frontend structure is scaffolded under <code>frontend/src/</code>. You can set up a Vite + React application, configure Tailwind CSS, and connect UI components to the endpoints documented in the <a href="#-api-documentation">API Reference</a>.
</details>

<details>
<summary><b>4. Does this platform store user medical history?</b></summary>
Persistent storage of diagnosis records is built into the data schema (Phase 2). Once PostgreSQL is connected, patient accounts will maintain an encrypted history of past triage sessions for review by consulting doctors.
</details>

---

## 🤝 Contributing

Contributions are what make the open-source community an incredible space to build and collaborate. Any contributions you make are **deeply appreciated**.

1. **Fork the Repository**
2. **Create your Feature Branch:** `git checkout -b feature/AmazingFeature`
3. **Commit your Changes:** `git commit -m 'Add some AmazingFeature'`
4. **Push to the Branch:** `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">
  <sub>Designed & Developed with ❤️ by <a href="https://github.com/Vish-0806">Vishal S Naik</a> and contributors.</sub>
</div>
