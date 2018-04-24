""" 
@author: Frank
@file: python_GIL.py 
@time: 18-4-24 下午1:54 
"""
"""
GIL global interpreter lock (cpython)
python中一个线程对应于C语言中的一个线程
GIL使得同一个时刻只有一个线程在一个CPU上执行字节码，无法将多个线程映射到多个CPU上执行
GIL会根据执行的字节码行数以及时间片释放GIL，GIL在遇到IO的操作时候主动释放

"""
# import dis
# def add (a):
# 	a = a + 1
# 	return a
#
# print(dis.dis(add))

total = 0


def add():
	global total
	for i in range(1000000):
		total += 1


def desc():
	global total
	for i in range(1000000):
		total -= 1

import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)

# 我们预想的结果应该是0，但是结果确实不确定的，这就是GIL带来的结果




































