#!/usr/bin/python3
"""A module that creates the State California with the City"""
import argparse
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker


def parse_cmd_args():
    """process command line arguments"""
    parser = argparse.ArgumentParser(prog="MySQL_login")
    parser.add_argument('username')
    parser.add_argument('password')
    parser.add_argument('db_name')
    args = parser.parse_args()

    cred = (args.username, args.password, args.db_name)

    return cred


def query_db_with_orm(uname, pword, db):
    """
    query a database with data passed as command line arguments
        Args:
        uname: (str): A username of the database
        pword: (str): The database password
        db_name: (str): The name of the database to use
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname,
                                                              pword,
                                                              db)
    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    new_state = State(name="California")
    city = City(name="San Francisco")
    new_state.cities.append(city)
    session.add(new_state)
    session.commit()
    session.close()


if __name__ == "__main__":
    cred = parse_cmd_args()
    username = cred[0]
    password = cred[1]
    database = cred[2]

    query_db_with_orm(username, password, database)
