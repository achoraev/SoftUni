import math

count_tournirs = int(input())
start_points = int(input())

current_point = 0
count_winnings = 0

for tours in range(0, count_tournirs):
    tour = input()
    if tour == "W":
        current_point += 2000
        count_winnings += 1
    elif tour == "F":
        current_point += 1200
    elif tour == "SF":
        current_point += 720

average = current_point / count_tournirs
percent_winnings = count_winnings / count_tournirs * 100

print(f"Final points: {math.floor(start_points + current_point)}")
print(f"Average points: {math.floor(average)}")
print(f"{percent_winnings:.2f}%")