import socket

def dns_client(server_address, server_port, domain_name):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Slanje upita serveru
        sock.sendto(domain_name.encode(), (server_address, server_port))

        # Primanje odgovora od servera
        response, _ = sock.recvfrom(1024)
        print(f"Odgovor sa servera: {response.decode()}")

if __name__ == "__main__":
    server_address = "127.0.0.1"
    server_port = 5000
    domain_name = input("Unesite ime domena za pretragu: ")

    dns_client(server_address, server_port, domain_name)
