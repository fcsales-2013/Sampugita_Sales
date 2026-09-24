# Woah! Its the Distance Calculator is epic
# Import stage to added required items
import time
from math import sqrt
import sys
pissed_off_count = 0 # Tiny little detail in where if you piss of the program

# quick greeting explaining the purpose
print("Today we will get the distance!")

# Validation loop just in case
while True:
    try: # <-- This basically lets me catch if you inpurted a string
        x1 = float(input("Input the first x axis! :"))
        y1 = float(input("Now input the first y axis! :"))
        x2 = float(input("Input the second x axis! :"))
        y2 = float(input("Now input the second y axis! :"))
        break
    except ValueError: # Response to a string output
        if pissed_off_count <= 10:
            print("Thats not it =/ INPUT A NUMBER INSTEAD")
            pissed_off_count += 1
        elif pissed_off_count <= 25:
            print("GRRRR.. IM GETTING REALLY ANGRY! DONT PUSH MY BUTTONS")
            pissed_off_count += 3
        else:
            print("THATS IT BUDDY! IM DONE BEING NICE!")
            time.sleep(1)
            print("CLOSING PROGRAM.....")
            time.sleep(0.5)
            sys.exit() # <--- Closes the program because it got pissed

# WHere the actual Calculating begins!!! 
print("NOW LETS GET TO CALCULATING!!")
time.sleep(0.5)
print("calulating.....")
d = sqrt((x2-x1)**2+(y2-y1)**2)
print("getting answer.......")
time.sleep(0.1)
print(f"The distance between your 2 given points is {d:.2f}")