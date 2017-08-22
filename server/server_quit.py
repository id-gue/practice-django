# communicatate with a server on my computer
import socketserver


class EchoRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        print('connection received. client adress is {}'.format(client_address))
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)

    def handle(self):
        data = b''
        # in shell QUIT shuts down the server
        while data != b'QUIT\r\n':
            data = self.request.recv(2048)
            data = data[0:8]
            print('data is {}'.format(data))
            self.request.send(data)
        return

address = ('0.0.0.0', 3478)
server = socketserver.TCPServer(address, EchoRequestHandler)

server.serve_forever()
