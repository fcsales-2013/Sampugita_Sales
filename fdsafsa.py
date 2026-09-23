# Gubby Reeee
print("Hello Folk 3!")
while True:
    try:
        print("THis time we check your scoreeeee!!!")
        scoreis = int(input("Enter your scoree:"))
        if scoreis < 0 or scoreis > 100:
            print("Too high.. or its like.. Negative try again buddy")
            continue
        break
    except ValueError:
        print("No, bro.. No")
        continue