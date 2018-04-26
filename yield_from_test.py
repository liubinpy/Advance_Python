"""
在python3.3新加了 yield from语法
"""

"""
先来看一个例子
"""
from itertools import chain
"""
chain 可以传入多个可迭代的对象，然后对这些迭代器进行遍历
"""
string_list = ['qqq', 'www', 'eee', 'ddd']
int_list = [1, 2, 3, 4]

# for value in chain(string_list, int_list, range(10)):
#     print(value)

"""
实现自己的chain
"""
# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         yield from my_iterable

# for value in my_chain(string_list, int_list, range(10)):
#     print(value)

def g1(gen):
    yield  from  gen

def main():
    g = g1()
    g.send(None)

"""
main：调用方
g1：委托生成器
gen：子生成器
yield from 会在调用方与子生成器之间建立一个双向通道
"""