""" 
@author: Frank
@file: super?.py 
@time: 18-4-18 下午4:45 
"""
"""
super真的是调用了父类的方法吗？
"""


class A:
	def __init__(self):
		print("A")


class B(A):
	def __init__(self):
		print("B")
		super().__init__()


class C(A):
	def __init__(self):
		print("C")
		super().__init__()


class D(B, C):
	def __init__(self):
		print("D")
		super().__init__()

if __name__ == "__main__":
	d = D()
	print(D.__mro__)

"""
super的继承会按照mro的顺序
"""



