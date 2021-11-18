while True:
    destination = input()

    if destination != "End":
        needed_money = float(input())
        money = 0

        while True:
            money += float(input())
            if  money >= needed_money:
                print(f"Going to {destination}!")
                break
    else:
        break