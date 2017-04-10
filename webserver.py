import argparse, socket, select, os, sys

if __name__ == "__main__":

    def process_http_header(request):
        print('Handling')
        request = request

        requestString = request.decode()
        print(requestString)

        returnString = ''
        returnString = 'HTTP/1.1 200 OK'
        response = returnString.encode()
        
        fileHandler = open('static/index.html', 'rb')
        htmlPage = fileHandler.read()
        fileHandler.close()

        response += htmlPage
        return response

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

