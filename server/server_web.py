# communicatate with a server in the web
import socketserver


class EchoRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):

        whole_request = b''
        # check if last four letters are rnrn (= new line)
        # (then the request is complete)
        while whole_request[-4:] != b'\r\n\r\n':
            data = self.request.recv(2048)
            whole_request = whole_request + data

        # print the http header in the shell
        print(whole_request)
        # send content status code and "hello world" to the client
        self.request.send(b'HTTP/1.1 200 OK\r\nContent-length: 29\r\nContent-type: text/html\r\n\r\n <strong>Hello</strong> World')
        # for json:
        # self.request.send(b'HTTP/1.1 200 OK\r\nContent-length: 16\r\nContent-type: text/json\r\n\r\n{ "foo": "bar" }')
        return

address = ('0.0.0.0', 3678)
server = socketserver.TCPServer(address, EchoRequestHandler)

server.serve_forever()

"""
in browser:
http://localhost:3678/
"""
