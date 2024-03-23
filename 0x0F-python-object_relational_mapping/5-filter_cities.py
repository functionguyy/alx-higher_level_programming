#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities
of that state in a database passed as argument
"""
import argparse
import MySQLdb


def query_db():
    """query a database with data passed as command line arguments"""
    parser = argparse.ArgumentParser(prog="MySQL_login")
    parser.add_argument('username')
    parser.add_argument('password')
    parser.add_argument('db_name')
    parser.add_argument('state_name')
    args = parser.parse_args()

    db_conn = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=args.username,
                              passwd=args.password,
                              db=args.db_name, charset="utf8")
    db_cur = db_conn.cursor()
    query_template = """SELECT c.name FROM cities c INNER JOIN states s ON
                        c.state_id = s.id WHERE s.name = %s"""

    state_name = args.state_name
    db_cur.execute(query_template, (state_name,))
    query_rows = db_cur.fetchall()
    row_count = db_cur.rowcount

    for row in query_rows:
        print(row[0], end="")
        row_count = row_count - 1
        if row_count > 0:
            print(",", end=" ")

    print()

    db_cur.close()
    db_conn.close()


if __name__ == '__main__':
    query_db()
