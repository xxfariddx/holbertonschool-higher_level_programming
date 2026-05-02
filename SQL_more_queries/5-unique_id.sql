-- Create table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE, -- ID column with default 1 and must be unique
    name VARCHAR(256) -- Name column
);
