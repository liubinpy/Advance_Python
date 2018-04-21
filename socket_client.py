""" 
@author: Frank
@file: socket_client.py 
@time: 18-4-21 上午9:54 
"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8001))

while True:
	msg = input("=>")
	client.send(msg.encode("utf-8"))
	if msg == "q":
		client.close()
	data = client.recv(1024)
	print(data.decode("utf-8"))

