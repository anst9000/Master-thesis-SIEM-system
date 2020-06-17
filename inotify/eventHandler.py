#!/usr/bin/python3

import pyinotify
import json
import datetime
from MqttModules import MqttPublisher as pub
from ConnectPostgreSQL import app_mqttlog
from ConnectPostgreSQL import app_postgreslog
from ConnectPostgreSQL import app_syslog


def handle_modify(self, event):
	date_time = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
	data = {
		'Event': f'File {event.path} was just modified',
		'Watch': f'Watch {event.wd}',
		'Date': date_time
	}
#	json_data = json.dumps(data)
#	print(json_data)

	switcher = {
		1: watcher_one,
		2: watcher_two,
		3: watcher_three
	}

	# Get the function from switcher dictionary
	func = switcher.get(event.wd, lambda: "Invalid month")

	# Execute the function
	func(data)
#	print(func())


def watcher_one(data):
	topic = 'Mosquitto'
	data['Topic'] = topic
	json_data = json.dumps(data)
	print(json_data)
	pub.main(json_data)
	print('Now going to app_syslog from mosquitto')
	app_syslog.main()


def watcher_two(data):
	topic = 'syslog'
	data['Topic'] = topic
	json_data = json.dumps(data)
	print(json_data)
	pub.main(json_data)
	print('Now going to app_syslog')
	app_syslog.main()


def watcher_three(data):
	topic = 'PostgreSQL'
	data['Topic'] = topic
	json_data = json.dumps(data)
	print(json_data)
	pub.main(json_data)
#	app_syslog.main()



class EventHandler(pyinotify.ProcessEvent):
	def process_IN_ACCESS(self, event):
		print("ACCESS event:", event.pathname)

	def process_IN_ATTRIB(self, event):
		print("ATTRIB event:", event.pathname)

	def process_IN_CLOSE_NOWRITE(self, event):
		print("CLOSE_NOWRITE event:", event.pathname)

	def process_IN_CLOSE_WRITE(self, event):
		print("CLOSE_WRITE event:", event.pathname)

	def process_IN_CREATE(self, event):
		print("CREATE event:", event.pathname)

	def process_IN_DELETE(self, event):
		print("DELETE event:", event.pathname)

	def process_IN_MODIFY(self, event):
		print("MODIFY event:", event.pathname)
		handle_modify(self, event)

	def process_IN_OPEN(self, event):
		print("OPEN event:", event.pathname)
