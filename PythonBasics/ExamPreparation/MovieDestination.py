budget = float(input())
destination = input()
season = input()
days = int(input())
price_per_day = 0

if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    else:
        price_per_day = 40000
elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    else:
        price_per_day = 12500
elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    else:
        price_per_day = 20250

total_price = days * price_per_day

if destination == "Dubai":
    total_price = total_price - (total_price * 0.3)

if destination == "Sofia":
    total_price = total_price + (total_price * 0.25)


if budget >= total_price:
    print(f"The budget for the movie is enough! We have {(budget - total_price):.2f} leva left!")
else:
    print(f"The director needs {(total_price - budget):.2f} leva more!")