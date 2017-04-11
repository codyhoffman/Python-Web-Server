import argparse, socket, select

if __name__ == "__main__":

    def process_http_header(request):
        print('\nProcessing HTTP request...')
        request = request

        requestString = request.decode()
        print(requestString, '\n')

        header = requestString.split('\n')
        header = header[0].split()

        isSlash = header[1]
        isSlash = isSlash[:1]

        if(header[0] == 'GET'):
            if(isSlash == '/'):
                if(header[2] == 'HTTP/1.1'):
                    # if file path is empty set to index else add static directory to filepath
                    if(header[1] != '/'):
                        filePath = ''.join(('static', '%s' % header[1]))
                        #print(filePath)
                    else:
                        filePath = 'static/index.html'
                    
                    try: 
                        fileHandler = open(filePath, 'rb')
                        htmlPage = fileHandler.read()
                        fileHandler.close()
                        num = 200
                    except IOError:
                        num = 404
                else:
                    num = 400
            else:
                num = 400
        else:
            num = 400

        response = getResponseHeader(num).encode()

        if(num == 400 or num == 404):
            return response
        else:
            response += htmlPage
            return response

    def getResponseHeader(num):
        if(num == 200):
            header = 'HTTP/1.1 200 Ok\r\n Content-Type: text/html\r\n\r\n'
        elif(num == 404):
            header = 'HTTP/1.1 404 Not Found\r\n'
        else:
            header = 'HTTP/1.1 400 Bad Request\r\n'

        return header

    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port")
    args = parser.parse_args()
    print("Server started on ", "host: ", args.host, "port: ", args.port)

    host = args.host
    port = int(args.port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)

    while True:
        # Get the list sockets which are ready to be read through select
        rlist, wlist, elist = select.select([sock], [], [])

        for socket in rlist:
            # Handle the case in which there is a new connection recieved through server_socket
            client, addr = sock.accept()
            wlist.append(client)
            print('accepted client', addr)

        for client in wlist:
            request = client.recv(1024)
            print('sending to http handler')
            returnRequest = process_http_header(request)

            client.send(returnRequest)
            print("response sent. Closing connection")
            print(returnRequest)
            client.close()
