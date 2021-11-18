import math

type = input()

if type == 'square':
    a = float(input())
    area = a * a
    print(f"{area:.3f}")
elif type == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif type == 'circle':
    r = float(input())
    area = r * r * math.pi
    print(f"{area:.3f}")
elif type == 'triangle':
    b = float(input())
    h = float(input())
    area = (b * h) / 2
    print(f"{area:.3f}")