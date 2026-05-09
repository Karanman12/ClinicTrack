# 🏥 ClinicTrack

A lightweight patient management system built for small clinics in India.
Doctors can manage patient records, log visit history, record prescriptions,
and print professional prescription slips — all without paper.

## ✨ Features

- Add, edit, and delete patient records
- Record visit history with symptoms, prescription, and notes
- Consultation fee tracking per visit
- Printable prescription slips
- Real-time patient search by name or phone
- Symptom autocomplete (type "fe" → "fever")
- Keyboard shortcut `/` to focus search
- SPA experience with no full page reloads
- Form validation with inline errors

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, FastAPI |
| Database | SQLite, SQLAlchemy |
| Templating | Jinja2 |
| Frontend | Tailwind CSS, Vanilla JavaScript |
| Icons | Feather Icons |
| Server | Uvicorn |

## 🚀 Getting Started

### 1. Clone the repo
git clone https://github.com/Karanman12/ClinicTrack.git
cd ClinicTrack

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the server
uvicorn main:app --reload

### 5. Open in browser
http://localhost:8000

## 📁 Project Structure

clinic_TrackPRO/
├── main.py              # FastAPI routes
├── models.py            # SQLAlchemy models
├── database.py          # Database config
├── requirements.txt     # Dependencies
├── templates/
│   ├── start.html       # Landing page
│   ├── index.html       # App dashboard
│   └── prescription.html # Print view
└── static/
    └── style.css        # Custom styles

## 👨‍💻 Built By

Karan Mandal — [GitHub](https://github.com/Karanman12)