number = int(input())
counter = 0

for i in range(0, number + 1):
    for j in range(0, number + 1):
        for k in range(0, number + 1):
            product = i + j + k
            if product == number:
                counter += 1

print(counter)