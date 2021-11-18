age = int(input())
price_wash = float(input())
price_toy = int(input())

saved_money = 0
toys = 0
count_brother_money = 0

for years in range(1, age + 1):
    if years % 2 == 0:
        saved_money += years * 5
        count_brother_money += 1
    else:
        toys += 1

saved_money += toys * price_toy
saved_money = saved_money - count_brother_money


if saved_money >= price_wash:
    ostatuk = saved_money - price_wash
    print(f"Yes! {ostatuk:.2f}")
else:
    print(f"No! {(price_wash - saved_money):.2f}")