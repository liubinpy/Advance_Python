""" 
@author: Frank
@file: thread_queue.py 
@time: 18-4-24 下午2:20 
"""
"""
线程通信的方式
"""
import time
import threading
from queue import Queue
# 使用queue
# 使用爬虫过程来模拟


def get_url(url_queue):
	for i in range(20):
		print("get url started")
		time.sleep(2)
		url = "http://www.baidu.com/{}".format(i)
		url_queue.put(url)
		print("get url end")


def get_html(url_queue):
	while True:
		print("get html started")
		url = url_queue.get()
		time.sleep(2)
		print("get html end")

if __name__ == "__main__":
	url_queue = Queue(maxsize=100)
	get_url_thread = threading.Thread(target=get_url, args=(url_queue,))
	get_html_thread = threading.Thread(target=get_html, args=(url_queue,))
	get_url_thread.start()
	get_html_thread.start()

	# url_queue.task_done()
	# url_queue.join()
