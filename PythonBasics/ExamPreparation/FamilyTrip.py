budget = float(input())
nights = int(input())
price_night = float(input())
percent_extra = int(input())

if nights > 7:
    price_night = price_night - (price_night * 0.05)

sum = nights * price_night
total_sum = sum + (budget * percent_extra / 100)

if total_sum <= budget:
    print(f"Ivanovi will be left with {(budget - total_sum):.2f} leva after vacation.")
else:
    print(f"{(total_sum - budget):.2f} leva needed.")