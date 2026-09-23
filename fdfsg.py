# No la polizina Nooo!!!
PINvalid = True
validchars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
while True:
    try:
        PINreal = int(input("Enter your PIN: "))
        for PINreal in validchars:
            if PINreal not in validchars:
                PINvalid = False
                break
        if PINreal == False:
            print("Thats invalid boiii")
            continue
        elif PINreal > 999999:
            print("Thats too high")
            continue
        break
    except ValueError:
        print("No, bro.. No")
print("Ok thats cool!")
