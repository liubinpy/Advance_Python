""" 
@author: Frank
@file: deque_test.py 
@time: 18-4-22 下午9:21 
"""

"""
deque(双端队列)是线程安全的，list是线程不安全的
"""
from collections import deque


user_deque = deque(("frank", "bob", "rose"))
print(user_deque)

user_deque.appendleft("jack")
print(user_deque)