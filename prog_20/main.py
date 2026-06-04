# Interactive Pet Data Ledger System
import os
from pet import Pet
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*45 + "\n       🐾  PET PROFILE REGISTRATION  🐾      \n" + "="*45)
    registered_pet = Pet()
    registered_pet.set_name(input("Enter Pet Name: "))
    registered_pet.set_animal_type(input("Enter Animal Type: "))
    while True:
        try: registered_pet.set_age(int(input("Enter Pet Age: "))); break
        except ValueError: print("❌ Invalid Age!")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*45 + "\n         🪪   VIRTUAL PET DIGITAL ID  🪪         \n" + "="*45)
    print(f"  Name: {registered_pet.get_name()}\n  Type: {registered_pet.get_animal_type()}\n  Age:  {registered_pet.get_age()} year(s) old\n" + "="*45)