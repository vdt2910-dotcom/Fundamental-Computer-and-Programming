class Elevator:
    def __init__(self, name, start_floor):
        self.name = name
        self.current_floor = start_floor

    def move(self, target_floor):
        print(f"{self.name} moving to floor {target_floor}")

        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"{self.name} at floor {self.current_floor}")

        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"{self.name} at floor {self.current_floor}")


class Building:
    def __init__(self):
        self.elevators = [
            Elevator("Elevator 1", 1),
            Elevator("Elevator 2", 1),
            Elevator("Elevator 3", 1)
        ]

    def run_elevator(self, number, floor):
        if number < len(self.elevators):
            self.elevators[number].move(floor)
        else:
            print("Elevator not found")


if __name__ == "__main__":
    building = Building()
    building.run_elevator(0, 5)
    building.run_elevator(2, 3)
