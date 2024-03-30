#!/usr/bin/python3
"""adds the state object 'Louisiana' to a database"""
import argparse
from sqlalchemy import create_engine
from model_state import Base, State
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
    """query a database with data passed as arguments"""

    db_url = f"mysql+mysqldb://{uname}:{pword}@localhost:3306/{db}"

    engine = create_engine(db_url)

    Session = sessionmaker()
    Session.configure(bind=engine)

    # create handle to interest with database
    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)


if __name__ == "__main__":
    cred = parse_cmd_args()
    username = cred[0]
    password = cred[1]
    database = cred[2]

    query_db_with_orm(username, password, database)
