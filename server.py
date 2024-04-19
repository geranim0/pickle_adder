import pickle
import socketserver

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.request.recv(1024)

        unpickled = pickle.loads(self.data)

        print("{} wrote:".format(self.client_address[0]))
        print(unpickled)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client

        unpickled['a'] += 1
        unpickled['b'] += 1

        self.request.sendall(pickle.dumps(unpickled, pickle.HIGHEST_PROTOCOL))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()