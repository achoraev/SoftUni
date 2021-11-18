people = int(input())
presentation = ""
total_score = 0
total_average = 0
count_presentation = 0

while True:
    command = input()
    if command == "Finish":
        break
    presentation = command
    score = 0
    count_presentation += 1
    for i in range(0, people):
        score += float(input())

    average_score = score / people
    total_score += average_score
    print(f"{presentation} - {average_score:.2f}.")

total_average = total_score / count_presentation
print(f"Student's final assessment is {total_average:.2f}.")



