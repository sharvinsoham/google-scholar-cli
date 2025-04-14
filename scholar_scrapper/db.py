import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path("papers.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            authors TEXT,
            year TEXT,
            topic TEXT,
            filename TEXT UNIQUE,
            added_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_paper(title, authors, year, topic, filename):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO papers (title, authors, year, topic, filename, added_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, authors, year, topic, filename, datetime.now().isoformat()))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"⚠️ Paper already in database: {filename}")
    finally:
        conn.close()

def list_all():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT title, authors, year, topic, filename FROM papers")
    papers = c.fetchall()
    conn.close()
    return papers

def get_papers_by_author(author_name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM papers WHERE authors LIKE ?", (f"%{author_name}%",))
    results = c.fetchall()
    conn.close()
    return results

def tag_paper(filename, topic):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE papers SET topic = ? WHERE filename = ?", (topic, filename))
    conn.commit()
    conn.close()

