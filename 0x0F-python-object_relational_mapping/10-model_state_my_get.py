#!/usr/bin/python3

""" script that prints the State object with the name passed as argument
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
    instance = session_b.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
