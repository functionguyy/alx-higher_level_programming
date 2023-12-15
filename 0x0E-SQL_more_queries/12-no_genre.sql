-- lists all shows contained in hbtn_0d_tvshows
-- without a genre linked
SELECT tvs.title, tvsg.genre_id 
FROM tv_shows AS tvs 
LEFT OUTER JOIN tv_show_genres AS tvsg
ON tvs.id = tvsg.show_id
	WHERE tvsg.show_id IS NULL
ORDER BY tvs.title ASC, tvsg.genre_id ASC;
