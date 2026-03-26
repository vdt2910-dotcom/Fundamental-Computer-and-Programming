import random

class car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


car_list = []

for i in range(1, 11):
    car_list.append(car(f"ABC-{i}", random.randint(150, 200)))


finish = False

while not finish:
    for c in car_list:
        c.accelerate(random.randint(-10, 15))
        c.drive(1)

        if c.travelled_distance >= 10000:
            finish = True


for c in car_list:
    print(f'{c.registration_number} | {c.maximum_speed} | {c.current_speed} | {c.travelled_distance} km')