""" 
@author: Frank
@file: array_test.py 
@time: 18-4-19 下午3:50 
"""

import array

# 数组里面的元素只能是一种类型的
my_array = array.array("i")  # i代表是整形的数字
my_array.append(1)
my_array.append(1)
my_array.append(1)
print(my_array)