import sys, os, socket, errno, time

serverAddr = ('127.0.0.1', 8000)
request = 'GET /index.html HTTP/1.1\r\n\r\n'

i=0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serverAddr)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect(serverAddr)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock3.connect(serverAddr)
sock4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock4.connect(serverAddr)
sock5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock5.connect(serverAddr)
'''
print('client1 sent 1 byte')
req = 'G'
req = req.encode()
sock.send(req)

print('Done1: client2 sent 28 bytes')
req = request
req = req.encode()
sock2.send(req)

print('client3 sent 4 bytes')
req = 'GET '
req = req.encode()
sock3.send(req)



# sent 1 byte from client1 and the entire request from client2 then sleep 5 and send 
# 3 more bytes
print('sleeping 5 secs')
time.sleep(5)

print('Done2: client3 finishes rest of request, but its FNF')
req = '/ads.html HTTP/1.1\r\n\r\n'
req = req.encode()
sock3.send(req)

print('client1 sending 3 bytes')
req = 'ET /'
req = req.encode()
sock.send(req)

#sleep 5 secs then finish sending the rest of the request
print('sleeping 5 secs')
time.sleep(5)
print('Done3: client1 sending rest of request')
req = 'index.html HTTP/1.1\r\n\r\n'
req = req.encode()
sock.send(req)

time.sleep(2)
'''
print('quick send files ')

print('Done4')
req = 'GET /index.html HTTP/1.1\r\n\r\n'
req = req.encode()
sock.send(req)

print('Done5')
req = 'GET /car.html HTTP/1.1\r\nCar\r\n\r\n'
req = req.encode()
sock2.send(req)

print('Done6')
req = 'car.html HTTP/1.1\r\n\r\n'
req = req.encode()
sock3.send(req)

print('Done7')
req = 'GET /404.html HTTP/1.1\r\n\r\n'
req = req.encode()
sock4.send(req)

print('Done8')
req = 'GET / HTTP/1.1\r\n\r\n'
req = req.encode()
sock5.send(req)
