import sqlite3
import logging
from pathlib import Path
import matplotlib.pyplot as plt

# --------------------------------------------------
# Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_PATH = BASE_DIR / "database" / "movies.db"
REPORTS_PATH = BASE_DIR / "reports"

REPORTS_PATH.mkdir(exist_ok=True)

# --------------------------------------------------
# Logging
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# --------------------------------------------------
# Database connection
# --------------------------------------------------
def get_connection():
    return sqlite3.connect(DATABASE_PATH)

# --------------------------------------------------
# Query 2: Top 10 most popular movies
# --------------------------------------------------
def visualize_top_popular_movies(conn, limit=10):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, popularity
        FROM movies
        ORDER BY popularity DESC
        LIMIT ?
    """, (limit,))
    
    rows = cursor.fetchall()
    titles = [row[0] for row in rows]
    popularity = [row[1] for row in rows]

    plt.figure(figsize=(10, 6))
    plt.barh(titles[::-1], popularity[::-1])
    plt.xlabel("Popularity")
    plt.title("Top 10 Most Popular Movies")
    plt.tight_layout()

    output_path = REPORTS_PATH / "top_popular_movies.png"
    plt.savefig(output_path)
    plt.close()

    logging.info(f"Saved visualization: {output_path.name}")

# --------------------------------------------------
# Query 3: Top rated movies with minimum votes
# --------------------------------------------------
def visualize_top_rated_movies(conn, min_votes=100, limit=10):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, vote_average
        FROM movies
        WHERE vote_count > ?
        ORDER BY vote_average DESC
        LIMIT ?
    """, (min_votes, limit))
    
    rows = cursor.fetchall()
    titles = [row[0] for row in rows]
    ratings = [row[1] for row in rows]

    plt.figure(figsize=(10, 6))
    plt.barh(titles[::-1], ratings[::-1])
    plt.xlabel("Average Rating")
    plt.title("Top Rated Movies (min 100 votes)")
    plt.xlim(0, 10)
    plt.tight_layout()

    output_path = REPORTS_PATH / "top_rated_movies.png"
    plt.savefig(output_path)
    plt.close()

    logging.info(f"Saved visualization: {output_path.name}")

# --------------------------------------------------
# Main
# --------------------------------------------------
if __name__ == "__main__":
    logging.info("📊 Starting visualization step...")

    conn = get_connection()

    visualize_top_popular_movies(conn)
    visualize_top_rated_movies(conn)

    conn.close()

    logging.info("✅ Visualization step completed!")
