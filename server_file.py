import pickle
import socketserver
import logging

logger = logging.getLogger(__name__)

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()

        unpickled = pickle.loads(self.data)

        logger.info("{} wrote:".format(self.client_address[0]))
        logger.info(unpickled)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client

        unpickled['a'] += 1
        unpickled['b'] += 1

        self.wfile.write(pickle.dumps(unpickled, pickle.HIGHEST_PROTOCOL))

if __name__ == "__main__":
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')

    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
    
    logger.info('Finished')