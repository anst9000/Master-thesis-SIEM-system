#!/usr/bin/python3
import psycopg2
from config import config


def printResult(rows):
	for row in rows:
		print(row)


def connect(type, query_string):
	conn = None

	try:
		params = config()

		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()

		print('PostgreSQL database version:')
		cur.execute('SELECT version()')

		db_version = cur.fetchone()
		print(db_version)

		print(query_string)
		cur.execute(query_string)
		rows = cur.fetchall()
		printResult(rows)

		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection is now closed')

if __name__ == '__main__':
	type = 'GET'
	table = 'people '
	filter = ''
	values = ''
	query = 'SELECT * FROM '
	query_string = query + table + filter + values
	connect(type, query_string)

