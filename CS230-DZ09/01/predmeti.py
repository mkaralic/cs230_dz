'''
Napraviti hijerarhisjku strukturu predmeta smera na kom studirate, tako da prati sledeću strukturu:
SMER
   ├── GODINA #X
   │           ├── SEMESTAR #Y
   │           │              ├── SIFRA - Ime predmeta1
   │           │              ├── SIFRA - Ime predmeta2
   │           │              └── SIFRA - Ime predmeta3 ...
   
Napisati program koji na osnovu unete šifre predmeta vraća punu putanju predmeta. Npr: 
Input: 
CS230
Output:
SOFTVERSKO INŽENJERSTVO > Godina #2 > Semestar #4 > CS230 - Distribuirani sistemi.
'''

courses = {
    "INFORMACIONE TEHNOLOGIJE": {
        "GODINA 1": {
            "SEMESTAR 1": {
                "IT101": "Osnove informacionih tehnologija",
                "CS101": "Uvod u programiranje (Python)",
                "NT110": "Poslovna komunikacija",
                "MA104": "Matematika",
                "NT111": "Enagleski 1",
            },
            "SEMESTAR 2": {
                "CS101": "Objektno-orijentisano programiranje 1",
                "CS120": "Organizacija računara",
                "CS105": "Osnove veb tehnologija",
                "IT131": "Računarske mreže",
                "NT112": "Engleski 2",
            },
        },
        "GODINA 2": {
            "SEMESTAR 3": {
                "CS202": "Objektno-orijentisano programiranje 2",
                "IT250": "Baze podataka",
                "CS215": "Diskretne strukture",
                "SE201": "Uvod u softversko inženjerstvo",
                "NT213": "Engleski za informatičare",
            },
            "SEMESTAR 4": {
                "CS203": "Algoritmi i strukture podataka",
                "CS230": "Distribuirani sistemi",
                "CS130": "C/C++ programski jezik",
                "MA273": "Osnove verovatnoće i statistike",
                "NT475": "Pravo na internetu",
            },
        },
        "GODINA 3": {
            "SEMESTAR 5": {
                "IT354": "Veb sistemi 1",
                "CS320": "Operativni sistemi",
                "IT380": "Inženjerstvo i integracija sistema",
                "CS360": "Veštačka inteligencija",
                "A1": "Izborni predmet A1",
            },
            "SEMESTAR 6": {
                "IT355": "Veb sistemi 2",
                "IT382": "Zaštita računarskih sistema",
                "IT335": "Administracija računarskih sistema i mreža",
                "CS310": "Skripting jezici u veb razvoju",
                "C1": "Izborni predmet C1",
            },
        },
        "GODINA 4": {
            "SEMESTAR 7": {
                "SE425": "Upravljanje projektima razvoja softvera",
                "MG470": "Inovacije i preduzetništvo u digitalnom biznisu",
                "C2": "Izborni predmet C2",
                "C3": "Izborni predmet C3",
            },
            "SEMESTAR 8": {
                "C4": "Izborni predmet C4",
                "C5": "Izborni predmet C5",
                "CS450": "Klaud računarstvo",
                "IT491": "Stručna praksa",
                "IT495": "Završni rad - istraživački rad",
                "IT496": "Završni rad - izrada i odbrana",
            },
        },

    }
}


def find_course(path, course_id):
    for key, value in path.items():
        if key == course_id:
            return f"{course_id} - {value}"
        elif isinstance(value, dict):
            result = find_course(value, course_id)
            if result is not None:
                return f"{key} > {result}"
    return None


def handle_request(course_id):
    course_location = find_course(courses, course_id)
    if course_location:
        return course_location
    else:
        return f"Predmet '{course_id}' nije nađen"


while True:
    client_request = input("Unesite šifru predmeta za traženje (ili 'exit' za izlaz): ")
    if client_request == "exit":
        break

    response = handle_request(client_request)
    print("Puna putanja predmeta:", response)
