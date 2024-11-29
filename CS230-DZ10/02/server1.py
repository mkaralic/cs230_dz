'''
Napisati program koji radi replikaciju podataka sa servera na server na osnovu datuma modifikacije.
Napraviti dva servera, svaki server ima svoj folder, S1 i S2, za server1 i server2, respektivno.
U svakom od foldera nalazi se datoteka "data.txt" sa nekim tekstom.

Najpre se pokreće server 2, koji osluškuje konekcije.

Server 1 se zatim pokreće i proverava da li je svoj data.txt noviji ili stariji od podataka servera 2.
Ukoliko nije, javlja poruku da nije potrebna replikacija.
Ukoliko jeste, javlja poruku da je potrebna replikacija i radi replikaciju u svoju datoteku.

Ispitati program ukoliko su podaci u folderu servera 1 najpra noviji, pa zatim stariji.
'''

import socket
import os

# Putanja do data.txt za server1
SERVER1_FILE_PATH = "./S1/data.txt"

def get_last_modified_time(file_path):
    """Vraća poslednji datum modifikacije datoteke."""
    return os.path.getmtime(file_path)

def replicate_data(new_content):
    """Ažurira data.txt u folderu server1."""
    with open(SERVER1_FILE_PATH, "w") as file:
        file.write(new_content)
    print("Server 1: Data.txt je ažuriran sa novim sadržajem.")

def start_server1():
    """Pokreće server1 koji proverava i ažurira podatke ako je potrebno."""
    # Povezivanje na server2
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 65432))

    # Primanje podataka od server2
    response = client_socket.recv(1024).decode()
    client_socket.close()

    server2_mtime, server2_content = response.split("\n", 1)
    server2_mtime = float(server2_mtime)
    
    # Provera vremena modifikacije
    server1_mtime = get_last_modified_time(SERVER1_FILE_PATH)
    print(f"Server 1: Vreme modifikacije - Lokalno: {server1_mtime}, Server 2: {server2_mtime}")

    if server1_mtime < server2_mtime:
        print("Server 1: Potrebna replikacija.")
        replicate_data(server2_content)
    else:
        print("Server 1: Replikacija nije potrebna.")

if __name__ == "__main__":
    start_server1()
