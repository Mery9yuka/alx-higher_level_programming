#!/usr/bin/python3

""" script that changes the name of a
    State object from the database hbtn_0e_6_usa
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
    nw_instance = session_b.query(State).filter_by(id=2).first()
    nw_instance.name = 'New Mexico'
    session_b.commit()
