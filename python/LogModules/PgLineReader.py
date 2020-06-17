#!/usr/bin/python3
from __future__ import print_function
import re
import os


def get_last_n_lines(file_name, N):
	print('wil get', N, 'lines')
	is_printed = False
	new_line = ""
	part_line_list = []
	list_of_lines = []
	regexp = '^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]'

	for index, line in enumerate(reversed(list(open(file_name)))):
		# if row begins with timestamp format YYYY-MM-DD hh:mm:ss
		if re.search(regexp, line):
			part_line_list.append(line)

			if len(part_line_list) > 1:
				for item in reversed(part_line_list):
					new_line += item
			else:
				new_line = line

			list_of_lines.append(new_line)
			new_line = ""
			part_line_list = []
			print('list_of_lines now', len(list_of_lines))
			print('N is', N)

			if len(list_of_lines) == int(N):
				for item in list_of_lines:
					print('the item of course is', item)
#				print(list_of_lines)
				return list_of_lines

		else:
			part_line_list.append(line)

#	for item in list_of_lines:
#		print('the item is', item)
	return list_of_lines

