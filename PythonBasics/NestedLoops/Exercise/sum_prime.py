prime_sum = 0
nonprime_sum = 0
isPrime = True

while True:
    isPrime = True
    command = input()
    if command == "stop":
        break
    number = int(command)
    if number < 0:
        print("Number is negative.")
        continue

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                nonprime_sum += number
                isPrime = False
                break
    if isPrime:
        prime_sum += number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {nonprime_sum}")