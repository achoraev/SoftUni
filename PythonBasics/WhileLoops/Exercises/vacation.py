needed_money = float(input())
owned_money = float(input())

days_counter = 0
spending_counter = 0

while True:
    action = input()
    amount = float(input())
    days_counter += 1

    if action == "spend":
        owned_money -= amount
        spending_counter += 1
        if owned_money < 0:
            owned_money = 0
        if spending_counter >= 5:
            print("You can\'t save the money.")
            print(f"{days_counter}")
            break
    else:
        owned_money += amount
        spending_counter = 0

    if owned_money >= needed_money:
        print(f"You saved the money for {days_counter} days.")
        break