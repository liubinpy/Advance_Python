""" 
@author: Frank
@file: customer_ORM.py 
@time: 18-4-20 下午4:48 
"""
import numbers

class Field:
	pass

class CharField(Field):
	def __init__(self, column_name=None, max_length=None):
		self.column_name = column_name
		self.max_length = max_length

	def __get__(self, instance, owner):
		return self._value

	def __set__(self, instance, value):
		if not isinstance(value, str):
			raise TypeError("CharField must be string")
		if self.max_length == None:
			raise ValueError("you must set max_length")
		if len(value) > self.max_length:
			raise ValueError("value len excess len of max_length")
		self._value = value


class InterField(Field):

	def __init__(self, column_name=None, min_value=None, max_value=None):
		self.column_name = column_name
		self.min_value = min_value
		self.max_value = max_value
		if min_value is not None:
			if not isinstance(min_value, numbers.Integral):
				raise TypeError("InterField must be Int")
			elif min_value < 0:
				raise ValueError("min_value must be positive int")

		if max_value is not None:
			if not isinstance(max_value, numbers.Integral):
				raise TypeError("InterField must be Int")
			elif max_value < 0:
				raise ValueError("max_value must be positive int")

		if max_value < min_value:
			raise ValueError("min_value must be smaller than max_value")

	def __get__(self, instance, owner):
		return self._value

	def __set__(self, instance, value):
		if not isinstance(value, numbers.Integral):
			raise ValueError("int value need")
		if value < self.min_value or value > self.max_value:
			raise ValueError("value must between min_value and max_value")
		self._value = value


class ModelMetaClass(type):
	def __new__(cls, class_name, bases, attrs, **kwargs):
		if class_name == "BaseModel":
			return super().__new__(cls, class_name, bases, attrs, **kwargs)
		fields = {}
		for key, value in attrs.items():
			if isinstance(value, Field):
				fields[key] = value
		attrs_meta = attrs.get("Meta", None)
		_meta = {}
		db_table = class_name.lower()
		if attrs_meta is not None:
			table_name = getattr(attrs_meta, "db_table")
			if table_name is not None:
				db_table = table_name

		_meta["db_table"] = db_table
		attrs["_meta"] = _meta
		attrs["fields"] = fields
		# del attrs["Meta"]
		return super().__new__(cls, class_name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
	def __init__(self, *args, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)
		# return super().__init__() ?

	def save(self):
		"""
		保存到数据库的逻辑
		:return: 
		"""
		pass


class User(BaseModel):
	name = CharField(column_name="name", max_length=30)
	age = InterField(column_name="age", min_value=0, max_value=100)

	class Meta:
		db_table = "user"


if __name__ == "__main__":
	user = User(name="frank", age=24)
	user.save()
