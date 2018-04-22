""" 
@author: Frank
@file: orderdict_test.py 
@time: 18-4-22 下午10:18 
"""
from collections import OrderedDict

order_dict = OrderedDict()  # 在python3中dict默认是有序的，但是在python2中是无序的，python2和python3的orderDict是一样的
# order_dict = dict()
order_dict["b"] = "bob"
order_dict["r"] = "rose"
order_dict["j"] = "jack"
order_dict["t"] = "tom"

# order_dict.popitem()
order_dict.move_to_end("b")
print(order_dict)