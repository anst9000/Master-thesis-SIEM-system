#!/usr/bin/python3

class Person:

	def __init__(self, name, company):
		self.name = name
		self.company = company


	def __repr__(self):
		return "<Test name:%s company:%s>" % (self.name, self.company)


	def __str__(self):
		return "From str method of Test: name is %s, company is %s" % (self.name, self.company)


	def see_company(self):
		print("The company is ", this.company)

