amount = 50

while True:
    print("Amount Due: " + str(amount))
    insert  = int(input("Insert Coin: "))

    if insert in [5,10,25]:
        amount = amount - insert
        if amount <= 0:
            print("Change Owed: " + str(abs(amount)))
            break