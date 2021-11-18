tabs = int(input())
salary = int(input())

globa = 0
isLostSalary = False

for i in range(0, tabs):
    tab = input()
    if tab == "Facebook":
        globa += 150
        if (salary - globa) <= 0:
            isLostSalary = True
            break
    elif tab == "Instagram":
        globa += 100
        if (salary - globa) <= 0:
            isLostSalary = True
            break
    elif tab == "Reddit":
        globa += 50
        if (salary - globa) <= 0:
            isLostSalary = True
            break

salary = salary - globa

if isLostSalary:
    print("You have lost your salary.")
else:
    print(salary)