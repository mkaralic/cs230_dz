"""Napisati program koji: a) sa klijentske strane prosleđuje proizvoljni SQL upit ka
tabeli MY_TABLE, i b) sa serverske strane vraća poruku da je upit prosleđen bazi
podataka (upit se zapravo čuva u queries.txt datoteci). Ukoliko klijent pošalje upit
DROP TABLE server vraća poruku o nevalidnom upitu."""

from socket import *

HOST = "localhost"
PORT = 50007


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))  # connect to server (block until accepted)
    print("Unesite SQL komandu (exit za kraj)")

    msg = input("> ")  # citaj komandu prvi put
    while msg and msg.lower() != "exit": # ako je komanda unesena i nije exit
        print('komanda', msg)
        s.send(msg.encode())  # posalji je
        data = s.recv(1024)  # primi odgovor od servera
        print(data.decode())  # stampaj odgovor
        msg = input("> ")  # ponovo cekaj unos

    s.close()  # zatvori konekciju

if __name__ == "__main__":
    main()
