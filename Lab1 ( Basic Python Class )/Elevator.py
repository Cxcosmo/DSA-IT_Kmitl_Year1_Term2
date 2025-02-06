class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        self.current_floor = floor

    def report_current_floor(self):
        print(self.current_floor)

elevator = Elevator(input())
max_elevator = elevator.max_floor

while True :
    floor = input()
    if floor == "Done" :
        elevator.report_current_floor()
        break
    if int(floor) > int(max_elevator) :
        print("Invalid Floor!")
    else :
        elevator.go_to_floor(floor)
