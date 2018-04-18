""" 
@author: Frank
@file: _And__.py 
@time: 18-4-18 下午3:44 
"""

"""
1、_xxx 不能用于’from module import *’ 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。 保护

2、__xxx 双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访问了。连子类也不可以.  私有

"""


class Area:
	"""
	矩形面积
	"""
	def __init__(self, width, height):
		self.__width = width
		self.__height = height

	def get_area(self):
		return self.__width * self.__height

a = Area(2, 3)
print(a.get_area())
print(a._Area__width)  # 获取私有属性的方法 _ClassName__Atrr
