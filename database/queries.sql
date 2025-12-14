SELECT COUNT(*) AS total_movies
FROM movies;
 
SELECT title, popularity
FROM movies
ORDER BY popularity DESC
LIMIT 10;

SELECT title, vote_average, vote_count
FROM movies
WHERE vote_count > 100
ORDER BY vote_average DESC
LIMIT 10;

