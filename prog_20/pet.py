class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    def set_age(self, pet_age):
        if pet_age >= 0: self.__age = pet_age
        else: self.__age = 0
    def get_age(self): return self.__age