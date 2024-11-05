'''
Napisati middleware koji podržava persistant tip komunikacije: kada klijent pošalje
poruku, middleware smešta u svojoj privremenoj memoriji, i šalje serveru kada se
server aktivira (jer osluškuje port servera). U ovom programu pokrenuti middleware,
pa klijenta, pa server.
'''

import socket
import threading
import queue
import time

ADDR = "127.0.0.1"
PORT_SERVER = 50008
PORT_CLIENT = 50018

message_queue = queue.Queue(0)

def create_server_listener():
    socket, address = create_endpoint(PORT_SERVER)
    print(f"Accepted server connection from {address}")
    while True:
        data = message_queue.get()
        if data:
            print(f"{data.decode()} -> SERVER")
            socket.sendall(data)
        time.sleep(3)

def create_client_listener():
    socket, address = create_endpoint(PORT_CLIENT)
    print(f"Accepted client connection from {address}")
    while True:
        data = socket.recv(1024)
        if data:
            print(f"{data.decode()} -> MESSAGE QUEUE")
            message_queue.put(data)
        else:
            socket.close()
            break

def create_endpoint(port):
    endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endpoint.bind((ADDR, port))
    endpoint.listen(5)
    return endpoint.accept()


if __name__ == "__main__":
    server_thread = threading.Thread(target = create_server_listener, args = ())
    client_thread = threading.Thread(target = create_client_listener, args = ())

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()