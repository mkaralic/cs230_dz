import socket
import time

ADDR = "127.0.0.1"
PORT_CLIENT = 50018

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ADDR, PORT_CLIENT))
server.sendall(b"First message")
time.sleep(1)
server.sendall(b"Second message")
server.close()
