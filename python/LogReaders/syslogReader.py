#!/usr/bin/python3

from __future__ import print_function
import re
import os
from LogModules.LineReader import get_last_n_lines as lastLines


def parse_not_time_part(ntp):
	host_and_tag, message = ntp.split(':', 1)
	hostname, syslogtag = host_and_tag.split(' ')
	message = message.lstrip()

	return hostname, syslogtag, message


def parse_string(s):
	timereported = s[:32]
	not_time_part = s[33:]

	hostname, syslogtag, message = parse_not_time_part(not_time_part)

	syslog_row = {
		'timereported': timereported,
		'hostname': hostname,
		'syslogtag': syslogtag,
		'message': message
		}
	return syslog_row


def print_list(item):
	syslog_row = parse_string(item)
	return syslog_row


def run():
	file_name = '/var/log/syslog'
	db_post_list = []
	nr_of_lines = 2
	lines = lastLines(file_name, nr_of_lines)

	for line in lines:
		if (line == ""):
			continue

		db_post = print_list(line)
		db_post_list.append(db_post)

	return db_post_list


if __name__ == '__main__':
	run()
