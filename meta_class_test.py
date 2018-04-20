""" 
@author: Frank
@file: meta_class_test.py 
@time: 18-4-20 下午12:26 
"""
# 元类就是创建类的类


# def say(self):
# 	return "hi"
#
# User = type("User", (), {"name": "frank", "say": say})  # type(类名,(父类,),{各种属性和方法})
# user = User()
# print(user.name)
# print(user.say())

# 在python3中可以通过metaclass来实现控制类的生成


class UserBase(type):
	def __new__(cls, *args, **kwargs):
		print("in metaclass")
		return super().__new__(cls, *args, **kwargs)


class User(metaclass=UserBase):
	def __init__(self, name):
		print("in class")
		self.name = name

user = User("frank")
print(user.name)



















