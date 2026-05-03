#!/usr/bin/python3
"""sdafsdf"""
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

    cursor.execute("SELECT * FROM states WHERE name = BINARY '{}' " \
    "ORDER BY id ASC".format(st_name))

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
