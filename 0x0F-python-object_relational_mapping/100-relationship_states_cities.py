#!/usr/bin/python3
"""Script to create State 'California' with the City 'San Francisco' from a
database"""
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
    """query a database with data passed as command line arguments"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname,
                                                              pword,
                                                              db)
    engine = create_engine(db_url)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # create database table
    Base.metadata.create_all(engine)

    new_state = State(name="California")
    new_state.cities = [City(name="San Francisco")]
    session.add(new_state)
    session.commit()
    # query the database for the state 'California' and if it returns None
    # create a State 'California' and add the city 'San Francisco' to it
    # add new state object to database using session
    # commit


if __name__ == "__main__":
    cred = parse_cmd_args()
    username = cred[0]
    password = cred[1]
    database = cred[2]

    query_db_with_orm(username, password, database)
