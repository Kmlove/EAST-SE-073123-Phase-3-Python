from pet import Pet

class Owner:

    def __init__(self, name, phone, email):
        self.name = name 
        self.phone = phone 
        self.email = email 

    def owners_pets(self):
        return [pet for pet in Pet.all_pets if pet.owner == self]

    #✅ 3. create relationship: owner has many pets

    #✅ 9. create a function for the total bill of the owner
    #✅ 9a. create helper method for all appointments of owner (owner has many appointments through pets)