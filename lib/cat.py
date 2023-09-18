#✅ 7. Create a subclass of Pet called Cat
#✅ 7a. Import Pet from lib.pet
from lib.pet import *

#✅ 7b. Create an __init__ method that has all parameters of Pet including an additional parameter: indoor
# self.name = name 
# self.age = age 
# self.breed = breed
# self.temperament = temperament
# self.image_url = image_url

#✅ 7c. Use super to pass Pet parameters to sub class

#✅ 7d. Update the instance in debug.py to rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)


#✅ 9. Create a method unique to the Cat subclass called talk which returns the string "Meowwwwwww"

#✅ 10. Create a method called print_pet_details, to match the print_pet_details in Pet    

#✅ 10a. Print the indoor attribute

class Cat(Pet):
    def __init__(self, name, age, breed, temperament, image_url, indoor):
        super().__init__(name, age, breed, temperament, image_url)
        self.indoor = indoor

    def say_meow(self):
        print("Meow")

    def print_pet_details(self):
        super().print_pet_details()
        print(f"indoor: {self.indoor}")