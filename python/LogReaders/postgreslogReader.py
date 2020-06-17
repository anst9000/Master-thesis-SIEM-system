#!/usr/bin/python3

from __future__ import print_function
import re
import os
from LogModules.PgLineReader import get_last_n_lines as lastPgLines


def get_hostname(hostname):
	return ''.join(filter(str.isalnum, hostname)) if hostname else ""


def get_db_info(db_info):
	if db_info:
		if '@' in db_info and len(db_info) > 1:
			return db_info.split('@')
		else:
			return db_info, ""
	else:
		return "", ''


def parse_rest_part(rest_part):
	rest_part_list = rest_part.split('|', 4)
	hostname = get_hostname(rest_part_list[1])
	db_user, database = get_db_info(rest_part_list[2])
	pid = rest_part_list[3]
	message = rest_part_list[4]

	return hostname, db_user, database, pid, message


def parse_string(s):
	date_part, rest_part_list = s.split('CEST', 1)
	timereported = date_part.rstrip()

	hostname, db_user, database, pid, message = parse_rest_part(rest_part_list)

	postgreslog_row = {
		'timereported': timereported,
		'hostname': hostname,
		'db_user': db_user,
		'database': database,
		'pid': pid,
		'message': message
	}

	return postgreslog_row


def print_list(item):
	postgreslog_row = parse_string(item)
	return postgreslog_row


def run(nr):
	print('so many lines', nr)
	file_name = '/var/log/postgresql/postgresql-9.6-main.log'
	db_post_list = []
	nr_of_lines = nr
	print('so many lines will be fetched', nr)
	lines = lastPgLines(file_name, nr_of_lines)

	for line in lines:
		print('>>>> line =', line)
		if (line == ""):
			continue

		db_post = print_list(line)
		db_post_list.append(db_post)

	return db_post_list


if __name__ == '__main__':
	run()
