import sqlite3
import logging
from pathlib import Path

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

DATABASE_PATH = Path(__file__).resolve().parents[1] / "database" / "movies.db"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

def get_connection():
    """
    Creates and returns a connection to the SQLite database.
    """
    return sqlite3.connect(DATABASE_PATH)

# --------------------------------------------------
# ANALYSIS FUNCTIONS
# --------------------------------------------------

def count_movies(conn):
    """
    Returns total number of movies in the database.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM movies")
    return cursor.fetchone()[0]


def top_popular_movies(conn, limit=10):
    """
    Returns the most popular movies.
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, popularity
        FROM movies
        ORDER BY popularity DESC
        LIMIT ?
    """, (limit,))
    return cursor.fetchall()


def top_rated_movies(conn, min_votes=100, limit=10):
    """
    Returns top rated movies with a minimum number of votes.
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, vote_average, vote_count
        FROM movies
        WHERE vote_count >= ?
        ORDER BY vote_average DESC
        LIMIT ?
    """, (min_votes, limit))
    return cursor.fetchall()

# --------------------------------------------------
# MAIN
# --------------------------------------------------

if __name__ == "__main__":
    logging.info("📊 Starting analysis step...")

    conn = get_connection()

    # Total movies
    total = count_movies(conn)
    logging.info(f"🎬 Total movies in database: {total}")

    # Most popular movies
    logging.info("🔥 Top popular movies:")
    for title, popularity in top_popular_movies(conn):
        logging.info(f" - {title} | popularity: {popularity:.2f}")

    # Best rated movies
    logging.info("⭐ Top rated movies (min 100 votes):")
    for title, rating, votes in top_rated_movies(conn):
        logging.info(f" - {title} | rating: {rating} ({votes} votes)")

    conn.close()
    logging.info("✅ Analysis step completed!")
