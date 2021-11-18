number = int(input())

sum_numbers = 0

while True:
    sum_numbers += int(input())
    if sum_numbers >= number:
        print(sum_numbers)
        break
