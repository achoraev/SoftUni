room_width = int(input())
room_daljina = int(input())
room_height = int(input())

free_space = room_height * room_width * room_daljina
total_space = 0

while True:
    command = input()
    if command == "Done":
        if free_space > total_space:
            print(f"{free_space - total_space} Cubic meters left.")
        break
    total_space += int(command)
    if total_space >= free_space:
        print(f"No more free space! You need {total_space - free_space} Cubic meters more.")
        break

