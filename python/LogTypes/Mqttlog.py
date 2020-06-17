#!/usr/bin/python3

class Mqttlog(object):

	timereported = None
	message = None

	def __init__(self, dictionary):
		self.__dict__.update(dictionary)


	def __repr__(self):
		return f"<Timereported:{self.timereported} message:{self.message}>"


	def __str__(self):
		return f"Mqttlog: date is {self.timereported}, message is {self.message}"


	def see_message(self):
		print(f"The message is {this.message}")

