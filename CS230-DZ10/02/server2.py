import socket
import os

# Putanja do data.txt za server2
SERVER2_FILE_PATH = "./S2/data.txt"

def get_last_modified_time(file_path):
    """Vraća poslednji datum modifikacije datoteke."""
    return os.path.getmtime(file_path)

def start_server2():
    """Pokreće server2 koji osluškuje konekcije."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 65432))  # Adresa i port servera 2
    server_socket.listen(1)
    print("Server 2 je pokrenut i osluškuje konekcije...")

    conn, addr = server_socket.accept()
    print(f"Server 2: Povezivanje od strane {addr}")

    with open(SERVER2_FILE_PATH, "r") as file:
        data_content = file.read()

    # Šaljemo sadržaj fajla i vreme poslednje modifikacije
    conn.sendall(f"{get_last_modified_time(SERVER2_FILE_PATH)}\n{data_content}".encode())
    print("Server 2: Podaci poslati.")
    conn.close()

if __name__ == "__main__":
    start_server2()
