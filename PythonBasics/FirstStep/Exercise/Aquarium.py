length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volumeCM = length * width * height
volumeLitres = volumeCM / 1000

result = volumeLitres * (1 - (percent/100))

print(result)