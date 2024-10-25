import socket
import threading
import queue

urls = ["https://www.google.com", "https://www.facebook.com", "https://www.nonexistentwebsite.com"]
url_queue = queue.Queue()

# Ubacivanje URL-ova u red
for url in urls:
    url_queue.put(url)

# Funkcija za rukovanje konekcijama od radnih čvorova
def handle_client(klijent_socket, adresa):
    while not url_queue.empty():
        try:
            url = url_queue.get()
            klijent_socket.send(url.encode())  # Slanje URL-a radnom čvoru
            status = klijent_socket.recv(1024).decode()  # Primanje statusa od radnog čvora
            print(f"URL: {url}, Status: {status}")
            url_queue.task_done()
        except Exception as e:
            print(f"Greska prilikom obrade URL-a od {adresa}: {e}")
            break
    klijent_socket.close()

# Pokretanje servera za distribuciju URL-ova
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(5)
    print("Server pokrenut i čeka radne čvorove...")

    while True:
        klijent_socket, client_address = server_socket.accept()
        print(f"Radni čvor povezan sa {client_address}")
        # Kreiranje niti za rukovanje radnim čvorom
        worker_thread = threading.Thread(target=handle_client, args=(klijent_socket, client_address))
        worker_thread.start()

start_server()