import socket
from datetime import datetime
from functools import wraps

# Funkcija koja služi kao interceptor za logovanje poruka sa vremenskom oznakom
def log_message(func):
    @wraps(func)
    def wrapper(message):
        # Dodaj vremensku oznaku poruci
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f"[{timestamp}] {message}"
        
        # Loguj poruku u terminal
        print(log)
        
        # Pozovi originalnu funkciju za dalje procesiranje
        func(log)
    return wrapper

# Funkcija za procesiranje poruka koje stignu na server
@log_message
def process_message(message):
    # Ova funkcija samo prikazuje logovanu poruku
    pass

def start_server(host="localhost", port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"Server pokrenut na {host}:{port}, čekam klijenta...")
    
    conn, addr = server_socket.accept()
    print(f"Klijent {addr} povezan.")

    try:
        while True:
            message = conn.recv(1024).decode()
            if not message:
                break
            # Procesuiraj poruku kroz interceptor
            process_message(message)
    finally:
        conn.close()
        print("Veza zatvorena.")

if __name__ == "__main__":
    start_server()
