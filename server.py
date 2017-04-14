import argparse, socket, select

if __name__ == "__main__":

    def process_http_header(request):
        print('\nProcessing HTTP request...')

        requestString = request
        print(requestString, '\n')

        header = requestString
        i = 0
        done = False
        num = 0

        while True:
            if(header[i] == 'G'):
                i+=1
                if len(header) <= i:
                    break
                if(header[i] == 'E'):
                    i+=1
                    if len(header) <= i:
                        break
                    if(header[i] == 'T'):
                        i+=1
                        if len(header) <= i:
                            break
                        if(header[i] == ' '):
                            i+=1
                            if len(header) <= i:
                                break
                            if(header[i] == '/'):
                                i+=1
                                if len(header) <= i:
                                    break
                                path ='/'
                                while(header[i] != ' '):
                                    path = path + header[i]
                                    i+=1
                                if(header[i] == ' '):
                                    i+=1
                                    if len(header) <= i:
                                        break
                                    if(header[i] == 'H'):
                                        i+=1
                                        if len(header) <= i:
                                            break
                                        if(header[i] == 'T'):
                                            i+=1
                                            if len(header) <= i:
                                                break
                                            if(header[i] == 'T'):
                                                i+=1
                                                if len(header) <= i:
                                                    break
                                                if(header[i] == 'P'):
                                                    i+=1
                                                    if len(header) <= i:
                                                        break
                                                    if(header[i] == '/'):
                                                        i+=1
                                                        if len(header) <= i:
                                                            break
                                                        if(header[i] == '1'):
                                                            i+=1
                                                            if len(header) <= i:
                                                                break
                                                            if(header[i] == '.'):
                                                                i+=1
                                                                if len(header) <= i:
                                                                    break
                                                                if(header[i] == '1'):
                                                                    i+=1
                                                                    if len(header) <= i:
                                                                        break
                                                                    if(header[i] == '\r'):
                                                                        i+=1
                                                                        if len(header) <= i:
                                                                            break
                                                                        if(header[i] == '\n'):
                                                                            i+=1
                                                                            if len(header) <= i:
                                                                                break
                                                                            while(header[i] != '\r'):
                                                                                i+=1
                                                                            if(header[i] == '\r'):
                                                                                i+=1
                                                                                if len(header) <= i:
                                                                                    break
                                                                                if(header[i] == '\n'):
                                                                                    num = 200
                                                                                    done = True
                                                                                    try:
                                                                                        # return index if path is /
                                                                                        if path == '/':
                                                                                            filePath = 'static/index.html'
                                                                                        else:
                                                                                            filePath = 'static' + path

                                                                                        fileHandler = open(filePath, 'rb')
                                                                                        htmlPage = fileHandler.read()
                                                                                        fileHandler.close()

                                                                                        break

                                                                                    except IOError:
                                                                                        done = True
                                                                                        num = 404
                                                                                        break
                                                                                else:
                                                                                    num = 400
                                                                                    break
                                                                            else:
                                                                                num = 400
                                                                                break
                                                                        else:
                                                                            num = 400
                                                                            break
                                                                    else:
                                                                        num = 400
                                                                        break
                                                                else:
                                                                    num = 400
                                                                    break
                                                            else:
                                                                num = 400
                                                                break
                                                        else:
                                                            num = 400
                                                            break
                                                    else:
                                                        num = 400
                                                        break
                                                else:
                                                    num = 400
                                                    break
                                            else:
                                                num = 400
                                                break
                                        else:
                                            num = 400
                                            break
                                    else:
                                        num = 400
                                        break
                                else:
                                    num = 400
                                    break
                            else:
                                num = 400
                                break
                        else:
                            num = 400
                            break
                    else:
                        num = 400
                        break
                else:
                    num = 400
                    break
            else:
                num = 400
                break

        if(num == 400 or num == 404):
            done = True
            response = getResponseHeader(num).encode()
            return response, done
        elif(num == 200):
            response = getResponseHeader(num).encode()
            response += htmlPage
            return response, done
        else:
            response = getResponseHeader(num)
            done = False
            return response, done


    def getResponseHeader(num):
        if(num == 200):
            header = 'HTTP/1.1 200 Ok\r\nContent-Type: text/html\r\n\r\n'
        elif(num == 404):
            header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        elif(num == 400):
            header = 'HTTP/1.1 400 Bad Request\r\n\r\n'
        else:
            header = ''

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

    clientDict = {}

    while True:
        # Get the list sockets which are ready to be read through select
        rlist, wlist, elist = select.select([sock], [], [])

        for socket in rlist:
            # Handle the case in which there is a new connection recieved through server_socket
            client, addr = sock.accept()
            print('\nAccepted client', addr)
            wlist.append(client)

        for client in wlist:
            request = client.recv(1024)
            request = request.decode()

            print('Sending to http handler')

            if client in clientDict:
                request = clientDict[client] + request
                returnRequest = process_http_header(request)
            else:
                returnRequest = process_http_header(request)

            print('Done?', returnRequest[1])

            if returnRequest[1] is True:
                client.sendall(returnRequest[0])
                print("Response sent. Closing connection")
                print(returnRequest[0])

                if client in clientDict:
                    del clientDict[client]

                wlist.remove(client)
                client.close()
            else:
                wlist.append(client)
                clientDict[client] = request

