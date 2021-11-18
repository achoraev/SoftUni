plastic = input()
paint = input()
razreditel = input()
hours = input()

pricePlastik = (int(plastic) + 2) * 1.5
pricePaint = (int(paint) + (int(paint) * 0.1)) * 14.5
priceRazreditel = int(razreditel) * 5
totalMaterials = 0.4 + pricePlastik + pricePaint + priceRazreditel
priceWorkers = totalMaterials * 0.3 * int(hours)

print(totalMaterials + priceWorkers)