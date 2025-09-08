import time
import random

while True:
    try:
        water_temp = int(input("Water temperature: "))
        break
    except ValueError:
        print("Use a integer")
        continue

tea = 100
coffee = 90


while True:

    option_user = input("Select your target temperature\n1.Tea\n2.Coffee\n3.Manual Setting\n(1/2/3): ").strip()

    if option_user == "1":
        target_tem = tea
        print("You're selecting Tea (100°C)")
        break

    elif option_user == "2":
        target_tem = coffee
        print("You're selecting Coffee (90°C)")
        break

    elif option_user == "3":
        while True:
            try:
                target_tem = int(input("Your target temperature: "))
                print(f"The target temperature is {target_tem}")
                break
            except ValueError:
                print("Use a integer")
                continue
        break
            
    else:
        print("The option has only 1/2/3")
        
        continue


while water_temp < target_tem:
    random_increase = random.randint(3, 7)
    print(f"\nWater isn't boiling yet \n{water_temp} °C +{(random_increase)}")
    water_temp += random_increase
    time.sleep(0.5)


if water_temp > 200:
    print("\n--------------------\nThe boiling machine is at risk\n--------------------\n")
elif water_temp > target_tem:
    print("\n--------------------\nWater is boiling now\n--------------------\n")

