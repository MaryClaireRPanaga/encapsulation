# Fan Domain Execution Interface
import os
from fan import Fan
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*45 + "\n        🌀 FAN CLASS ENCAPSULATION 🌀        \n" + "="*45)
    first_fan = Fan(Fan.FAST, 10.0, "yellow", True)
    second_fan = Fan(Fan.MEDIUM, 5.0, "blue", False)
    first_fan.display_properties("Fan Object #1")
    second_fan.display_properties("Fan Object #2")