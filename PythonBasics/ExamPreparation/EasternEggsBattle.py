eggs_first_player = int(input())
eggs_second_player = int(input())
eggs_first = eggs_first_player
egss_second = eggs_second_player

while True:
    command = input()
    if command == "End of battle":
        print(f"Player one has {eggs_first} eggs left.")
        print(f"Player two has {egss_second} eggs left.")
        break

    if command == "one":
        egss_second -= 1
    elif command == "two":
        eggs_first -= 1

    if eggs_first <= 0:
        print(f"Player one is out of eggs. Player two has {egss_second} eggs left.")
        break
    elif egss_second <= 0:
        print(f"Player two is out of eggs. Player one has {eggs_first} eggs left.")
        break