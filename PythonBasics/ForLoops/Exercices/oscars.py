name_actor = input()
academy_points = float(input())
reviewers = int(input())

for names in range(0, reviewers):
    name = input()
    points = float(input())
    academy_points += (len(name) * points) / 2
    if academy_points >= 1250.5:
        break

if academy_points > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {(1250.5 - academy_points):.1f} more!")