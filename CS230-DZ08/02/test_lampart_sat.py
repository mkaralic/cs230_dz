
from lampart_clock import lampart_clock

def test_lampart_clock():
    # Kreiramo dva procesa
    process1 = lampart_clock()
    process2 = lampart_clock()

    # Provera da li su inicijalno podeseni na 0
    assert process1.get_time() == 0, "Inicijalno vreme Procesa 1 treba biti 0"
    assert process2.get_time() == 0, "Inicijalno vreme Procesa 2 treba biti 0"

    # Process 1 salje poruku procesu 2
    process1.send_message(process2, "Hello from Process 1")
    assert process1.get_time() == 1, "Vreme Procesa 1 treba biti povecano na 1"
    assert process2.get_time() == 2, "Vreme Procesa 2 treba biti postavljeno na 2 (max(0, 1) + 1)"

    # Process 2 salje poruku procesu 1. Poruku salje u sledecem taktu
    process2.send_message(process1, "Hello from Process 2")
    assert process2.get_time() == 3, "Vreme Procesa 2 treba biti povecano na 3"
    assert process1.get_time() == 4, "Vreme Procesa 1 treba biti postavljeno na 4 (max(1, 3) + 1)"

    # Azuriranje vremena procesa na osnovu prosledjenog vremena, tako da prosledjeno vreme bude "happens before"
    process1.update_time(5)  
    process2.update_time(3)  
    assert process1.get_time() == 6, "Vreme Procesa 1 treba biti povecano na 6"
    assert process2.get_time() == 4, "Vreme Procesa 2 treba ostati na 4, jer je prosledjena manja vrednost"

    print("Svi testovi su prosli!")

# Running the test suite
if __name__ == "__main__":
    test_lampart_clock()
