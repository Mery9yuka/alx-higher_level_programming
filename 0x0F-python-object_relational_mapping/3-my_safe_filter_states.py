#!/usr/bin/python3

""" script that takes in arguments and displays
    all values in the states table of hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    data_base = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = data_base.cursor()
    match_str = sys.argv[4]
    curs.execute("SELECT * FROM states WHERE name LIKE %s", (match_str, ))
    row = curs.fetchall()
    for r in row:
        print(r)
    curs.close()
    data_base.close()
