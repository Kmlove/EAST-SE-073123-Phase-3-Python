#!/usr/bin/env python3
from appointments import Appointment

class Pet:
    all_pets = []
    #✅ 1. create relationship: pet belongs to an owner
    #✅ 2. use chatGPT to create owners and pets in debug.py
    #✅ 2a. create __repr__ function to more easily read output
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner
        Pet.all_pets.append(self) 

    def __repr__(self):
        return f"<Pet {self.name} the {self.breed} belongs to {self.owner.name}>"
    
     #✅ 5. create relationship: pet has many appointments
    def appointments(self):
        return [appointment for appointment in Appointment.all_appts if appointment.pet == self]

    #✅ 6. create relationship: pet has many procedures (but make it unique)
    def procedures(self):
        all_procedures = [appointment.procedure for appointment in self.appointments()]
        return list(set(all_procedures))
    
    def print_pet_details(self):
        print( f'''
            name: {self.name}
            age: {self.age}
            breed: {self.breed}
            ''')
        
    #✅ 10. add all bills for current pet
    # All the appointments -> procedures for this pet
    def bills(self):
        all_procedures = [appt.procedure.price for appt in self.appointments()]
        return f"{self.owner.name} owes ${sum(all_procedures)} for {self.name}"