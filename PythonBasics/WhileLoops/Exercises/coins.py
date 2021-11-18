import math

price = float(input())
count = 0

while price > 0.0:
    if price >= 2:
        count += price // 2
        price = round(price % 2, 2)
    elif price >= 1:
        count += price // 1
        price = round(price % 1, 2)
    elif price >= 0.5:
        count += price // 0.5
        price = round(price % 0.5, 2)
    elif price >= 0.2:
        count += price // 0.2
        price = round(price % 0.2, 2)
    elif price >= 0.1:
        count += price // 0.1
        price = round(price % 0.1, 2)
    elif price >= 0.05:
        count += price // 0.05
        price = round(price % 0.05, 2)
    elif price >= 0.02:
        count += price // 0.02
        price = round(price % 0.02, 2)
    elif price >= 0.01:
        count += price // 0.01
        price = round(price % 0.01, 2)


print(f"{count:.0f}")