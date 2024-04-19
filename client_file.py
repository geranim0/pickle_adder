import pickle
import socket
import sys

data = {
    'a': 1,
    'b': 2
}

HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(pickle.dumps(data, pickle.HIGHEST_PROTOCOL) + bytes("\n", "utf-8"))

    # Receive data from the server and shut down
    received = sock.recv(1024)
    unpickled = pickle.loads(received)

print("Sent:     {}".format(data))
print("Received: {}".format(unpickled))