<div align="center">
  <img src="https://via.placeholder.com/100x100?text=CT" alt="ClinicTrack Pro Logo" width="80" height="80">
  <h1>ClinicTrack Pro</h1>
  <p><b>A modern, fast, and feature-rich Clinic Management System for efficient healthcare operations.</b></p>
</div>

---

## 📖 Project Overview

ClinicTrack Pro is a production-ready Web Application designed to streamline clinical workflows, patient management, and prescription generation. Built with a robust **FastAPI** backend and a responsive, beautifully crafted **Tailwind CSS / Vanilla JS** frontend, it ensures a frictionless experience for doctors and clinic administrators.

It completely abandons clunky, legacy medical software interfaces in favor of a clean, modern SaaS-style aesthetic featuring optimized SQL queries, dynamic dashboards, and PDF-ready prescriptions.

## ✨ Features

- **📊 Dynamic Dashboard:** Instantly view daily visits, total patients, monthly revenue, and upcoming follow-ups.
- **👩‍⚕️ Patient Management:** Quickly onboard, search, and manage comprehensive patient profiles including medical history and vitals.
- **🩺 Visit Tracking:** Document symptoms, diagnoses, prescriptions, and follow-up dates on a structured clinical timeline.
- **🖨️ Prescription Printing/PDF Export:** Professional, print-ready prescription formatting with customizable clinic branding.
- **⚡ Lightning Fast Search:** Client-side instant filtering across patient databases.
- **🏥 Multi-Doctor Support:** Setup separate profiles, specializations, and mapping for larger clinics.

## 📸 Screenshots

| Dashboard | Patient Profile |
| --------- | --------------- |
| *[Insert Dashboard Screenshot Here]* | *[Insert Patient Profile Screenshot Here]* |

| Settings | Prescription Slip & Print View |
| -------- | ------------------------------ |
| *[Insert Settings Screenshot Here]* | *[Insert Prescription Screenshot Here]* |

## 🛠️ Tech Stack

**Backend:**
- **Python 3.11+**
- **FastAPI** (High-performance API framework)
- **SQLAlchemy** (ORM)
- **PostgreSQL** (Relational Database)
- **Uvicorn** (ASGI Server)

**Frontend:**
- **Jinja2** (Server-side templating)
- **Tailwind CSS** (Utility-first styling)
- **Vanilla JavaScript** (Lightweight DOM bindings & interactions)
- **Feather Icons** (Clean vector icons)

**Deployment:**
- **Render** (Fully managed PaaS)

## 🚀 Installation & Local Setup

### Prerequisites
- Python 3.11+
- PostgreSQL server running locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/clinictrack-pro.git
cd clinictrack-pro
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Configuration
Create a PostgreSQL database (e.g., `clinictrack_pro`).
Copy the environment example file and update it with your database credentials:
```bash
cp .env.example .env
```
Ensure your `.env` contains the correct PostgreSQL URL:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/clinictrack_pro
```

### 5. Run the Application
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 3000
```
Open **http://localhost:3000** in your browser.

## ☁️ Deployment (Render)

This project includes a `render.yaml` configuration file for zero-config deployments on Render.

1. Fork or push this repository to your GitHub account.
2. Log in to [Render](https://render.com).
3. Go to your Dashboard and click **New+** -> **Blueprint**.
4. Connect your GitHub repository.
5. Render will automatically detect the `render.yaml` and provision both the **Web Service** and the **PostgreSQL Database**. No manual environment variable setup is required.

## 🔮 Future Enhancements

- Expand PDF generation using WeasyPrint for bulk history exports.
- Multi-tenant role-based access control (Admin, Doctor, Receptionist).
- Automated SMS/Email reminders for upcoming follow-ups.
- Appointment scheduling calendar view.

---
*Developed with a focus on code quality, scalability, and UX design.*
