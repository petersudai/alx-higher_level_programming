#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "___main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    ecngine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(username, password, db_name))

    Base.medadate.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
