'''
• Napisati program client.py koji treba da:
◦ Poveže se sa serverom na određenoj IP adresi i portu.
◦ Traži od korisnika da unese poruku u konzoli.
◦ Pošalje poruku serveru.
◦ Primi modifikovanu poruku od servera.
◦ Prikaže modifikovanu poruku od servera.
• Napomena: za svaku stavku klijent šalje poruku o tome šta radi u konzoli.
'''

import socket

ADDR = "127.0.0.1"
PORT = 50008

if __name__ == "__main__":
    print("Type the message to be send to the server")

    while True:
        data = input("> ")
        if data.lower() == "exit":
            break
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ADDR, PORT))
        client.send(data.encode())
        ret_data = client.recv(1024)
        print(f"Response from server: {ret_data.decode()}")
        client.close()
