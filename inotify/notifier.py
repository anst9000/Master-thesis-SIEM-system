#!/usr/bin/python3

import os
import pyinotify
from eventHandler import EventHandler


def main():
	# watch manager
	wm = pyinotify.WatchManager()

	# watched events
	mask = \
		pyinotify.IN_MODIFY | \
		pyinotify.IN_ACCESS | \
		pyinotify.IN_CLOSE_WRITE | \
		pyinotify.IN_CLOSE_NOWRITE

	# Exclude patterns from file
	excl_file = os.path.join(os.getcwd(), 'exclude.lst')
	excl = pyinotify.ExcludeFilter(excl_file)

	watch_path_list = [
#		'/var/log/mosquitto/mosquitto.log',
		'/var/log/syslog',
#		'/var/log/postgresql/postgresql-9.6-main.log'
	]

	# Add watches
	wdd = wm.add_watch(
		watch_path_list,
		mask,
		rec=True,
		exclude_filter=excl
	)

	# event handler
	eh = EventHandler()

	# notifier
	notifier = pyinotify.ThreadedNotifier(wm, eh)
	notifier.start()


if __name__ == '__main__':
	main()
