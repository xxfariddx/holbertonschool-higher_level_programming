#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup connection
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query only the first state ordered by id
    # .first() returns None if no match is found
    first_state = session.query(State).order_by(State.id).first()

    # Display results or "Nothing"
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close session
    session.close()
