from car import Car
if __name__ == "__main__":
    test_car = Car("2026", "Mustang")
    for step in range(5): test_car.accelerate()
    for step in range(5): test_car.brake()
    print(f"Final speed of the car: {test_car.get_speed()}")