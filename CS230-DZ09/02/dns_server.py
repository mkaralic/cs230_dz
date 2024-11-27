import socket
import sys

# Funkcije za učitavanje i čuvanje DNS baze
def load_dns_db(filename):
    dns_db = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                domain, ip = line.strip().split(':')
                dns_db[domain] = ip
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty database.")
    return dns_db

# Funkcija za pokretanje DNS servera
def dns_server(server_address_port, dns_file, external_servers=None):
    server_address, server_port = server_address_port.split(':')
    server_port = int(server_port)

    dns_db = load_dns_db(dns_file)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((server_address, server_port))
        print(f"DNS server pokrenut na {server_address}:{server_port}")

        while True:
            # Primanje upita od klijenta
            query, client_address = sock.recvfrom(1024)
            domain_name = query.decode()
            print(f"Primljen upit za domen: {domain_name}")

            # Provera lokalne baze
            if domain_name in dns_db:
                response = dns_db[domain_name]
                print(f"Domen pronađen u bazi: {domain_name} -> {response}")
            else:
                print(f"Domen nije pronađen u lokalnoj bazi.")

                # Ako postoje eksterni serveri, kontaktiraj ih
                response = None
                if external_servers:
                    for ext_server in external_servers:
                        ext_address, ext_port = ext_server.split(':')
                        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ext_sock:
                            ext_sock.sendto(domain_name.encode(), (ext_address, int(ext_port)))
                            try:
                                ext_sock.settimeout(2)  # Postavljanje vremenskog ograničenja za odgovor
                                ext_response, _ = ext_sock.recvfrom(1024)
                                response = ext_response.decode()
                                print(f"Dobijen odgovor od eksternog servera {ext_server}: {response}")

                                # Ako je pronađen odgovor, prekini petlju
                                if response != "Domen nije pronađen.":
                                    break
                            except socket.timeout:
                                print(f"Sekundarni server {ext_server} nije odgovorio.")

                # Ako nijedan eksterni server nije pronašao domen
                if not response:
                    response = "Domen nije pronađen."

            # Slanje odgovora klijentu
            sock.sendto(response.encode(), client_address)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python dns_server.py <address:port> <dns_file> [<external_server1> <external_server2> ...]")
        sys.exit(1)

    server_address_port = sys.argv[1]
    dns_file = sys.argv[2]
    external_servers = sys.argv[3:] if len(sys.argv) > 3 else None

    dns_server(server_address_port, dns_file, external_servers)
