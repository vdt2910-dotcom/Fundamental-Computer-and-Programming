class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Floor: {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor!")
            return

        print(f"Move to floor {target_floor}")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [
            Elevator(bottom_floor, top_floor)
            for _ in range(num_elevators)
        ]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRun elevator {elevator_number}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Elevator not found!")

    def fire_alarm(self):
        print("\nFIRE ALARM! All elevators go to ground floor!")

        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i}:")
            elevator.go_to_floor(elevator.bottom_floor)


if __name__ == "__main__":
    h = Elevator(1, 10)
    h.go_to_floor(5)
    h.go_to_floor(1)

    building = Building(1, 10, 3)
    building.run_elevator(0, 7)
    building.run_elevator(2, 4)
    building.fire_alarm()
