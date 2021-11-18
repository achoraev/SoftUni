chickenMenu = int(input())
fishMenu = int(input())
vegeMenu = int(input())

priceChicken = chickenMenu * 10.35
priceFish = fishMenu * 12.4
priceVege = vegeMenu * 8.15

total = priceChicken + priceFish + priceVege
desert = total * 0.2
print(total + desert + 2.5)