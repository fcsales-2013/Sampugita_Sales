# The Age Checkers

print("They call me, Lord Verity! Master of Humanity")
print("Hello Folk! We check thy age!!!")
while True:
    try:
        age = int(input("Now Input age bud"))
        if age <= 0:
            print("... Negative Age??? Or were you born just now???")
            continue
        elif age < 12:
            print("Nooo... Too young!! Go back! Go back!")
            continue
        elif age > 18:
            print("Noooo... Thats too old!! Try again!")
            continue
        break
    except ValueError:
        print("NOOO Only Integer.. or you typed ""pizza"" either way...")
        continue
print("Ok!!! You made a valid age boiii")
