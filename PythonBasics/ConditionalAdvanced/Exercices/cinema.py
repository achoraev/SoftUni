type = input()
rows = int(input())
cols = int(input())

income = 0
cinema_capacity = rows * cols

if type == 'Premiere':
    income = cinema_capacity * 12
elif type == 'Normal':
    income = cinema_capacity * 7.5
elif type == 'Discount':
    income = cinema_capacity * 5

print(f"{income:.2f} leva")