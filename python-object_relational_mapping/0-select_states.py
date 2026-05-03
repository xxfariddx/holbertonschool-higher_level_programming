#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Access arguments provided in the command line
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query and sort by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the executed query
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
