#!/usr/bin/python3
"""
Lists all values in the states table where name matches the argument
in a way that is safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    st_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (st_name,))

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
