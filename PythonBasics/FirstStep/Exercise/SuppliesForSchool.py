pens = input();
markers = input();
litters = input();
discount = input();

pricePens = int(pens) * 5.8;
priceMarkers = int(markers) * 7.2;
priceLitters = int(litters) * 1.2;
totalPrice = pricePens + priceMarkers + priceLitters;

print(totalPrice - (totalPrice * int(discount) / 100));