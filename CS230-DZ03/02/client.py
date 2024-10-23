import socket

def start_client(host="localhost", port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    print(f"Klijent povezan na {host}:{port}")

    try:
        while True:
            message = input("Unesi poruku za slanje (ili 'exit' za izlaz): ")
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode())
    finally:
        client_socket.close()
        print("Veza zatvorena.")

if __name__ == "__main__":
    start_client()
