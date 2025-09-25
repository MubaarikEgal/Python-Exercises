# Task 1
import random

dice_ran = int(input("How many dice do you want to roll? "))
total = 0

for i in range(dice_ran):
    roll = random.randint(1, 6)  # random number between 1 and 6
    print("You've rolled:", roll)
    total = total + roll

print("The total sum is:", total)

#Task 2

numbers = []

while True:
    num = input("Enter a number (or press Enter to quit): ")
    if num == "":
        break
    numbers.append(int(num))

numbers.sort(reverse=True)

print("The 5 greatest numbers are:")
for n in numbers[:5]:
    print(n)
