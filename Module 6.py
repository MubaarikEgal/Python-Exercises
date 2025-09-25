# Task 1

import random

def roll_dice():
    return random.randint(1, 6)

while True:
    result = roll_dice()
    print("You rolled:", result)
    if result == 6:
        break

# Task 2

import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("How many sides gentlemen? "))

while True:
    result = roll_dice(sides)
    print("You rolled:", result)
    if result == sides:
        break

# Task 3
def gallons_to_liters(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input("Enter gallons (negative number to quit): "))
    if gallons < 0:
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is {liters:.2f} liters")

