import sys, os, socket, errno

serverAddr = ('127.0.0.1', 8000)
request = 'GET /index.html HTTP/1.1\r\n\r\n'
request = request.encode()


def main(maxClients, maxConns):
	socks = []
	for clientNum in range(maxClients):
		pid = os.fork()
		if pid ==0:
			for connectionNum in range(maxConns):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect(serverAddr)
				sock.sendall(request)
				socks.append(sock)
				print(connectionNum)
				os._exit(0)

if __name__ == '__main__':
	main(5,2)
	print('We are concurrent')
