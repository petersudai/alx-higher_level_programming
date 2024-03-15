#!/usr/bin/python3
"""
Lists all states with a name matching the argument
from the database hbtn_0e_0_usa, safe from MySQL injection.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    # Create cursor object
    cursor = db.cursor()

    #Execute SQL  query to select states
    cursor.execute("SELECT * FROM states WHERE name = %s \
                    ORDER BY states.id ASC", (sys.argv[4],))

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close cursor and MySQL connection
    cursor.close()
    db.close()
