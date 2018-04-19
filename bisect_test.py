""" 
@author: Frank
@file: bisect_test.py 
@time: 18-4-19 下午3:36 
"""
import bisect

bisect_list = []

bisect.insort(bisect_list, 1)
bisect.insort(bisect_list, 4)
bisect.insort(bisect_list, 3)
bisect.insort(bisect_list, 2)
bisect.insort(bisect_list, 10)

print(bisect_list)