-- Lists all cities and their corresponding states from the database
-- The database name is passed as an argument
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
