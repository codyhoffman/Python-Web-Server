import argparse, socket, select, os, sys

if __name__ == "__main__":

    def process_http_header(request):
        print('\nProcessing HTTP request...')
        request = request

        requestString = request.decode()
        print('\n', requestString, '\n')

        header = requestString.split('\n')
        header = header[0].split()
        
        if(header[0] == 'GET'):
            if(header[1].split()[0] == '/'):
                if(header[2] == 'HTTP/1.1'):
                    # if file path is empty set to index else add static directory to filepath
                    if(header[1] == '/'):
                        filePath = 'static/index.html'
                    else:
                        filePath = ''.join(('static','%s' % header[1])) 
                    
                    try: 
                        fileHandler = open(filePath, 'rb')
                        htmlPage = fileHandler.read()
                        fileHandler.close()
                        num = 200
                    except:
                        print('IOError')
                        num = 404
                        htmlPage = "404 File Not Found"
                        htmlPage = htmlPage.encode()
                else:
                    num = 400
            else:
                num = 400
        else:
            num = 400

                        
        response = getResponseHeader(num).encode()
        if(num == 400):
            htmlPage = "400 Bad Request"
            htmlPage = htmlPage.encode()
            
        response += htmlPage
        
        return response

    def getResponseHeader(num):
        if(num == 200):
            r = 'HTTP/1.1 200 OK'
        if(num == 404):
            r = 'HTTP/1.1 404 NOT FOUND'
        else:
            r = 'HTTP/1.1 400 BAD REQUEST'
        return r

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
        print('executing for loop')
        if sock in rlist:
            # Handle the case in which there is a new connection recieved through server_socket
            client, addr = sock.accept()
            print('accepted client', addr)

            # handle a situation where the connection stops half way through, a different client requests, then resume the previous
            request = client.recv(1024)

            print('sending to http handler')
            returnRequest = process_http_header(request)

            #check out that file you book marked

            print("sending response...")
            client.send(returnRequest)
            print("response sent. Closing connection")
            client.close()
        else:
            while rlist.len == 0:
                print("waiting for next connection")

