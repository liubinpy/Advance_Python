""" 
@author: Frank
@file: abstract_base_class.py 
@time: 18-4-17 下午10:55 
"""

from collections.abc import *

import abc


class DataBase(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def connect(self):
		pass

	@abc.abstractmethod
	def get(self):
		pass


class RedisDataBase(DataBase):
	pass

r = RedisDataBase()  # TypeError: Can't instantiate abstract class RedisDataBase with abstract methods connect, get