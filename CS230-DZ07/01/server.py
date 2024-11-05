import socket
import time

ADDR = "127.0.0.1"
PORT_SERVER = 50008

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ADDR, PORT_SERVER))
while True:
    data = server.recv(1024)
    if data:
        print(f"MIDDLEWARE -> {data.decode()}")
    else:
        server.close()
