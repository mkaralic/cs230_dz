'''Napisati program koji: a) sa klijentske strane prosleđuje proizvoljni SQL upit ka
tabeli MY_TABLE, i b) sa serverske strane vraća poruku da je upit prosleđen bazi
podataka (upit se zapravo čuva u queries.txt datoteci). Ukoliko klijent pošalje upit
DROP TABLE server vraća poruku o nevalidnom upitu.'''

import socket
host = "localhost"
port = 50007

def main():
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.bind((host, port))

    sck.listen(5)
    print("Server listening on {}:{}".format(host, port))
    client_socket, addr = sck.accept()
    print('Got connection from', addr)
    # primanje komandi sa klijenta
    new_file_name = "queries.txt"

    data = client_socket.recv(1024)
    
    while True:
        if not data:
            break

        error_msg = ""
        cmd = data.decode()
        cmd_upper = cmd.upper()
        if not ("MY_TABLE" in cmd_upper):
            error_msg += 'Upit mora sadrzati tabelu MY_TABLE\n'
        if cmd_upper.startswith('DROP TABLE'):
            error_msg += 'DROP TABLE nije dozvoljena komanda\n'

        if error_msg:
            client_socket.send(error_msg.encode())
        else:
            with open(new_file_name, 'a') as new_file:
                new_file.write(f'{cmd}\n')
            client_socket.send(f'primljena komanda: {cmd}'.encode())

        data = client_socket.recv(1024)
    
    client_socket.close()

if __name__ == '__main__':
    main()