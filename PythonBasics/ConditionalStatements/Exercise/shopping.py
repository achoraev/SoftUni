budget = float(input())
videocards = int(input())
processors = int(input())
ram = int(input())

price_videocards = videocards * 250
price_processors = price_videocards * 0.35 * processors
price_ram = price_videocards * 0.1 * ram

total_price = price_videocards + price_processors + price_ram

if videocards > processors:
    total_price = total_price - (total_price * 0.15)

if budget >= total_price:
    print(f"You have {(budget - total_price):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total_price - budget):.2f} leva more!")
