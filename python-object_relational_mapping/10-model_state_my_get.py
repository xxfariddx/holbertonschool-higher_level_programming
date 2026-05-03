#!/usr/bin/python3
"""
Prints the State object ID with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get arguments from command line
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_to_search = sys.argv[4]

    # Create engine and connect to the database
    # localhost at port 3306
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object based on the name argument
    # SQLAlchemy's .filter() method handles SQL injection protection
    state = session.query(State).filter(State.name == state_to_search).first()

    # Check if state exists and print results
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
