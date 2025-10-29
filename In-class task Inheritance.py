class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some animal sound")

    def print_info(self):
        print(f"Name: {self.name}, Species: {self.species}")


class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "Snake")

    def make_sound(self):
        print("Hiss!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def make_sound(self):
        print("Meowwwww!")


class Crow(Animal):
    def __init__(self, name):
        super().__init__(name, "Crow")

    def make_sound(self):
        print("KAWWWKKKK!")



class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to the zoo.")

    def show_animals(self):
        print("\nAnimals in the zoo:")
        for a in self.animals:
            a.print_info()
        print(f"Total animals: {len(self.animals)}")

    def make_all_sounds(self):
        print("\nAnimal sounds:")
        for a in self.animals:
            a.make_sound()



zoo = Zoo()

a1 = Crow("Kenny")
a2 = Cat("Tom")
a3 = Snake("Sylva")

zoo.add_animal(a1)
zoo.add_animal(a2)
zoo.add_animal(a3)

zoo.show_animals()
zoo.make_all_sounds()
