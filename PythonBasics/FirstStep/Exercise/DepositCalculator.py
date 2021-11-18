amount = int(input())
srok = int(input())
percentYear = float(input())
interestMonth = amount * (percentYear / 100) / 12
print(amount + interestMonth * srok)