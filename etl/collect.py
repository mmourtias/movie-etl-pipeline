import os
import sys
import json
import logging
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

TMDB_V4_ACCESS_TOKEN = os.getenv("TMDB_V4_ACCESS_TOKEN")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3/movie/popular"

RAW_DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw"
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

if not TMDB_V4_ACCESS_TOKEN and not TMDB_API_KEY:
    logging.error("No TMDB credentials found. Set TMDB_V4_ACCESS_TOKEN or TMDB_API_KEY in the .env file (project root).")
    sys.exit(1)

def fetch_popular_movies(page=1, timeout=10):
    params = {"language": "en-US", "page": page}
    headers = {}

    if TMDB_V4_ACCESS_TOKEN:
        headers = {"Authorization": f"Bearer {TMDB_V4_ACCESS_TOKEN}"}
    else:
        params["api_key"] = TMDB_API_KEY

    try:
        response = requests.get(BASE_URL, params=params, headers=headers or None, timeout=timeout)
        response.raise_for_status()
    except requests.HTTPError:
        logging.error("TMDB API HTTP error: %s %s", response.status_code, response.text)
        raise
    except requests.RequestException as e:
        logging.error("Network error when calling TMDB: %s", str(e))
        raise

    try:
        return response.json()
    except ValueError:
        logging.error("Failed to decode TMDB JSON response: %s", response.text)
        raise

def save_raw_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = RAW_DATA_PATH / f"movies_raw_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    logging.info("Raw data saved to %s", file_path)

if __name__ == "__main__":
    logging.info("🔎 Fetching popular movies from TMDB...")

    data = fetch_popular_movies(page=1)
    save_raw_data(data)

    logging.info("✅ Collect step completed!")
