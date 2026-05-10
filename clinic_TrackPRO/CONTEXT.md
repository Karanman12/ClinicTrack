# ClinicTrack - Development Context

## Project Info
Clinic management web app for small clinics in India.
Building as a startup with co-founder.
Business model: Freemium - Free basic, ₹199/month Pro

## GitHub
https://github.com/Karanman12/ClinicTrack

## Tech Stack
- Python, FastAPI, SQLAlchemy, SQLite
- Jinja2, Tailwind CSS, Vanilla JavaScript
- Uvicorn server, Feather Icons

## How To Run
- Open clinic_TrackPRO folder in VS Code
- Terminal: ..\venv\Scripts\Activate.ps1
- Terminal: uvicorn main:app --reload
- Open: http://localhost:8000

## Database Models

### Patient
id, name, phone, age, gender, blood_group (optional), 
allergies (optional), created_at

### Visit
id, patient_id, symptoms, diagnosis, prescription, 
visit_type, notes, amount, followup_date, visit_date

### Settings
id, clinic_name, doctor_name, degree, phone, 
address, created_at

## What Is Built And Working
- Add/edit/delete patients
- Blood group (optional) + allergies (optional)
- Dynamic visit form based on visit type:
  - Consultation: all fields, diagnosis optional
  - Follow-up: follow-up date required
  - Emergency: urgent symptoms required
  - Check-up: diagnosis optional
  - Procedure: diagnosis optional
- Visit type colored badges on history timeline
- Visit history with edit/delete working
- Real-time patient search + symptom autocomplete
- Print prescription with clinic settings,
  blood group, allergy warning, follow-up date
- Settings page for clinic/doctor profile
- Professional landing page
- GitHub repo with README and CONTEXT.md

## AI Tools
- Claude Code in VS Code terminal
- GitHub Copilot in VS Code
- Claude.ai for planning and review

## Workflow
- Medium sized tasks one at a time
- Clean well commented code
- After each feature: 
  git add . && git commit -m "feature: x" && git push
- If something breaks: git reset --hard HEAD

## Next Features To Build
1. Patient visit summary stats on profile
   (total visits, last visit, total amount paid)
2. Show diagnosis on prescription slip
3. UI overhaul - premium design on landing page
4. Login/auth system
5. Deploy to cloud (Railway or Render)

## How To Start New Chat
1. Upload this CONTEXT.md file
2. Upload the specific file you need help with
3. Say "Continue building ClinicTrack"