from appointments import Appointment
# ✅ 5. Use procedure 
# ✅ 5a. Use chatGPT to create some procedures
# ✅ 5b. Update appointments.py to use procedures
class Procedure:
    def __init__(self, name, price):
        self.name = name 
        self.price = price

    # return all appointments associated with current procedure
    def appointments(self):
        return [appt for appt in Appointment.all_appts if appt.procedure == self]

    # get all associated pets through appointsments()    
    def pets(self):
        all_pets_for_procedure = [appt.pet.name for appt in self.appointments()]
        return list(set(all_pets_for_procedure))

    def __repr__(self):
        return f'''<Procedure {self.name} is ${self.price}>'''
    

