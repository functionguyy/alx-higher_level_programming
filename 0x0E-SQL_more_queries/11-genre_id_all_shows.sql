-- list all shows contained in the database hbtn_0d_tvshows
-- The database name will be passed as an argument of the mysql
-- command
SELECT tvs.title, tvsg.genre_id 
FROM tv_shows AS tvs 
LEFT OUTER JOIN tv_show_genres AS tvsg
ON tvs.id = tvsg.show_id
ORDER BY tvs.title ASC, tvsg.genre_id ASC;
