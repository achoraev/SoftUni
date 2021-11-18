total_tickets = 0
student_tickets = 0
standart_tickets = 0
kids_tickets = 0
count_seats = 0

while True:
    command = input()
    if command == "Finish":
        print(f"Total tickets: {total_tickets}")
        percent_student = student_tickets / total_tickets * 100
        percent_standart = standart_tickets / total_tickets * 100
        percent_kid = kids_tickets / total_tickets * 100

        print(f"{percent_student:.2f}% student tickets.")
        print(f"{percent_standart:.2f}% standard tickets.")
        print(f"{percent_kid:.2f}% kids tickets.")
        break

    count_seats = 0

    movie = command
    free_seats = int(input())
    seats = free_seats

    while True:
        if seats <= 0:
            break
        command = input()
        if command == "End":
            break
        count_seats += 1
        total_tickets += 1
        ticket = command
        seats -= 1
        if ticket == "standard":
            standart_tickets += 1
        elif ticket == "kid":
            kids_tickets += 1
        elif ticket == "student":
            student_tickets += 1

    print(f"{movie} - {(count_seats / free_seats * 100):.2f}% full.")