balance = 0

while True:
    current = input()
    if current == "NoMoreMoney":
        break
    current = float(current)
    if current < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {current:.2f}")

    balance += current

print(f"Total: {balance:.2f}")



