-- wget https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
-- after importing table dump into database, cat [filename] | mysql -hlocalhost -uroot -p [database_name]
-- script that displays the max temperature of each state (ordered by State name)

SELECT state, MAX(value) AS 'max_temp'
FROM temperatures
GROUP BY state
ORDER BY state;
