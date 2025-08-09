# 📄 Job Application Tracker with Auto-Cover Letter Writer

A modern Python + React web application that helps job seekers **track job applications** and **auto-generate tailored cover letters** using AI (OpenAI GPT models).

---

## 🚀 Features

✅ **Job Board Scraper** — Fetch job listings from job boards (e.g., Indeed, LinkedIn, RemoteOK)  
✅ **Application Tracker** — Store and search all job applications in a database  
✅ **AI Cover Letter Writer** — Automatically generate professional cover letters tailored to each job  
✅ **Responsive Web UI** — Built with React and a clean, modern design  
✅ **SQLite Database** — Simple and lightweight job storage  
✅ **REST API Backend** — Built with FastAPI for speed and clarity  
✅ **Search & Filter** — Quickly find previously saved applications  
✅ **Export Applications** — Download job applications as CSV for record-keeping

---

## 🛠️ Tech Stack

**Frontend**:  
- React (Vite)
- CSS (Modern minimal theme)

**Backend**:  
- FastAPI (Python)
- BeautifulSoup4 (for scraping)
- SQLite3 (lightweight DB)
- OpenAI Python SDK (AI cover letter generation)

---

## 📂 Project Structure

job-application-tracker/
│
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI app entry point
│ │ ├── database.py # SQLite connection
│ │ ├── models.py # DB schema
│ │ ├── routers/
│ │ │ ├── jobs.py # Job CRUD routes
│ │ │ └── cover_letter.py # AI cover letter generation route
│ │ ├── services/
│ │ │ ├── job_scraper.py # Web scraping logic
│ │ │ └── cover_letter.py # AI integration
│ ├── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx # Main React app
│ │ ├── App.css # Styling
│ │ ├── api.js # API calls to backend
│ │ ├── components/
│ │ │ ├── JobList.jsx
│ │ │ ├── JobForm.jsx
│ │ │ └── CoverLetter.jsx
│ ├── package.json
│
├── README.md

yaml
Copy
Edit

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/job-application-tracker.git
cd job-application-tracker
2️⃣ Setup Backend (FastAPI)
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
pip install -r requirements.txt
Create .env in backend/ with:

env
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
Run backend:

bash
Copy
Edit
uvicorn app.main:app --reload
Backend will run at http://127.0.0.1:8000.

3️⃣ Setup Frontend (React)
bash
Copy
Edit
cd ../frontend
npm install
npm run dev
Frontend will run at http://localhost:5173.

📌 Usage
Enter job title, company, and details into the form

Click Save Job — application is stored in database

Click Generate Cover Letter — AI writes a tailored letter for you

Search saved jobs anytime

📸 Screenshots
Dashboard View

Cover Letter Example

🔮 Future Enhancements
🔍 Multi-job board integration (LinkedIn, Glassdoor, etc.)

🌐 Multi-language cover letters

📤 Email applications directly from app

🔖 Tagging & categorizing jobs

📅 Application deadline reminders

📝 License
MIT License — feel free to use and modify.
