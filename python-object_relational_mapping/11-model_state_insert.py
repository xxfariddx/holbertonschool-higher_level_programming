#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get database credentials from arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Set up the connection engine
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. Create a new State object
    new_state = State(name="Louisiana")

    # 2. Add the object to the session
    session.add(new_state)

    # 3. Commit the session to save changes to the database
    session.commit()

    # 4. Print the new state's id
    # After commit, SQLAlchemy automatically retrieves the generated ID
    print(new_state.id)

    # Close the session
    session.close()
