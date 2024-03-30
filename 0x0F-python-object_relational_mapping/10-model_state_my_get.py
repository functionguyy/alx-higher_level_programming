#!/usr/bin/python3
"""prints the State object with name passed as argument from the database
passed as argument"""
import argparse
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


def parse_cmd_args():
    """process command line argument"""
    parser = argparse.ArgumentParser(prog="MySQL_login")
    parser.add_argument('username')
    parser.add_argument('password')
    parser.add_argument('db_name')
    parser.add_argument('state_name')
    args = parser.parse_args()

    cred = (args.username, args.password, args.db_name, args.state_name)

    return cred


def query_db_with_orm(uname, pword, db, state):
    """query a database with data passed as arguments"""

    db_url = f"mysql+mysqldb://{uname}:{pword}@localhost:3306/{db}"

    engine = create_engine(db_url)

    Session = sessionmaker()
    Session.configure(bind=engine)

    # create handle to interact with database
    session = Session()

    try:
        result = session.query(State).filter(State.name == state).one()
        print(f"{result.id}")
    except NoResultFound:
        print("Not found")


if __name__ == "__main__":
    cred = parse_cmd_args()
    username = cred[0]
    password = cred[1]
    database = cred[2]
    sname = cred[3]

    query_db_with_orm(username, password, database, sname)
