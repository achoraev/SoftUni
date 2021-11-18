town = input()
sales = float(input())
discount = 0
is_sales_negative = False

if sales >= 0 and sales <= 500:
    if town == 'Sofia':
        discount = 0.05
    elif town == 'Varna':
        discount = 0.045
    elif town == 'Plovdiv':
        discount = 0.055
elif sales > 500 and sales <= 1000:
    if town == 'Sofia':
        discount = 0.07
    elif town == 'Varna':
        discount = 0.075
    elif town == 'Plovdiv':
        discount = 0.08
elif sales > 1000 and sales <= 10000:
    if town == 'Sofia':
        discount = 0.08
    elif town == 'Varna':
        discount = 0.10
    elif town == 'Plovdiv':
        discount = 0.12
elif sales > 10000:
    if town == 'Sofia':
        discount = 0.12
    elif town == 'Varna':
        discount = 0.13
    elif town == 'Plovdiv':
        discount = 0.145
else:
    is_sales_negative = True


if discount == 0 or is_sales_negative:
    print('error')
else:
    print(f"{(sales * discount):.2f}")