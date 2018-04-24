""" 
@author: Frank
@file: progress_queue.py 
@time: 18-4-24 下午4:51 
"""
import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe

# from queue import Queue # queue里面的Queue不能用于多进程编程


# def producer(queue):
# 	queue.put("a")
# 	time.sleep(2)
#
#
# def consumer(queue):
# 	time.sleep(2)
# 	print(queue.get())
#
#
# if __name__ == "__main__":
# 	queue = Queue(10)
# 	my_producer = Process(target=producer, args=(queue,))
# 	my_consumer = Process(target=consumer, args=(queue,))
# 	my_producer.start()
# 	my_consumer.start()
# 	my_producer.join()
# 	my_consumer.join()

# nultiprocessing里面的Queue不能用于进场池, 所以要使用Manager中的Queue

# def producer(queue):
# 	queue.put("a")
# 	time.sleep(2)
#
#
# def consumer(queue):
# 	time.sleep(2)
# 	print(queue.get())
#
#
# if __name__ == "__main__":
# 	queue = Manager().Queue(10)
# 	pool = Pool(2)
# 	pool.apply_async(producer, args=(queue,))
# 	pool.apply_async(consumer, args=(queue,))
# 	pool.close()
# 	pool.join()
#
# 通过Pipe实现进程间的通信
# Pipe适用于两个指定的的进程
#
# def producer(send_pipe):
# 	send_pipe.send("frank")
#
#
# def consumer(recevie_pipe):
# 	print(recevie_pipe.recv())
#
#
# if __name__ == "__main__":
# 	recevie_pipe, send_pipe = Pipe()
# 	my_producer = Process(target=producer, args=(send_pipe,))
# 	my_consumer = Process(target=consumer, args=(recevie_pipe,))
# 	my_producer.start()
# 	my_consumer.start()
# 	my_producer.join()
# 	my_consumer.join()

# 进程间的共享内存
def add_data(pd, k, v):
	pd[k] = v

if __name__ == "__main__":
	progress_dict = Manager().dict()
	p1 = Process(target=add_data, args=(progress_dict, "a", 1))
	p2 = Process(target=add_data, args=(progress_dict, "b", 2))
	p3 = Process(target=add_data, args=(progress_dict, "c", 3))
	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()
	print(progress_dict)