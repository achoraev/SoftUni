import sys

n = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize

for i in range(0, n):
    num = int(input())
    if num > max_number:
        max_number = num

    if num < min_number:
        min_number = num

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")