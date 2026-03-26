class car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


my_car = car("ABC-123", 142)

print(f'Hello, this car is {my_car.registration_number}')
print(f'Current speed: {my_car.current_speed}')
print(f'Maximum speed: {my_car.maximum_speed}')
print(f'Travelled distance: {my_car.travelled_distance}')