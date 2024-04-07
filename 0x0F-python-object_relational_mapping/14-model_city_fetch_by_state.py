#!/usr/bin/python3
"""scripts that prints all City objects from a database passed as argument"""
import argparse
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
from model_state import Base, State


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

    result = session.query(State, City).join(City).all()

    for s, c in result:
        print(f"{s.name}: ({c.id}) {c.name}")


if __name__ == "__main__":
    cred = parse_cmd_args()
    username = cred[0]
    password = cred[1]
    database = cred[2]

    query_db_with_orm(username, password, database)
