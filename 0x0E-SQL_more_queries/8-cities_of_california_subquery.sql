--  lists all the cities of California that can be found in the database hbtn_0d_usa
--  must be sorted in ascending order by cities.id
--  not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name FROM cities
WHERE cities.state_id = (
	SELECT states.id FROM states
        WHERE states.name = 'California'
	LIMIT 1)
ORDER BY cities.id;
