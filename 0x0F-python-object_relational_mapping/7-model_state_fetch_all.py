#!/usr/bin/python3

"""Start link class to table in database
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    Engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(Engine)
    session = sessionmaker(bind=Engine)
    Session = session()
    for instance in Session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
