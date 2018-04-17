""" 
@author: Frank
@file: everything_is_object.py 
@time: 18-4-16 下午3:59 
"""
"""
 函数和类也是对象，给属于pytho的一等公民。
 那什么是一等公民呢？
 1. 可以赋值给一个变量
 2. 可以添加到集合对象中
 3. 可以做为参数传递给函数
 4. 可以当做函数的返回值

"""


def print_name(name):

	return "my name is " + name


class People:
	def __init__(self, name, age):
		self.name = name
		self.age = age

# 1
pname = print_name
print(pname('frank'))

hummer = People
h = hummer('frank', 24)
print(h.name)

# 2
lis = [print_name, People]
li = lis[1]('rose', 22)
print(li.name)

# 3,4
def wrapper(func):
	return func

wrapper(print_name)














