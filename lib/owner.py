from pet import Pet

class Owner:

    def __init__(self, name, phone, email):
        self.name = name 
        self.phone = phone 
        self.email = email
    def __repr__(self):
        return f"<Owner {self.name}>" 

    #✅ 3. create relationship: owner has many pets
    def pets(self):
        return [pet for pet in Pet.all_pets if pet.owner == self]

    #✅ 9. create a function for the total bill of the owner
    #✅ 9a. create helper method for all appointments of owner (owner has many appointments through pets) 
    def appointments(self):
        all_appts = []
        for pet in self.pets():
            for appt in pet.appointments():
                all_appts.append(appt)
        return all_appts
        
    def bills(self):
    # what pet/pets the owner has
    # all the appointments for each pet
    # cost of each appointment
    # total the appointment costs

        # Without helper function
        # proc_prices = []
        # for pet in self.pets():
        #     for appt in pet.appointments():
        #         proc_prices.append(appt.procedure.price)

        # With helper function
        proc_prices = [appt.procedure.price for appt in self.appointments()]
        
        return f"{self.name} owes ${sum(proc_prices)}"