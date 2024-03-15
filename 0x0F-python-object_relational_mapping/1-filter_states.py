#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N' from a MySQL database.
"""

import MySQLdb
import sys

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

    # Execute SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")
    
    # Fetch all results
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and MySQL connection
    cursor.close()
    db.close()
