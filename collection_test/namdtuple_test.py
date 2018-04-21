""" 
@author: Frank
@file: namdtuple_test.py 
@time: 18-4-21 下午11:05 
"""
from collections import namedtuple

User = namedtuple("User", ("name", "age", "company"))
info_list = ["frank", 24, "Cisco"]

#
# user = User(name="Frank", age=23, company="Cisco")
# user = User(*info_list)
#
# print(user.name)
# print(user.age)
# print(user.company)

# _make  可以直接传递一个可迭代的对象,不用加*
user = User._make(info_list)
# print(user.name)

# _asdict 可以将namedtuple转换成一个排序过的字典
user_dict = user._asdict()  # OrderedDict([('name', 'frank'), ('age', 24), ('company', 'Cisco')])
print(user_dict["name"])