month = input()
nights = int(input())

total_price_apartment = 0
total_price_studio = 0
discount_studio = 0
discount_apartment = 0

if month == 'May' or month == 'October':
    total_price_studio = nights * 50
    total_price_apartment = nights * 65

    if nights > 14:
        discount_studio = 0.30
    elif nights > 7:
        discount_studio = 0.05
elif month == 'June' or month == 'September':
    total_price_studio = nights * 75.2
    total_price_apartment = nights * 68.7

    if nights > 14:
        discount_studio = 0.2
elif month == 'July' or month == 'August':
    total_price_studio = nights * 76
    total_price_apartment = nights * 77

if nights > 14:
    discount_apartment = 0.1

total_price_studio = total_price_studio - (total_price_studio * discount_studio)
total_price_apartment = total_price_apartment - (total_price_apartment * discount_apartment)

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")