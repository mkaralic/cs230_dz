import socket
import requests

# Povezivanje radnog čvora sa serverom
def startuj_radni_cvor():
    klijent_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    klijent_socket.connect(("localhost", 12345))

    while True:
        try:
            # Primanje URL-a od servera
            url = klijent_socket.recv(1024).decode()
            if not url:
                break

            # Provera statusa URL-a
            try:
                odgovor = requests.get(url, timeout=5)
                if odgovor.status_code == 200:
                    status = "Aktivan"
                else:
                    status = "Neaktivan"
            except requests.RequestException:
                status = "Neaktivan"

            # Slanje statusa serveru
            klijent_socket.send(status.encode())
        except Exception as e:
            print(f"Greska prilikom provere URL-a: {e}")
            break

    klijent_socket.close()

# Pokretanje radnog čvora
startuj_radni_cvor()