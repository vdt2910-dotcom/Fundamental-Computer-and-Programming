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


my_car = car("ABC-123", 142)

my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)

print(f'Current speed: {my_car.current_speed} km/h')

my_car.accelerate(-200)

print(f'Speed after braking: {my_car.current_speed} km/h')