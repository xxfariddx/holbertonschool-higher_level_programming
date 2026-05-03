#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Command line arqumentlərini götürürük
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Verilənlər bazasına qoşulma mühərrikini yaradırıq
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Session (sessiya) yaradırıq
    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. Adında 'a' hərfi olan bütün State obyektlərini tapırıq
    # .like('%a%') SQL-dəki LIKE '%a%' ifadəsinə bərabərdir
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # 2. Tapılan hər bir obyekti session-dan silirik
    for state in states_to_delete:
        session.delete(state)

    # 3. Dəyişiklikləri bazada qalıcı edirik
    session.commit()

    # Sessiyanı bağlayırıq
    session.close()
