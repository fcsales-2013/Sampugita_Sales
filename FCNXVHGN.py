# We check your payment!
print("Hello Folk!")
validpayment = ["cash", "card", "gcash"]
while True:
    print("How will you pay thy bill!")
    payment = input("Cash, Card of Gcash???").lower().strip()
    if payment not in validpayment:
        print("Woah! THats not Card, Cash or GCash! Try again")
        continue
    elif payment == "paypal":
        print("You havent paid your pays, pal.")
        continue
    break
