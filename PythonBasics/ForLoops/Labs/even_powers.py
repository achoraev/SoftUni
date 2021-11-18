import math

n = int(input())

for i in range(0, n + 1, 2):
    num = math.pow(2, i)
    print(f"{num:.0f}")