""" 
@author: Frank
@file: python_thread.py 
@time: 18-4-24 下午2:04 
"""
import time
import threading
"""
thread开启多线程的两种方式
"""
# 通过Thread类实例化


# def get_detail_html():
# 	print("get detail html started")
# 	time.sleep(2)
# 	print("get detail html end")
#
#
# def get_detail_url():
# 	print("get detail url started")
# 	time.sleep(4)
# 	print("get detail url end")

# 继承threading.Thread
class GetDetailHtml(threading.Thread):
	def __init__(self):
		super().__init__(name="html")

	def run(self):
		print("get detail html started")
		time.sleep(2)
		print("get detail html end")


class GetDetailURL(threading.Thread):
	def __init__(self):
		super().__init__(name="url")

	def run(self):
		print("get detail url started")
		time.sleep(4)
		print("get detail url end")


if __name__ == "__main__":
	# 实例化Thread类
	# get_html_thread = threading.Thread(target=get_detail_html)
	# get_url_thread = threading.Thread(target=get_detail_url)
	# get_html_thread.start()
	# get_url_thread.start()
	# get_html_thread.join()
	# get_url_thread.join()
	#
	# print("ending")

	get_html_thread = GetDetailHtml()
	get_url_thread = GetDetailURL()
	get_html_thread.start()
	get_url_thread.start()
	get_html_thread.join()
	get_url_thread.join()

	print("ending")





































