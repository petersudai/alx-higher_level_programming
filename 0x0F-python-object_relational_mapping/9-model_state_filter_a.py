#!/usr/bin/python3
"""Lists all State objects that contain the letter a"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create Session
    session = Session()

    # Query all State objects containing letter 'a' and print
    states_with_a = session.query(State) \
                           .filter(State.name.like('%a%')) \
                           .order_by(State.id) \
                           .all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
