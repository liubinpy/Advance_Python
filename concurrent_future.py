""" 
@author: Frank
@file: concurrent_future.py 
@time: 18-4-24 下午3:59 
"""
"""
线程池
使用concurrent下的future，可以是主线程虎丘某一个线程的状态或者某个任务的状态，以及返回值
当一个线程完成时候，主线程能够立即知道
future可以让多线程和多进程编码接口一致
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED


def get_html(times):
	time.sleep(times)
	print("get page {} success".format(times))
	return times

executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中，submit是立即返回而且是非阻塞的
# task1 = executor.submit(get_html, 3)
# task2 = executor.submit(get_html, 2)
#
# print(task1.done())
# print(task2.cancel())  # 如任务在执行中或者已经执行完成执行不能取消任务
# time.sleep(4)
# print(task1.done())
# print(task1.result())

# 获取已经成功的task的返回
urls = [3, 2, 4]
all_task = [executor.submit(get_html, url) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED)
print("main")
#

# for future in as_completed(all_task):
# 	print(future.result())

# 通过executor获取以及完成的task
# for data in executor.map(get_html, urls):
# 	print(data)


