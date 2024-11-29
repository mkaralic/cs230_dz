import socket

FILE_PATH = "preostali_predmeti_server2.txt"

def save_received_data(data):
    with open(FILE_PATH, "w") as file:
        file.write(data)

def main():
    server_address = ("localhost", 5001)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(server_address)
        sock.listen(1)
        print("Server2 čeka prijem datoteke...")

        conn, addr = sock.accept()
        with conn:
            print(f"Povezan sa: {addr}")
            data = conn.recv(1024).decode()
            save_received_data(data)
            print("Datoteka primljena i sačuvana.")

if __name__ == "__main__":
    main()
