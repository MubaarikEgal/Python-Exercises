# Task 1
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        return

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print("Elevator at floor " + str(self.current_floor))
        return

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print("Elevator at floor " + str(self.current_floor))
        return

    def go_to_floor(self, floor):
        if floor < self.bottom_floor:
            floor = self.bottom_floor
        if floor > self.top_floor:
            floor = self.top_floor
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()
        return

# Task 2
class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.elevators = []
        for i in range(elevator_count):
            self.elevators.append(Elevator(bottom_floor, top_floor))
        return

    def run_elevator(self, number, destination_floor):
        self.elevators[number - 1].go_to_floor(destination_floor)
        return
# Task 3
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom_floor)
        return


elevator = Elevator(1, 10)
elevator.go_to_floor(6)
elevator.go_to_floor(1)

building = Building(1, 10, 3)
building.run_elevator(1, 8)
building.run_elevator(2, 6)
building.run_elevator(3, 4)
building.fire_alarm()
