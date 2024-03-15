#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    # Create cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")

    # Fetch all the rows and print them
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
