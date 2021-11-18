budget = float(input())
statists = int(input())
price_per_statist = float(input())

decor_movie = budget * 0.1
total_clothes = statists * price_per_statist

if statists > 150:
    total_clothes = total_clothes - (total_clothes * 0.1)

total_budget = decor_movie + total_clothes

if total_budget > budget:
    print('Not enough money!')
    print(f"Wingard needs {(total_budget - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget - total_budget):.2f} leva left.")

