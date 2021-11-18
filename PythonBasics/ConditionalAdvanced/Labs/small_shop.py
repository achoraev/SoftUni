product = input()
town = input()
quantity = float(input())

if product == 'coffee':
    if town == 'Sofia':
        print(quantity * 0.5)
    elif town == 'Plovdiv':
        print(quantity * 0.4)
    elif town == 'Varna':
        print(quantity * 0.45)
elif product == 'water':
    if town == 'Sofia':
        print(quantity * 0.8)
    elif town == 'Plovdiv' or town == 'Varna':
        print(quantity * 0.7)
elif product == 'beer':
    if town == 'Sofia':
        print(quantity * 1.2)
    elif town == 'Plovdiv':
        print(quantity * 1.15)
    elif town == 'Varna':
        print(quantity * 1.1)
elif product == 'sweets':
    if town == 'Sofia':
        print(quantity * 1.45)
    elif town == 'Plovdiv':
        print(quantity * 1.3)
    elif town == 'Varna':
        print(quantity * 1.35)
elif product == 'peanuts':
    if town == 'Sofia':
        print(quantity * 1.6)
    elif town == 'Plovdiv':
        print(quantity * 1.5)
    elif town == 'Varna':
        print(quantity * 1.55)
