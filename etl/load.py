import json
import logging
import sqlite3
from pathlib import Path

PROCESSED_DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "processed"
DATABASE_PATH = Path(__file__).resolve().parents[1] / "database" / "movies.db"

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

if __name__ == "__main__":
    logging.info("📥 Starting load step...")

    processed_files = sorted(PROCESSED_DATA_PATH.glob("movies_processed_*.json"))
    if not processed_files:
        raise FileNotFoundError("No processed data files found.")
    processed_file = processed_files[-1]
    logging.info(f"Using processed file: {processed_file.name}")

    with open(processed_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            original_language TEXT,
            release_date TEXT,
            popularity REAL,
            vote_average REAL,
            vote_count INTEGER,
            adult BOOLEAN,
            overview TEXT
        )
    ''')

    for movie in data:
        cursor.execute('''
            INSERT OR REPLACE INTO movies (id, title, original_language, release_date, popularity, vote_average, vote_count, adult, overview)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            movie['id'],
            movie['title'],
            movie['original_language'],
            movie['release_date'],
            movie['popularity'],
            movie['vote_average'],
            movie['vote_count'],
            movie['adult'],
            movie['overview']
        ))

    conn.commit()
    conn.close()

    logging.info("✅ Load step completed!")
