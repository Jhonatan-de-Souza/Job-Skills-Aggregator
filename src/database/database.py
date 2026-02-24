import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "jobs.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def save_jobs(jobs: list):
    with get_connection() as conn:
        conn.executemany(
            "INSERT INTO jobs (title, description) VALUES (?, ?)",
            [(job.title, job.description) for job in jobs]
        )
