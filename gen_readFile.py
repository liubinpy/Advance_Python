""" 
@author: Frank
@file: gen_readFile.py 
@time: 18-4-21 上午9:08 
"""
# 可用于读取大文件


def read_file(f, delimiter):
	"""
	生成器读取文件
	:param f: 文件句柄
	:param delimiter: 分隔符 
	:return: 
	"""
	buff = ""
	while True:
		while delimiter in buff:
			position = buff.index(delimiter)
			yield buff[:position]
			buff = buff[position + len(delimiter):]
		chunk = f.read(4096)

		if not chunk:
			"""
			说明已经读到文件结尾
			"""
			yield buff
			break
		buff += chunk

with open("example.txt") as f:
	for line in read_file(f, "|"):
		print(line)
