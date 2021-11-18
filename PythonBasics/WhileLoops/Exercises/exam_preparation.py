count = int(input())
average_score = 0
total_grades = 0
count_tasks = 0
count_grades = 0
last_problem = ""

while True:
    task = input()
    if task == "Enough":
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {count_tasks}")
        print(f"Last problem: {last_problem}")
        break

    last_problem = task
    count_tasks += 1
    grade = int(input())
    if grade <= 4:
        count_grades += 1
        if count_grades == count:
            print(f"You need a break, {count_grades} poor grades.")
            break

    total_grades += grade
    average_score = total_grades / count_tasks