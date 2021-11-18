number1 = int(input())
number2 = int(input())
operator = input()

if number2 == 0:
    print(f"Cannot divide {number1} by zero")
elif operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = number1 + number2
        is_even_or_odd = 'odd'
        if result %2 == 0:
            is_even_or_odd = 'even'

        print(f"{number1} {operator} {number2} = {result} - {is_even_or_odd}")
    elif operator == '-':
        result = number1 - number2
        is_even_or_odd = 'odd'
        if result % 2 == 0:
            is_even_or_odd = 'even'

        print(f"{number1} {operator} {number2} = {result} - {is_even_or_odd}")
    elif operator == '*':
        result = number1 * number2
        is_even_or_odd = 'odd'
        if result % 2 == 0:
            is_even_or_odd = 'even'

        print(f"{number1} {operator} {number2} = {result} - {is_even_or_odd}")
elif operator == '/':
    print(f"{number1} / {number2} = {(number1 / number2):.2f}")
elif operator == '%':
    ostatak = number1 % number2
    print(f"{number1} % {number2} = {ostatak}")