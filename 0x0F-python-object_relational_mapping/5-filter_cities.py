#!/usr/bin/python3

""" takes in the name of a state as an
    argument and lists all cities of that state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    data_base = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = data_base.cursor()
    curs.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = curs.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    curs.close()
    data_base.close()
