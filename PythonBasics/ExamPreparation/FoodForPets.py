import math

days = int(input())
total_food = float(input())
total_eaten = 0
dog_eaten = 0
cat_eaten = 0
eaten_buiscuits = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    dog_eaten += dog_food
    cat_eaten += cat_food
    total_eaten += dog_food + cat_food
    if day % 3 == 0:
        eaten_buiscuits += (dog_food + cat_food) * 0.1

percent_eaten = total_eaten / total_food * 100
percent_dog = dog_eaten / total_eaten * 100
percent_cat = cat_eaten / total_eaten * 100

print(f"Total eaten biscuits: {math.floor(eaten_buiscuits)}gr.")
print(f"{percent_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")