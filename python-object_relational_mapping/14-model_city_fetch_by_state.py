#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Verilənlər bazası məlumatlarını arqumentlərdən alırıq
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Engine yaradılır
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Session yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # Həm State, həm City obyektlərini çəkirik
    # filter hissəsində id-ləri bərabərləşdirərək JOIN məntiqini qururuq
    results = session.query(State, City).filter(State.id == City.state_id)\
                     .order_by(City.id.asc()).all()

    # Nəticələri tələb olunan formatda çap edirik
    # Format: <state name>: (<city id>) <city name>
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Sessiyanı bağlayırıq
    session.close()
