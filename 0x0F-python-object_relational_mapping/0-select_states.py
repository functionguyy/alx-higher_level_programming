#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import argparse
import sys
import MySQLdb


def query_db():
    parser = argparse.ArgumentParser(prog="MySQL_login")
    parser.add_argument('username')
    parser.add_argument('password')
    parser.add_argument('db_name')
    args = parser.parse_args()

    db_conn = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=args.username,
                              passwd=args.password,
                              db=args.db_name, charset="utf8")
    db_cur = db_conn.cursor()
    db_cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = db_cur.fetchall()
    for row in query_rows:
        print(row)
    db_cur.close()
    db_conn.close()


if __name__ == '__main__':
    query_db()
