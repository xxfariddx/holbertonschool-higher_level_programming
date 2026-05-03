#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup connection parameters
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db_name), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: Filter by name containing 'a', sorted by id
    # .filter(State.name.like('%a%')) matches 'a' anywhere in the string
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
