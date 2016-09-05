'''
This program determines whether you will receive a ticket from the police for driving too fast.
There is tolerance if it's your birthday today.

'''

speed = input("Please enter your speed: ")
speed = float(speed)
birthday = input("Is it your birthday today? (Yes/No) ")

if birthday == "Yes":
    if speed <= 65:
        print("No ticket")
    elif speed <= 85:
        print("Small ticket")
    else:
        print("Big ticket")
else:
    if speed <= 60:
        print("No ticket")
    elif speed <= 80:
        print("Small ticket")
    else:
        print("Big ticket")
