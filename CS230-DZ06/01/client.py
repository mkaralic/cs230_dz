import socket
import threading
import time

ADDRESS = "127.0.0.1"
PORT = 12345
OOB_PORT = 50008

def send_data(port, stop_event):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ADDRESS, port))
    
    while not stop_event.is_set():
        client.send(b'Hello from client')
        time.sleep(1)

    client.close()

def send_oob_data(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ADDRESS, port))
    
    while True:
        data = input("Enter OOB message: ")
        if data == "c":
            stop_event.set()
        elif data.lower() == "exit":
            break
        else:
            client.send(data.encode())

    client.close()

if __name__ == "__main__":
    stop_event = threading.Event()

    main_thread = threading.Thread(target=send_data, args=(PORT, stop_event))
    oob_thread = threading.Thread(target=send_oob_data, args=(OOB_PORT,))

    main_thread.start()
    oob_thread.start()

    main_thread.join()
    oob_thread.join()