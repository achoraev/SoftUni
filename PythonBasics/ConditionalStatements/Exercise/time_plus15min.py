hour = int(input())
minutes = int(input())

time = (hour * 60) + minutes + 15

hour = time // 60
minutes = time % 60

if hour >= 24:
    hour = hour % 24

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")