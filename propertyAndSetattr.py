""" 
@author: Frank
@file: propertyAndSetattr.py 
@time: 18-4-20 上午9:47 
"""
from datetime import datetime, date

class Person:
	def __init__(self, name, birthday):
		self.name = name
		self.birthday = birthday
		self._age = 0

	@property
	def age(self):
		return datetime.now().year - self.birthday.year

	@age.setter
	def age(self, value):
		self._age = value


p = Person("frank", date(year=1994, month=11, day=7))


print(p.age)
p.age = 21
print(p.age)
print(p._age)
