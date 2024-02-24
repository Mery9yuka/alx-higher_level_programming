#!/usr/bin/python3

""" script that lists all State objects that contain the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    Engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(Engine)
    Session_a = sessionmaker(bind=Engine)
    session_b = Session_a()
    for Instance in session_b.query(State).filter(State.name.like('%a%')):
        print(Instance.id, Instance.name, sep=": ")
