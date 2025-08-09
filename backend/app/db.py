import sqlite3
import os
from typing import List, Dict

DB_FILE = os.path.join(os.path.dirname(__file__), "applymate.db")

def init_db():
    """Initialize the database and create the jobs table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            link TEXT,
            notes TEXT,
            date_applied TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_job(job: Dict):
    """Save a new job application."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jobs (title, company, location, link, notes, date_applied)
        VALUES (?, ?, ?, ?, ?, date('now'))
    """, (
        job.get("title"),
        job.get("company"),
        job.get("location"),
        job.get("link"),
        job.get("notes", "")
    ))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Job saved successfully."}

def get_all_jobs() -> List[Dict]:
    """Fetch all saved job applications."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, company, location, link, notes, date_applied FROM jobs")
    rows = cursor.fetchall()
    conn.close()

    jobs = []
    for row in rows:
        jobs.append({
            "id": row[0],
            "title": row[1],
            "company": row[2],
            "location": row[3],
            "link": row[4],
            "notes": row[5],
            "date_applied": row[6]
        })
    return jobs

# Initialize DB on import
init_db()
