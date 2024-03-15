#!/usr/bin/python3
"""
Script to list all states from a MySQL database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", E)
        sys.exit(1)

    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        cursor.close()
        db.close()
        sys.exit(1)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
