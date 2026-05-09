#!/usr/bin/python3
"""Lists all states with a name starting with N from hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_user,
        passwd=mysql_password,
        db=db_name,
        port=3306
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
