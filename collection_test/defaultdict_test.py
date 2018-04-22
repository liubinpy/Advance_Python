""" 
@author: Frank
@file: defaultdict_test.py 
@time: 18-4-22 下午8:56 
"""
from collections import defaultdict


name_list = ["frank1", "frank2", "frank3", "frank4", "frank2", "frank1", "frank2"]

# name_nums_dict = {}
#
# for name in name_list:
# 	name_nums_dict.setdefault(name, 0)
# 	name_nums_dict[name] += 1
#
# print(name_nums_dict)

name_nums_defaultdict = defaultdict(int)  # defaultdict传入的是一个可调用的对象，比如函数，如果是函数那么字典的默认值为函数的返回值，当传入int的时候返回0


for name in name_list:
	name_nums_defaultdict[name] += 1

print(name_nums_defaultdict)

















