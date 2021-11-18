days = int(input())
room = input()
rate = input()

discount = 0
total = 0

if days < 10:
    if room == 'apartment':
        discount = 0.3
        total = (days - 1) * 25
    elif room == 'president apartment':
        discount = 0.1
        total = (days - 1) * 35
    else:
        total = (days - 1) * 18
elif days >= 10 and days <= 15:
    if room == 'apartment':
        discount = 0.35
        total = (days - 1) * 25
    elif room == 'president apartment':
        discount = 0.15
        total = (days - 1) * 35
    else:
        total = (days - 1) * 18
else:
    if room == 'apartment':
        discount = 0.5
        total = (days - 1) * 25
    elif room == 'president apartment':
        discount = 0.2
        total = (days - 1) * 35
    else:
        total = (days - 1) * 18


total = total - (total * discount)
if rate == 'positive':
    total = total + (total * 0.25)
else:
    total = total - (total * 0.1)

print(f"{total:.2f}")