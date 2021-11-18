price = float(input())

puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_toys = puzzles + dolls + bears + minions + trucks

price_puzzles = puzzles * 2.6
price_dolls = dolls * 3
price_bears = bears * 4.1
price_minions = minions * 8.2
price_trucks = trucks * 2

total_price = price_puzzles + price_dolls + price_bears + price_minions + price_trucks

if total_toys >= 50:
    total_price = total_price - (total_price * 0.25)

rent = total_price * 0.1
total_price = total_price - rent

if total_price >= price:
    print(f"Yes! {(total_price - price):.2f} lv left.")
else:
    print(f"Not enough money! {(price - total_price):.2f} lv needed.")
