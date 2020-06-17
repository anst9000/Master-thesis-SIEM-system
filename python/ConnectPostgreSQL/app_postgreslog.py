#!/usr/bin/python3

import sys
import psycopg2
from ConnectPostgreSQL.config import config
from LogTypes.Postgreslog import Postgreslog
from LogReaders import postgreslogReader as pgReader


def getData(nr=1):
	print('nr of lines', nr)
	return pgReader.run(nr)


def makePostgreslogs(data_list):
	postgreslog_list = []

	for data in data_list:
		postgreslog = Postgreslog(data)
		postgreslog_list.append(postgreslog)

	return postgreslog_list


def connect(data_list):
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

		print('Inserting data into table postgresprimary:')
		insert_query = \
			f'''INSERT INTO postgresprimary
			(timereported, hostname, db_user, database, pid, message)
			VALUES (%s, %s, %s, %s, %s, %s)'''
		for data in data_list:
			record_to_insert = (data.timereported, data.hostname, data.db_user, data.database, data.pid, data.message)
			cur.execute(insert_query, record_to_insert)
			conn.commit()

#		print('Show all content from table postgresprimary:')
#		all_query = 'SELECT * FROM postgresprimary'
#		cur.execute(all_query)
#		postgresprimary_result = cur.fetchall()
#		print(postgresprimary_result)
#
#		for row in postgresprimary_result:
#			print('id = ', row[0])
#			print('timereported = ', row[1])
#			print('hostname = ', row[2])
#			print('db_user = ', row[3])
#			print('database = ', row[4])
#			print('pid = ', row[5])
#			print('message = ', row[6])

		cur.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Database connection is now closed')


def main():
#	nr_of_lines = sys.argv[1]
	data = getData()
	postgres_list = makePostgreslogs(data)
	connect(postgres_list)


if __name__ == '__main__':
	main()
