class Appointment:
    all_appts = []
    #✅ 4. create relationship: appointment belongs to a pet
    #✅ 4a. use chatGPT to create instances

    def __init__(self, staff, pet, procedure):
        self.staff = staff 
        self.pet = pet 
        self.procedure = procedure
        Appointment.all_appts.append(self)

    def __repr__(self):
        return f"<Appointment for {self.procedure} for {self.pet.name}>"

    #✅ 7. Create a function that prints details for the appointment 
        
    #✅ 8. Create a class method for all unique clients of the clinic