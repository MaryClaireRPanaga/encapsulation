# Encapsulated Pet Profile Properties
class Pet:
    def __init__(self): self.__name, self.__animal_type, self.__age = "", "", 0
    def set_name(self, name_string): self.__name = name_string.strip() or "Unknown"
    def set_animal_type(self, type_string): self.__animal_type = type_string.strip().capitalize() or "Unknown"
    def set_age(self, age_integer): self.__age = max(0, age_integer)
    def get_name(self): return self.__name
    def get_animal_type(self): return self.__animal_type
    def get_age(self): return self.__age