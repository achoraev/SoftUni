day = input()

if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    print(12)
elif day == 'Saturday' or day == 'Sunday':
    print(16)
else:
    print(14)