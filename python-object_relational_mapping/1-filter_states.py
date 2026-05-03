#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
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

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query with a filter for names starting with 'N'
    # Binary is used to ensure the 'N' is strictly uppercase
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                   "ORDER BY states.id ASC")

    # Fetch and print the results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Close connection
    cursor.close()
    db.close()
