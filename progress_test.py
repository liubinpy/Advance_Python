""" 
@author: Frank
@file: progress_test.py 
@time: 18-4-24 下午4:27 
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor

# 对于计算密集型，多进程优于多线程
# def fib(n):
# 	"""
# 	斐波那契
# 	:param n:
# 	:return:
# 	"""
# 	if n <= 2:
# 		return 1
# 	return fib(n-1) + fib(n-2)
#
# if __name__ == "__main__":
# 	with ProcessPoolExecutor(3) as executor:
# 		all_task = [executor.submit(fib, num) for num in range(25, 40)]
# 		start_time = time.time()
# 		for future in as_completed(all_task):
# 			print(future.result())
#
# 		print("last time is: {}".format(time.time() - start_time))

#  2. 对于io操作来说，多线程优于多进程


def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))

        print("last time is: {}".format(time.time()-start_time))