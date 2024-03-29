#!/usr/bin/python3
"""script that print first state"""
import argparse
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def parse_cmd_args():
    """process command line argument"""
    parser = argparse.ArgumentParser(prog="MySQL_login")
    parser.add_argument('username')
    parser.add_argument('password')
    parser.add_argument('db_name')
    args = parser.parse_args()

    cred = (args.username, args.password, args.db_name)

    return cred


def query_db_with_orm(uname, pword, db):
    """query a database with data passed as command line arguments"""

    db_url = f"mysql+mysqldb://{uname}:{pword}@localhost:3306/{db}"

    engine = create_engine(db_url)

    Session = sessionmaker()
    Session.configure(bind=engine)

    # create handle to interact with database
    session = Session()

    result = session.query(State).filter(State.name.ilike('%a%')).\
        order_by(State.id)

    for row in result:
        print(f"{row.id}: {row.name}")


if __name__ == "__main__":
    cred = parse_cmd_args()
    username = cred[0]
    password = cred[1]
    database = cred[2]

    query_db_with_orm(username, password, database)
