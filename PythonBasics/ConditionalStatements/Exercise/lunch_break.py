import math

serial_name = input()
time_episod = int(input())
time_break = int(input())

time_lunch = time_break * 0.125
time_rest = time_break * 0.25

time_left = time_break - time_lunch - time_rest

if time_episod > time_left:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(time_episod - time_left)} more minutes.")
else:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(time_left - time_episod)} minutes free time.")
