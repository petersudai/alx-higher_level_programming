#!/usr/bin/python3
"""
Lists all cities of a given state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Parse command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object
    cursor = db.cursor()

    # Prepare SQL query to retrieve citiies of given state
    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """

    # Execute SQL query
    cursor.execute(query, (state_name,))

    # Fetch all the results
    cities = cursor.fetchall()

    # Print names of cities
    print(', '.join(city[0] for city in cities))

    # Close cursor and database connection
    cursor.close()
    db.close()
