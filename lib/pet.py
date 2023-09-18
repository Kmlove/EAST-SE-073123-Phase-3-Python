#!/usr/bin/env python3
# Class Attributes and Methods 

#✅ 6. Keep track of the total number of Pets created
#✅ 6a. Create a class attribute

#✅ 6b. Update class attribute whenever an instance is initialized
#Pet.total_pets += 1

#✅ 6c. Create a class method increase_pets that will increment total_pets

class Pet:
    total_pets = 0

    def __init__(self, name, age, breed, temperament, image_url):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        Pet.increase_pets()

    @classmethod
    def increase_pets(cls):
        cls.total_pets += 1

    def print_pet_details(self):
        print(f'''
            name: {self.name}
            age: {self.age}
            breed: {self.breed}
            temperament: {self.temperament}
            image_url: {self.image_url}
        ''')

