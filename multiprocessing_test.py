""" 
@author: Frank
@file: multiprocessing_test.py 
@time: 18-4-24 下午4:38 
"""
import multiprocessing
import time


def get_html(n):
	time.sleep(n)
	print("sub_process success")
	return n


if __name__ == "__main__":
	# progress = multiprocessing.Process(target=get_html, args=(3,))
	# progress.start()
	# progress.join()
	# print("main")

	# 使用线程池
	pool = multiprocessing.Pool(multiprocessing.cpu_count())
	# result = pool.apply_async(get_html, args=(3,))
	# result1 = pool.apply_async(get_html, args=(3,))
	# # result = pool.apply_async(get_html, args=(3,))
	# pool.close()
	# pool.join()
	# print(result.get())

	# imap
	# for result in pool.imap(get_html, [1,5,3]):
	# 	print(result)

	# for result in pool.imap_unordered(get_html, [1,5,3]):
	# 	print(result)
