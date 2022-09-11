#!/usr/bin/python3
"""
Module 0-select_states
lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    myCursor = db.cursor()
    myCursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = myCursor.fetchall()
    for row in rows:
        print(row)

    myCursor.close()
    db.close()
