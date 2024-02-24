#!/usr/bin/python3

""" script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    nw_state = State(name='Louisiana')
    session_b.add(nw_state)
    nw_instance = session_b.query(State).filter_by(name='Louisiana').first()
    print(nw_instance.id)
    session_b.commit()
