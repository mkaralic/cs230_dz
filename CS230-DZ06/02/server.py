'''
Serverska strana:
• Napisati program iterative_server.py koji treba da:
◦ Poveže se i osluškuje dolazne konekcije na specifičnom portu.
◦ Prihvata klijentsku konekciju.
◦ Primi poruku od klijenta.
◦ Konvertuje primljenu poruku u sva velika slova.
◦ Vrati modifikovanu poruku klijentu.
◦ Zatvori konekciju.
◦ Nastavlja sa slušanjem za nove konekcije.
• Napomena: za svaku stavku server šalje poruku o tome šta radi u konzoli.
'''

import socket

ADDR = "127.0.0.1"
PORT = 50008

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ADDR, PORT))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"Client connected on {address}")

        data = client.recv(1024)
        if data:
            dec_data = data.decode()
            print(f"Primljena poruka: {dec_data}")
            return_message = dec_data.upper()
            client.send(return_message.encode())
            print(f"Rezultat: {return_message}")

        client.close()
