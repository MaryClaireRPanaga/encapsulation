# Encapsulated Fan Data Configuration Rules
class Fan:
    SLOW, MEDIUM, FAST = 1, 2, 3
    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed, self.__radius, self.__color, self.__on = speed, radius, color, on
    def get_speed(self): return self.__speed
    def is_on(self): return self.__on
    def get_radius(self): return self.__radius
    def get_color(self): return self.__color
    def set_speed(self, speed_level): self.__speed = speed_level
    def set_on(self, power_state): self.__on = power_state
    def set_radius(self, radius_size): self.__radius = radius_size
    def set_color(self, color_name): self.__color = color_name
    def display_properties(self, fan_identity):
        status_text = "🟢 ON" if self.__on else "🔴 OFF"
        print(f"🔹 {fan_identity}:\n   • State: {status_text} | Speed: {self.__speed} | Radius: {self.__radius} | Color: {self.__color.title()}\n" + "-"*45)