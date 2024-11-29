'''
Napraviti hijerarhisjku strukturu predmeta smera na kom studirate, tako da prati sledeću strukturu:
(ili iskoristiti strukturu iz prethodnog domaćeg zadatka)
SMER
   ├── GODINA #X
   │           ├── SEMESTAR #Y
   │           │              ├── SIFRA - Ime predmeta1
   │           │              ├── SIFRA - Ime predmeta2
   │           │              └── SIFRA - Ime predmeta3 ...
   
Najpre ovu strukturu izvesti kao tektualni podatak "preostali_predmeti.txt". Ovaj podatak repliciraju dva servera kako se ažurira 
broj položenih predmeta.

Zatim, napisati program (server1) koji će na osnovu unete šifre (tekst "exit" zatvara petlju) pamtiti sve predmete koje ste položili, 
i ažurirati spisak tako što će izbrisati taj unos u strukturi, i ažurirati datoteku.

Konačno, server1 će nakon ažuriranja poslati novu verziju datoteke drugom serveru. 

'''

import socket
import json

FILE_PATH = "preostali_predmeti.txt"
SERVER2_ADDRESS = ("localhost", 5001)

def load_courses():
    with open(FILE_PATH, "r", encoding="utf-8", errors="replace") as file:
        return json.load(file)

def save_courses(courses):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(courses, file, ensure_ascii=False, indent=4)

def remove_course(courses, course_code):
    for year, semesters in courses["INFORMACIONE TEHNOLOGIJE"].items():
        for semester, subjects in semesters.items():
            if course_code in subjects:
                del subjects[course_code]
                return courses, f"Predmet '{course_code}' uspešno obrisan."
    return courses, f"Šifra '{course_code}' nije pronađena."

def send_to_server2():
    with open(FILE_PATH, "r") as file:
        data = file.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(SERVER2_ADDRESS)
        sock.sendall(data.encode())
        print("Datoteka poslata Serveru2.")

def main():
    courses = load_courses()
    print("Server1 pokrenut. Unosite šifre položenih predmeta ('exit' za izlaz).")

    while True:
        course_code = input("Unesite šifru predmeta: ").strip()
        if course_code.lower() == "exit":
            break

        courses, message = remove_course(courses, course_code)
        print(message)
        save_courses(courses)

    send_to_server2()

if __name__ == "__main__":
    main()
