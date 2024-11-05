'''
Napisati program koji podržava pet RPC operacija (sabiranje dva cela broja, oduzimanje dva
cela broja, množenje dva realna broja, deljenje dva realna broja, konkatenacija stringova).
Na klijentskoj strani na konzoli napraviti meni gde korisnik ubacuje redni broj operacije, a
zatim i operande.
Nakon toga, klijent šalje RPC poziv ka serveru, koji prepoznaje tip operacije i operande,
lokalno ih računa i vraća rezultat klijentu.
Na klijentu se prikazuje rezultat u konzoli.
'''

import socket
import json

ADDR = "127.0.0.1"
PORT = 50008

menu_options = [ 
    ['1. Add Integers', 'add'],
    ['2. Subtract Integers', 'sub'],
    ['3. Multiply Floats', 'mul'],
    ['4. Divide Floats', 'div'],
]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ADDR, PORT))

while True:
    print('\nRPC Client Menu:')
    for opt in menu_options:
        print(opt[0])
    option = input("> ")
    if option == 0:
        server.close()
        break
    elif option in ("1","2"):
        x = int(input("x = "))
        y = int(input("y = "))
    elif option in ("3","4"):
        x = float(input("x = "))
        y = float(input("y = "))
    else:
        continue

    rpc_body = { "operation": menu_options[int(option) - 1][1], "x": x, "y": y }
    server.sendall(json.dumps(rpc_body).encode())
    result = server.recv(1024)
    print(f"Rezultat: {result.decode()}")