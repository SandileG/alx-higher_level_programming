#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                        user=username, passwd=password, db=database)

    # Create a sursor object
    cur = db.cursor()

    # Execute SQL query to select all states sorted by id
    sur.execute("SELECT * FROM states ORDER BY id")

    # Fetch all rows
    rows = cur.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

   
