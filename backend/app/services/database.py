# backend/app/services/database.py

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "jobs.db"

def init_db():
    """Initialize the database with necessary tables."""
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT,
                description TEXT,
                date_posted TEXT,
                cover_letter TEXT
            )
        """)
        conn.commit()

def add_job(title: str, company: str, location: str, description: str, date_posted: str, cover_letter: str = None):
    """Insert a new job record."""
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            INSERT INTO jobs (title, company, location, description, date_posted, cover_letter)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, company, location, description, date_posted, cover_letter))
        conn.commit()

def get_jobs():
    """Retrieve all stored jobs."""
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM jobs ORDER BY id DESC")
        rows = c.fetchall()
        return [
            {
                "id": row[0],
                "title": row[1],
                "company": row[2],
                "location": row[3],
                "description": row[4],
                "date_posted": row[5],
                "cover_letter": row[6]
            }
            for row in rows
        ]

def get_job_by_id(job_id: int):
    """Retrieve a job by its ID."""
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM jobs WHERE id = ?", (job_id,))
        row = c.fetchone()
        if row:
            return {
                "id": row[0],
                "title": row[1],
                "company": row[2],
                "location": row[3],
                "description": row[4],
                "date_posted": row[5],
                "cover_letter": row[6]
            }
        return None

def update_cover_letter(job_id: int, cover_letter: str):
    """Update the cover letter for a given job."""
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("UPDATE jobs SET cover_letter = ? WHERE id = ?", (cover_letter, job_id))
        conn.commit()
