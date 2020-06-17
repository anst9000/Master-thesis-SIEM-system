#!/usr/bin/python3

import psycopg2
from ConnectPostgreSQL.config import config
from LogTypes.Syslog import Syslog
from LogReaders import syslogReader as sysReader


def getData():
	return sysReader.run()


def makeSyslogs(data_list):
	syslog_list = []
#	print('data_list = ', data_list)

	for data in data_list:
		syslog = Syslog(data)
		syslog_list.append(syslog)

	return syslog_list


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

		print('Inserting data into table syslogprimary:')
		insert_query = \
			f'''INSERT INTO syslogprimary
			(timereported, hostname, syslogtag, message)
			VALUES (%s, %s, %s, %s)'''
		for data in data_list:
			record_to_insert = (data.timereported, data.hostname, data.syslogtag, data.message)
			cur.execute(insert_query, record_to_insert)
			conn.commit()
#			count = cur.rowcount
#
#		print('Show all content from table syslogprimary:')
#		all_query = 'SELECT * FROM syslogprimary'
#		cur.execute(all_query)
#		syslogprimary_result = cur.fetchall()
#		print(syslogprimary_result)
#
#		for row in syslogprimary_result:
#			print('id = ', row[0])
#			print('timereported = ', row[1])
#			print('hostname = ', row[2])
#			print('syslogtag = ', row[3])
#			print('message = ', row[4])

		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection is now closed, man...')


def main():
	print('Now in app_syslog')
	data = getData()
#	print('\n--------------> data is', data)
	syslog_list = makeSyslogs(data)
	connect(syslog_list)



if __name__ == '__main__':
	main()
