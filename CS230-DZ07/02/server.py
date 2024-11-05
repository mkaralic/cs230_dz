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

operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x / y if y != 0 else 'Error: Division by zero'
}

def calculate(operation, x, y):
    if operation in operations:
        return operations[operation](x, y)
    else:
        return "Error: Invalid operation"

endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
endpoint.bind((ADDR, PORT))
endpoint.listen(5)
endpoint, address = endpoint.accept()
print(f"Client connected on {address}")

while True:
    try:
        data = endpoint.recv(1024)
        if data:
            rpc_body = json.loads(data.decode())
            print(f"Received command body {rpc_body}")
            result = str(calculate(rpc_body["operation"], rpc_body["x"], rpc_body["y"]) )
            endpoint.sendall(result.encode())
            print(f"Returned result {result}")
    except:
        if endpoint:
            endpoint.close()
            print("Veza sa klijentom je prekinuta")
            break
