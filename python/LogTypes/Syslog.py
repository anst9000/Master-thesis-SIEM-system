#!/usr/bin/python3

class Syslog(object):

	timereported = None
	hostname = None
	syslogtag = None
	message = None

	def __init__(self, dictionary):
		self.__dict__.update(dictionary)


	def __repr__(self):
		return "<hostname:%s syslogtag:%s>" % (self.hostname, self.syslogtag)


	def __str__(self):
		return "Syslog: date is %s, syslogtag is %s" % (self.timereported, self.syslogtag)


	def see_message(self):
		print("The message is ", this.message)

