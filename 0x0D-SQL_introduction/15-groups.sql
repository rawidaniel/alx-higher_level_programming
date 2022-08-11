-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0
-- should display score and the number of records for this score with the label number

SELECT score, count(score) number
FROM second_table
GROUP BY score
ORDER BY number DESC;
