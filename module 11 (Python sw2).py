class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f" Author: {self.author}")
        print(f" Pages: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f" Chief Editor: {self.chief_editor}")


# main program

donald_duck = Magazine("Donald Duck", "Aki Hyypää")
compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
print()
compartment_no_6.print_information()


#Part 2

class Car:
    def __init__(self, registration_number: str, max_speed: float):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0.0
        self.travelled_distance = 0.0  # in km

    def set_speed(self, speed: float):
        # clamp between 0 and max_speed
        self.current_speed = max(0.0, min(speed, self.max_speed))

    def drive(self, hours: float):
        # distance = speed * time
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number: str, max_speed: float, battery_capacity_kwh: float):
        super().__init__(registration_number, max_speed)
        self.battery_capacity_kwh = battery_capacity_kwh


class GasolineCar(Car):
    def __init__(self, registration_number: str, max_speed: float, tank_volume_liters: float):
        super().__init__(registration_number, max_speed)
        self.tank_volume_liters = tank_volume_liters


electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)


electric.set_speed(150)
gasoline.set_speed(140)


electric.drive(3)
gasoline.drive(3)

print(f"Electric car {electric.registration_number} has driven {electric.travelled_distance} km.")
print(f"Gasoline car {gasoline.registration_number} has driven {gasoline.travelled_distance} km.")


