--listing all genres from hbtn_0d_tvshows
-- displaying the number of shows linked to each
SELECT genre AS genre, COUNT(*) AS number_of_shows
FROM hbtn_0d_tvshows.shows
JOIN hbtn_0d_tvshows.show_genres ON shows.id = show_genres.show_id
JOIN hbtn_0d_tvshows.genres ON show_genres.genre_id = genres.id
GROUP BY genre HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;