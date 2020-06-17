#!/usr/bin/python3
import os
from pathlib import Path
from configparser import ConfigParser

def config(filename='/database.ini', section='postgresql'):
	filepath = Path(__file__).resolve().parent
	full_file_name = str(filepath) + filename
	parser = ConfigParser()
	parser.read(full_file_name)
	db = {}

	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception(f'Section {section} not found in the {filename} file')

	return db
