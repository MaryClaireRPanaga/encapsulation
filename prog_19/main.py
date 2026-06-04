# Car Dashboard Velocity Tracker Simulation
import os, time
from car import Car
def dash(car_object, status_label):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*45 + f"\n   🚗 TRACK DASHBOARD: {car_object.get_info()} 🚗    \n" + "="*45)
    print(f"Status: {status_label}\nSpeedometer: [{'⚡'*(car_object.get_speed()//5)}{'░'*(10-(car_object.get_speed()//5))}] {car_object.get_speed()} km/h\n" + "="*45)
    time.sleep(0.4)
if __name__ == "__main__":
    my_track_car = Car("2026", "Mustang-GT")
    for cycle in range(5): my_track_car.accelerate(); dash(my_track_car, "Accelerating...")
    for cycle in range(5): my_track_car.brake(); dash(my_track_car, "Braking...")