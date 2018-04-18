""" 
@author: Frank
@file: contextlib_with.py 
@time: 18-4-18 下午6:17 
"""
import contextlib


@contextlib.contextmanager
def file_open(file_name):
	print("file open")
	yield {}
	print("file end")


with file_open("a.txt") as f_open:
	print("file processing")






