""" 
@author: Frank
@file: iterable_test.py 
@time: 18-4-20 下午8:38 
"""
# 什么是迭代器
# 迭代器是什么？ 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性访问数据的方式

from collections.abc import Iterable, Iterator
#
# a = [1, 2, 3]
#
# print(isinstance(a, Iterable))  # True
# print(isinstance(a, Iterator))  # False


class Company:
	def __init__(self, staffs):
		self.staffs = staffs

	def __iter__(self):
		return CompanyIterator(self.staffs)


class CompanyIterator(Iterator):
	def __init__(self, staffs):
		self.staffs = staffs
		self.index = 0

	def __next__(self):
		try:
			value = self.staffs[self.index]
		except IndexError:
			raise StopIteration
		self.index += 1
		return value

if __name__ == "__main__":
	c = Company(['Frank', 'Jeff', 'Tom'])
	for staff in c:
		print(staff)

	print(isinstance(c, Iterable))
	print(isinstance(iter(c), Iterator))
