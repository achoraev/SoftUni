import math

record = float(input())
distance = float(input())
time_seconds_metres = float(input())

total_time = distance * time_seconds_metres

if distance >= 15:
    total_time = total_time + (math.floor(distance / 15) * 12.5)

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(total_time - record):.2f} seconds slower.")