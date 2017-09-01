# communicatate with a server on my computer
import socketserver


class EchoRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        print('connection received. client adress is {}'.format(client_address))
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)

    def handle(self):
        # receive a data package not bigger than 2048 bytes
        data = self.request.recv(2048)
        # just show the first four letters
        data = data[0:4]
        # tell my, if someone is talking to my server
        print('data is {}'.format(data))
        # send the received data back
        self.request.send(data)
        return

# address = (ip address, port)
address = ('0.0.0.0', 3478)
# create TCP server
server = socketserver.TCPServer(address, EchoRequestHandler)

# activate server
server.serve_forever()


"""
in shell window 1:
$ pyenv activate server-3.6.1
$ python server.py

in shell window 2 (talk with myself):
$ telnet localhost 3478
$ random text that gets echoed
or (talk with another ip adress)
$ telnet 10.10.14.247 5102
$ random text that gets echoed
"""
