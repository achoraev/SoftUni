name = input()
current_class = 1
average_score = 0
total_grade = 0
is_graduated = False
count_excluded = 0

while True:
    if current_class == 13:
        is_graduated = True
        break

    grade = float(input())
    if grade < 4:
        count_excluded += 1
        if count_excluded == 2:
            break
    else:
        current_class += 1
        total_grade += grade


average_score = total_grade / 12

if is_graduated:
    print(f"{name} graduated. Average grade: {average_score:.2f}")
else:
    print(f"{name} has been excluded at {current_class} grade")