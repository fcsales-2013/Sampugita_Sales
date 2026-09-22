# CHECK MY USERNAME BRO!
validchar = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

print("Hey Its me Its verity!")
print("Hello Boii we will see if username is very very valid!")
while True:
    didyoudoyourchores = True
    username = input("Please enter your username: ").lower().strip()
    if 5 <= len(username) <= 10:
        for letter in username:
            if letter not in validchar:
                didyoudoyourchores = False
                break
        if didyoudoyourchores == False:
            print("Boiii... Invalid user detected!!! Only character is allowed is number and letter.")
            continue
        else:
            print(f"Wow! This is so so Valid! Welcome to IDF database {username}!")
            break
    else:
        print("HOLD ON! 2 SHORT OR 2 LONG!!! ONLY 5-10 CHARACTERS!!!")
        continue