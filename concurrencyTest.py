import sys, os, socket

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddr = ('127.0.0.1', 6666)

client1.connect(serverAddr)
client2.connect(serverAddr)

try:
	httpGet = 'GET / HTTP/1.1\r\n'
	httpGet = httpGet.encode()

	client1.sendall(httpGet)
	client2.sendall(httpGet)
	client1.sendall(httpGet)
	client1.sendall(httpGet)
	client2.sendall(httpGet)

	webpage1 = client1.recv(1)
	webpage2 = client2.recv(1024)
	print('webpages recieved')
