#!/usr/bin/python3
import psycopg2
from config import config
from Person import Person


def getData():
	names = ['Ammaarah Lord', 'Adem Thomson', 'Kaylan Schneider', 'Rebeca Sanford', 'Mya Searle', 'Aaliya Fuentes', 'Maggie Bateman', 'Isma Obrien', 'Darcey Orr', 'Yehuda Plant']
	companies = ['tually', 'earthluck', 'sinyard', 'hybridpoof', 'indywall', 'bondover', 'keepmint', 'reviewwhew', 'oildote', 'utahfond']
	return zip(names, companies)


def makePersons(data_list):
	person_list = []

	for data in data_list:
		person = Person(data[0], data[1])
		person_list.append(person)

	return person_list


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

		print('Inserting data into table people:')
		insert_query = 'INSERT INTO people VALUES (%s, %s)'
		for data in data_list:
			record_to_insert = (data.name, data.company)
			cur.execute(insert_query, record_to_insert)
			conn.commit()
#			count = cur.rowcount

		print('Show all content from table people:')
		all_query = 'SELECT * FROM people'
		cur.execute(all_query)
		people_result = cur.fetchall()
		print(people_result)

		for row in people_result:
			print('Name = ', row[0])
			print('Company = ', row[1])


		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection is now closed')

if __name__ == '__main__':
	data = getData()
	person_list = makePersons(data)
	connect(person_list)


