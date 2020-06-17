#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys, os.path, time
from os import listdir
from os.path import isfile, isdir, join


def get_all_files(path, filename):
	file_list = [f for f in listdir(path) if isfile(join(path, f))]
	dir_list = [d for d in listdir(path) if isdir(join(path, d))]
	print('dir_list')
	print(dir_list)

	filtered_list = list(filter(lambda x: x != filename, file_list))
	print('filtered_list')
	print(filtered_list)

	prepared_file_list = list(map(lambda x: '^/' + x, filtered_list))
	prepared_dir_list = list(map(lambda x: '^/' + x + '/', dir_list))

	full_list = prepared_file_list + prepared_dir_list
	print(full_list)
	return full_list


def main(file_path=None):
#	LOG_WATCH_FILENAME = 'postgresql-9.6-main.log'
	LOG_WATCH_FILENAME = 'mosquitto.log'
	EXCLUDE_FILE = 'exclude.lst'

	watched_dir = os.path.split(file_path)[0]
	print(f'watched_dir = {watched_dir}')

	ignore_patterns = get_all_files(watched_dir, LOG_WATCH_FILENAME)

	with open(EXCLUDE_FILE, 'a') as ex_f:
		for item in ignore_patterns:
			print(item)
			ex_f.write(item + '\n')


if __name__ == "__main__":
	if len(sys.argv) > 1:
		path = sys.argv[1]
		main(file_path=path.strip())
	else:
		sys.exit(1)
