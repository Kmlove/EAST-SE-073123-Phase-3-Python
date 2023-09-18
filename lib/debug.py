#!/usr/bin/env python3
#✅ import owner, pet, and appointments
from owner import Owner
from pet import Pet 
from appointments import Appointment
from procedure import Procedure

import ipdb;

owner1 = Owner("John Doe", "555-1234", "john@example.com")
owner2 = Owner("Alice Smith", "555-5678", "alice@example.com")
owner3 = Owner("Bob Johnson", "555-9876", "bob@example.com")
owner4 = Owner("Eve Brown", "555-4321", "eve@example.com")
owner5 = Owner("Charlie Davis", "555-8765", "charlie@example.com")

pet1 = Pet("Buddy", 2, "Golden Retriever", owner1)
pet2 = Pet("Luna", 3, "Siamese", owner2)
pet3 = Pet("Max", 1, "German Shepherd", owner3)
pet4 = Pet("Milo", 5, "Bengal", owner3)
pet5 = Pet("Bailey", 4, "Labrador", owner5)
pet6 = Pet("Rocky", 2, "Poodle", owner5)
pet7 = Pet("Oscar", 6, "Maine Coon", owner2)
pet8 = Pet("Charlie", 3, "Bulldog", owner3)
pet9 = Pet("Lucy", 4, "Ragdoll", owner4)
pet10 = Pet("Sadie", 2, "Beagle", owner5)

appointment1 = Appointment("Dr. Smith", pet1, "Checkup")
appointment2 = Appointment("Dr. Johnson", pet3, "Vaccination")
appointment3 = Appointment("Dr. Davis", pet3, "Dental Cleaning")
appointment4 = Appointment("Dr. Wilson", pet4, "Surgery")
appointment5 = Appointment("Dr. Anderson", pet5, "Grooming")
appointment6 = Appointment("Dr. Brown", pet6, "Checkup")
appointment7 = Appointment("Dr. Clark", pet5, "Vaccination")
appointment8 = Appointment("Dr. Evans", pet8, "Dental Cleaning")
appointment9 = Appointment("Dr. Garcia", pet9, "Surgery")
appointment10 = Appointment("Dr. Hall", pet10, "Grooming")
appointment11 = Appointment("Dr. Smith", pet10, "Checkup")
appointment12 = Appointment("Dr. Johnson", pet9, "Vaccination")
appointment13 = Appointment("Dr. Davis", pet8, "Dental Cleaning")
appointment14 = Appointment("Dr. Wilson", pet4, "Surgery")
appointment15 = Appointment("Dr. Anderson", pet6, "Grooming")
appointment16 = Appointment("Dr. Brown", pet2, "Checkup")
appointment17 = Appointment("Dr. Clark", pet7, "Vaccination")
appointment18 = Appointment("Dr. Evans", pet3, "Dental Cleaning")
appointment19 = Appointment("Dr. Garcia", pet2, "Surgery")
appointment20 = Appointment("Dr. Hall", pet1, "Grooming")

ipdb.set_trace()