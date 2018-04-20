""" 
@author: Frank
@file: __new__And__init__.py 
@time: 18-4-20 上午11:11 
"""


class User:
	def __new__(cls, *args, **kwargs):
		print("in new")
		return super().__new__(cls)

	def __init__(self):
		print("in init")
		pass

if __name__ == "__main__":
	user = User()

# __new__  是用来控制对象的生产过程，在对象生成之前
# __init__ 是用来完善对象的，比如给对象赋值
# 如果__new__不返回对象，则不会返回init函数
