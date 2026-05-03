#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # 1. Setup connection parameters
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # 2. Create the Engine
    # Format: mysql+mysqldb://user:password@host:port/database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db_name), pool_pre_ping=True)

    # 3. Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Query all State objects, sorted by id
    # This replaces the "SELECT * FROM states ORDER BY id ASC" raw SQL
    states = session.query(State).order_by(State.id).all()

    # 5. Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 6. Close the session
    session.close()
