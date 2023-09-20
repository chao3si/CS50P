due, inserted = 50, 0
while inserted < due:
    print("Amount Due:", due - inserted)
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        inserted += coin
print("Change Owed:", inserted - due)