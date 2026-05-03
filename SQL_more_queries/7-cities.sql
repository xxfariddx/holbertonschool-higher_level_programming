-- Creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Creates the table cities
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, -- ID column
    state_id INT NOT NULL, -- State ID column
    name VARCHAR(256) NOT NULL, -- Name column
    FOREIGN KEY(state_id) REFERENCES states(id) -- Foreign key to states table
);
