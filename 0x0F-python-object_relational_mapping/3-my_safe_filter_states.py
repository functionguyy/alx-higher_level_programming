#!/usr/bin/python3
""" script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument state_name
"""
import argparse
import MySQLdb


def query_db():
    """query a database with command line arguments"""
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
    query_template = """SELECT * FROM states WHERE name LIKE %s
                        ORDER BY id ASC"""
    state_name = args.state_name
    db_cur.execute(query_template, (state_name,))
    query_rows = db_cur.fetchall()
    for row in query_rows:
        print(row)
    db_cur.close()
    db_conn.close()


if __name__ == '__main__':
    query_db()
