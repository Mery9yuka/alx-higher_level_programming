#!/usr/bin/python3

""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys


if __name__ == "__main__":
    data_base = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = data_base.cursor()
    curs.execute("SELECT * FROM states")
    r = curs.fetchall()
    for row in r:
        print(row)
    curs.close()
    data_base.close()
