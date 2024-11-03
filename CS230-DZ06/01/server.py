'''
Napisati serverski program koji ima dva thread-a: jedan osluškuje na jednom portu,
drugi osluškuje na drugom portu. Zatim, napraviti klijentski program koji jednim
thread-om šalje podatke ka prvom portu servera, a drugim thread-om šalje OOB
podatke ka drugom portu, kroz konzolu. Ako korisnik klikne u konzoli "c", prekinuće
se proces slanja podataka na prvom portu.
'''

import socket
import threading

ADDRESS = "127.0.0.1"
PORT = 12345
OOB_PORT = 50008

def handle_client(client_socket, address):
    print(f"Connection accepted for {address}")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Message received from client {address}: {data.decode()}")
        except Exception as ex:
            print(f"Exception handling client {address}: {ex}")
    
    client_socket.close()
    print(f"Connection from client {address} closed.")

def create_server_thread(port):
    srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_socket.bind((ADDRESS, port))
    srv_socket.listen(5)
    print(f"Listening on port {port}")

    while True:
        client, address = srv_socket.accept()
        handle_client(client, address)

if __name__ == "__main__":
    main_thread = threading.Thread(target=create_server_thread, args=(PORT,))
    oob_thread = threading.Thread(target=create_server_thread, args=(OOB_PORT,))

    main_thread.start()
    oob_thread.start()

    main_thread.join()
    oob_thread.join()