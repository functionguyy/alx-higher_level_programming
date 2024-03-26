#!/home/functionguyy/myenv/bin/python3
""" script """
import argparse
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select


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
    # create connection to database
    engine = create_engine(db_url)
    # Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()

    for instance in result:
        print(f"{instance.id}: {instance.name}")


if __name__ == "__main__":
    cred = parse_cmd_args()
    username = cred[0]
    password = cred[1]
    database = cred[2]

    query_db_with_orm(username, password, database)
