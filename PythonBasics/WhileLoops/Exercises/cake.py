cake_width = int(input())
cake_height = int(input())

cake_size = cake_width * cake_height
pieces = 0
is_cake_finish = False

while True:
    command = input()
    if command == "STOP":
        break
    pieces += int(command)

    if pieces >= cake_size:
        is_cake_finish = True
        break

if pieces < cake_size:
    print(f"{cake_size - pieces} pieces are left.")
else:
    print(f"No more cake left! You need {pieces - cake_size} pieces more.")