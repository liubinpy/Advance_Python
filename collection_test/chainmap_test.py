""" 
@author: Frank
@file: chainmap_test.py 
@time: 18-4-22 下午10:34 
"""
from collections import ChainMap

dict1 = {"b": "bob", "f": "frank"}
dict2 = {"b": "bob", "r": "rose"}

dict_new = ChainMap(dict1, dict2)
print(dict_new)

for k,v in dict_new.items():
	print(k, v)   # 对于相同的元素只会取一次

dict_new.new_child({"j": "jeff"})
