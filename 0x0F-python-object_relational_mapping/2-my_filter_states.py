#!/usr/bin/python3
"""
Script to list all values in the states table of a MySQL database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> "
              "<database name> <state name searched>".format(sys.argv[0]))
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    cursor = db.cursor()

    try:
        cursor.execute("""SELECT * FROM states
                          WHERE name LIKE BINARY '{}'
                          ORDER BY states.id ASC""".format(
                              sys.argv[4]).strip("'"))
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        cursor.close()
        db.close()
        sys.exit(1)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
