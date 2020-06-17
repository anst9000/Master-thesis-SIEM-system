#!/usr/bin/python3

import psycopg2
from ConnectPostgreSQL.config import config
from LogTypes.Mqttlog import Mqttlog
from LogReaders import mqttlogReader as mqttReader


def getData():
	return mqttReader.run()


def makeMqttlogs(data_list):
	mqttlog_list = []

	for data in data_list:
		mqttlog = Mqttlog(data)
		mqttlog_list.append(mqttlog)

	return mqttlog_list


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

		print('Inserting data into table mqttprimary:')

		insert_query = \
			f'''INSERT INTO mqttprimary 
			(timereported, message) 
			VALUES (%s, %s)'''
		for data in data_list:
			record_to_insert = (data.timereported, data.message)
			cur.execute(insert_query, record_to_insert)
			conn.commit()

#		print('Show all content from table mqttprimary:')
#		all_query = 'SELECT * FROM mqttprimary'
#		cur.execute(all_query)
#		mqttprimary_result = cur.fetchall()
#		print(mqttprimary_result)
#
#		for row in mqttprimary_result:
#			print('id = ', row[0])
#			print('timereported = ', row[1])
#			print('message = ', row[2])

		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection is now closed')


def main():
	data = getData()
	mqttlog_list = makeMqttlogs(data)
	connect(mqttlog_list)


if __name__ == '__main__':
	main()
