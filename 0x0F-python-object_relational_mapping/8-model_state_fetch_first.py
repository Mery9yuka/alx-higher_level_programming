#!/usr/bin/python3

""" script that prints the first
    State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session_a = sessionmaker(bind=engine)
    session_b = Session_a()
    Instance = session_b.query(State).first()
    if Instance is None:
        print("Nothing")
    else:
        print(Instance.id, Instance.name, sep=": ")
