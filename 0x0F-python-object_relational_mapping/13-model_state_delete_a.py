#!/usr/bin/python3

""" script that deletes all State objects with a
    name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    Engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(Engine)
    Session_a = sessionmaker(bind=Engine)
    session_b = Session_a()

    for Instance in session_b.query(State).filter(State.name.like('%a%')):
        session_b.delete(Instance)
    session_b.commit()
