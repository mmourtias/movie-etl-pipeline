
import json
import logging
from pathlib import Path
from datetime import datetime

RAW_DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw"
PROCESSED_DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "processed"

PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def get_latest_raw_file():
    files = sorted(RAW_DATA_PATH.glob("movies_raw_*.json"))
    if not files:
        raise FileNotFoundError("No raw data files found.")
    return files[-1]

def transform_movies(raw_data):
    movies = []
    for movie in raw_data.get("results", []):
        clean_movie = {
            "id": movie.get("id"),
            "title": movie.get("title"),
            "original_language": movie.get("original_language"),
            "release_date": movie.get("release_date"),
            "popularity": movie.get("popularity"),
            "vote_average": movie.get("vote_average"),
            "vote_count": movie.get("vote_count"),
            "adult": movie.get("adult"),
            "overview": movie.get("overview"),
        }
        movies.append(clean_movie)
    return movies

def save_processed_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = PROCESSED_DATA_PATH / f"movies_processed_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    logging.info(f"Processed data saved to {file_path}")

if __name__ == "__main__":
    logging.info("🔄 Starting transform step...")

    raw_file = get_latest_raw_file()
    logging.info(f"Using raw file: {raw_file.name}")

    with open(raw_file, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    processed_movies = transform_movies(raw_data)
    save_processed_data(processed_movies)

    logging.info("✅ Transform step completed!")
