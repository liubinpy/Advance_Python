""" 
@author: Frank
@file: socket_server.py 
@time: 18-4-21 上午9:54 
"""
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8001))
server.listen()


def data_handle(sock, addr):
	while True:
		data = sock.recv(1024)
		rev_data = data.decode("utf-8")
		if rev_data == "q":
			break
		print(rev_data)
		msg = input("=>")
		sock.send(msg.encode("utf-8"))
	sock.close()


while True:
	sock, addr = server.accept()
	t1 = threading.Thread(target=data_handle, args=(sock, addr))
	t1.start()

server.close()












