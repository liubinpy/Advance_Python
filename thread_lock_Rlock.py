""" 
@author: Frank
@file: thread_lock_Rlock.py 
@time: 18-4-24 下午2:56 
"""
# from threading import Lock
# total = 0
# lock = Lock()
#
#
# def add():
# 	global lock
# 	global total
# 	for i in range(100000):
# 		lock.acquire()
# 		total += 1
# 		lock.release()
#
#
# def desc():
# 	global lock
# 	global total
# 	for i in range(100000):
# 		lock.acquire()
# 		total -= 1
# 		lock.release()
#
# if __name__ == "__main__":
# 	import threading
# 	thread1 = threading.Thread(target=add)
# 	thread2 = threading.Thread(target=desc)
# 	thread1.start()
# 	thread2.start()
#
# 	thread1.join()
# 	thread2.join()
# 	print(total)

"""
用锁会影响性能
锁会引出死锁 比如：A需要锁a，b，B需要锁a，b，存在这样的时刻，当A获取了a，正准备获取b的时候，B已经获取了b，正准备回去a
这个时候就会出现卡死的情况，也就是所谓的死锁
A(a,b)
acquire(a)
acquire(b)

B(a,b)
acquire(b)
acquire(a)

出现死锁的第二种情况就是同一个线程内多次获取锁 比如
A(a)
acquire(a)
acquire(a)  这个时候就会出现死锁 那么解决这种方法就是使用递归锁，也就是Rlock

"""

from threading import RLock
total = 0
lock = RLock()


def add():
	global lock
	global total
	for i in range(100000):
		lock.acquire()
		lock.acquire()
		lock.acquire()
		total += 1
		lock.release()
		lock.release()
		lock.release()


def desc():
	global lock
	global total
	for i in range(100000):
		lock.acquire()
		total -= 1
		lock.release()

if __name__ == "__main__":
	import threading
	thread1 = threading.Thread(target=add)
	thread2 = threading.Thread(target=desc)
	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()
	print(total)
