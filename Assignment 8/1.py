class Machine:
    def __init__(self, name):
        self.name = name
        
    def show_info(self):
        print(f"This is {self.name}")
class Elevator(Machine):
    def __init__(self, name, start_floor):
        super().__init__(name)
        self.current_floor = start_floor
        
    def move(self, target_floor):
        print(f"{self.name} is moving to floor {target_floor}")
        
        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Floor: {self.current_floor}")
            
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Floor: {self.current_floor}")


if __name__ == "__main__":
    elevator = Elevator("Elevator A", 1)
    elevator.show_info()
    elevator.move(5)
    elevator.move(2)
