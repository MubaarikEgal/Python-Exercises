# Task 1

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        return
# Task 2
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
        return
# Task 4
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
        return


car = Car("ABC-123", 142)
print(car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(car.current_speed)

car.accelerate(-200)
print(car.current_speed)

car.travelled_distance = 2000
car.current_speed = 60
car.drive(1.5)
print(car.travelled_distance)
