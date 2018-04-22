""" 
@author: Frank
@file: counter_test.py 
@time: 18-4-22 下午9:38 
"""
from collections import Counter

name_list = ["frank1", "frank2", "frank3", "frank4", "frank2", "frank1", "frank2"]


name_counter = Counter(name_list)
print(name_counter)
print(name_counter.most_common(2))