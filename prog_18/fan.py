class Fan:
    SLOW, MEDIUM, FAST = 1, 2, 3
    def __init__(self):
        self.__speed = self.SLOW
        self.__radius = 5.0
        self.__color = "blue"
        self.__on = False
    def get_speed(self): return self.__speed
    def set_speed(self, speed_level): self.__speed = speed_level
    def get_radius(self): return self.__radius
    def set_radius(self, radius_size): self.__radius = radius_size
    def get_color(self): return self.__color
    def set_color(self, color_name): self.__color = color_name
    def is_on(self): return self.__on
    def set_on(self, power_state): self.__on = power_state