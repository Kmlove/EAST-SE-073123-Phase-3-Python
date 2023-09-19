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

proc1 = Procedure("Checkup", 30)
proc2 = Procedure("Vaccination", 50)
proc3 = Procedure("Surgery", 1000)
proc4 = Procedure("Dental Cleaning", 45)

appointment1 = Appointment("Dr. Smith", pet1, proc1)
appointment2 = Appointment("Dr. Johnson", pet3, proc2)
appointment3 = Appointment("Dr. Davis", pet3, proc4)
appointment4 = Appointment("Dr. Wilson", pet4, proc1)
appointment5 = Appointment("Dr. Anderson", pet5, proc3)
appointment6 = Appointment("Dr. Brown", pet6, proc4)
appointment7 = Appointment("Dr. Clark", pet5, proc1)
appointment8 = Appointment("Dr. Evans", pet8, proc4)
appointment9 = Appointment("Dr. Garcia", pet9, proc3)
appointment10 = Appointment("Dr. Hall", pet10, proc1)
appointment11 = Appointment("Dr. Smith", pet10, proc1)
appointment12 = Appointment("Dr. Johnson", pet9, proc2)
appointment13 = Appointment("Dr. Davis", pet8, proc1)
appointment14 = Appointment("Dr. Wilson", pet4, proc3)
appointment15 = Appointment("Dr. Anderson", pet6, proc3)
appointment16 = Appointment("Dr. Brown", pet2, proc1)
appointment17 = Appointment("Dr. Clark", pet7, proc2)
appointment18 = Appointment("Dr. Evans", pet3, proc4)
appointment19 = Appointment("Dr. Garcia", pet2, proc1)
appointment20 = Appointment("Dr. Hall", pet1, proc2)

ipdb.set_trace()