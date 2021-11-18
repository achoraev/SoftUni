budget = float(input())
season = input()

needed = 0
destination = 'Europe'
place = 'Hotel'

if budget <= 100:
    if season == 'summer':
        needed = budget * 0.3
        place = 'Camp'
    else:
        needed = budget * 0.7
    destination = 'Bulgaria'
elif budget > 100 and budget <= 1000:
    if season == 'summer':
        needed = budget * 0.4
        place = 'Camp'
    else:
        needed = budget * 0.8
    destination = 'Balkans'
else:
        needed = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {needed:.2f}")