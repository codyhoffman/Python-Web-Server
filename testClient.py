import sys, os, socket, errno, time

serverAddr = ('127.0.0.1', 8000)
request = 'GET /index.html HTTP/1.1\r\n\r\n'

i=0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serverAddr)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect(serverAddr)

print('client1 sent 1 byte')
req = 'G'
req = req.encode()
sock.send(req)

print('client2 sent 28 bytes')
req = request
req = req.encode()
sock2.send(req)

# sent 1 byte from client1 and the entire request from client2 then sleep 5 and send 
# 3 more bytes
print('sleeping 5 secs')
time.sleep(5)
print('client1 sending 3 bytes')
req = 'ET /'
req = req.encode()
sock.send(req)

#sleep 5 secs then finish sending the rest of the request
print('sleeping 5 secs')
time.sleep(5)
print('client1 sending rest of request')
req = '/index.html HTTP/1.1\r\n\r\n'
req = req.encode()
sock.send(req)





print('done sending both requests')







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
