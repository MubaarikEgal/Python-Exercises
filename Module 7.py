# Task 1

seasons = ("Spring", "Summer", "Autumn", "Winter")


month = int(input("Enter the number of a month (1-12): "))

if month == 12 or month == 1 or month == 2:
    season = seasons[0]
elif month >= 3 and month <= 5:
    season = seasons[1]
elif month >= 6 and month <= 8:
    season = seasons[2]
elif month >= 9 and month <= 11:
    season = seasons[3]
else:
    season = None


if season:
    print(f"Month {month} is in {season} :)")
else:
    print("ERRRR TRY AGAIN >:( !")

# Task 2

