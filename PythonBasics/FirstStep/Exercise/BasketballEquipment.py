yearPrice = int(input())

basketballShoes = yearPrice - (yearPrice * 0.4)
basketballEkip = basketballShoes - (basketballShoes * 0.2)
basketballBall = basketballEkip / 4
basketballAccessories = basketballBall / 5
total = yearPrice + basketballShoes + basketballEkip + basketballBall + basketballAccessories

print(total)