import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def change_speed(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-15, 15)
            car.change_speed(change)
            car.drive(1)

    def print_status(self):
        print("\n" + "-" * 60)
        print("Plate | Max | Current | Distance")
        print("-" * 60)

        for car in self.cars:
            print(f"{car.registration_number} | {car.max_speed} | {car.current_speed} | {car.travelled_distance}")

        print("-" * 60)

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


if __name__ == "__main__":
    cars = []

    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        car = Car(f"ABC-{i}", max_speed)
        cars.append(car)

    race = Race("Grand Race", 8000, cars)

    hours = 0

    while not race.race_finished():
        race.hour_passes()
        hours += 1

        if hours % 10 == 0:
            print(f"\n[STATUS AFTER {hours} HOURS]")
            race.print_status()

    print("\n" + "=" * 40)
    print(f"RACE FINISHED AFTER {hours} HOURS")
    print("=" * 40)

    race.print_status()