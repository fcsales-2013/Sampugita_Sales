# WE CHECK YOUR GRADE. THATS ALL!
print("Woah! 4 x 5 = 20?!!!!")
print("We will see if your grade level is valid, quite simple!")
while True:
    try:
        grade = int(input("What is your grade level? "))
        if grade >= 0 or grade >= 12 or grade < 0:
            print("NO! THATS NOT VALID BOI!!!!")
            continue
        break
    except ValueError:
        print("Please enter a number!!! Or...... Get my point brother?")
        continue
print("Woah thats so valid! Its like validation!")