import sys, os, socket, errno

serverAddr = ('127.0.0.1', 8000)
request = 'GET /index.html HTTP/1.1\r\n\r\n'

i=0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serverAddr)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect(serverAddr)

req = request[i]
req = req.encode()
sock.send(req)
'''
def main(maxClients, maxConns):
	i = 0
	socks = []
	for clientNum in range(maxClients):
		if i < 29:
			req = request[i]
			req = req.encode()
			i+=1
		pid = os.fork()
		if pid ==0:
			for connectionNum in range(maxConns):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect(serverAddr)
				sock.sendall(req)
				socks.append(sock)
				print(connectionNum)
				os._exit(0)

if __name__ == '__main__':
	main(5,2)
	print('We are concurrent')
'''
