""" 
@author: Frank
@file: isinstanceAndType.py 
@time: 18-4-17 下午11:18 
"""
"""
在判断对象的类型的时候尽量使用isinstance
"""

class A:
	pass

class B(A):
	pass

b = B()
print(isinstance(b, B))  # True
print(isinstance(b, A))  # True

print(type(b) is B)  # True,is是判断内存地址是否一样
print(type(b) is A)  # False
