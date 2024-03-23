#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import argparse
import MySQLdb


def query_db():
    """query a database with data passed as command line arguments"""
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
    query = """SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s ON
               c.state_id = s.id ORDER BY c.id ASC"""

    db_cur.execute(query)
    query_rows = db_cur.fetchall()
    for row in query_rows:
        print(row)
    db_cur.close()
    db_conn.close()


if __name__ == '__main__':
    query_db()
