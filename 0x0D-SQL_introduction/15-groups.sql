-- lists the number of records with the same score in table
-- second_table of the database hbtn_0c_0
-- The database name will be passed as argument to the mysql command
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score
ORDER BY number DESC; 
