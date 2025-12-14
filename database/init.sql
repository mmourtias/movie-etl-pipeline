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
);

