n = int(input())
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for num in range(0, n):
    number = int(input())

    if number < 200:
        count1 += 1
    elif number >= 200 and number <= 399:
        count2 += 1
    elif number >= 400 and number <= 599:
        count3 += 1
    elif number >= 600 and number <= 799:
        count4 += 1
    else:
        count5 += 1

p1 = count1 / n * 100
p2 = count2 / n * 100
p3 = count3 / n * 100
p4 = count4 / n * 100
p5 = count5 / n * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")