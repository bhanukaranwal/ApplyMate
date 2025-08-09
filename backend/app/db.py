import sqlite3
from typing import List, Dict

DB_FILE = "jobs.db"

def init_db():
    """
    Initializes the SQLite database and creates the jobs table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            summary TEXT,
            link TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def save_job(job: Dict) -> Dict:
    """
    Saves a job entry to the database.
    Ignores duplicates based on the job link.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO jobs (title, company, location, summary, link)
            VALUES (?, ?, ?, ?, ?)
        """, (
            job.get("title"),
            job.get("company"),
            job.get("location"),
            job.get("summary"),
            job.get("link")
        ))
        conn.commit()
        return {"status": "success", "message": "Job saved successfully."}
    except sqlite3.IntegrityError:
        return {"status": "error", "message": "Job already exists in the database."}
    finally:
        conn.close()

def get_all_jobs() -> List[Dict]:
    """
    Fetches all jobs from the database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT title, company, location, summary, link FROM jobs")
    rows = cursor.fetchall()
    conn.close()
    
    jobs = []
    for row in rows:
        jobs.append({
            "title": row[0],
            "company": row[1],
            "location": row[2],
            "summary": row[3],
            "link": row[4]
        })
    return jobs

# Run this when the module is imported to ensure DB is ready
init_db()
