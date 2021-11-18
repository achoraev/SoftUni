count_groups = int(input())

total_people = 0
musala_percents = 0
monblan_percents = 0
kilimanjaro_percents = 0
k2_percents = 0
everest_percents = 0

for groups in range(0, count_groups):
    people = int(input())
    total_people += people

    if people <= 5:
        musala_percents += people
    elif people >= 6 and people <= 12:
        monblan_percents += people
    elif people >= 13 and people <= 25:
        kilimanjaro_percents += people
    elif people >= 26 and people <= 40:
        k2_percents += people
    else:
        everest_percents += people

musala_percents = musala_percents / total_people * 100
monblan_percents = monblan_percents / total_people * 100
kilimanjaro_percents = kilimanjaro_percents / total_people * 100
k2_percents = k2_percents / total_people * 100
everest_percents = everest_percents / total_people * 100

print(f"{musala_percents:.2f}%")
print(f"{monblan_percents:.2f}%")
print(f"{kilimanjaro_percents:.2f}%")
print(f"{k2_percents:.2f}%")
print(f"{everest_percents:.2f}%")
