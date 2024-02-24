#!/usr/bin/python3

""" Script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    data_base = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3])

    curs = data_base.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    row = curs.fetchall()
    for r in row:
        print(row)
    curs.close()
    data_base.close()
