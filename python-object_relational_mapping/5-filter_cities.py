#!/usr/bin/python3
"""
dszf
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = ("SELECT cities.name FROM cities "
             "INNER JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")

    cursor.execute(query, (state_name,))

    query_rows = cursor.fetchall()

    cities_list = [row[0] for row in query_rows]
    print(", ".join(cities_list))

    # Clean up
    cursor.close()
    db.close()
