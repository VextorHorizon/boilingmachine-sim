import time
import random

while True:
    try:
        water_temp = int(input("Water temperature: "))
        break
    except ValueError:
        print("Use a integer")
        continue


while water_temp < 100:
    random_increase = random.randint(3, 7)
    print(f"\nWater isn't boiling yet \n{water_temp} °C +{(random_increase)}")
    water_temp += random_increase
    time.sleep(0.5)


if water_temp > 150:
    print("\n--------------------\nThe Boiling machine is at risk\n--------------------\n")

else:
    print("\n--------------------\nWater is boiling now\n--------------------\n")

