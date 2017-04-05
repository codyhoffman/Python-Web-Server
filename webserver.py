import socket, codecs 

Host = '127.0.0.1'
Port = 8000

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((Host, Port))
listener.listen(5)
print('Serving HTTP on port %s ...' % Port)

while True:
	client, clientAddr = listener.accept();
	request = client.recv(1024)
	print(request)
        
        httpResponse = "This Works" 


	client.sendall(httpResponse)
	client.close()



def process_http_header(socket):
    print('Implement HTTP Header Processing')




