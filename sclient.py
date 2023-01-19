import socket
import sys

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((sys.argv[1], int(sys.argv[2])))
    sock.sendall(str.encode(sys.argv[3]))
