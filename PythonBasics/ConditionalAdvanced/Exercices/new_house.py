flowers = input()
count = int(input())
budget = int(input())

price_flowers = 0;

if flowers == 'Roses':
    price_flowers = count * 5
    if count > 80:
        price_flowers = price_flowers - (price_flowers * 0.1)
elif flowers == 'Dahlias':
    price_flowers = count * 3.8
    if count > 90:
        price_flowers = price_flowers - (price_flowers * 0.15)
elif flowers == 'Tulips':
    price_flowers = count * 2.8
    if count > 80:
        price_flowers = price_flowers - (price_flowers * 0.15)
elif flowers == 'Narcissus':
    price_flowers = count * 3
    if count < 120:
        price_flowers = price_flowers + (price_flowers * 0.15)
elif flowers == 'Gladiolus':
    price_flowers = count * 2.5
    if count < 80:
        price_flowers = price_flowers + (price_flowers * 0.20)


if price_flowers <= budget:
    print(f"Hey, you have a great garden with {count} {flowers} and {(budget - price_flowers):.2f} leva left.")
else:
    print(f"Not enough money, you need {(price_flowers - budget):.2f} leva more.")
