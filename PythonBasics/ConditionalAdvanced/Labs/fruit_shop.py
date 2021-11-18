product = input()
day = input()
quantity = float(input())
price = 0
isError = False

if day == 'Saturday' or day == 'Sunday':
    if product == 'banana':
        price = 2.7
    elif product == 'apple':
        price = 1.25
    elif product == 'orange':
        price = 0.9
    elif product == 'grapefruit':
        price = 1.60
    elif product == 'kiwi':
        price = 3
    elif product == 'pineapple':
        price = 5.6
    elif product == 'grapes':
        price = 4.2
    else:
        print('error')
        isError = True
elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if product == 'banana':
        price = 2.5
    elif product == 'apple':
        price = 1.2
    elif product == 'orange':
        price = 0.85
    elif product == 'grapefruit':
        price = 1.45
    elif product == 'kiwi':
        price = 2.7
    elif product == 'pineapple':
        price = 5.5
    elif product == 'grapes':
        price = 3.85
    else:
        print('error')
        isError = True
else:
    print('error')
    isError = True

if isError == False:
    print(f"{(price * quantity):.2f}")