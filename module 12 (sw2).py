import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
data = response.json()

print("Here's a Chuck Norris joke:")
print(data["value"])


# part 2

import requests

API_KEY = "b241d66b696a318fc8a121a5307bbff8" # It keeps saying city not found, I've tried multiple keys

city = input("Enter a city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)
data = response.json()


if str(data.get("cod")) != "200":

    print("City not found. Try again.")
else:
    description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    print(f"Weather in {city}: {description}")
    print(f"Temperature: {temp_celsius:.1f} °C")
