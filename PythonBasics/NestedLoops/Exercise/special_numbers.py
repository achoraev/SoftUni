import math

number = int(input())


for i in range(1111, 9999):
    is_special = True
    current_number = i

    while current_number > 0:
        current_digit = current_number % 10
        if current_digit > 0:
            if number % current_digit != 0:
                is_special = False
                break
        else:
            is_special = False
        current_number = current_number // 10

    if is_special:
        print(i, end =" ")
