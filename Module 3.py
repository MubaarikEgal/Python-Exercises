# Task 1
zlenght = int(input("What length is the zander you caught? "))

if zlenght >= 42:
    print("Amazing!")
else:
    margin = str(42 - zlenght)
    print("Release the fish back into the water...")
    print("The fish is " + margin + "cm below the size limit")

# Task 2

cclass = str(input("What is your cabin class sir?: "))
if cclass == "LUX":
    print("upper-deck cabin with a balcony.")
elif cclass == "A".lower():
    print("above the car deck, equipped with a window.")
elif cclass == "B".lower():
    print("windowless cabin above the car deck.")
elif cclass == "C".lower():
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class, please try again.")

#Task 3

gender = str(input("What is your gender? "))
Hvalue = float(input("What is your hemoglobin value? "))

if gender == "female" and 117 <= Hvalue <= 155:
    print("Your hemoglobin value is just right ")
elif Hvalue < 117:
        print("Your hemoglobin value is too low, go see a doctor.")
elif Hvalue > 155:
            print("Your hemoglobin value is too high, go see a doctor.")

elif gender == "male" and 134 <= Hvalue <= 167:
    print("Your hemoglobin levels are just right ")
elif Hvalue < 134:
        print("Your hemoglobin value is too low, go see a doctor.")
elif Hvalue > 167:
            print("Your hemoglobin value is too high, go see a doctor.")

else:
    print("please try again")











