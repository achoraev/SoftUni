number1 = input()
number2 = input()

for i in range(int(number1), int(number2) + 1):
    number = str(i)
    odd_sum = 0
    even_sum = 0

    #for index, digit in enumerate(number):

    for digit in range(0, 6):
        current_digit = number[digit]
        if digit % 2 == 0:
            even_sum += int(current_digit)
        else:
            odd_sum += int(current_digit)

    if even_sum == odd_sum:
        print(number, end=" ")
