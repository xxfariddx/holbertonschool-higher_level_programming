-- List all cities of California from hbtn_0d_usa database
-- Using a subquery because JOIN is not allowed
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
ORDER BY id ASC;
