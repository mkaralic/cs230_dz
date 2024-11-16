class lampart_clock:
    def __init__(self):
        self.time = 0

    def get_time(self):
        return self.time

    def update_time(self, event_time):
        '''Update svog vremena na osnovu formule za Lamportov algoritam'''
        self.time = max(self.get_time(), event_time + 1)

    def send_message(self, destination, message):
        self.time += 1
        destination.receive_message(self, {"message": message, "time": self.time})

    def receive_message(self, sender, message):
        '''Radi update vremena na osnovu polja time iz poruke'''
        self.update_time(message["time"])
        print(f"Primljena poruka od {hash(sender)} - {message["message"]}")

