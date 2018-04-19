""" 
@author: Frank
@file: slice_object.py 
@time: 18-4-19 下午3:02 
"""
"""
实现一个可切片的序列
"""
from collections import abc
import numbers

class Company:
	def __init__(self, company_name, group_name, staffs):
		self.company_name = company_name
		self.group_name = group_name
		self.staffs = staffs

	def __len__(self):
		return len(self.staffs)

	def __getitem__(self, item):
		cls = type(self)
		if isinstance(item, slice):
			return cls(self.company_name, self.group_name, self.staffs[item])
		elif isinstance(item, numbers.Integral):
			return cls(self.company_name, self.group_name, [self.staffs[item]])

	def __contains__(self, item):
		return True if item in self.staffs else False

	def __reversed__(self):
		return reversed(self.staffs)


com = Company("sony", "user", ["Tom", "Frank", "Rose", "Jeff", "Andy"])


print(len(com))  # 获取长度
c0 = com[0:2]
c = com[1]
if "tom" in com:
	print("in")
else:
	print("not in")
print(reversed(com))