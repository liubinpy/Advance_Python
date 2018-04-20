""" 
@author: Frank
@file: __getattr__And__getAttribute.py 
@time: 18-4-20 上午10:00 
"""
from datetime import datetime, date

class Person:
	def __init__(self, name, birthday, info):
		self.name = name
		self.birthday = birthday
		self.info = info

	def __getattr__(self, item):  # getattr 在属性查找不到的时候执行
		return self.info[item]

	def __getattribute__(self, item):  # getattribute 不管查不查的到都会调用
		return "here"



p = Person("frank", date(year=1994, month=11, day=7), {"company": "commverge", "salary": "10k"})


print(p.company)
