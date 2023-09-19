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
        return f"<Appointment for {self.procedure.name} for {self.pet.name}>"

    #✅ 7. Create a function that prints details for the appointment 
    def print_appt_details(self):
        print (f'''
            {self.pet.print_pet_details()}
            has a {self.procedure.name} appointment with {self.staff}
            ''')
        
    #✅ 8. Create a class method for all unique clients of the clinic
    @classmethod
    def clients(cls):
        # unique list of all of the owners for all of the pets that have appointmtns
        return list(set([appt.pet.owner.name for appt in cls.all_appts]))