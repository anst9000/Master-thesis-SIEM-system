#!/usr/bin/python3

class Postgreslog(object):

	timereported = None
	hostname = None
	db_user = None
	database = None
	pid = None
	message = None

	def __init__(self, dictionary):
		self.__dict__.update(dictionary)


	def __repr__(self):
		return "<Date is:%s database:%s>" % (self.timereported, self.database)


	def __str__(self):
		return "Postgreslog: Date is %s, database is %s" % (self.timereported, self.database)


	def see_message(self):
		print("The message is ", this.message)

