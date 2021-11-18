budget = int(input())
season = input()
fishers = int(input())

rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fishers <= 6:
    rent = rent - (rent * 0.1)
elif fishers > 6 and fishers <= 11:
    rent = rent - (rent * 0.15)
else:
    rent = rent - (rent * 0.25)

if season != 'Autumn' and fishers % 2 == 0:
    rent = rent - (rent * 0.05)

if rent > budget:
    print(f"Not enough money! You need {(rent - budget):.2f} leva.")
else:
    print(f"Yes! You have {(budget - rent):.2f} leva left.")
