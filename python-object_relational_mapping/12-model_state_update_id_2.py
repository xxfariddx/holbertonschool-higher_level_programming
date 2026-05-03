#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get database credentials from command line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create the connection engine
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. Fetch the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # 2. If the state exists, update its name
    if state_to_update:
        state_to_update.name = "New Mexico"

        # 3. Commit the session to persist changes in the database
        session.commit()

    # Close the session
    session.close()
